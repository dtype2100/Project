import streamlit as st
import requests
import pandas as pd

# Streamlit UI
st.title("Streamlit to FastAPI Workflow")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.write(df)
    

    selected_columns = st.multiselect('select columns', [cols for cols in df.columns])

    if selected_columns:
        st.subheader("selected dataframe")
        st.write(df[selected_columns])

