# App initialization and styling
import streamlit as st

def initialize_app():
    """Initialize the app with custom styling and branding"""
    # Set page config
    st.set_page_config(
        page_title="All-in-one Toolkit",
        page_icon="🧰",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Apply custom CSS
    st.markdown("""
    <style>
    /* Main theme colors and fonts */
    :root {
        --primary-color: #6a0dad !important;
        --secondary-color: #9b59b6 !important;
        --background-color: #ffffff !important;
        --text-color: #000000 !important;
        --card-background: #ffffff !important;
        --accent-color: #333333 !important;
    }
    
    /* Global styles */
    body {
        background-color: var(--background-color) !important;
        color: var(--text-color) !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }
    
    /* Force white background on all Streamlit elements */
    .stApp, .main, .block-container, .css-18e3th9, .css-1d391kg, .css-1lcbmhc {
        background-color: var(--background-color) !important;
    }
    
    /* Sidebar styling */
    .css-1d391kg, .css-1lcbmhc, .css-18e3th9, .css-1oe6wy4, .css-1aehpvj, .css-12oz5g7, .css-1v3fvcr, .css-qbe2hs,
    .css-hxt7ib, .css-1offfwp, .css-14xtw13, .css-1n76uvr, .css-1vq4p4l, .css-163ttbj, .css-1l02zno {
        background-color: var(--background-color) !important;
        color: var(--text-color) !important;
    }
    
    /* Additional sidebar elements */
    .sidebar .sidebar-content, .sidebar-content, [data-testid="stSidebar"] {
        background-color: var(--background-color) !important;
    }
    
    /* Navigation container */
    .nav-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 15px;
        margin-top: 20px;
    }
    
    .nav-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 15px;
    }
    
    .nav-label {
        margin-top: 8px;
        font-size: 12px;
        font-weight: 500;
        color: #000000;
        text-align: center;
    }
    
    /* App container styling */
    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: #ffffff !important;
    }
    
    /* Card styling */
    .stCard {
        border-radius: 15px;
        box-shadow: 0 2px 24px rgba(106, 13, 173, 0.2);
        padding: 2.5rem 2rem 2rem 2rem;
        background-color: #ffffff !important;
    }
    .stAlert, .stNotification {
        border-radius: 10px;
        font-weight: 500;
        background-color: #ffffff !important;
    }
    .stAlert[data-baseweb="alert"] {
        background-color: #ffffff !important;
        border-left: 4px solid #6a0dad;
        box-shadow: 0 1px 6px rgba(106, 13, 173, 0.2);
    }
    p, li, span, label, div {
        color: #000000;
    }
    
    /* Override Streamlit default styles */
    .reportview-container .main {
        background-color: #ffffff !important;
    }
    .reportview-container .sidebar-content {
        background-color: #ffffff !important;
    }
    .css-1d391kg, .css-1lcbmhc, .css-12oz5g7 {
        background-color: #ffffff !important;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>select, .stTextArea>div>div>textarea {
        border: 1px solid #6a0dad;
        border-radius: 0.3rem;
        background-color: white !important;
        color: black !important;
    }
    
    /* Style for input placeholder text */
    .stTextInput>div>div>input::placeholder, .stTextArea>div>div>textarea::placeholder {
        color: #666666 !important;
    }
    .stSlider>div>div>div>div {
        background-color: #6a0dad;
    }
    
    /* Custom styling for portfolio-like appearance */
    .stButton>button, button, .stButton button, [data-baseweb="button"] {
        background-color: var(--background-color) !important;
        color: var(--accent-color) !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover, button:hover, .stButton button:hover, [data-baseweb="button"]:hover {
        background: linear-gradient(135deg, var(--accent-color) 0%, var(--primary-color) 100%) !important;
        color: white !important;
        border-color: var(--primary-color) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(106, 13, 173, 0.2) !important;
    }
    
    /* Main content area styling */
    .main .block-container, .block-container, [data-testid="stAppViewContainer"], .appview-container, .css-1wrcr25, .css-18ni7ap {
        background-color: var(--background-color) !important;
        border-radius: 15px !important;
        padding: 2rem !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05) !important;
    }
    
    /* Additional overrides for Streamlit components */
    .stTabs [data-baseweb="tab-list"], .stTabs, [role="tablist"] {
        background-color: var(--background-color) !important;
    }
    .stTabs [data-baseweb="tab"], [role="tab"] {
        background-color: var(--background-color) !important;
        color: var(--accent-color) !important;
    }
    .stTabs [aria-selected="true"], [role="tab"][aria-selected="true"] {
        background-color: var(--primary-color) !important;
        color: white !important;
    }
    
    /* Ensure white background everywhere */
    .element-container, .stMarkdown, .stDataFrame, .stTable, .stText, .stCode, .stExpander, .stFileUploader, .stDownloadButton,
    .stImage, .stVideo, .stAudio, .stNumberInput, .stDateInput, .stTimeInput, .stColorPicker, .stMultiselect, .stSelectbox,
    .stRadio, .stCheckbox, .stMetric, .stProgress, .stSpinner, .stBalloon, .stTooltip, .stWidgetLabel, .stWidgetLabelText,
    .stHeader, .stSubheader, .stTitle, .stCaption, .stContainer, .stColumn, .stColumns, .stGrid, .stRow, .stRows,
    .stDeckGlChart, .stPydeckChart, .stPlotlyChart, .stBokehChart, .stAltairChart, .stVegaLiteChart, .stGraphvizChart,
    .stAgGrid, .stDataEditor, .stDataTable, .stJson, .stYaml, .stToml, .stMarkmap, .stEcharts, .stFoldable, .stStatus,
    .stHeading, .stExpander, .stTabs, .stTabContent, .stTabItem, .stPanel, .stPanelContent, .stPanelHeader {
        background-color: var(--background-color) !important;
        color: var(--text-color) !important;
    }
    
    /* Force all text to be black */
    p, h1, h2, h3, h4, h5, h6, span, div, label, a, li, ul, ol, td, th, tr, table, code, pre {
        color: var(--text-color) !important;
    }
    
    /* Force all borders and accents to use primary color */
    input:focus, select:focus, textarea:focus, button:focus, [data-baseweb="input"]:focus, [data-baseweb="select"]:focus,
    [data-baseweb="textarea"]:focus, [data-baseweb="button"]:focus, [data-baseweb="checkbox"]:focus, [data-baseweb="radio"]:focus {
        border-color: var(--primary-color) !important;
        outline-color: var(--primary-color) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    create_header()
    create_metrics()
    create_sidebar()

def create_header():
    """Create the app header with title"""
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #333333 0%, #6a0dad 100%); border-radius: 15px; margin-bottom: 20px;">
        <h1 style="color: white; margin-bottom: 0; font-size: 2.2rem; font-weight: 600;">All-in-one Linux, Python, ML, and Project Toolkit</h1>
        <p style="color: #f0f0f0; margin-top: 0.5rem; font-size: 1.1rem;">A comprehensive collection of tools for developers and data scientists</p>
    </div>
    """, unsafe_allow_html=True)

def create_metrics():
    """Create dashboard metrics"""
    st.markdown("""
    <div style="display: flex; justify-content: space-between; margin-bottom: 30px;">
        <div style="background-color: white; padding: 20px; border-radius: 10px; width: 30%; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 4px solid #6a0dad;">
            <h3 style="margin: 0; color: #333333; font-size: 16px;">Server Uptime</h3>
            <p style="margin: 0; font-size: 24px; font-weight: 600; color: #6a0dad;">5 days</p>
        </div>
        <div style="background-color: white; padding: 20px; border-radius: 10px; width: 30%; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 4px solid #6a0dad;">
            <h3 style="margin: 0; color: #333333; font-size: 16px;">CPU Load</h3>
            <p style="margin: 0; font-size: 24px; font-weight: 600; color: #6a0dad;">0.67</p>
        </div>
        <div style="background-color: white; padding: 20px; border-radius: 10px; width: 30%; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 4px solid #6a0dad;">
            <h3 style="margin: 0; color: #333333; font-size: 16px;">RAM Usage</h3>
            <p style="margin: 0; font-size: 24px; font-weight: 600; color: #6a0dad;">3.2 GB / 8 GB</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_sidebar():
    """Create sidebar branding and navigation"""
    st.sidebar.markdown("""
    <div style="text-align: center; margin-bottom: 30px; background: linear-gradient(135deg, #333333 0%, #6a0dad 100%); padding: 20px; border-radius: 10px;">
        <h2 style="color: white; margin-bottom: 10px; font-weight: 600;">🧭 Navigation</h2>
        <p style="color: #f0f0f0; font-size: 14px;">Select a category to explore</p>
    </div>
    """, unsafe_allow_html=True)
    
    # CSS for hover buttons with icons
    st.sidebar.markdown("""
    <style>
    .nav-button {
        display: flex;
        justify-content: center;
        align-items: center;
        background: #ffffff;
        color: #333333;
        width: 60px;
        height: 60px;
        border-radius: 50%; /* Changed to circular shape */
        margin: 0 auto 15px auto;
        text-decoration: none;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 2px solid #f0f0f0;
        position: relative;
        overflow: hidden;
    }
    
    .nav-button:hover {
        background: linear-gradient(135deg, #333333 0%, #6a0dad 100%);
        color: white;
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(106, 13, 173, 0.4);
        border-color: #6a0dad;
    }
    
    .nav-button:hover .nav-icon {
        animation: pulse 0.5s;
        color: white !important;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    
    .nav-icon {
        font-size: 28px;
        text-align: center;
        transition: all 0.3s ease;
        color: #333333;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Navigation buttons with icons in a grid
    # Create navigation buttons using Streamlit components instead of raw HTML
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        if st.button("🔧", key="linux_btn", help="Linux Tools"):
            st.session_state.category = "linux"
            st.rerun()
        st.markdown("<div style='text-align:center;font-size:12px;'>Linux</div>", unsafe_allow_html=True)
        
        if st.button("🤖", key="ml_btn", help="Machine Learning Tools"):
            st.session_state.category = "ml"
            st.rerun()
        st.markdown("<div style='text-align:center;font-size:12px;'>ML</div>", unsafe_allow_html=True)
        
        if st.button("📊", key="projects_btn", help="Projects"):
            st.session_state.category = "projects"
            st.rerun()
        st.markdown("<div style='text-align:center;font-size:12px;'>Projects</div>", unsafe_allow_html=True)
    
    with col2:
        if st.button("🐍", key="python_btn", help="Python Utilities"):
            st.session_state.category = "python"
            st.rerun()
        st.markdown("<div style='text-align:center;font-size:12px;'>Python</div>", unsafe_allow_html=True)
        
        if st.button("🐳", key="devops_btn", help="DevOps Tools"):
            st.session_state.category = "devops"
            st.rerun()
        st.markdown("<div style='text-align:center;font-size:12px;'>DevOps</div>", unsafe_allow_html=True)
        
        if st.button("🟨", key="javascript_btn", help="JavaScript Demos"):
            st.session_state.category = "javascript"
            st.rerun()
        st.markdown("<div style='text-align:center;font-size:12px;'>JavaScript</div>", unsafe_allow_html=True)
        
        if st.button("👤", key="user_btn", help="User Page"):
            st.session_state.category = "user"
            st.rerun()
        st.markdown("<div style='text-align:center;font-size:12px;'>User</div>", unsafe_allow_html=True)
    
    # System stats in footer
    st.sidebar.markdown("""
    <div style="margin-top: 50px; padding: 20px; background: white; border-radius: 10px; font-size: 0.8rem; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-left: 4px solid #6a0dad;">
        <h4 style="color: #333333; margin-bottom: 15px; font-size: 1rem; font-weight: 600;">System Stats</h4>
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="background: linear-gradient(135deg, #333333 0%, #6a0dad 100%); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px;">🖥️</div>
            <p style="margin: 0;">CPU: 4 cores @ 2.5GHz</p>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="background: linear-gradient(135deg, #333333 0%, #6a0dad 100%); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px;">🧠</div>
            <p style="margin: 0;">Memory: 8GB DDR4</p>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="background: linear-gradient(135deg, #333333 0%, #6a0dad 100%); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px;">💾</div>
            <p style="margin: 0;">Storage: 256GB SSD</p>
        </div>
        <div style="display: flex; align-items: center;">
            <div style="background: linear-gradient(135deg, #333333 0%, #6a0dad 100%); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px;">🌐</div>
            <p style="margin: 0;">Network: 1Gbps Ethernet</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
