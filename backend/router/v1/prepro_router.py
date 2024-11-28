from fastapi import APIRouter, Request
from pydantic import BaseModel
from services.prepro import Preprocessing
import pandas as pd

router = APIRouter(
    prefix='/prepro_router',
    tags='/prepro_router'
)

pc = Preprocessing()

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
async def apply_schedule_workflow(request: Request):

    result = await request.json()

    df_data = result['df_data']
    prepro_params = result['prepro_params']

    df = pd.read_json(df_data)
    
    # 데이터 전처리 적용 예정

    return df

