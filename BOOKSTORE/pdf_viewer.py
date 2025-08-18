import streamlit as st
import os

st.title("📖 PDF Viewer")

pdf_path = st.session_state.get("selected_pdf", None)

if pdf_path and os.path.exists(pdf_path):
    st.markdown(
        f'<iframe src="/{os.path.abspath(pdf_path)}" width="100%" height="600px"></iframe>',
        unsafe_allow_html=True
    )
else:
    st.error("❌ No PDF selected or file missing.")
