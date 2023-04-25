# minimal code
from airflow.operators.bash_operator import BashOperator
from airflow.utils.task_group import TaskGroup
from airflow.decorators import dag, task, task_group
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from process_missing_data.query_missing_data import query_missing_data
from database.transformed_columns import transformed_columns

import os
from pathlib import Path
import pandas as pd
import numpy as np

from datetime import datetime, timedelta

default_args = {
    'owner': 'projet_afroscreen',
    'start_date': datetime(2022, 2, 10)
}

# unique DAG id across your pipelines
@dag(default_args=default_args, schedule='@daily', catchup=False, tags=['Afroscreen'])
def afroscreen_data_processing():

    @task_group()
    def bobo():
        @task_group()
        def import_data():
            is_bobo_path_available = FileSensor(
                task_id="is_bobo_path_available",
                poke_interval=30,
                fs_conn_id='raw_folder_path',
                filepath='bobo'
            )
            
            @task()
            def read_bobo_csv_files():
                converter = {'Code Echantillon': str, 'Geometry': str, 'COVID Temperature': float}
                # list of the columns to drop
                cols_to_drop = ['Event', 'Program stage', 'Program instance', 'Longitude', 'Latitude', 'Organisation unit code', 'Organisation unit', 'Tracked entity instance', 'Numero Enregistrement']
                raw_data_dir = '/home/ibra/documents/afroscreen/raw_data/bobo'
                cols_section_1 = list(pd.read_csv(os.path.join(raw_data_dir, "1.csv"), nrows=1))
                cols_section_2 = list(pd.read_csv(os.path.join(raw_data_dir, "2.csv"), nrows=1))
                cols_section_3 = list(pd.read_csv(os.path.join(raw_data_dir, "3.csv"), nrows=1))
                cols_section_4 = list(pd.read_csv(os.path.join(raw_data_dir, "4.csv"), nrows=1))
                cols_section_5 = list(pd.read_csv(os.path.join(raw_data_dir, "5.csv"), nrows=1))
                cols_section_6 = list(pd.read_csv(os.path.join(raw_data_dir, "6.csv"), nrows=1))
                cols_section_7 = list(pd.read_csv(os.path.join(raw_data_dir, "7.csv"), nrows=1))
                cols_section_8 = list(pd.read_csv(os.path.join(raw_data_dir, "8.csv"), nrows=1))
                cols_section_9 = list(pd.read_csv(os.path.join(raw_data_dir, "9.csv"), nrows=1))
                cols_section_10 = list(pd.read_csv(os.path.join(raw_data_dir, "10.csv"), nrows=1))
                # read all the individual files
                df_section_1 = pd.read_csv(os.path.join(raw_data_dir, "1.csv"), usecols = [i for i in cols_section_1 if i not in cols_to_drop], converters=converter)
                df_section_1['Ville/Village'] = df_section_1['Ville/Village'].apply(lambda x: pd.Series(str(x).replace("'", "")))
                df_section_1['District de residence'] = df_section_1['District de residence'].apply(lambda x: pd.Series(str(x).replace("'", "")))
                # Remove the single quote in the COVID Preciser Symptomes column
                df_section_2 = pd.read_csv(os.path.join(raw_data_dir, "2.csv"), usecols = [i for i in cols_section_2 if i not in cols_to_drop], converters=converter)
                df_section_2['COVID Preciser Symptomes'] = df_section_2['COVID Preciser Symptomes'].apply(lambda x: pd.Series(str(x).replace("'", "")))
                df_section_3 = pd.read_csv(os.path.join(raw_data_dir, "3.csv"), usecols = [i for i in cols_section_3 if i not in cols_to_drop], converters=converter)
                df_section_3['COVID Preciser Autre Profession'] = df_section_3['COVID Preciser Autre Profession'].apply(lambda x: pd.Series(str(x).replace("'", "")))
                df_section_4 = pd.read_csv(os.path.join(raw_data_dir, "4.csv"), usecols = [i for i in cols_section_4 if i not in cols_to_drop], converters=converter)
                df_section_5 = pd.read_csv(os.path.join(raw_data_dir, "5.csv"), usecols = [i for i in cols_section_5 if i not in cols_to_drop], converters=converter)
                
                lnrg_cols = {
                    "COVID Date de la PCR": "COVID Date de la PCR LNRG",
                    "COVID PCR realisee": "COVID PCR realisee LNRG",
                    "N° Colis SONAPOST": "N° Colis SONAPOST LNRG",
                }
                df_section_6 = pd.read_csv(os.path.join(raw_data_dir, "6.csv"), usecols = [i for i in cols_section_6 if i not in cols_to_drop], converters=converter)
                # renaming section 6
                df_section_6.rename(lnrg_cols, inplace=True) 
                
                df_section_7 = pd.read_csv(os.path.join(raw_data_dir, "7.csv"), usecols = [i for i in cols_section_7 if i not in cols_to_drop], converters=converter)
                
                sec8_cols = {
                    "COVID Temperature": "COVID Temperature Investigation"
                }
                df_section_8 = pd.read_csv(os.path.join(raw_data_dir, "8.csv"), usecols = [i for i in cols_section_8 if i not in cols_to_drop], converters=converter)
                # renaming section 6
                df_section_8.rename(sec8_cols, inplace=True)

                df_section_9 = pd.read_csv(os.path.join(raw_data_dir, "9.csv"), usecols = [i for i in cols_section_9 if i not in cols_to_drop], converters=converter)
                df_section_10 = pd.read_csv(os.path.join(raw_data_dir, "10.csv"), usecols = [i for i in cols_section_10 if i not in cols_to_drop], converters=converter)
                # write the files as clean files
                clean_data_dir = '/home/ibra/documents/afroscreen/clean_data/bobo'
                Path(clean_data_dir).mkdir(parents=True, exist_ok=True)

                df_section_1.to_csv(os.path.join(clean_data_dir, "section_1.csv"), index=False)
                df_section_2.to_csv(os.path.join(clean_data_dir, "section_2.csv"), index=False)
                df_section_3.to_csv(os.path.join(clean_data_dir, "section_3.csv"), index=False)
                df_section_4.to_csv(os.path.join(clean_data_dir, "section_4.csv"), index=False)
                df_section_5.to_csv(os.path.join(clean_data_dir, "section_5.csv"), index=False)
                df_section_6.to_csv(os.path.join(clean_data_dir, "section_6.csv"), index=False)
                df_section_7.to_csv(os.path.join(clean_data_dir, "section_7.csv"), index=False)
                df_section_8.to_csv(os.path.join(clean_data_dir, "section_8.csv"), index=False)
                df_section_9.to_csv(os.path.join(clean_data_dir, "section_9.csv"), index=False)
                df_section_10.to_csv(os.path.join(clean_data_dir, "section_10.csv"), index=False)


            is_bobo_path_available >> read_bobo_csv_files()
        
        @task_group()
        def process_data():
            # check for missing data and produce queries for correction/confirmation
            @task(retries=1, retry_delay=timedelta(seconds=60))
            def inspect_missing_data():
                clean_data_dir = '/home/ibra/documents/afroscreen/clean_data/bobo/'
                section_1_path = os.path.join(clean_data_dir, "section_1.csv")
                section_2_path = os.path.join(clean_data_dir, "section_2.csv")
                section_3_path = os.path.join(clean_data_dir, "section_3.csv")
                section_4_path = os.path.join(clean_data_dir, "section_4.csv")
                section_5_path = os.path.join(clean_data_dir, "section_5.csv")
                section_6_path = os.path.join(clean_data_dir, "section_6.csv")
                section_7_path = os.path.join(clean_data_dir, "section_7.csv")
                section_8_path = os.path.join(clean_data_dir, "section_8.csv")
                section_9_path = os.path.join(clean_data_dir, "section_9.csv")
                section_10_path = os.path.join(clean_data_dir, "section_10.csv")
                
                number_of_sections_with_errors = 0
                
                sections_path = [section_1_path, section_2_path, section_3_path, section_4_path, section_5_path, section_6_path, section_7_path, section_8_path, section_9_path, section_10_path]

                for i, path in enumerate(sections_path):
                    section = f"Section {i+1}"
                    section_queries = query_missing_data(path=path, section=section)
                    if len(section_queries) > 0:
                        outname = f"queries_section_{i+1}.xlsx"
                        outdir = '/home/ibra/documents/afroscreen/queries/bobo'
                        Path(outdir).mkdir(parents=True, exist_ok=True)
                        bobo_queries = os.path.join(outdir, outname)    
                        section_queries.to_excel(bobo_queries)
                        number_of_sections_with_errors += 1

                return number_of_sections_with_errors
            
            @task.branch
            def check_number_of_errors(number_of_sections_with_errors):
                # return the task id that needs to be run
                if int(number_of_sections_with_errors) < 0: # > original
                    return 'bobo.handle_missing_data.copy_queries_generated'
                else:
                    return 'bobo.store_data.load_and_merge_data'

            check_number_of_errors(inspect_missing_data())
        
        @task_group()
        def handle_missing_data():
            copy_queries_generated = BashOperator(
                task_id='copy_queries_generated',
                bash_command="sudo cp /home/ibra/documents/afroscreen/queries/*.xlsx /mnt/hgfs/shared_folder"
            )

            send_queries_by_email = BashOperator(
                task_id='send_queries_by_email',
                bash_command="python3 /home/ibra/documents/airflow/dags/send_email/send_email.py -c /home/ibra/documents/airflow/dags/send_email/email_conf.ini --r brahim.oued@gmail.com ibra.oued@outlook.com --p '/home/ibra/documents/afroscreen/queries'"
            )

            copy_queries_generated  >> send_queries_by_email


        @task_group()
        def store_data():
            @task()
            def load_and_merge_data():
                converter = {'Code Echantillon': str, 'Geometry': str, 'COVID Temperature': float}
                # read all the individual files
                df_section_1 = pd.read_csv('/home/ibra/documents/afroscreen/clean_data/bobo/section_1.csv', converters=converter)
                df_section_2 = pd.read_csv('/home/ibra/documents/afroscreen/clean_data/bobo/section_2.csv', converters=converter)
                df_section_3 = pd.read_csv('/home/ibra/documents/afroscreen/clean_data/bobo/section_3.csv', converters=converter)
                df_section_4 = pd.read_csv('/home/ibra/documents/afroscreen/clean_data/bobo/section_4.csv', converters=converter)
                df_section_5 = pd.read_csv('/home/ibra/documents/afroscreen/clean_data/bobo/section_5.csv', converters=converter)
                df_section_6 = pd.read_csv('/home/ibra/documents/afroscreen/clean_data/bobo/section_6.csv', converters=converter)
                df_section_7 = pd.read_csv('/home/ibra/documents/afroscreen/clean_data/bobo/section_7.csv', converters=converter)
                df_section_8 = pd.read_csv('/home/ibra/documents/afroscreen/clean_data/bobo/section_8.csv', converters=converter)
                df_section_9 = pd.read_csv('/home/ibra/documents/afroscreen/clean_data/bobo/section_9.csv', converters=converter)
                df_section_10 = pd.read_csv('/home/ibra/documents/afroscreen/clean_data/bobo/section_10.csv', converters=converter)

                # merge the data regarding the code of echantillon
                df_merged = df_section_1.merge(df_section_2, how="left", on="Code Echantillon", suffixes=('', '_delme'))\
                            .merge(df_section_3, how="left", on="Code Echantillon", suffixes=('', '_delme'))\
                            .merge(df_section_4, how="left", on="Code Echantillon", suffixes=('', '_delme'))\
                            .merge(df_section_5, how="left", on="Code Echantillon", suffixes=('', '_delme'))\
                            .merge(df_section_6, how="left", on="Code Echantillon", suffixes=('', '_delme'))\
                            .merge(df_section_7, how="left", on="Code Echantillon", suffixes=('', '_delme'))\
                            .merge(df_section_8, how="left", on="Code Echantillon", suffixes=('', '_delme'))\
                            .merge(df_section_9, how="left", on="Code Echantillon", suffixes=('', '_delme'))\
                            .merge(df_section_10, how="left", on="Code Echantillon", suffixes=('', '_delme'))

                df = df_merged[[c for c in df_merged.columns if not c.endswith('_delme')]]
                df.rename(columns=transformed_columns(), inplace=True)
                df.reset_index()
                # Transform the GPS data
                df[['longitude', 'latitude']] = df['coords_gps'].apply(lambda x: pd.Series(str(x).split(",")))
                df['longitude'] = df['longitude'].str.removeprefix('[')
                df['latitude'] = df['latitude'].str.removesuffix(']')

                # rename the columns of the dataframe
                outname = 'merged_dhis2_data.csv'
                outdir = '/home/ibra/documents/afroscreen/clean_data/bobo'
                Path(outdir).mkdir(parents=True, exist_ok=True)
                fullname = os.path.join(outdir, outname)    
                df.to_csv(fullname, index=False)

            create_patients_table = PostgresOperator(
                task_id="create_patients_table",
                postgres_conn_id="postgres_local_db",
                sql="sql/patients.sql"
            )

            @task()
            def convert_df_to_sql():
                converter_echantillon = {'code_echantillon': str}
                df = pd.read_csv('/home/ibra/documents/afroscreen/clean_data/bobo/merged_dhis2_data.csv', converters=converter_echantillon)
                df = df.fillna('NULL')

                SOURCE = df
                TARGET = 'patientsafroscreen'
                sql_texts = []
                for index, row in SOURCE.iterrows():
                    sql_texts.append('INSERT INTO '+ TARGET + ' (' + str(', '.join(SOURCE.columns)) + ') VALUES ' + str(tuple(row.values)))        

                query = '; '.join(map(str, sql_texts))
                return query

            convert_df_to_sql = convert_df_to_sql()
            
            insert_data_to_postgres = PostgresOperator(
                task_id="insert_data_to_postgres",
                postgres_conn_id="postgres_local_db",
                sql=f"{convert_df_to_sql}"
            )
            
            convert_df_to_sql >> insert_data_to_postgres
            load_and_merge_data() >> create_patients_table >> convert_df_to_sql

        import_data() >> process_data() >> [handle_missing_data(), store_data()]

    
    [bobo()]


afroscreen_data_processing = afroscreen_data_processing()


        