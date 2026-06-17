import streamlit as st
import time

st.set_page_config(
    page_title="DriftShield",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ DriftShield")

st.write(
    "Welcome to DriftShield."
)

text = """


A production-ready Machine Learning Monitoring Platform.

An LLM response will be displayed here in very shortly so the animation will fell like 
an AI is repsonding the the users and giving answers.

More features coming soon...
"""

placeholder = st.empty()

rendered = ""

for char in text:
    rendered += char
    placeholder.markdown(rendered)
    time.sleep(0.01)