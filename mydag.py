# Step 1
import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd

# Step 2
def CSVToJson():
    df = pd.read_csv('/home/ibra/documents/CSV/data.csv')
    for i, r in df.iterrows():
        print(r['name'])
    df.to_json('fromAirflow.JSON', orient='records')

# Step 3
default_args = {
    'owner' : 'ibra',
    'start_date' : dt.datetime(2022, 7, 31),
    'retries' : 1,
    'retry_delay' : dt.timedelta(minutes=5),
}

# Step 4
with DAG('MyCSVDAG',
    default_args = default_args,
    schedule_interval = timedelta(minutes=5),
    # '0 * * * *',
    ) as dag:
    # Step 5
    print_starting = BashOperator(task_id='starting', bash_command='echo "I am reading the CSV now..."')
    CSVJson = PythonOperator(task_id='convertCSVtoJSON', python_callable=CSVToJson)

# Step 6
print_starting.set_downstream(CSVJson)
CSVJson.set_upstream(print_starting)
# or we can use the bit shift operator
# print_starting >> CSVJson
# CSVJson << print_starting

# Step 7
# We need to set a directory for our DAGs, in the airflow.cfg we can find the settings
# of our DAGs in the format $AIRFLOW_HOME/dags

# Step 8
# airflow webserver
# airflow scheduler
