from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.decorators import task
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.task_group import TaskGroup

from random import uniform
from datetime import datetime

default_args = {
    'start_date' : datetime(2022, 1, 1)
}


with DAG('xcom_dag_with_task', schedule_interval='@daily', default_args=default_args, tags=['Hands on'], catchup=False):
    downloading_data = BashOperator(task_id='downloading_data', bash_command='sleep 3', do_xcom_push=False) # last parameter for the operators creating xcom by defaults
    
    @task
    def training_model(accuracy):
        accuracy = uniform(.1, 10.)
        print(f'model\'s accuracy: {accuracy}')
        return accuracy

    @task.branch
    def choose_best_model(accuracies):
        print('choose best model')
        # return the task id that needs to be run
        for accuracy in accuracies:
            if accuracy > 5.0:
                return 'accurate'
            else:
                return 'inaccurate'
                # return ['accurate', 'inaccurate'] if you want to return multiple task ids
    

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

    downloading_data >> choose_best_model(training_model.expand(accuracy=[5, 10, 6])) >> [accurate, inaccurate] >> storing