import streamlit as st


def render_sidebar():
    st.sidebar.title("📌 Project Information")

    st.sidebar.markdown("""
    ### 🌍 AI Language Translation Tool

    **Tech Stack**
    - Python
    - Streamlit
    - Deep Translator

    **Features**
    - Multi-language Translation
    - Translation History
    - Download Translation
    - Character Counter

    **Internship**
    CodeAlpha AI Internship
    """)

    st.sidebar.markdown("---")

    st.sidebar.info(
        "Built as part of the CodeAlpha AI Internship Program."
    )