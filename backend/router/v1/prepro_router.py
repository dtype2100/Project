from fastapi import APIRouter, Request
import pandas as pd

router = APIRouter(
    prefix='/prepro_router',
    tags='/prepro_router'
)

@router.get('/prepro_sample_df')
async def prepro_sample_df(request: Request):

    result = await request.json()

    df_data = result['df_data']
    payload = result['payload']

    df = pd.read_json(df_data)
    
    # 데이터 전처리 적용 예정

    return df

@router.get('/prepro_all_df')
async def prepro_all_df(request: Request):

    result = await request.json()

    df_data = result['df_data']
    payload = result['payload']

    df = pd.read_json(df_data)
    
    # 데이터 전처리 적용 예정

    return df

@router.get('/apply_schedule_workflow')
async def apply_schedule_workflow(request: Request):

    result = await request.json()

    df_data = result['df_data']
    payload = result['payload']

    df = pd.read_json(df_data)
    
    # 데이터 전처리 적용 예정

    return df

