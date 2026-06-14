from typing import Dict, List
from career_data import ROLE_DATA
from llm import LLMClient

class SkillGapAgent:
    
    def __init__(self):
        self.llm = LLMClient()
        self.role_data = ROLE_DATA
    
    def run(self, target_role: str, candidate_skills: Dict) -> Dict:
        """Analyze skill gap for target role"""
        
        if target_role not in self.role_data:
            return self._handle_unknown_role(target_role)
        
        role_info = self.role_data[target_role]
        required_skills = role_info["skills"]
        
        technical_skills = candidate_skills.get("technical_skills", [])
        soft_skills = candidate_skills.get("soft_skills", [])
        all_candidate_skills = technical_skills + soft_skills
        
        missing_skills = [skill for skill in required_skills if skill not in all_candidate_skills]
        existing_skills = [skill for skill in required_skills if skill in all_candidate_skills]
        
        readiness_score = self._calculate_readiness_score(existing_skills, required_skills)
        readiness_label = self._get_readiness_label(readiness_score)
        
        gap_summary = self._generate_gap_summary(
            target_role,
            existing_skills,
            missing_skills,
            readiness_score
        )
        
        missing_skills_detailed = self._prioritize_missing_skills(missing_skills)
        
        return {
            "target_role": target_role,
            "required_skills": required_skills,
            "existing_skills": existing_skills,
            "missing_skills": missing_skills_detailed,
            "readiness_score": readiness_score,
            "readiness_label": readiness_label,
            "gap_summary": gap_summary,
            "total_skills_matched": len(existing_skills),
            "total_skills_required": len(required_skills)
        }
    
    def _handle_unknown_role(self, role: str) -> Dict:
        """Handle unknown role"""
        return {
            "target_role": role,
            "required_skills": [],
            "existing_skills": [],
            "missing_skills": [],
            "readiness_score": 0,
            "readiness_label": "Unknown Role",
            "gap_summary": f"Role '{role}' not found in database. Please select from available roles."
        }
    
    def _calculate_readiness_score(self, existing_skills: List[str], required_skills: List[str]) -> int:
        """Calculate readiness score"""
        if not required_skills:
            return 0
        score = (len(existing_skills) / len(required_skills)) * 100
        return min(int(score), 100)
    
    def _get_readiness_label(self, score: int) -> str:
        """Get readiness label based on score"""
        if score >= 80:
            return "Ready"
        elif score >= 60:
            return "Intermediate"
        elif score >= 40:
            return "Beginner"
        else:
            return "Starting Point"
    
    def _prioritize_missing_skills(self, missing_skills: List[str]) -> List[Dict]:
        """Prioritize missing skills"""
        priority_keywords = {
            "High": ["Machine Learning", "Deep Learning", "System Design", "Cloud", "Kubernetes", "Python", "Java"],
            "Medium": ["React", "SQL", "Docker", "Git", "REST API", "Testing"],
            "Low": ["CSS", "HTML", "Design Tools", "Office"]
        }
        
        prioritized = []
        for skill in missing_skills:
            priority = "Medium"
            for level, keywords in priority_keywords.items():
                if any(kw.lower() in skill.lower() for kw in keywords):
                    priority = level
                    break
            
            prioritized.append({
                "skill": skill,
                "priority": priority,
                "reason": f"Required for {skill} competency in target role"
            })
        
        return sorted(prioritized, key=lambda x: {"High": 0, "Medium": 1, "Low": 2}[x["priority"]])
    
    def _generate_gap_summary(self, role: str, existing: List[str], missing: List[str], score: int) -> str:
        """Generate gap summary using LLM"""
        prompt = f"""
        Analyze the skill gap for a candidate applying for {role}.
        
        Existing Skills ({len(existing)}): {', '.join(existing[:5]) if existing else 'None'}
        Missing Skills ({len(missing)}): {', '.join(missing[:5]) if missing else 'None'}
        Readiness Score: {score}%
        
        Provide a concise summary (2-3 sentences) about their readiness and key areas to focus on.
        """
        
        return self.llm.generate(prompt, max_tokens=300)