import streamlit as st

def show():
    st.set_page_config(
        page_title="CareerPilot AI - Home",
        page_icon="🚀",
        layout="wide"
    )
    
    # Hero Section
    st.markdown("""
    <div style="text-align: center; padding: 50px 0;">
        <h1 style="color: #FF6B6B; font-size: 3em;">🚀 CareerPilot AI</h1>
        <p style="font-size: 1.5em; color: #555;">Your AI-Powered Career Guidance Platform</p>
        <p style="font-size: 1.1em; color: #888;">Analyze your skills, identify gaps, and chart your path to success</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #f0f2f6; padding: 30px; border-radius: 10px; margin: 20px 0;">
            <h3>📄 Upload Resume</h3>
            <p>Have a resume? Upload it and let our AI analyze your skills, experience, and education automatically.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📤 Upload Resume", key="btn_upload", use_container_width=True):
            st.session_state.page = "upload_resume"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div style="background-color: #f0f2f6; padding: 30px; border-radius: 10px; margin: 20px 0;">
            <h3>⚡ Quick Start</h3>
            <p>Don't have a resume? No problem! Start with our quick questionnaire and get personalized guidance.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Quick Start", key="btn_quick", use_container_width=True):
            st.session_state.page = "no_resume"
            st.rerun()
    
    # Features Section
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>✨ What CareerPilot AI Offers</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h3>📊 Skill Analysis</h3>
            <p>AI-powered analysis of your technical and soft skills</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h3>🎯 Gap Identification</h3>
            <p>Identify skill gaps for your target role with priority levels</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h3>🛣️ Learning Roadmap</h3>
            <p>Personalized learning path with phases and milestones</p>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h3>💡 Career Strategy</h3>
            <p>Actionable strategies to reach your target role</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h3>🏆 Portfolio Guidance</h3>
            <p>Recommended projects to build your portfolio</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h3>📜 Certifications</h3>
            <p>Industry certifications aligned with your goals</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Supported Roles Section
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>🎯 15 Career Paths Available</h2>", unsafe_allow_html=True)
    
    roles = [
        "🤖 AI Engineer",
        "📊 Data Scientist",
        "🌐 Full Stack Developer",
        "🎨 Frontend Developer",
        "⚙️ Backend Developer",
        "☁️ Cloud Engineer",
        "🔒 Cybersecurity Analyst",
        "🚀 DevOps Engineer",
        "🧠 Machine Learning Engineer",
        "📈 Data Analyst",
        "💻 Software Engineer",
        "📱 Android Developer",
        "🎭 UI/UX Designer",
        "🛍️ Product Manager",
        "⛓️ Blockchain Developer"
    ]
    
    cols = st.columns(3)
    for i, role in enumerate(roles):
        with cols[i % 3]:
            st.markdown(f"• {role}")
    
    # CTA Section
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 40px; background-color: #f0f2f6; border-radius: 10px;">
        <h2>Ready to Transform Your Career?</h2>
        <p style="font-size: 1.1em;">Choose your path and start your journey with CareerPilot AI today!</p>
    </div>
    """, unsafe_allow_html=True)