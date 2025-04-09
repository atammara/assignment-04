# data_app.py
import streamlit as st
import pandas as pd

# Upload data
uploaded_file = st.file_uploader("Choose CSV")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Show raw data
    st.write("Raw Data:", df)
    
    # Interactive filters
    col = st.selectbox("Select column", df.columns)
    st.write(df[col].describe())
    
    # Visualization
    chart_type = st.radio("Chart type:", ["Line", "Bar"])
    if chart_type == "Line":
        st.line_chart(df[col])
    else:
        st.bar_chart(df[col])