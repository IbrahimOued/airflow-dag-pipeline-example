from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
# NEVER USE SubDagOperator in production use TaskGroup instead
# from airflow.operators.subdag import SubDagOperator
# from subdags.subdag_parallel_dag import subdag_parallel_dag
from datetime import datetime

default_args = {
    'start_date': datetime(2020, 1, 1)
}
# some parameters to keep in mind in the airflow.cfg file
#
# parallelism                   ==> allow you to define the maximum number of tasks that can be executed in parallel for the entire airflow instance
# max_active_tasks_per_dag      ==> allow you to define the maximum number of tasks that can be executed in parallel for a given DAG accross all of its dag runs
# max_active_runs_per_dag       ==> allow you to define the maximum number of dag runs that can be executed in parallel for a given dag
with DAG(
    'parallel_dag',
    schedule_interval='@daily',
    tags=['Hands on'],
    default_args=default_args,
    # concurrency=1,            # in contrary to the changes make in the airflow.cfg file (max_active_tasks_per_dag), this parameter applied only to this specific DAG
    # max_active_runs=1,        # in contrary to the changes make in the airflow.cfg file (max_active_runs_per_dag), this parameter applied only to this specific DAG
    catchup=False
) as dag:
    task_1 = BashOperator(task_id='task_1', bash_command='sleep 3')

    with TaskGroup('processing_tasks') as processing_tasks:
        task_2 = BashOperator(task_id='task_2', bash_command='sleep 3')
        with TaskGroup('spark_tasks') as spark_tasks:
            task_3 = BashOperator(task_id='task_3', bash_command='sleep 3')
        with TaskGroup('flink_tasks') as flink_tasks:
            task_3 = BashOperator(task_id='task_3', bash_command='sleep 3')

    # processing = SubDagOperator(
    #     task_id='processing_tasks',
    #     subdag=subdag_parallel_dag('parallel_dag', 'processing_tasks', default_args)
    # )
  

    task_4 = BashOperator(task_id='task_4', bash_command='sleep 3')

    # task_1 >> [task_2, task_3] >> task_4
    # task_1 >> processing >> task_4
    task_1 >> processing_tasks >> task_4