import streamlit as st
from resume_analyst import ResumeAnalystAgent
from orchestrator import CareerPilotOrchestrator
import tempfile
import os

def show():
    st.set_page_config(page_title="Upload Resume", page_icon="📤")
    
    st.title("📤 Upload Your Resume")
    st.write("Upload your resume and select your target role to get started!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        uploaded_file = st.file_uploader(
            "Choose your resume (PDF or DOCX)",
            type=["pdf", "docx"],
            help="Upload your resume in PDF or DOCX format"
        )
    
    with col2:
        orchestrator = CareerPilotOrchestrator()
        available_roles = orchestrator.get_available_roles()
        
        target_role = st.selectbox(
            "Select your target role",
            available_roles,
            help="Choose the role you're aiming for"
        )
    
    if uploaded_file and target_role:
        if st.button("🔍 Analyze Resume", use_container_width=True):
            st.session_state.analyzing = True
    
    if st.session_state.get("analyzing"):
        with st.spinner("Processing your resume..."):
            try:
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                    tmp_file.write(uploaded_file.getbuffer())
                    tmp_path = tmp_file.name
                
                # Extract resume text
                resume_analyst = ResumeAnalystAgent()
                if uploaded_file.type == "application/pdf":
                    resume_text = resume_analyst.extract_from_pdf(tmp_path)
                else:
                    resume_text = resume_analyst.extract_from_docx(tmp_path)
                
                os.unlink(tmp_path)
                
                # Run full pipeline
                orchestrator = CareerPilotOrchestrator()
                
                progress_container = st.container()
                with progress_container:
                    status_placeholder = st.empty()
                
                def status_callback(message):
                    status_placeholder.info(f"⏳ {message}")
                
                results = orchestrator.run_full_pipeline(
                    resume_text,
                    target_role,
                    status_callback
                )
                
                # Store results in session
                st.session_state.career_results = results
                st.session_state.target_role = target_role
                st.session_state.analyzing = False
                
                st.success("✅ Analysis complete! View your career report.")
                
                if st.button("📊 View Career Report", use_container_width=True):
                    st.session_state.page = "career_report"
                    st.rerun()
            
            except Exception as e:
                st.error(f"❌ Error processing resume: {str(e)}")
                st.session_state.analyzing = False
    
    st.info("""
    ### 📋 Supported Formats:
    - **PDF**: Standard resume format
    - **DOCX**: Microsoft Word documents
    
    ### 🔒 Privacy:
    Your resume is processed locally and not stored permanently.
    """)