import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Padlet Embedded", layout="centered")

st.title("📝 Feedback: Padlet")

st.write("""
Welcome! Use the live Padlet wall below to ask questions, share feedback, or respond to others.
Click anywhere on the board to post—your insights and participation are always appreciated.
""")

# Replace this with your actual Padlet embed URL
padlet_url = "https://padlet.com/mirankim316/GNU_EED_QA"

# Display the Padlet
components.iframe(padlet_url, height=800, scrolling=True)
