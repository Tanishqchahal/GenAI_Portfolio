import streamlit as st
import requests

def send_to_webhook(name, email, message):
    url = "https://api.jsonbin.io/v3/b/66da2bd7ad19ca34f8a08f99"
    data = {"name": name, "email": email, "message": message}
    headers = {"Content-Type": "application/json", "X-Master-Key": "$2a$10$pRVvJpifOYS8EcKXwzCM.el7XAMWGGANVxN9FCs7dJCJGKbFltvii"}
    response = requests.put(url, json=data, headers=headers)
    return response.status_code == 200


def contact_page():
    st.markdown(
        """
    <style>
    .contact-form {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        font-family: Arial, sans-serif;
    }
    .contact-form h2 {
        color: #0078D7;
        text-align: center;
        font-size: 28px;
    }
    .contact-form label {
        font-size: 16px;
        color: #333;
    }
    .contact-form input, .contact-form textarea {
        width: 100%;
        padding: 10px;
        margin: 5px 0 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-sizing: border-box;
    }
    .contact-form button {
        background-color: #0078D7;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .contact-form button:hover {
        background-color: #005bb5;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


# Create a form
    with st.form(key="contact_form"):

        st.markdown("<h2>Let's Connect</h2>", unsafe_allow_html=True)

        # Form fields
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        # Submit button
        submit_button = st.form_submit_button(label="Send Message")

        st.markdown("</div>", unsafe_allow_html=True)

    # Handle form submission
    if submit_button:
        if send_to_webhook(name, email, message):
            st.success("Message sent successfully!")
        else:
            st.error("Failed to send message.")
