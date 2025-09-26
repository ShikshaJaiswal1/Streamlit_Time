import streamlit as st

st.title("Hello World! ")

st.subheader("This is a subheader. ")

st.text("This is a simple text element. ")

st.write("This is a write element that can display various types of content.")



chai = st.selectbox("Your Favorite Chai", ["Masala Chai", "Ginger Chai", "Cardamon Chai", "Tulsi Chai", "Lemon chai"])

st.write(f"You selected: {chai}. Excellent choice.")

st.success("Your chai has been brewed. Enjoy! ")