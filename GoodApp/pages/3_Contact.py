import streamlit as st
st.set_page_config(page_title="Contact", page_icon="🍏", layout="centered")

st.title("Contact")

st.markdown("We horen graag van u! Vul onderstaand formulier in om uw feedback of vragen met ons te delen:")

# Feedbackformulier
with st.form("feedback_form"):
    name = st.text_input("Naam")
    email = st.text_input("E-mail")
    feedback = st.text_area("Uw feedback")
    submitted = st.form_submit_button("Verzenden")

    if submitted:
        st.success("Bedankt voor uw feedback!")