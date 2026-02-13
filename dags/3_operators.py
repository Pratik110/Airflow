from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator

@dag(
    dag_id="operators_dag",
)
def operators_dag():
    @task.python
    def first_task():
        print("This is the first task")
        
    @task.python
    def second_task():
        print("This is the second task")
        
    @task.python
    def third_task():
        print("This is the third task")
    
    #defining task dependecies
    
    @task.bash
    def bash_task_moden() -> str:
        return "echo https://airflow.apache.org/"
    
    bash_task_old = BashOperator(
        task_id="bash_task_old",
        bash_command="echo https://airflow.apache.org/",
        )
    
    first = first_task()
    second = second_task()
    third = third_task()
    bash_task_moden = bash_task_moden()
    bash_task_old = bash_task_old
    
    
    first >> second >> third >> bash_task_moden >> bash_task_old

#instantiating the DAG
operators_dag()