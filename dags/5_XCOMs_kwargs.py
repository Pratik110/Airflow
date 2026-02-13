from airflow.sdk import dag, task

@dag(dag_id="xcoms_dag_kwargs")
def xcoms_dag_kwargs():
    
    @task.python
    def first_task(**kwargs):
        ti = kwargs['ti']
        print("Extracting data for first task")
        
        fetched_data = {"data": [1, 2, 3, 4, 5]}
        
        sample_data = {"dummy": [8,9,10]}
        print("fetched data is",fetched_data )
        ti.xcom_push(key='return_result', value=fetched_data)
        ti.xcom_push(key='return_result_1', value=sample_data)
    
    @task.python
    def second_task(**kwargs):
        ti = kwargs['ti']
        print("Using task instance")
        
        data_from_first_task = ti.xcom_pull(task_ids="first_task", key='return_result')
        modified_data = data_from_first_task['data']
        modified_data.append(5)
        
        new_data = {"new_data": modified_data}
        print("new data is", new_data)
        ti.xcom_push(key='return_result_2', value=new_data)
        
        sample_data_from_first_task = ti.xcom_pull(task_ids="first_task", key='return_result_1')
        print("sample data from first task is", sample_data_from_first_task)
    
    @task.python
    def third_task(**kwargs):
        ti = kwargs['ti']
        load_data = ti.xcom_pull(task_ids='second_task', key='return_result_2')
        return load_data
    
        
    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third
    
    
#Instantiating the DAG
xcoms_dag_kwargs()