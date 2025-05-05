import streamlit as st
from send_email import send_email

st.header("Contact ME")

with st.form(key="email_forms"):
    user_email = st.text_input("your email address")
    raw_message = st.text_area("your message here")
    message = f"""\
subject: new email from {user_email}
    
    
from: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("your email was sent successfully")
