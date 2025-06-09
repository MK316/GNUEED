import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Padlet Embedded", layout="centered")

st.title("📝 Collaborative Wall: Padlet")

st.write("""
Welcome! Below is a live Padlet wall where you can share your ideas, reflections, or resources.
Just click and start contributing.
""")

# Replace this with your actual Padlet embed URL
padlet_url = "https://padlet.com/mirankim316/GNU_EED_QA"

# Display the Padlet
components.iframe(padlet_url, height=800, scrolling=True)
