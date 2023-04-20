import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch


# We will now define the tasks

def queryPostgresql():
    conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='postgres'"
    conn = db.connect(conn_string)
    df = pd.read_sql("select name, city from users", conn)
    df.to_csv('postgresqldata.csv')
    print('--------------Data saved--------------')


# To insert the data into elasticsearch
def insertElasticsearch():
    es = Elasticsearch('https://127.0.0.1:9200', verify_certs=False, basic_auth=("ibra", "sphynxm@lynx"))
    df = pd.read_csv('postgresqldata.csv')
    for i, r in df.iterrows():
        doc = r.to_json()
        res = es.index(index="frompostgresql", document=doc)
        print(res)



# Next we'll specify the arguments the DAG wil take
# remeber the start time should be a day behind if we
# schedule the task to run daily

default_args = {
        'owner': 'ibra',
        'start_date': dt.datetime(2020, 4, 2),
        'retries': 1,
        'retry_delay': dt.timedelta(minutes=5),
}
# Now we can pass the arguments to the DAG, name it and set the run
# interval

with DAG('MyDBdag',
        default_args=default_args,
        schedule_interval=timedelta(minutes=5), # '0 * * * *',
        ) as dag:

    getData = PythonOperator(task_id='QueryPostgreSQL',
            python_callable=queryPostgresql)

    insertData = PythonOperator(task_id='InsertDataElasticsearch',
            python_callable=insertElasticsearch)

getData >> insertData


"""
a) @once

b) @hourly => 0 * * * *

c) @daily => 0 0 * * *

d) @weekly => 0 0 * * 0

e) @monthly => 0 0 1 * *

f) @yearly => 0 0 1 1 *

crontab uses the format minute, hour, day of month, month, day of week. The value for @yearly is 0 0 1 1 *,
which means run yearly on January 1 (1 1), at 0:0 (midnight), on any day of the week (*).

"""