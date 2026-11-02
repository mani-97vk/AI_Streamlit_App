import streamlit as st

st.title("AI-enabled Web Application")

st.write("Welcome to the AI-enabled Web Application")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Welcome {name}! Your application is running successfully.")
