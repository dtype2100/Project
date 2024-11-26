import streamlit as st
import requests

st.set_page_config(layout='wide')

st.title("Data Preproccessing")


with st.form('show_tables'):
    if st.form_submit_button('show tables'):
        response = requests.get('http://backend:8000/select_router/select_data')   
        if response.status_code == 200:
            st.success('show tables successfully!')
            result = response.json()
            st.multiselect('Choose table', [table[0] for table in result['tables']])
            # st.write(result['tables']) # test

        else:
            st.write('An error occurred in showing table')
            st.warning(response.status_code)