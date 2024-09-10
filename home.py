import streamlit as st


def home_page():
    img, desc = st.columns([1, 3])

    with img:
        st.image("static/profile.png", width=250)

    with desc:
        st.title("Tanishq Chahal")
        st.subheader(
            "Software Developer | Machine Learning Enthusiast", divider="red"
        )
        st.header("About Me")
        st.markdown(
            """
        <p style='font-size:20px;'>
            👋🏼 Hi, I'm Tanishq - a passionate <span style="color: #ff4b4b;">Data, AI, and Machine Learning</span> enthusiast, and problem-solving coder.
        </p>

        <p style='font-size:20px;'>
            I'm currently pursuing a Bachelor's in <span style="color: #ff4b4b;">Computer Science at McMaster University</span>, where my journey in tech has fueled my passion for understanding and innovating with cutting-edge technology.        
        </p>

        <p style='font-size:20px;'>
            With a strong focus on Data Science, Artificial Intelligence, and Machine Learning, I thrive on leveraging my coding and analytical skills to build intelligent systems that <span style="color: #ff4b4b;">solve real-world challenges</span>.        
        </p>

        <p style='font-size:20px;'>
            As I explore the frontiers of AI and Machine Learning, I'm driven to create <span style="color: #ff4b4b;">impactful solutions</span> and continuously push the boundaries of innovation.        
        </p>

        <p style='font-size:20px;'>
            <span style="color: #ff4b4b;">Let's connect</span> and collaborate on transformative projects that shape the future!        
        </p>

        """, unsafe_allow_html=True)

    

