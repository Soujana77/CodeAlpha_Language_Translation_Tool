import streamlit as st

from src.data.languages import LANGUAGES
from src.services.translator import translate_text
from src.components.sidebar import render_sidebar
from src.styles.custom_css import load_css


# Page Config
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Load CSS
load_css()

# Sidebar
render_sidebar()

# Session State
if "history" not in st.session_state:
    st.session_state.history = []

# Title
st.title("🌍 AI Language Translation Tool")

st.write(
    "Translate text between multiple languages using AI-powered translation."
)

# Language Selection
col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Source Language",
        list(LANGUAGES.keys())
    )

with col2:
    target_language = st.selectbox(
        "Target Language",
        list(LANGUAGES.keys()),
        index=1
    )

# Input Text
user_text = st.text_area(
    "Enter Text",
    height=150,
    placeholder="Type or paste text here..."
)

# Character Counter
st.caption(f"Characters: {len(user_text)}")

# Translate Button
if st.button("Translate", use_container_width=True):

    if user_text.strip() == "":
        st.warning("Please enter some text.")

    elif source_language == target_language:
        st.warning(
            "Source and Target languages cannot be the same."
        )

    else:
        try:

            translated_text = translate_text(
                user_text,
                LANGUAGES[source_language],
                LANGUAGES[target_language]
            )

            st.session_state.history.append({
                "source_language": source_language,
                "target_language": target_language,
                "original_text": user_text,
                "translated_text": translated_text
            })

            st.subheader("Translated Text")

            st.text_area(
                "Output",
                translated_text,
                height=150
            )

            st.download_button(
                label="⬇ Download Translation",
                data=translated_text,
                file_name="translation.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Translation Error: {e}")

# Clear History
if st.session_state.history:
    if st.button("🗑 Clear History"):
        st.session_state.history = []
        st.rerun()

# History
if st.session_state.history:

    st.markdown("---")
    st.subheader("📜 Translation History")

    for item in reversed(st.session_state.history):

        with st.expander(
            f"{item['source_language']} → {item['target_language']}"
        ):
            st.write("**Original Text:**")
            st.write(item["original_text"])

            st.write("**Translated Text:**")
            st.write(item["translated_text"])