import streamlit as st
import pandas as pd
import requests

# Streamlit UI
st.title("Data Preprocessing Workflow")

uploaded_data = st.file_uploader("Upload a CSV file", type=["csv"])


if 'df' not in st.session_state:
    st.session_state['df'] = None

if uploaded_data:
    st.session_state['df'] = pd.read_csv(uploaded_data)
    st.success('Data uploaded successfully!')

df = st.session_state['df']

if df is not None:
    with st.form('filter_data'):
        selected_columns = st.multiselect("Select columns", options=df.columns)
        table_name = st.text_input('Please write table name')
        if selected_columns:
            filtered_df = df[selected_columns]
            st.subheader("Filtered DataFrame")
            st.write(filtered_df)
            
            json_data = {'filtered_df': filtered_df.to_json(),
                        'table_name': table_name}
        if st.form_submit_button('Save!'):
            response = requests.post('http://backend:8000/save_router/save_data', json=json_data)
            if response.status_code == 200:
                st.success('Save data successfully!')
            else:
                st.write('An error occurred')
                st.warning(response.status_code)
else:
    st.warning("Please upload a CSV file to proceed.")