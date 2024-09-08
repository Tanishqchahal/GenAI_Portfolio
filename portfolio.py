import streamlit as st
from linkedin_badge import LINKEDIN_PROFILE
from home import home_page
from resume import resume_page
from projects import projects_page
from contact import contact_page
from chat import chat_page
import streamlit.components.v1 as components

st.set_page_config(page_title="Tanishq's Portfolio", page_icon="👨🏼‍💻", layout="wide", initial_sidebar_state="expanded")

# Initialize session state for the page
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Function to update page
def set_page(page_name):
    st.session_state.page = page_name

with st.sidebar:
    st.image("static/profile-pic.png", width=150)
    st.title("Tanishq's Portfolio")
    page = st.selectbox("Select Page", ["Home", "AI Assistant", "Resume", "Projects", "Connect"], 
                        index=["Home", "AI Assistant", "Resume", "Projects", "Connect"].index(st.session_state.page))
    components.html(LINKEDIN_PROFILE, height=400, width=500)

# Update session state when selectbox changes
if page != st.session_state.page:
    set_page(page)

if st.session_state.page == "Home":
    home_page()
    _, underdesc = st.columns([1, 3])

    with underdesc:
        button1, button2, button3, button4 = st.columns(4)
        
        with button1:
            st.button("Chat with Buddy", on_click=set_page, args=("AI Assistant",), type="primary" , use_container_width=True)

        with button2:
            st.button("Resume", on_click=set_page, args=("Resume",), type="primary", use_container_width=True)

        with button3:
            st.button("Projects", on_click=set_page, args=("Projects",), type="primary", use_container_width=True)

        with button4:
            st.button("Connect", on_click=set_page, args=("Connect",), type="primary", use_container_width=True)

elif st.session_state.page == "AI Assistant":
    chat_page()

elif st.session_state.page == "Resume":
    resume_page()

elif st.session_state.page == "Projects":
    projects_page()

elif st.session_state.page == "Connect":
    contact_page()


