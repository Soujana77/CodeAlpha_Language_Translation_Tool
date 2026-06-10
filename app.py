import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Application Title
st.title("🌍 Language Translation Tool")

# Description
st.write(
    "Translate text between multiple languages using AI-powered translation."
)

# Text Input Area
user_text = st.text_area(
    "Enter Text",
    height=150
)

# Translate Button
translate_button = st.button("Translate")

# Temporary Action
if translate_button:
    st.success("Translation functionality will be added in the next step.")