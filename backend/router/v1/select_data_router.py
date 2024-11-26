from fastapi import APIRouter, Request
import duckdb

router = APIRouter(
    prefix='/select_router',
    tags=['select_router']
)


@router.get('/show_tables')
async def show_tables():
    con = duckdb.connect('./database.db')
    tables = con.execute('SHOW TABLES;').fetchall()
    
    return {'tables': tables}


@router.get('/select_table/{table_name}')
async def select_table(table_name: str):

    con = duckdb.connect('./database.db')
    query_table = con.execute(f'SELECT * FROM {table_name};').df()
    
    return {'query_table': query_table.to_json()}
