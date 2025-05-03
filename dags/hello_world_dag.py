from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators import EmptyOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

# define the funtion to be executed 
def say_hello():
    print('Hello world from a function!')

# default arguments for the DAG
default_args = { 
    'owner': 'Emanuel Calderon', 
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# define the DAG
with DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval=None, # run once
    start_date=(2023, 1, 1), # run once
    catchup=False, # don't catch up
    tags=['hello_world'],
) as dag:
    # define the task
    start = EmptyOperator(
        task_id='start'
        )
    end = EmptyOperator(
        task_id='end'
        )
    hello_task = PythonOperator(
        task_id='hello_task',
        python_callable=say_hello
        )
    # define the dependencies
    (
        start >> hello_task >> end
    )