import streamlit as st
from datetime import datetime
import time

from src.data.languages import LANGUAGES
from src.services.translator import translate_text
from src.components.sidebar import render_sidebar
from src.styles.custom_css import load_css


# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
load_css()

# Sidebar
render_sidebar()

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
if "history" not in st.session_state:
    st.session_state.history = []

if "translated_text" not in st.session_state:
    st.session_state.translated_text = None

if "show_success" not in st.session_state:
    st.session_state.show_success = False


# ============================================================================
# HERO HEADER SECTION
# ============================================================================
st.markdown("""
<div class='hero-header'>
    <div class='hero-content'>
        <h1 class='hero-title'>🌍 AI Language Translation</h1>
        <p class='hero-subtitle'>Break language barriers with AI-powered translation</p>
        <div class='hero-badges'>
            <span class='badge'>✨ Professional</span>
            <span class='badge'>⚡ Fast</span>
            <span class='badge'>🔒 Secure</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)


# ============================================================================
# MAIN CONTENT AREA
# ============================================================================
# Language Selection Section
st.markdown("<h2 class='section-title'>📝 Language Configuration</h2>", unsafe_allow_html=True)

lang_col1, lang_swap_col, lang_col2 = st.columns([1, 0.1, 1])

with lang_col1:
    st.markdown("<div class='input-label'>Source Language</div>", unsafe_allow_html=True)
    source_language = st.selectbox(
        "Select source language",
        list(LANGUAGES.keys()),
        label_visibility="collapsed",
        key="source_lang"
    )

with lang_swap_col:
    st.markdown("<div style='text-align: center; margin-top: 22px;'>", unsafe_allow_html=True)
    if st.button("⇅", help="Swap languages", key="swap_btn", use_container_width=True):
        source_lang_key = "source_lang"
        target_lang_key = "target_lang"
        if source_lang_key in st.session_state and target_lang_key in st.session_state:
            st.session_state[source_lang_key], st.session_state[target_lang_key] = (
                st.session_state[target_lang_key],
                st.session_state[source_lang_key]
            )
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

with lang_col2:
    st.markdown("<div class='input-label'>Target Language</div>", unsafe_allow_html=True)
    target_language = st.selectbox(
        "Select target language",
        list(LANGUAGES.keys()),
        index=1,
        label_visibility="collapsed",
        key="target_lang"
    )

st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)


# ============================================================================
# INPUT SECTION
# ============================================================================
st.markdown("<h2 class='section-title'>📌 Input Text</h2>", unsafe_allow_html=True)

st.markdown("<div class='card-container'>", unsafe_allow_html=True)

col_char1, col_char2 = st.columns([0.7, 0.3])
with col_char1:
    st.markdown("<div class='input-label'>Enter text to translate</div>", unsafe_allow_html=True)
with col_char2:
    st.markdown(f"<div class='char-counter'><strong>Characters:</strong> {len(st.session_state.get('current_text', ''))}</div>", unsafe_allow_html=True)

user_text = st.text_area(
    "text_input",
    height=180,
    placeholder="📝 Type or paste your text here...",
    label_visibility="collapsed",
    key="current_text"
)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)


# ============================================================================
# ACTION BUTTONS
# ============================================================================
btn_col1, btn_col2, btn_col3 = st.columns(3)

with btn_col1:
    translate_clicked = st.button(
        "🚀 Translate",
        use_container_width=True,
        key="translate_btn"
    )

with btn_col2:
    if st.session_state.history:
        clear_clicked = st.button(
            "🗑️ Clear History",
            use_container_width=True,
            key="clear_btn"
        )
    else:
        st.markdown("<div style='height: 38px;'></div>", unsafe_allow_html=True)

with btn_col3:
    st.markdown("<div style='height: 38px;'></div>", unsafe_allow_html=True)

st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)


# ============================================================================
# TRANSLATION LOGIC
# ============================================================================
if translate_clicked:
    if user_text.strip() == "":
        st.error("❌ Please enter some text to translate.")
        st.stop()

    elif source_language == target_language:
        st.error("⚠️ Source and target languages cannot be the same.")
        st.stop()

    else:
        try:
            # Show loading state
            with st.spinner("⏳ Translating... Please wait"):
                translated_text = translate_text(
                    user_text,
                    LANGUAGES[source_language],
                    LANGUAGES[target_language]
                )

            # Store in session state
            st.session_state.translated_text = translated_text

            # Add to history with timestamp
            st.session_state.history.append({
                "source_language": source_language,
                "target_language": target_language,
                "original_text": user_text,
                "translated_text": translated_text,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            # Show success message
            st.success("✅ Translation completed successfully!")

        except Exception as e:
            st.error(f"❌ Translation Error: {str(e)}")
            st.stop()


# ============================================================================
# TRANSLATION OUTPUT SECTION
# ============================================================================
if st.session_state.translated_text:
    st.markdown("<h2 class='section-title'>✨ Translated Output</h2>", unsafe_allow_html=True)

    st.markdown("<div class='card-container output-card'>", unsafe_allow_html=True)

    col_lang1, col_lang2 = st.columns([0.7, 0.3])
    with col_lang1:
        st.markdown(
            f"<div class='output-language'>{source_language} → {target_language}</div>",
            unsafe_allow_html=True
        )
    with col_lang2:
        st.markdown(
            f"<div class='char-counter'><strong>Characters:</strong> {len(st.session_state.translated_text)}</div>",
            unsafe_allow_html=True
        )

    st.markdown("<div class='spacing-small'></div>", unsafe_allow_html=True)

    st.text_area(
        "translated_output",
        st.session_state.translated_text,
        height=180,
        disabled=True,
        label_visibility="collapsed"
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

    # Output Action Buttons
    output_col1, output_col2 = st.columns(2)

    with output_col1:
        # Copy Button
        copy_code = f"""
        <script>
        function copyTranslation() {{
            const text = `{st.session_state.translated_text}`;
            navigator.clipboard.writeText(text).then(() => {{
                alert('✅ Translation copied to clipboard!');
            }});
        }}
        </script>
        <button onclick="copyTranslation()" class="copy-btn">📋 Copy Translation</button>
        """
        st.markdown(copy_code, unsafe_allow_html=True)

    with output_col2:
        st.download_button(
            label="⬇️ Download Translation",
            data=st.session_state.translated_text,
            file_name=f"translation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )

    st.markdown("<div class='spacing-large'></div>", unsafe_allow_html=True)


# Clear History
if st.session_state.history and "clear_clicked" in locals() and clear_clicked:
    st.session_state.history = []
    st.session_state.translated_text = None
    st.rerun()


# ============================================================================
# TRANSLATION HISTORY SECTION
# ============================================================================
if st.session_state.history:
    st.markdown("<h2 class='section-title'>📜 Translation History</h2>", unsafe_allow_html=True)

    # Statistics
    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

    with stats_col1:
        st.markdown(f"""
        <div class='stat-card'>
            <div class='stat-number'>{len(st.session_state.history)}</div>
            <div class='stat-label'>Total Translations</div>
        </div>
        """, unsafe_allow_html=True)

    with stats_col2:
        total_chars = sum(len(item['original_text']) for item in st.session_state.history)
        st.markdown(f"""
        <div class='stat-card'>
            <div class='stat-number'>{total_chars}</div>
            <div class='stat-label'>Characters</div>
        </div>
        """, unsafe_allow_html=True)

    with stats_col3:
        unique_langs = set()
        for item in st.session_state.history:
            unique_langs.add(item['source_language'])
            unique_langs.add(item['target_language'])
        st.markdown(f"""
        <div class='stat-card'>
            <div class='stat-number'>{len(unique_langs)}</div>
            <div class='stat-label'>Languages Used</div>
        </div>
        """, unsafe_allow_html=True)

    with stats_col4:
        st.markdown(f"""
        <div class='stat-card'>
            <div class='stat-number'>⚡</div>
            <div class='stat-label'>Lightning Fast</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)

    # History Items
    for idx, item in enumerate(reversed(st.session_state.history)):
        with st.expander(
            f"📌 {item['source_language']} → {item['target_language']} • {item['timestamp']}",
            expanded=False
        ):
            history_col1, history_col2 = st.columns(2)

            with history_col1:
                st.markdown("<div class='history-section-title'>Original Text</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='history-text'>{item['original_text']}</div>", unsafe_allow_html=True)

            with history_col2:
                st.markdown("<div class='history-section-title'>Translated Text</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='history-text'>{item['translated_text']}</div>", unsafe_allow_html=True)

    st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)