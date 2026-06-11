import streamlit as st


def load_css():
    """
    Load modern, professional CSS styling for the translation tool.
    Includes hero sections, cards, buttons, animations, and responsive design.
    """
    st.markdown("""
    <style>
    
    /* ============================================================================
       ROOT & GENERAL STYLES
       ============================================================================ */
    
    :root {
        --primary-color: #0F6FFF;
        --primary-dark: #0051CC;
        --primary-light: #E3F2FD;
        --success-color: #10B981;
        --warning-color: #F59E0B;
        --danger-color: #EF4444;
        --text-primary: #1F2937;
        --text-secondary: #6B7280;
        --text-light: #F3F4F6;
        --border-color: #E5E7EB;
        --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    * {
        box-sizing: border-box;
    }
    
    body {
        color: var(--text-primary);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    }
    
    
    /* ============================================================================
       MAIN CONTAINER & LAYOUT
       ============================================================================ */
    
    .main {
        padding: 2rem 1rem;
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
        min-height: 100vh;
    }
    
    .block-container {
        padding: 0 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    
    /* ============================================================================
       HERO HEADER SECTION
       ============================================================================ */
    
    .hero-header {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
        border-radius: var(--radius-lg);
        padding: 3rem 2rem;
        margin-bottom: 2rem;
        color: white;
        box-shadow: var(--shadow-lg);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-header::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 300px;
        height: 300px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        z-index: 0;
    }
    
    .hero-header::after {
        content: '';
        position: absolute;
        bottom: -30%;
        left: -5%;
        width: 250px;
        height: 250px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 50%;
        z-index: 0;
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.95;
        margin: 0 0 1.5rem 0;
        font-weight: 300;
        line-height: 1.6;
    }
    
    .hero-badges {
        display: flex;
        gap: 0.75rem;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    .badge {
        background: rgba(255, 255, 255, 0.2);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
    }
    
    
    /* ============================================================================
       DIVIDERS & SPACING
       ============================================================================ */
    
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--border-color), transparent);
        margin: 2rem 0;
    }
    
    .spacing {
        height: 2rem;
    }
    
    .spacing-small {
        height: 1rem;
    }
    
    .spacing-large {
        height: 3rem;
    }
    
    
    /* ============================================================================
       SECTION TITLES
       ============================================================================ */
    
    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 2rem 0 1.25rem 0;
        letter-spacing: -0.01em;
        position: relative;
        padding-left: 0.5rem;
    }
    
    .section-title::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 1.5em;
        background: linear-gradient(180deg, var(--primary-color), var(--primary-dark));
        border-radius: 2px;
    }
    
    
    /* ============================================================================
       CARD CONTAINERS
       ============================================================================ */
    
    .card-container {
        background: white;
        border-radius: var(--radius-md);
        padding: 1.75rem;
        box-shadow: var(--shadow-md);
        border: 1px solid var(--border-color);
        transition: var(--transition);
    }
    
    .card-container:hover {
        box-shadow: var(--shadow-lg);
        border-color: var(--primary-light);
    }
    
    .output-card {
        background: linear-gradient(135deg, #ffffff 0%, var(--primary-light) 100%);
        border: 2px solid var(--primary-light);
    }
    
    
    /* ============================================================================
       INPUT LABELS
       ============================================================================ */
    
    .input-label {
        font-size: 0.95rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.75rem;
        display: block;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    
    /* ============================================================================
       CHARACTER COUNTER
       ============================================================================ */
    
    .char-counter {
        font-size: 0.85rem;
        color: var(--text-secondary);
        background: var(--primary-light);
        padding: 0.5rem 0.75rem;
        border-radius: var(--radius-sm);
        display: inline-block;
        font-weight: 500;
    }
    
    
    /* ============================================================================
       TEXT AREA STYLING
       ============================================================================ */
    
    .stTextArea > div > div > textarea {
        border: 2px solid var(--border-color);
        border-radius: var(--radius-md) !important;
        padding: 1rem !important;
        font-size: 0.95rem !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', monospace;
        line-height: 1.6;
        resize: vertical;
        transition: var(--transition);
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 3px var(--primary-light) !important;
    }
    
    .stTextArea > div > div > textarea::placeholder {
        color: var(--text-secondary);
        opacity: 0.7;
    }
    
    
    /* ============================================================================
       SELECT BOX STYLING
       ============================================================================ */
    
    .stSelectbox > div > div > select {
        border: 2px solid var(--border-color);
        border-radius: var(--radius-md);
        padding: 0.75rem;
        font-size: 0.95rem;
        color: var(--text-primary);
        background-color: white;
        cursor: pointer;
        transition: var(--transition);
    }
    
    .stSelectbox > div > div > select:hover {
        border-color: var(--primary-color);
    }
    
    .stSelectbox > div > div > select:focus {
        outline: none;
        border-color: var(--primary-color);
        box-shadow: 0 0 0 3px var(--primary-light);
    }
    
    
    /* ============================================================================
       BUTTON STYLING
       ============================================================================ */
    
    .stButton > button {
        border-radius: var(--radius-md);
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 0.95rem;
        letter-spacing: 0.3px;
        border: none;
        cursor: pointer;
        transition: var(--transition);
        background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
        color: white;
        box-shadow: var(--shadow-md);
        text-transform: none;
        height: 38px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .stButton > button:hover {
        box-shadow: var(--shadow-lg);
        transform: translateY(-2px);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    .copy-btn {
        width: 100%;
        background: linear-gradient(135deg, var(--success-color), #059669);
        color: white;
        border: none;
        border-radius: var(--radius-md);
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 0.95rem;
        cursor: pointer;
        box-shadow: var(--shadow-md);
        transition: var(--transition);
        height: 38px;
    }
    
    .copy-btn:hover {
        box-shadow: var(--shadow-lg);
        transform: translateY(-2px);
    }
    
    
    /* ============================================================================
       DOWNLOAD BUTTON STYLING
       ============================================================================ */
    
    .stDownloadButton > button {
        background: linear-gradient(135deg, var(--success-color), #059669);
        color: white;
        border: none;
        border-radius: var(--radius-md);
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 0.95rem;
        box-shadow: var(--shadow-md);
        transition: var(--transition);
    }
    
    .stDownloadButton > button:hover {
        box-shadow: var(--shadow-lg);
        transform: translateY(-2px);
    }
    
    
    /* ============================================================================
       ALERTS & NOTIFICATIONS
       ============================================================================ */
    
    .stAlert {
        border-radius: var(--radius-md);
        padding: 1rem;
        border-left: 4px solid;
        box-shadow: var(--shadow-sm);
    }
    
    .stSuccess {
        border-left-color: var(--success-color);
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(16, 185, 129, 0.05));
    }
    
    .stError {
        border-left-color: var(--danger-color);
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(239, 68, 68, 0.05));
    }
    
    .stWarning {
        border-left-color: var(--warning-color);
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(245, 158, 11, 0.05));
    }
    
    
    /* ============================================================================
       SPINNER & LOADING
       ============================================================================ */
    
    .stSpinner > div > div {
        border-color: var(--primary-light);
        border-right-color: var(--primary-color);
    }
    
    
    /* ============================================================================
       EXPANDER STYLING
       ============================================================================ */
    
    .stExpander {
        border: 1px solid var(--border-color);
        border-radius: var(--radius-md);
        box-shadow: var(--shadow-sm);
        transition: var(--transition);
    }
    
    .stExpander:hover {
        box-shadow: var(--shadow-md);
        border-color: var(--primary-light);
    }
    
    .streamlit-expanderHeader {
        border-radius: var(--radius-md);
        background: linear-gradient(135deg, #ffffff, var(--primary-light));
        padding: 1rem;
        font-weight: 600;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, var(--primary-light), var(--primary-color));
        color: white;
    }
    
    .streamlit-expanderHeader p {
        font-weight: 600;
        font-size: 0.95rem;
    }
    
    
    /* ============================================================================
       STATISTICS CARDS
       ============================================================================ */
    
    .stat-card {
        background: linear-gradient(135deg, #ffffff, var(--primary-light));
        border: 2px solid var(--primary-light);
        border-radius: var(--radius-md);
        padding: 1.5rem;
        text-align: center;
        transition: var(--transition);
        box-shadow: var(--shadow-sm);
    }
    
    .stat-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
        border-color: var(--primary-color);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--primary-color);
        margin-bottom: 0.5rem;
        line-height: 1;
    }
    
    .stat-label {
        font-size: 0.85rem;
        color: var(--text-secondary);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    
    /* ============================================================================
       HISTORY STYLING
       ============================================================================ */
    
    .history-section-title {
        font-size: 0.9rem;
        font-weight: 700;
        color: var(--text-primary);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.75rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--primary-light);
        display: inline-block;
    }
    
    .history-text {
        color: var(--text-primary);
        line-height: 1.6;
        font-size: 0.95rem;
        padding: 0.75rem;
        background: var(--primary-light);
        border-radius: var(--radius-sm);
        border-left: 3px solid var(--primary-color);
    }
    
    .output-language {
        font-size: 1rem;
        font-weight: 700;
        color: var(--primary-color);
        display: inline-block;
        padding: 0.5rem 1rem;
        background: var(--primary-light);
        border-radius: var(--radius-md);
        text-transform: uppercase;
        letter-spacing: 0.3px;
    }
    
    
    /* ============================================================================
       SIDEBAR STYLING
       ============================================================================ */
    
    .sidebar .sidebar-content {
        padding: 2rem 0;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--primary-light) 0%, white 100%);
        border-right: 1px solid var(--border-color);
    }
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: var(--primary-color);
        font-weight: 700;
        margin-top: 1.5rem;
    }
    
    [data-testid="stSidebar"] h1:first-child {
        margin-top: 0;
    }
    
    
    /* ============================================================================
       MARKDOWN STYLING
       ============================================================================ */
    
    .stMarkdown h1 {
        color: var(--text-primary);
        font-weight: 700;
        letter-spacing: -0.02em;
    }
    
    .stMarkdown h2 {
        color: var(--text-primary);
        font-weight: 700;
        margin-top: 1.5rem;
    }
    
    .stMarkdown p {
        line-height: 1.7;
        color: var(--text-primary);
    }
    
    .stMarkdown strong {
        font-weight: 700;
        color: var(--primary-color);
    }
    
    
    /* ============================================================================
       RESPONSIVE DESIGN
       ============================================================================ */
    
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2rem;
        }
        
        .hero-subtitle {
            font-size: 1rem;
        }
        
        .hero-badges {
            flex-direction: column;
        }
        
        .badge {
            width: 100%;
        }
        
        .section-title {
            font-size: 1.25rem;
        }
        
        .stat-card {
            padding: 1rem;
        }
        
        .stat-number {
            font-size: 1.75rem;
        }
        
        .stat-label {
            font-size: 0.75rem;
        }
        
        .card-container {
            padding: 1.25rem;
        }
    }
    
    @media (max-width: 480px) {
        .hero-header {
            padding: 2rem 1rem;
        }
        
        .hero-title {
            font-size: 1.5rem;
        }
        
        .stButton > button {
            font-size: 0.85rem;
            padding: 0.6rem 1rem;
        }
    }
    
    
    /* ============================================================================
       SCROLLBAR STYLING
       ============================================================================ */
    
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: transparent;
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--primary-color);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--primary-dark);
    }
    
    
    </style>
    """, unsafe_allow_html=True)