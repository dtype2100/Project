from fastapi import APIRouter, Request
import pandas as pd
import duckdb

router = APIRouter(
    prefix='/save_router',
    tags=['save_router']
)


@router.post('/save_data')
async def save_data(request: Request):
    result = await request.json()
    filtered_df = result['filtered_df']
    table_name = result['table_name']
    
    df = pd.read_json(filtered_df)

    con = duckdb.connect('./database.db')
    con.execute(f'CREATE TABLE IF NOT EXISTS "{table_name}" AS SELECT * FROM df')
    
    return {'message': 'Save data successfully!'}