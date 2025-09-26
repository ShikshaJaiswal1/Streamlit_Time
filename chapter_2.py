import streamlit as st

st.title("Chai maker app")

if st.button("Make Chai"):
    st.write("Chai is being made...")
    st.balloons()
    st.success("Your chai is ready! Enjoy!")
    
add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chai.")    
    
tea_type = st.radio("Select your tea type", ["Black Tea", "Green Tea", "Herbal Tea"])


if tea_type:
    st.write(f"You selected: {tea_type}. Great choice!")
    
flavour = st.selectbox("Select a flavour", ["Ginger", "Cardamom", "Tulsi", "Lemon"])       

st.write(f"You selected: {flavour}. Delicious!")


sugar = st.slider("Select sugar level", 0, 5, 0)

st.write(f"Sugar level set to: {sugar}")


cups = st.number_input("Number of cups", min_value=1, max_value=10, value=1)

st.write("Number of cups:", cups) 


name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}! Your chai will be ready soon.")


dob = st.date_input("Enter your date of birth")
if dob:
    st.write(f"Your date of birth is: {dob}")