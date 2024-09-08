import streamlit as st

def projects(name, image, repo_link):
    st.image(image, width=300)
    st.subheader(f"[{name}]({repo_link})")
    st.write("[View GitHub Repo](%s)" % repo_link)
    st.write("")

def projects_page():
    st.title("Projects")
    st.subheader("Here are some of the projects I have worked on:", divider="red")
    proj1, proj2, proj3 = st.columns(3)
    with proj1:
        projects(
            name="Voice Assistant Bot",
            image="static/voice_bot.jpg",
            repo_link="https://github.com/Tanishqchahal/Voice_assistant_bot"
        )
    with proj2:
        projects(
            name="Data Visualizing Agent",
            image="static/data007.png",
            repo_link="https://github.com/Tanishqchahal/Data007_data-visualiser"
        )
    with proj3:
        projects(
            name="Object Detection with R-CNN",
            image="static/resnet.png",
            repo_link="https://github.com/Tanishqchahal/Object_detection_Faster_R-CNN"
        )    
        