from fastapi import FastAPI, Request, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

sample_dict = {1: {"name": "jin",
               "age": 30,
               "city": "Seoul"
               }}

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    name: str
    age: int
    city: str

@app.get("/read_data")
def read_data(request: Request):
    data = request.json()
    return {"data": data}

@app.post("/create_data")
def create_data(item: Item):
    new_key = max(sample_dict.keys()) + 1
    sample_dict[new_key] = item.model_dump()
    return sample_dict

