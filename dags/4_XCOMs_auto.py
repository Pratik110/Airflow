from airflow.sdk import dag, task

@dag(dag_id="xcoms_auto")
def xcoms_dag_auto():
    @task.python
    def push_xcom():
        return "Hello from XComs!"
    
    @task.python
    def pull_xcom(xcom_value: str):
        xcom_value = xcom_value.upper()
        print(f"Received XCom value: {xcom_value}")
    
    xcom_value = push_xcom()
    pull_xcom(xcom_value)
xcoms_dag_auto()