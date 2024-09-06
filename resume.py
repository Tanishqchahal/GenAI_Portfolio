import streamlit as st
import base64

def resume_page():
    with open("static/Tanishq_Chahal_Resume.pdf", "rb") as file:
        pdf_bytes = file.read()
    pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
    
    st.title("My Resume")
    st.markdown(f'<iframe src="data:application/pdf;base64,{pdf_base64}#zoom=110" width="80%" height="800"></iframe>', unsafe_allow_html=True)
