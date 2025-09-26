import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.header("🍕 Pizza")
    st.button("Order Pizza")

with col2:
    st.header("🥤 Drink")
    st.button("Order Drink")
