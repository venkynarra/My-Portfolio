import streamlit as st


st.header("Contact ME")

with st.form(key = "email_forms"):
    user_email = st.text_input("your email address")
    message = st.text_area("your message here")
    button = st.form_submit_button("Submit")
    if button:
        print(" I was pressed")