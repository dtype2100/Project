import streamlit as st
import pandas as pd

# Streamlit UI
st.title("Streamlit to FastAPI Workflow")

uploaded_data = st.file_uploader("Upload a CSV file", type=["csv"])


if 'df' not in st.session_state:
    st.session_state['df'] = None

if uploaded_data:
    st.session_state['df'] = pd.read_csv(uploaded_data)
    st.success('Data uploaded successfully!')

df = st.session_state['df']

if df is not None:
    selected_columns = st.multiselect("Select columns", options=df.columns)
    if selected_columns:
        filtered_df = df[selected_columns]
        st.subheader("Filtered DataFrame")
        st.write(filtered_df)
else:
    st.warning("Please upload a CSV file to proceed.")