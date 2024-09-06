import streamlit as st


def home_page():
    img, desc = st.columns([1, 3])

    with img:
        st.image("static/profile-pic.png", width=230)

    with desc:
        st.title("Tanishq Chahal")
        st.subheader(
            "Software Developer | Machine Learning Engineer", divider="rainbow"
        )
        st.header("About Me")
        st.markdown(
            """
        <p style='font-size:20px;'>
            👋🏼 Hello, I'm Tanishq - a tech-driven problem solver, coding enthusiast, and innovative thinker.
        </p>

        <p style='font-size:20px;'>
            Currently pursuing a Bachelor's in Computer Science at McMaster University.
        </p>

        <p style='font-size:20px;'>
            In my tech journey, I've cultivated a deep curiosity for understanding how things work. With exposure to programming, web design, and data analytics, I've honed my analytical skills. I balance studies with diverse activities, emphasizing physical and mental well-being.
        </p>

        <p style='font-size:20px;'>
            With experience at McMaster's technology frontier, I bring analytical skills, a passion for innovation, innovative problem-solving, and a commitment to positive impact.
        </p>

        <p style='font-size:20px;'>
            Looking ahead, my ambitions lie in creating a positive impact through continuous learning and innovative endeavors. Let's connect and collaborate on exciting projects!
        </p>

        """, unsafe_allow_html=True)

    

