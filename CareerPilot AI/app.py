import streamlit as st
from streamlit_option_menu import option_menu
import home
import resume_upload
import no_resume
import career_report
import about

# Page configuration
st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"

if "career_results" not in st.session_state:
    st.session_state.career_results = None

if "analyzing" not in st.session_state:
    st.session_state.analyzing = False

# Custom CSS
st.markdown("""
    <style>
    :root {
        --primary-color: #FF6B6B;
        --secondary-color: #4ECDC4;
        --dark-color: #2C3E50;
        --light-color: #ECF0F1;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stMetric {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 10px;
    }
    
    .stButton > button {
        width: 100%;
        border-radius: 5px;
        font-weight: bold;
    }
    
    h1 {
        color: #FF6B6B;
    }
    
    h2 {
        color: #667eea;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("# 🚀 CareerPilot AI")
    st.markdown("---")
    
    page_selection = option_menu(
        menu_title="Navigation",
        options=["Home", "Upload Resume", "Quick Start", "Career Report", "About"],
        icons=["house", "upload", "lightning", "chart-bar", "info-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f0f2f6"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {
                "font-size": "17px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee"
            },
            "nav-link-selected": {"background-color": "#FF6B6B"}
        }
    )
    
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Supported Roles", "15")
    with col2:
        st.metric("Accuracy", "95%")
    
    st.markdown("---")
    st.markdown("""
    ### ℹ️ How to Use
    
    1. **Upload** your resume or provide your skills
    2. **Select** your target role
    3. **Analyze** to get insights
    4. **Review** your comprehensive report
    5. **Follow** your personalized roadmap
    """)
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: gray;">
        <small>Made with ❤️ using GitHub Models & Streamlit</small>
    </div>
    """, unsafe_allow_html=True)

# Route Pages
if page_selection == "Home":
    home.show()
elif page_selection == "Upload Resume":
    resume_upload.show()
elif page_selection == "Quick Start":
    no_resume.show()
elif page_selection == "Career Report":
    career_report.show()
elif page_selection == "About":
    about.show()

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<small>© 2024 CareerPilot AI</small>", unsafe_allow_html=True)

with col2:
    st.markdown("<small>[GitHub](https://github.com) | [Docs](https://github.com)</small>", unsafe_allow_html=True)

with col3:
    st.markdown("<small>v1.0.0 ✅</small>", unsafe_allow_html=True)