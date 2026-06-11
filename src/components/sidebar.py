import streamlit as st


def render_sidebar():
    """
    Render a professional, modern sidebar with project information,
    tech stack, features, and developer details.
    """

    # Sidebar Header
    st.sidebar.markdown("""
    <style>
    .sidebar-header {
        text-align: center;
        padding: 1.5rem 0;
        border-bottom: 2px solid rgba(15, 111, 255, 0.2);
        margin-bottom: 1.5rem;
    }
    
    .sidebar-header h2 {
        margin: 0;
        color: #0F6FFF;
        font-size: 1.25rem;
        font-weight: 700;
    }
    
    .sidebar-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    .sidebar-section {
        margin: 1.5rem 0;
        padding: 1rem;
        background: linear-gradient(135deg, rgba(15, 111, 255, 0.05), rgba(15, 111, 255, 0.02));
        border-radius: 10px;
        border-left: 3px solid #0F6FFF;
    }
    
    .sidebar-section h3 {
        margin: 0 0 0.75rem 0;
        color: #0F6FFF;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 700;
    }
    
    .sidebar-section p {
        margin: 0.5rem 0;
        color: #1F2937;
        font-size: 0.85rem;
        line-height: 1.5;
    }
    
    .feature-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .feature-list li {
        padding: 0.5rem 0;
        color: #1F2937;
        font-size: 0.85rem;
        display: flex;
        align-items: flex-start;
    }
    
    .feature-list li::before {
        content: "✓";
        color: #10B981;
        font-weight: 700;
        margin-right: 0.5rem;
        font-size: 0.95rem;
    }
    
    .tech-badge {
        display: inline-block;
        background: #0F6FFF;
        color: white;
        padding: 0.35rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 0.25rem 0.25rem 0.25rem 0;
        text-transform: uppercase;
        letter-spacing: 0.3px;
    }
    
    .divider-light {
        height: 1px;
        background: rgba(15, 111, 255, 0.2);
        margin: 1.5rem 0;
    }
    
    .info-box {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(16, 185, 129, 0.05));
        border-left: 3px solid #10B981;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
    }
    
    .info-box p {
        margin: 0;
        color: #1F2937;
        font-size: 0.85rem;
        line-height: 1.5;
    }
    
    .stat-mini {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.5rem 0;
        font-size: 0.85rem;
        color: #1F2937;
        border-bottom: 1px solid rgba(15, 111, 255, 0.1);
    }
    
    .stat-mini:last-child {
        border-bottom: none;
    }
    
    .stat-value {
        font-weight: 700;
        color: #0F6FFF;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.sidebar.markdown("""
    <div class='sidebar-header'>
        <div class='sidebar-icon'>🌍</div>
        <h2>Translation Tool</h2>
    </div>
    """, unsafe_allow_html=True)

    # Project Information Section
    st.sidebar.markdown("""
    <div class='sidebar-section'>
        <h3>📋 About</h3>
        <p><strong>AI Language Translation Tool</strong> is a modern, professional application for translating text between multiple languages using Google Translate API through deep-translator.</p>
    </div>
    """, unsafe_allow_html=True)

    # Features Section
    st.sidebar.markdown("""
    <div class='sidebar-section'>
        <h3>✨ Features</h3>
        <ul class='feature-list'>
            <li>Multi-language translation</li>
            <li>Real-time character counter</li>
            <li>Translation history with timestamps</li>
            <li>Download translations as files</li>
            <li>Copy to clipboard functionality</li>
            <li>Language swap button</li>
            <li>Professional UI/UX design</li>
            <li>Responsive layout</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Tech Stack Section
    st.sidebar.markdown("""
    <div class='sidebar-section'>
        <h3>🛠️ Tech Stack</h3>
        <div>
            <span class='tech-badge'>Python</span>
            <span class='tech-badge'>Streamlit</span>
            <span class='tech-badge'>Deep-Translator</span>
            <span class='tech-badge'>Google Translate</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Languages Supported Section
    st.sidebar.markdown("""
    <div class='sidebar-section'>
        <h3>🌐 Supported Languages</h3>
        <p>11+ Languages including:</p>
        <p style='font-size: 0.80rem; color: #6B7280;'>
        English, Hindi, Kannada, Tamil, Telugu, Malayalam, French, German, Spanish, Japanese, Chinese
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Developer Section
    st.sidebar.markdown("""
    <div class='sidebar-section'>
        <h3>👨‍💻 Developer</h3>
        <p><strong>Portfolio Project</strong></p>
        <p>Built as a showcase of modern web development with Python and Streamlit, demonstrating UI/UX best practices and professional code structure.</p>
    </div>
    """, unsafe_allow_html=True)

    # Internship Section
    st.sidebar.markdown("""
    <div class='sidebar-section'>
        <h3>🎓 Internship Program</h3>
        <p><strong>CodeAlpha AI Internship</strong></p>
        <p>This project was developed as part of the CodeAlpha AI Internship Program, showcasing practical application of AI and modern web technologies.</p>
    </div>
    """, unsafe_allow_html=True)

    # Divider
    st.sidebar.markdown("<div class='divider-light'></div>", unsafe_allow_html=True)

    # Info Box
    st.sidebar.markdown("""
    <div class='info-box'>
        <p><strong>💡 Tip:</strong> Use the swap button (⇅) to quickly interchange source and target languages. All translations are stored in history for easy reference.</p>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.sidebar.markdown("""
    <div style='text-align: center; padding-top: 1.5rem; border-top: 1px solid rgba(15, 111, 255, 0.2); color: #6B7280; font-size: 0.75rem;'>
        <p style='margin: 0.5rem 0;'><strong>v1.0 - Professional Edition</strong></p>
        <p style='margin: 0;'>Built with ❤️ using Streamlit</p>
    </div>
    """, unsafe_allow_html=True)