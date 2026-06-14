import streamlit as st

def show():
    st.set_page_config(page_title="About", page_icon="ℹ️")
    
    st.title("ℹ️ About CareerPilot AI")
    
    st.markdown("""
    ## 🚀 What is CareerPilot AI?
    
    CareerPilot AI is an intelligent career guidance platform that uses artificial intelligence 
    to analyze your professional profile and create personalized career development strategies.
    
    ### 🎯 Our Mission
    
    We believe that everyone deserves access to expert career guidance. CareerPilot AI democratizes 
    career planning by leveraging AI to provide:
    
    - **Skill Assessment**: Comprehensive analysis of your technical and soft skills
    - **Gap Identification**: Clear understanding of what you need to learn
    - **Career Strategies**: Actionable steps to reach your career goals
    - **Learning Plans**: Personalized roadmaps with timelines and milestones
    - **Portfolio Guidance**: Recommended projects to build your professional portfolio
    
    ### 🔬 How It Works
    
    1. **Resume Analysis**: Upload your resume (PDF/DOCX) or enter your skills manually
    2. **Skill Gap Analysis**: Compare your skills against your target role requirements
    3. **Career Strategy Generation**: Get AI-powered career advancement strategies
    4. **Learning Roadmap Creation**: Receive a personalized learning plan with phases and milestones
    5. **Comprehensive Report**: Download a detailed career report with all insights
    
    ### 🛠️ Technology Stack
    
    - **Frontend**: Streamlit - for interactive web interface
    - **AI Model**: GitHub Models - Llama 4 Scout 17B
    - **Backend**: Python - for core business logic
    - **Processing**: PDF/DOCX parsing, NLP, Text analysis
    
    ### 🎓 Supported Career Paths
    
    CareerPilot AI supports guidance for 15 different career paths:
    
    1. 🤖 AI Engineer
    2. 📊 Data Scientist
    3. 🌐 Full Stack Developer
    4. 🎨 Frontend Developer
    5. ⚙️ Backend Developer
    6. ☁️ Cloud Engineer
    7. 🔒 Cybersecurity Analyst
    8. 🚀 DevOps Engineer
    9. 🧠 Machine Learning Engineer
    10. 📈 Data Analyst
    11. 💻 Software Engineer
    12. 📱 Android Developer
    13. 🎭 UI/UX Designer
    14. 🛍️ Product Manager
    15. ⛓️ Blockchain Developer
    
    ### 💡 Key Features
    
    - **AI-Powered Analysis**: Uses advanced language models for intelligent insights
    - **Multi-Format Support**: Works with PDF and DOCX resumes
    - **Comprehensive Reports**: Detailed insights on skills, gaps, and strategies
    - **Personalized Roadmaps**: Customized learning paths based on your profile
    - **Portfolio Recommendations**: Curated project ideas for each career path
    - **Certification Guidance**: Industry-relevant certifications for career growth
    - **Privacy First**: Your data is processed securely and not permanently stored
    
    ### 🔒 Privacy & Security
    
    - Resumes are processed locally and not stored permanently
    - No personal data is shared with third parties
    - Secure API calls using GitHub Models infrastructure
    - Compliant with data protection standards
    
    ### 📞 Support
    
    For issues, feedback, or suggestions:
    - Create an issue on GitHub
    - Contact: support@careerpilot.ai
    - Documentation: https://github.com/yourusername/CareerPilot-AI
    
    ### 📄 License
    
    CareerPilot AI is open-source and available under the MIT License.
    
    ### 🙏 Acknowledgments
    
    Built with:
    - GitHub Models for AI capabilities
    - Streamlit for the web framework
    - Python community for amazing libraries
    
    ---
    
    **Version**: 1.0.0  
    **Last Updated**: 2024  
    **Status**: Production Ready ✅
    """)
    
    # Footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("[GitHub](https://github.com)")
    
    with col2:
        st.markdown("[Documentation](https://github.com)")
    
    with col3:
        st.markdown("[Report Issue](https://github.com)")