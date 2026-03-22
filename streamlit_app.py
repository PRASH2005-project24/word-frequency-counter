"""
Word Frequency Counter — Streamlit App
Upload a .txt file, search any word, see instant frequency results.
"""

import re
import streamlit as st
from collections import Counter

# ─── Page Config ───
st.set_page_config(
    page_title="Word Frequency Counter",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ───
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* Root overrides */
    .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* Header */
    .app-header {
        text-align: center;
        padding: 1.5rem 0 1rem;
    }
    .app-header .icon {
        font-size: 3rem;
        display: block;
        margin-bottom: 0.3rem;
        animation: pulse 3s ease-in-out infinite;
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    .app-header h1 {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1, #818cf8, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
        margin: 0;
    }
    .app-header p {
        color: #94a3b8;
        font-size: 0.95rem;
        margin-top: 0.2rem;
    }

    /* Step labels */
    .step-label {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #a5b4fc;
        margin-bottom: 0.75rem;
    }

    /* Stat cards */
    .stat-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 12px;
        padding: 1.2rem 1rem;
        text-align: center;
        transition: transform 0.3s ease;
    }
    .stat-card:hover {
        transform: translateY(-3px);
    }
    .stat-value {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1, #818cf8, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
    }
    .stat-value.green {
        background: linear-gradient(135deg, #34d399, #6ee7b7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .stat-label {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #64748b;
        margin-top: 0.3rem;
        font-weight: 600;
    }

    /* Search result callout */
    .search-callout {
        background: rgba(52, 211, 153, 0.08);
        border: 1px solid rgba(52, 211, 153, 0.25);
        border-radius: 12px;
        padding: 1rem 1.25rem;
        font-size: 0.95rem;
        color: #f1f5f9;
        margin: 0.5rem 0 1rem;
    }
    .search-callout .word {
        color: #34d399;
        font-weight: 700;
    }
    .search-callout .count {
        font-size: 1.4rem;
        font-weight: 800;
        color: #34d399;
    }

    /* Bar row */
    .bar-row {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 0.45rem;
    }
    .bar-word {
        width: 90px;
        font-size: 0.82rem;
        font-weight: 500;
        color: #94a3b8;
        text-align: right;
        flex-shrink: 0;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
    .bar-track {
        flex: 1;
        height: 24px;
        background: rgba(30, 41, 59, 0.5);
        border-radius: 6px;
        overflow: hidden;
    }
    .bar-fill {
        height: 100%;
        background: linear-gradient(135deg, #6366f1, #818cf8, #a78bfa);
        border-radius: 6px;
        min-width: 4px;
    }
    .bar-count {
        width: 40px;
        font-size: 0.82rem;
        font-weight: 600;
        color: #a5b4fc;
        text-align: left;
        flex-shrink: 0;
    }

    /* Hide default Streamlit header/footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Smoother file uploader */
    .stFileUploader > div {
        border-radius: 12px !important;
    }

    /* Button style */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1, #818cf8, #a78bfa) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 24px rgba(129, 140, 248, 0.25) !important;
    }

    /* Text input */
    .stTextInput > div > div > input {
        border-radius: 10px !important;
        border: 1px solid rgba(99, 102, 241, 0.2) !important;
        background: rgba(30, 41, 59, 0.6) !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #818cf8 !important;
        box-shadow: 0 0 0 3px rgba(129, 140, 248, 0.25) !important;
    }
</style>
""", unsafe_allow_html=True)


# ─── Header ───
st.markdown("""
<div class="app-header">
    <span class="icon">📊</span>
    <h1>Word Frequency Counter</h1>
    <p>Upload a text file, search any word, see instant results</p>
</div>
""", unsafe_allow_html=True)

# ─── Step 1: File Upload ───
st.markdown('<div class="step-label">📁 Step 1 — Upload your file</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "Drag & drop or click to upload a .txt file",
    type=["txt"],
    label_visibility="collapsed",
)

# ─── Step 2: Word Search ───
st.markdown('<div class="step-label">🔍 Step 2 — Enter a word to search</div>', unsafe_allow_html=True)
col_input, col_btn = st.columns([4, 1])
with col_input:
    search_word = st.text_input(
        "Search word",
        placeholder="Type a word…",
        label_visibility="collapsed",
    )
with col_btn:
    analyze_clicked = st.button("Count", use_container_width=True)

# ─── Analysis ───
if uploaded_file is not None and analyze_clicked:
    # Read file
    try:
        text = uploaded_file.read().decode("utf-8", errors="ignore")
    except Exception:
        st.error("⚠️ Could not read the file.")
        st.stop()

    # Process
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", text.lower())
    words = cleaned.split()

    if not words:
        st.error("⚠️ The file contains no readable words.")
        st.stop()

    counter = Counter(words)
    total_words = len(words)
    unique_words = len(counter)

    # Search
    clean_search = re.sub(r"[^a-zA-Z0-9]", "", search_word.strip().lower())
    search_count = counter.get(clean_search, 0) if clean_search else None

    # ─── Results ───
    st.markdown("---")
    st.markdown('<div class="step-label">📈 Results</div>', unsafe_allow_html=True)

    # Stats row
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{total_words:,}</div>
            <div class="stat-label">Total Words</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{unique_words:,}</div>
            <div class="stat-label">Unique Words</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        count_display = search_count if search_count is not None else "—"
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value green">{count_display}</div>
            <div class="stat-label">Search Hits</div>
        </div>
        """, unsafe_allow_html=True)

    # Search callout
    if clean_search:
        st.markdown(f"""
        <div class="search-callout">
            The word "<span class="word">{clean_search}</span>" appears
            <span class="count">{search_count}</span> time(s) in
            <em>{uploaded_file.name}</em>.
        </div>
        """, unsafe_allow_html=True)

    # Top words bar chart
    top_words = counter.most_common(15)
    if top_words:
        max_count = top_words[0][1]
        st.markdown('<div class="step-label">📊 Top Words</div>', unsafe_allow_html=True)

        bars_html = ""
        for word, count in top_words:
            pct = max((count / max_count) * 100, 2)
            bars_html += f"""
            <div class="bar-row">
                <span class="bar-word" title="{word}">{word}</span>
                <div class="bar-track">
                    <div class="bar-fill" style="width: {pct}%"></div>
                </div>
                <span class="bar-count">{count}</span>
            </div>
            """
        st.markdown(bars_html, unsafe_allow_html=True)

elif analyze_clicked and uploaded_file is None:
    st.warning("⚠️ Please upload a .txt file first.")

# ─── Footer ───
st.markdown("""
<div style="text-align: center; padding: 2rem 0 1rem; font-size: 0.78rem; color: #64748b;">
    Built with Python & Streamlit • Word Frequency Counter
</div>
""", unsafe_allow_html=True)
