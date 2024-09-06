import streamlit as st
from chain import chat

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm Tanishq's AI assistant, Buddy. How may I assist you today?"}
        ]


def chat_page():
    initialize_session_state()

    st.title("AI Assistant")
    st.subheader("Chat with Buddy to know more about Me")

    prompt = st.chat_input("Enter your prompt")
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
    
    if st.session_state.messages[-1]["role"] == "user":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat(prompt)
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

