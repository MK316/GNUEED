import streamlit as st

# Google Drive video ID
file_id = "1sJ6zdP-6-lW__m8y4lX-qRQhnVUoTYGc"
# https://drive.google.com/file/d/1sJ6zdP-6-lW__m8y4lX-qRQhnVUoTYGc/view?usp=sharing
# Embed video using an iframe (Google Drive preview)
video_html = f"""
<iframe src="https://drive.google.com/file/d/{file_id}/preview" width="640" height="360" allow="autoplay"></iframe>
"""

st.markdown("### 📹 Video Preview from Google Drive", unsafe_allow_html=True)
st.markdown(video_html, unsafe_allow_html=True)


file_id2 = "1roW9ovZC7UA8mncElEdz0WFVURZwcOny"
# https://drive.google.com/file/d/1sJ6zdP-6-lW__m8y4lX-qRQhnVUoTYGc/view?usp=sharing
# Embed video using an iframe (Google Drive preview)
video_html = f"""
<iframe src="https://drive.google.com/file/d/{file_id2}/preview" width="640" height="360" allow="autoplay"></iframe>
"""

st.markdown("### 📹 Video Preview from Google Drive 2", unsafe_allow_html=True)
st.markdown(video_html, unsafe_allow_html=True)
