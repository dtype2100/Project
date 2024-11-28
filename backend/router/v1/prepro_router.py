from fastapi import APIRouter, Request, HTTPException
from schemas.prepro import PreprocessingJob
from services.prepro import Preprocessing, AirflowDag
import pandas as pd
import requests

router = APIRouter(
    prefix='/prepro_router',
    tags='/prepro_router'
)

pc = Preprocessing()
ad = AirflowDag()

AIRFLOW_API_URL = 'http://localhost:8080/api/v1/dags'
AIRFLOW_USER = 'airflow'
AIRFLOW_PASSWORD = 'airflow'

@router.get('/prepro_sample_df')
async def prepro_sample_df(request: Request):

    result = await request.json()

    df_data = result['df_data']
    prepro_params = result['prepro_params']

    df = pd.read_json(df_data)
    
    df = pc.prepro_all_columns(df_data=df_data, prepro_params=prepro_params)

    return df

@router.get('/prepro_all_df')
async def prepro_all_df(request: Request) -> pd.DataFrame:

    result = await request.json()

    df_data = result['df_data']
    prepro_params = result['prepro_params']

    df = pc.prepro_all_columns(df_data=df_data, prepro_params=prepro_params)

    return df

@router.get('/apply_schedule_workflow')
async def apply_schedule_workflow(job: PreprocessingJob):

    dag_file_path = ad.create_dag_file(job.dag_id, job.schedule_interval, job.script_path, job.task_id)


    response = requests.post(
        f"{AIRFLOW_API_URL}/{job.dag_id}",
        json={"conf": {}},
        auth=(AIRFLOW_USER, AIRFLOW_PASSWORD)
    )
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to trigger DAG")

    return {"message": "DAG and Task created successfully", "dag_id": job.dag_id}

