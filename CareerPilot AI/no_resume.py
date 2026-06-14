import streamlit as st
from orchestrator import CareerPilotOrchestrator

def show():
    st.set_page_config(page_title="Quick Start", page_icon="⚡")
    
    st.title("⚡ Quick Start - No Resume Needed")
    st.write("Tell us about yourself and get personalized career guidance!")
    
    orchestrator = CareerPilotOrchestrator()
    available_roles = orchestrator.get_available_roles()
    
    with st.form("quick_start_form"):
        st.markdown("### 👤 Your Background")
        
        col1, col2 = st.columns(2)
        
        with col1:
            experience_level = st.selectbox(
                "Experience Level",
                ["Beginner", "Intermediate", "Advanced", "Expert"]
            )
        
        with col2:
            years_experience = st.number_input(
                "Years of Experience",
                min_value=0,
                max_value=50,
                value=0
            )
        
        st.markdown("### 💻 Your Skills")
        
        technical_skills_input = st.text_area(
            "Technical Skills (comma-separated)",
            placeholder="e.g., Python, JavaScript, React, Node.js",
            height=100
        )
        
        soft_skills_input = st.text_area(
            "Soft Skills (comma-separated)",
            placeholder="e.g., Leadership, Communication, Problem Solving",
            height=80
        )
        
        st.markdown("### 🎓 Education")
        
        col1, col2 = st.columns(2)
        
        with col1:
            education = st.selectbox(
                "Highest Education",
                ["High School", "Bachelor's", "Master's", "PhD", "Other"]
            )
        
        with col2:
            field_of_study = st.text_input(
                "Field of Study",
                placeholder="e.g., Computer Science"
            )
        
        st.markdown("### 🎯 Your Goal")
        
        target_role = st.selectbox(
            "Target Role",
            available_roles
        )
        
        submit_button = st.form_submit_button("🚀 Get Career Guidance", use_container_width=True)
    
    if submit_button:
        if not target_role:
            st.error("Please select a target role")
        else:
            with st.spinner("Generating your personalized career plan..."):
                try:
                    # Parse skills
                    technical_skills = [s.strip() for s in technical_skills_input.split(",") if s.strip()]
                    soft_skills = [s.strip() for s in soft_skills_input.split(",") if s.strip()]
                    
                    # Create candidate profile
                    candidate_profile = {
                        "technical_skills": technical_skills,
                        "soft_skills": soft_skills,
                        "education": education,
                        "field_of_study": field_of_study,
                        "years_experience": years_experience,
                        "experience_level": experience_level
                    }
                    
                    # Run pipeline
                    progress_container = st.container()
                    with progress_container:
                        status_placeholder = st.empty()
                    
                    def status_callback(message):
                        status_placeholder.info(f"⏳ {message}")
                    
                    results = orchestrator.run_full_pipeline(
                        None,
                        target_role,
                        status_callback
                    )
                    
                    st.session_state.career_results = results
                    st.session_state.target_role = target_role
                    st.session_state.candidate_profile = candidate_profile
                    
                    st.success("✅ Career plan ready!")
                    
                    if st.button("📊 View Your Career Report", use_container_width=True):
                        st.session_state.page = "career_report"
                        st.rerun()
                
                except Exception as e:
                    st.error(f"❌ Error generating plan: {str(e)}")