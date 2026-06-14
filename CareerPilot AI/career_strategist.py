from typing import Dict, List
from career_data import ROLE_DATA
from llm import LLMClient

class CareerStrategistAgent:
    
    def __init__(self):
        self.llm = LLMClient()
        self.role_data = ROLE_DATA
    
    def run(self, target_role: str, skill_gap: Dict, candidate_profile: Dict) -> Dict:
        """Generate career strategy"""
        
        if target_role not in self.role_data:
            return {"error": f"Role {target_role} not found"}
        
        role_info = self.role_data[target_role]
        
        career_path = role_info.get("career_path", [])
        certifications = role_info.get("recommended_certifications", [])
        portfolio_projects = role_info.get("portfolio_projects", [])
        
        strategy = self._generate_strategy(
            target_role,
            skill_gap,
            candidate_profile,
            certifications
        )
        
        networking_tips = self._generate_networking_tips(target_role)
        
        return {
            "target_role": target_role,
            "career_path": career_path,
            "strategy": strategy,
            "certifications": certifications,
            "portfolio_projects": portfolio_projects,
            "networking_tips": networking_tips,
            "estimated_timeline": self._estimate_timeline(skill_gap)
        }
    
    def _generate_strategy(self, role: str, skill_gap: Dict, profile: Dict, certs: List[str]) -> List[str]:
        """Generate career strategy using LLM"""
        missing_skills = skill_gap.get("missing_skills", [])
        readiness = skill_gap.get("readiness_score", 0)
        
        missing_skill_names = [s["skill"] if isinstance(s, dict) else s for s in missing_skills[:3]]
        
        prompt = f"""
        Create a concise career strategy for someone transitioning to {role}.
        
        Current Readiness: {readiness}%
        Top Missing Skills: {', '.join(missing_skill_names)}
        Recommended Certifications: {', '.join(certs[:2])}
        
        Provide 4-5 specific action items they should take in the next 3 months to move towards this role.
        Format as a numbered list.
        """
        
        response = self.llm.generate(prompt, max_tokens=500)
        
        strategies = []
        lines = response.split('\n')
        for line in lines:
            if line.strip() and len(line) > 10:
                strategies.append(line.strip())
        
        return strategies[:5] if strategies else self._default_strategy()
    
    def _default_strategy(self) -> List[str]:
        """Default strategy if LLM fails"""
        return [
            "Focus on mastering core technical skills through structured learning",
            "Build 2-3 portfolio projects demonstrating your target role skills",
            "Pursue relevant industry certifications",
            "Contribute to open-source projects in your target domain",
            "Network with professionals in your target role"
        ]
    
    def _generate_networking_tips(self, role: str) -> List[str]:
        """Generate networking tips"""
        tips = [
            f"Join {role} communities on LinkedIn and GitHub",
            "Attend industry conferences and meetups related to your role",
            "Connect with professionals already in {role} position on LinkedIn",
            "Participate in online forums and discussion groups",
            "Find mentors working in the {role} field"
        ]
        
        return [tip.format(role=role) for tip in tips]
    
    def _estimate_timeline(self, skill_gap: Dict) -> str:
        """Estimate timeline to reach target role"""
        readiness = skill_gap.get("readiness_score", 0)
        
        if readiness >= 80:
            return "3-6 months"
        elif readiness >= 60:
            return "6-12 months"
        elif readiness >= 40:
            return "12-18 months"
        else:
            return "18-24 months"