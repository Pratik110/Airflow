from airflow.sdk import dag, task

@dag(dag_id="parallel_tasks_dag")
def parallel_tasks_dag():
    
    @task.python
    def extract_data(**kwargs):
        print("Extracting data...")
        extracted_data = {
                            "api_data": ["api_1", "api_2", "api_3"],
                            "db_data": ["db_1", "db_2", "db_3"],
                            "file_data": ["file_1", "file_2", "file_3"]
                            }
        ti = kwargs['ti']
        ti.xcom_push(key='extracted_data', value=extracted_data)
    
    @task.python
    def transform_api_data(**kwargs):
        ti = kwargs['ti']
        extracted_data = ti.xcom_pull(task_ids='extract_data', key='extracted_data')
        api_data = extracted_data['api_data']
        transformed_api_data = [data.upper() for data in api_data]
        ti.xcom_push(key='transformed_api_data', value=transformed_api_data)
    
    @task.python
    def transform_db_data(**kwargs):
        ti = kwargs['ti']
        extracted_data = ti.xcom_pull(task_ids='extract_data', key='extracted_data')
        db_data = extracted_data['db_data']
        transformed_db_data = [data.upper() for data in db_data]
        ti.xcom_push(key='transformed_db_data', value=transformed_db_data)
    
    @task.python
    def transform_file_data(**kwargs):
        ti = kwargs['ti']
        extracted_data = ti.xcom_pull(task_ids='extract_data', key='extracted_data')
        file_data = extracted_data['file_data']
        transformed_file_data = [data.upper() for data in file_data]
        ti.xcom_push(key='transformed_file_data', value=transformed_file_data)
    
    @task.python
    def load_data(**kwargs):
        ti = kwargs['ti']
        transformed_api_data = ti.xcom_pull(task_ids='transform_api_data', key='transformed_api_data')
        transformed_db_data = ti.xcom_pull(task_ids='transform_db_data', key='transformed_db_data')
        transformed_file_data = ti.xcom_pull(task_ids='transform_file_data', key='transformed_file_data')
        print("Loading data...")
        print("Transformed API Data:", transformed_api_data)
        print("Transformed DB Data:", transformed_db_data)
        print("Transformed File Data:", transformed_file_data)

    extract_task = extract_data()
    transform_api_task = transform_api_data()
    transform_db_task = transform_db_data()
    transform_file_task = transform_file_data()
    load_data_task = load_data()
    
    extract_task >> [transform_api_task, transform_db_task, transform_file_task] >> load_data_task

parallel_tasks_dag()