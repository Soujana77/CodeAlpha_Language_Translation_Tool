import streamlit as st
from deep_translator import GoogleTranslator

# Page Configuration
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)
# Sidebar
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

# Session State
if "history" not in st.session_state:
    st.session_state.history = []
if "source_lang" not in st.session_state:
    st.session_state.source_lang = "English"

if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Hindi"
# Title
st.title("🌍 AI Language Translation Tool")

st.write(
    "Translate text between multiple languages using AI-powered translation."
)

# Supported Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

# Language Selection
col1, col2, col3 = st.columns([5, 1, 5])

with col1:
    source_language = st.selectbox(
        "Source Language",
        list(languages.keys()),
        index=list(languages.keys()).index(
            st.session_state.source_lang
        )
    )

with col2:
    st.write("")
    st.write("")

    if st.button("⇄"):
        st.session_state.source_lang, st.session_state.target_lang = (
            st.session_state.target_lang,
            st.session_state.source_lang
        )
        st.rerun()

with col3:
    target_language = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=list(languages.keys()).index(
            st.session_state.target_lang
        )
    )

st.session_state.source_lang = source_language
st.session_state.target_lang = target_language

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
        st.warning("Please enter some text to translate.")

    elif source_language == target_language:
        st.warning("Source and Target languages cannot be the same.")

    else:
        try:
            translated_text = GoogleTranslator(
                source=languages[source_language],
                target=languages[target_language]
            ).translate(user_text)

            # Save translation history
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

# Clear History Button
if st.session_state.history:
    if st.button("🗑 Clear History"):
        st.session_state.history = []
        st.rerun()

# Translation History
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