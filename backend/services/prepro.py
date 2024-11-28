import os
import pandas as pd
from typing import Union, Dict, Any
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class Preprocessing:
    def __init__(self):
        pass

    def prepro_all_columns(
            self, 
            df_data: Union[str, Dict[str, Any]], 
            prepro_params: Dict[str, str]
            ) -> pd.DataFrame:
        
        df = pd.read_json(df_data)
        for _, var in prepro_params.items():
            if var == 'all_col_dropna':
                df.dropna(inplace=True)

            elif var == 'all_col_bfill':
                df.fillna(method='bfill', inplace=True)

            elif var == 'all_col_ffill':
                df.fillna(method='ffill', inplace=True)

            elif var == 'minmax_scale':  
                scaler = MinMaxScaler()
                df = scaler.fit_transform(df)

            elif var == 'standard_scale':
                scaler = StandardScaler()
                df = scaler.fit_transform(df)

        return df

class AirflowDag:
    def __init__(self):
        pass 

    def create_dag_file(self, dag_id, schedule_interval, script_path, task_id):
        """
        DAG 파일 생성 함수
        """
        dag_content = f"""
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    from datetime import datetime

    # 전처리 스크립트를 동적으로 import
    import sys
    sys.path.append("{os.path.dirname(script_path)}")
    from {os.path.basename(script_path).replace('.py', '')} import run_preprocessing

    default_args = {{
        'start_date': datetime(2024, 12, 1),
        'retries': 1
    }}

    with DAG(dag_id='{dag_id}',
            default_args=default_args,
            schedule_interval='{schedule_interval}',
            catchup=False) as dag:

        task_{task_id} = PythonOperator(
            task_id='{task_id}',
            python_callable=run_preprocessing
        )
    """
        # 생성된 DAG 파일 저장
        dag_file_path = f"/path/to/airflow/dags/{dag_id}.py"
        with open(dag_file_path, "w") as file:
            file.write(dag_content)

        return dag_file_path
