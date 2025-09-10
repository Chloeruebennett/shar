from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_main(**kwargs):
    start_date = '2023-10-01'
    end_date = '2023-10-15'
    subprocess.run(['python', 'main.py', start_date, end_date], check=True)

with DAG('automator_dag', default_args=default_args, schedule_interval='@daily') as dag:
    task = PythonOperator(
        task_id='run_pipeline',
        python_callable=run_main
    )
