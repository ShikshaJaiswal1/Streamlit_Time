import streamlit as st

st.title("Chai Taste Poll")


col1, col2 = st.columns(2)

with col1:
    st.header(" ☕️ Masala Chai")
    st.image("https://i.pinimg.com/1200x/43/6d/a4/436da44985d61c713fbc4e2676e18a68.jpg", width=200)
    vote1 = st.button("Vote Masala Chai")
        
with col2:
    st.header(" 🍋 Lemon Chai")
    st.image("https://i.pinimg.com/1200x/a3/3c/cd/a33ccdfdfe21d98106e2c3f252d08b7a.jpg", width=200)
    vote2 = st.button("Vote Lemon Chai")
    
if vote1:
    st.success("You voted for Masala Chai. Great choice!")
    
if vote2:
    st.success("You voted for Lemon Chai. Excellent choice!")    


name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Select your favorite chai", ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Tulsi Chai", "Lemon Chai"])  


with st.expander("Show chai making instructions. "):
    st.write("""
    1. Boil water.
    2. Add tea leaves and spices.
    3. Let it simmer.
    4. Add milk and sugar.
    5. Strain and serve hot.
    """)  
    
st.markdown(" ## Welcome to chai app. Enjoy your stay! ☕️")    
st.info("This app is created to celebrate the love for chai. Vote for your favorite chai and share your thoughts in the sidebar.")
st.markdown('> blockquote')