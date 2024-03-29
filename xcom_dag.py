from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.task_group import TaskGroup

from random import uniform
from datetime import datetime

default_args = {
    'start_date' : datetime(2022, 1, 1)
}

def _training_model(ti):
    accuracy = uniform(.1, 10.)
    print(f'model\'s accuracy: {accuracy}')
    ti.xcom_push(key='model_accuracy', value=accuracy)

def _choose_best_model(ti):
    print('choose best model')
    accuracies = ti.xcom_pull(key='model_accuracy', task_ids=[
        'processing_tasks.training_model_a',
        'processing_tasks.training_model_b',
        'processing_tasks.training_model_c'
    ])
    # return the task id that needs to be run
    for accuracy in accuracies:
        if accuracy > 5.0:
            return 'accurate'
        else:
            return 'inaccurate'
            # return ['accurate', 'inaccurate'] if you want to return multiple task ids


with DAG('xcom_dag', schedule_interval='@daily', default_args=default_args, tags=['Hands on'], catchup=False) as dag:
    downloading_data = BashOperator(task_id='downloading_data', bash_command='sleep 3', do_xcom_push=False) # last parameter for the operators creating xcom by defaults
    
    with TaskGroup('processing_tasks') as processing_tasks:
        training_model_a = PythonOperator(task_id='training_model_a', python_callable=_training_model)
        training_model_b = PythonOperator(task_id='training_model_b', python_callable=_training_model)
        training_model_c = PythonOperator(task_id='training_model_c', python_callable=_training_model)

    choose_model = BranchPythonOperator(task_id='choose_best_model', python_callable=_choose_best_model)


    accurate = DummyOperator(
        task_id='accurate'
    )

    inaccurate = DummyOperator(
        task_id='inaccurate'
    )

    storing = DummyOperator(
        task_id='storing',
        trigger_rule='none_failed_or_skipped'
    )

    downloading_data >> processing_tasks >> choose_model
    choose_model >> [accurate, inaccurate] >> storing