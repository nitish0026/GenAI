import streamlit as st
st.title("Hello GenAI Team, Greetings for the day!!!")
name = st.text_input("Enter your Name here :")
about_yourself = st.text_area("Please provide your brief introduction here :")
click_button = st.button("Submit your details here :")
if click_button ==True:
            st.text("You have submitted your details now.")
            st.text(f"User Name : {name}")
            st.text(f"Your Introduction : {about_yourself}")

# pip install streamlit "proxy link"