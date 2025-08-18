import streamlit as st
import random

def login_system():
    st.sidebar.subheader("🔑 Admin Login")

    user = st.sidebar.text_input("Username")
    pwd = st.sidebar.text_input("Password", type="password")

    captcha_code = str(random.randint(10000, 99999))
    st.sidebar.text(f"Captcha: {captcha_code}")
    captcha_in = st.sidebar.text_input("Enter Captcha")

    if st.sidebar.button("Login"):
        if user == "admin" and pwd == "1234" and captcha_in == captcha_code:
            st.session_state["admin"] = True
            st.sidebar.success("✅ Login Successful")
        else:
            st.sidebar.error("❌ Invalid Credentials or Captcha")

if "admin" not in st.session_state:
    st.session_state["admin"] = False
