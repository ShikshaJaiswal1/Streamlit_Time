import streamlit as st

import pandas as pd

st.title("Chai sales Dashboard")

file =  st. file_uploader("Upload your file", type = ["csv"])

if file:
    df= pd.read_csv(file) 
    st.subheader("Data Preview")
    st.dataframe(df )
    
if file:
    st.subheader("Summary Stats")
    st.write(df.describe())
    
if file:
    cities = df["Region"].unique()
    selected_city = st.selectbox("Filter data by cities", cities)
    filtered_data = df[df["Region "] == selected_city]
    st.dataframe(filtered_data)            