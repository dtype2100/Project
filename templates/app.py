import requests
import streamlit as st
from pydantic import BaseModel

# FastAPI와 동일한 데이터 모델 사용
class Item(BaseModel):
    name: str
    age: int
    city: str

st.title("FastAPI and Streamlit Integration")

# 사용자로부터 데이터 입력
name = st.text_input("Name:")
age = st.number_input("Age:")
city = st.text_input("City:")

if st.button("Create Data"):
    # 사용자 입력을 FastAPI로 전송
    item = Item(name=name, age=age, city=city)
    response = requests.post("http://127.0.0.1:8000/create_data", json=item.dict())

    if response.status_code == 200:
        data = response.json()
        st.write("Data Created Successfully!")
        st.write("Updated Data:")
        for key, value in data.items():
            st.write(f"ID: {key}, Name: {value['name']}, Age: {value['age']}, City: {value['city']}")
    else:
        st.write("Error creating data. Please try again.")
