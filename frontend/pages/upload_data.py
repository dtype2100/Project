import streamlit as st
import pandas as pd
import requests

# Streamlit UI
st.title("Data Preprocessing Workflow")

uploaded_data = st.file_uploader("Upload a CSV file", type=["csv"])


if 'df' not in st.session_state:
    st.session_state['df'] = None

if 'filtered_df' not in st.session_state:
    st.session_state['filtered_df'] = None


if uploaded_data:
    st.session_state['df'] = pd.read_csv(uploaded_data)
    st.success('Data uploaded successfully!')

df = st.session_state['df']


if df is not None:
    with st.form('save data'):
        
        selected_columns = st.multiselect("Select columns", options=df.columns)
        table_name = st.text_input('Please write table name')
        
        if selected_columns:
        
            st.subheader("Filtered DataFrame")
    
            filtered_df = df[selected_columns]
            st.write(filtered_df)
            
            json_data = {
                'filtered_df': filtered_df.to_json(),
                'table_name': table_name
                }
            
        else:
            st.subheader("DataFrame")

            st.write(df)
            
            json_data = {
                'filtered_df': df.to_json(),
                'table_name': table_name
                }

        if st.form_submit_button('Save!'):
            response = requests.post('http://backend:8000/save_router/save_data', json=json_data)
            if response.status_code == 200:
                st.success('Save data successfully!')
            else:
                st.write('An error occurred in filter_data')
                st.warning(response.status_code)

    # with st.form('prepro_null'):    
    #     if st.session_state['filtered_df'] is not None:
    #         payload_null = st.multiselect('select null preprocessing', ['ffill', 'bfill', 'dropna'])
    #         if payload_null == 'ffill':
    #             prepro_null = filtered_df.fillna(method='ffill')
    #             st.write(prepro_null)
    #         if payload_null == 'bfill':
    #             prepro_null = filtered_df.fillna(method='bfill')
    #             st.write(prepro_null)
    #         if payload_null == 'dropna':
    #             prepro_null = filtered_df.dropna(axis=0)
    #             st.write(prepro_null)

    #         json_data =  {
    #             'payload_null': payload_null
    #         }
    #         response = requests.post('http://backend:8000/save_router/payload_null', json=json_data)   
    #         if response.status_code == 200:
    #             st.success('apply payload successfully!')
    #         else:
    #             st.write('An error occurred in prepro_null')
    #             st.warning(response.status_code)

    with st.form('show_tables'):
        if st.form_submit_button('show tables'):
            response = requests.get('http://backend:8000/select_router/select_data')   
            if response.status_code == 200:
                st.success('apply payload successfully!')
                result = response.json()
                st.write(result['tables']) # test

            else:
                st.write('An error occurred in select_database')
                st.warning(response.status_code)

else:
    st.warning("Please upload a CSV file to proceed.")