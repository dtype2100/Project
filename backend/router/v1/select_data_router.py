from fastapi import APIRouter
import pandas as pd
import duckdb

router = APIRouter(
    prefix='/select_router',
    tags=['select_router']
)


@router.get('/show_tables')
async def save_data():
    con = duckdb.connect('./database.db')
    tables = con.execute('SHOW TABLES;').fetchall()
    
    return {'tables': tables}


