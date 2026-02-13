from airflow.sdk import dag, task
from pendulum import datetime

@dag(
    dag_id="schedule_preset_dag",
    start_date=datetime(year=2026, month=2, day=12, hour=20, minute=15, tz="Asia/Kolkata"),
    schedule="@daily",
    is_paused_upon_creation=False,
    catchup=True
)
def schedule_preset_dag():
    
    @task.python
    def task_one(**kwargs):
        print("This is task one. It runs daily at 8:15 PM Asia/Kolkata time.")
    
    @task.python
    def task_two():
        print("This is task two. It runs after task one.")
        
    print_execution_date = task_one()
    another_task = task_two()
    
    print_execution_date >> another_task
    
schedule_preset_dag()