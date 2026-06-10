import streamlit as st


def load_css():
    st.markdown("""
    <style>

    .main {
        padding-top: 1rem;
    }

    .stButton > button {
        width: 100%;
        border-radius: 10px;
    }

    .stDownloadButton > button {
        width: 100%;
        border-radius: 10px;
    }

    </style>
    """, unsafe_allow_html=True)