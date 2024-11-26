import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout='wide')

st.title("Data Preproccessing")

table_name = None

with st.form('show_tables'):

    if st.form_submit_button('show tables', use_container_width=True):
        response = requests.get('http://backend:8000/select_router/show_tables')   

        if response.status_code == 200:

            st.success('show tables successfully!')

            result = response.json()
            table_name = st.multiselect('Choose table', [table[0] for table in result['tables']])

        else:
            st.write('An error occurred in showing table')
            st.warning(response.status_code)

