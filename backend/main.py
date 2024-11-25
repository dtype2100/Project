from fastapi import FastAPI
from router.v1 import save_data_router as save_data

app = FastAPI()

app.include_router(save_data.router)

@app.get('/')
def index():
    return {'message': 'is connected successfully!'}
