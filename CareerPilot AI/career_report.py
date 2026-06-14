import streamlit as st

def show():
    st.set_page_config(page_title="Career Report", page_icon="📊", layout="wide")
    
    st.title("📊 Your Career Analysis Report")
    
    if "career_results" not in st.session_state:
        st.warning("⚠️ No career analysis found. Please complete an analysis first.")
        if st.button("← Go Back"):
            st.session_state.page = "home"
            st.rerun()
        return
    
    results = st.session_state.career_results
    target_role = st.session_state.get("target_role", "Unknown")
    
    # Header
    st.markdown(f"<h2>Career Path: {target_role}</h2>", unsafe_allow_html=True)
    
    # Resume Summary Section
    if results.get("resume_analysis"):
        st.markdown("---")
        st.markdown("### 📄 Resume Summary")
        
        col1, col2 = st.columns(2)
        
        with col1:
            resume = results["resume_analysis"]
            st.markdown(f"**Education:** {resume.get('education', 'Not specified')}")
            
            if resume.get("technical_skills"):
                st.markdown("**Technical Skills:**")
                for skill in resume["technical_skills"][:8]:
                    st.markdown(f"- {skill}")
        
        with col2:
            if resume.get("soft_skills"):
                st.markdown("**Soft Skills:**")
                for skill in resume["soft_skills"][:6]:
                    st.markdown(f"- {skill}")
            
            if resume.get("experience"):
                st.markdown("**Experience Highlights:**")
                for exp in resume["experience"][:3]:
                    st.markdown(f"- {exp[:60]}...")
    
    # Skill Analysis Section
    if results.get("skill_gap"):
        st.markdown("---")
        st.markdown("### 🎯 Skill Analysis")
        
        skill_gap = results["skill_gap"]
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Readiness Score",
                f"{skill_gap.get('readiness_score', 0)}%",
                skill_gap.get('readiness_label', 'N/A')
            )
        
        with col2:
            total_required = skill_gap.get("total_skills_required", 0)
            st.metric("Required Skills", total_required)
        
        with col3:
            total_matched = skill_gap.get("total_skills_matched", 0)
            st.metric("Matched Skills", total_matched)
        
        with col4:
            missing = total_required - total_matched
            st.metric("Skill Gaps", missing)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Existing Skills:**")
            existing = skill_gap.get("existing_skills", [])
            if existing:
                for skill in existing[:8]:
                    st.markdown(f"✅ {skill}")
            else:
                st.markdown("*No matched skills identified*")
        
        with col2:
            st.markdown("**Missing Skills (Priority-Based):**")
            missing_skills = skill_gap.get("missing_skills", [])
            if missing_skills:
                for item in missing_skills[:8]:
                    if isinstance(item, dict):
                        priority_emoji = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(item.get("priority"), "⚪")
                        st.markdown(f"{priority_emoji} **{item['skill']}** ({item['priority']})")
                    else:
                        st.markdown(f"- {item}")
            else:
                st.markdown("*No missing skills identified*")
        
        st.info(f"**Gap Summary:** {skill_gap.get('gap_summary', 'N/A')}")
    
    # Career Strategy Section
    if results.get("career_strategy"):
        st.markdown("---")
        st.markdown("### 💡 Career Strategy")
        
        strategy = results["career_strategy"]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Career Path:**")
            career_path = strategy.get("career_path", [])
            for i, role in enumerate(career_path, 1):
                st.markdown(f"{i}. {role}")
            
            st.markdown("**Estimated Timeline:**")
            st.markdown(f"📅 {strategy.get('estimated_timeline', 'N/A')}")
        
        with col2:
            st.markdown("**Key Action Items:**")
            strategy_items = strategy.get("strategy", [])
            for item in strategy_items[:5]:
                st.markdown(f"✓ {item}")
        
        st.markdown("**Networking Tips:**")
        networking = strategy.get("networking_tips", [])
        for tip in networking[:4]:
            st.markdown(f"🤝 {tip}")
    
    # Certifications Section
    if results.get("career_strategy"):
        st.markdown("---")
        st.markdown("### 🏆 Recommended Certifications")
        
        certs = results["career_strategy"].get("recommended_certifications", [])
        if certs:
            for i, cert in enumerate(certs, 1):
                st.markdown(f"{i}. **{cert}**")
        else:
            st.markdown("*No specific certifications found*")
    
    # Portfolio Projects Section
    if results.get("career_strategy"):
        st.markdown("---")
        st.markdown("### 🎨 Portfolio Projects to Build")
        
        projects = results["career_strategy"].get("portfolio_projects", [])
        if projects:
            for project in projects:
                st.markdown(f"📁 {project}")
        else:
            st.markdown("*No specific projects found*")
    
    # Learning Roadmap Section
    if results.get("learning_roadmap"):
        st.markdown("---")
        st.markdown("### 🛣️ Personalized Learning Roadmap")
        
        roadmap = results["learning_roadmap"]
        
        total_weeks = roadmap.get("total_estimated_weeks", 0)
        total_months = roadmap.get("estimated_months", 0)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Duration", f"{total_weeks} weeks")
        with col2:
            st.metric("Approx. Months", f"{total_months} months")
        
        phases = roadmap.get("phases", [])
        for i, phase in enumerate(phases, 1):
            with st.expander(f"**Phase {i}: {phase.get('title', 'Unknown')}** ({phase.get('weeks', 0)} weeks)"):
                st.markdown("**Topics:**")
                for topic in phase.get("topics", []):
                    st.markdown(f"- {topic}")
                
                if phase.get("projects"):
                    st.markdown("**Projects:**")
                    for project in phase["projects"]:
                        st.markdown(f"- {project}")
        
        if roadmap.get("milestones"):
            st.markdown("**Milestones:**")
            for milestone in roadmap["milestones"]:
                st.markdown(f"✓ {milestone}")
        
        st.markdown("**Learning Resources:**")
        resources = roadmap.get("learning_resources", {})
        for category, items in resources.items():
            st.markdown(f"**{category}:**")
            for item in items:
                st.markdown(f"- {item}")
    
    # Summary Metrics
    st.markdown("---")
    st.markdown("### 📈 Summary Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        readiness = results.get("skill_gap", {}).get("readiness_score", 0)
        st.metric("Readiness", f"{readiness}%")
    
    with col2:
        weeks = results.get("learning_roadmap", {}).get("total_estimated_weeks", 0)
        st.metric("Learning Duration", f"{weeks} weeks")
    
    with col3:
        missing = len(results.get("skill_gap", {}).get("missing_skills", []))
        st.metric("Skills to Learn", missing)
    
    # Action Buttons
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏠 Back to Home"):
            st.session_state.page = "home"
            st.rerun()
    
    with col2:
        if st.button("📤 New Analysis"):
            st.session_state.page = "upload_resume"
            st.rerun()
    
    with col3:
        st.download_button(
            label="📥 Download Report",
            data=generate_report_text(results, target_role),
            file_name=f"CareerReport_{target_role}.txt",
            mime="text/plain"
        )

def generate_report_text(results, target_role):
    """Generate downloadable report text"""
    report = f"CAREER ANALYSIS REPORT\n"
    report += f"Target Role: {target_role}\n"
    report += f"{'=' * 50}\n\n"
    
    if results.get("skill_gap"):
        sg = results["skill_gap"]
        report += f"SKILL GAP ANALYSIS\n"
        report += f"Readiness Score: {sg.get('readiness_score', 0)}%\n"
        report += f"Readiness Level: {sg.get('readiness_label', 'N/A')}\n"
        report += f"Skills Matched: {sg.get('total_skills_matched', 0)}/{sg.get('total_skills_required', 0)}\n\n"
    
    if results.get("learning_roadmap"):
        lr = results["learning_roadmap"]
        report += f"LEARNING ROADMAP\n"
        report += f"Total Duration: {lr.get('total_estimated_weeks', 0)} weeks\n"
        report += f"Estimated Months: {lr.get('estimated_months', 0)} months\n\n"
    
    return report