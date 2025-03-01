import streamlit as st

def contact_form():
 with st.form("contact_form"):
    name=st.text_input("Your Name")
    email=st.text_input("Your Email")
    message=st.text_input("Your Message..")
    submit_button=st.form_submit_button("Submit")
    
    if submit_button:
        if not name:
            st.error("Please provide your name.")
            st.stop()

        if not email:
            st.error("Please provide your Email address.")
            st.stop()

        if not message:
            st.error("Message field is empty.")
            st.stop()

        else:
           st.success("Your message successfully sent!")