import streamlit as st
import base64

def resume_page():
    with open("static/Tanishq Chahal Resume.pdf", "rb") as file:
        pdf_bytes = file.read()
    pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
    
    st.title("My Resume")
        
    st.download_button(
        label="Download Resume",
        data=pdf_bytes,
        file_name="Tanishq Chahal Resume.pdf",
        mime="application/pdf"
    )

    st.image("static/Tanishq Chahal Resume.jpg", width=900)