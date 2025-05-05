import streamlit as st

st.set_page_config(layout="wide")
col1, col2, = st.columns(2) #opening colums for to fit in the web page
with col1:
    st.image("images/ss_myphoto.png")
with col2:
    st.title("Venkateswara Narra")
    content = """ 
    Hi, I’m Venkateswara Rao Narra, a full-stack Python developer with a strong interest in backend systems, cloud, and real-time web apps. I recently completed my Master’s in Computer Science from George Mason University, where I not only sharpened my technical skills in Python, ML, and cloud development — but also learned the value of consistency, time management, and collaboration through team projects and hands-on learning.

Outside of tech, I’m big on staying active — I enjoy going to the gym regularly, practicing yoga to keep my mind balanced, and playing cricket whenever I get the chance. These hobbies keep me disciplined, focused, and energized. I believe in always pushing my limits — whether it's writing clean code, learning a new framework, or improving my fitness and mindset every day.


    """
    st.info(content)
