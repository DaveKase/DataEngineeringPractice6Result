import airflow
import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

default_args_dict = {
    'start_date': airflow.utils.dates.days_ago(0),
    'concurrency': 1,
    'schedule_interval': None,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

first_dag = DAG(
    dag_id='first_dag_stub',
    default_args=default_args_dict,
    catchup=False,
)

task_one = DummyOperator(
    task_id='get_spreadsheet',
    dag=first_dag
)

task_two = DummyOperator(
    task_id='transmute_to_csv',
    dag=first_dag)

task_three = DummyOperator(
    task_id='time_filter',
    dag=first_dag
)

task_four = DummyOperator(
    task_id='load',
    dag=first_dag
)


task_five = DummyOperator(
    task_id='cleanup',
    dag=first_dag)


task_one >> task_two >> task_three >> task_four >> task_five



