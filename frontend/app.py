import streamlit as st
import sys
import os

sys.path.append(os.path.abspath('./pages/'))

pages = {
    'Home': [
        st.Page('./pages/home.py', title='Main page')
    ]
    ,
    "Upload data": [
        st.Page('./pages/upload_data.py', title='Upload data and Create table')
    ]
}

pg = st.navigation(pages)
pg.run()