from typing import Dict, Callable, Optional
from resume_analyst import ResumeAnalystAgent
from skill_gap import SkillGapAgent
from career_strategist import CareerStrategistAgent
from learning_roadmap import LearningRoadmapAgent

class CareerPilotOrchestrator:
    
    def __init__(self):
        self.resume_analyst = ResumeAnalystAgent()
        self.skill_gap = SkillGapAgent()
        self.career_strategist = CareerStrategistAgent()
        self.learning_roadmap = LearningRoadmapAgent()
    
    def run_full_pipeline(
        self,
        resume_text: Optional[str],
        target_role: str,
        status_callback: Optional[Callable] = None
    ) -> Dict:
        """Execute full career analysis pipeline"""
        
        results = {
            "resume_analysis": None,
            "skill_gap": None,
            "career_strategy": None,
            "learning_roadmap": None,
            "status": "completed"
        }
        
        try:
            # Step 1: Analyze Resume
            if status_callback:
                status_callback("Analyzing resume...")
            
            if resume_text:
                results["resume_analysis"] = self.resume_analyst.run(resume_text)
                candidate_profile = results["resume_analysis"]
            else:
                candidate_profile = {
                    "technical_skills": [],
                    "soft_skills": [],
                    "education": "Not provided",
                    "projects": [],
                    "experience": []
                }
                results["resume_analysis"] = candidate_profile
            
            # Step 2: Analyze Skill Gap
            if status_callback:
                status_callback("Analyzing skill gaps...")
            
            results["skill_gap"] = self.skill_gap.run(target_role, candidate_profile)
            
            # Step 3: Generate Career Strategy
            if status_callback:
                status_callback("Generating career strategy...")
            
            results["career_strategy"] = self.career_strategist.run(
                target_role,
                results["skill_gap"],
                candidate_profile
            )
            
            # Step 4: Create Learning Roadmap
            if status_callback:
                status_callback("Creating personalized learning roadmap...")
            
            missing_skills = results["skill_gap"].get("missing_skills", [])
            readiness = results["skill_gap"].get("readiness_score", 0)
            
            results["learning_roadmap"] = self.learning_roadmap.run(
                target_role,
                missing_skills,
                readiness
            )
            
            if status_callback:
                status_callback("Career analysis complete!")
        
        except Exception as e:
            results["status"] = f"error: {str(e)}"
            if status_callback:
                status_callback(f"Error: {str(e)}")
        
        return results
    
    def get_available_roles(self) -> list:
        """Get list of available roles"""
        return list(self.skill_gap.role_data.keys())