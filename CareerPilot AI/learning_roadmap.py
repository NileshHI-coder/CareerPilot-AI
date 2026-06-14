from typing import Dict, List
from llm import LLMClient

class LearningRoadmapAgent:
    
    def __init__(self):
        self.llm = LLMClient()
    
    def run(self, target_role: str, missing_skills: List, readiness_score: int) -> Dict:
        """Generate personalized learning roadmap"""
        
        missing_skill_names = [s["skill"] if isinstance(s, dict) else s for s in missing_skills[:5]]
        
        phases = self._generate_phases(target_role, missing_skill_names, readiness_score)
        total_weeks = sum(phase["weeks"] for phase in phases)
        
        return {
            "target_role": target_role,
            "phases": phases,
            "total_estimated_weeks": total_weeks,
            "estimated_months": round(total_weeks / 4, 1),
            "learning_resources": self._get_learning_resources(target_role),
            "milestones": self._generate_milestones(phases)
        }
    
    def _generate_phases(self, role: str, missing_skills: List[str], readiness: int) -> List[Dict]:
        """Generate learning phases"""
        
        prompt = f"""
        Create a 4-phase learning roadmap for someone with {readiness}% readiness for {role}.
        
        Missing Skills: {', '.join(missing_skills)}
        
        Return exactly 4 phases in this format:
        Phase 1: [title] - [weeks] weeks
        Topics: [topics separated by semicolon]
        
        Phase 2: [title] - [weeks] weeks
        Topics: [topics separated by semicolon]
        
        Phase 3: [title] - [weeks] weeks
        Topics: [topics separated by semicolon]
        
        Phase 4: [title] - [weeks] weeks
        Topics: [topics separated by semicolon]
        
        Make it realistic and actionable.
        """
        
        response = self.llm.generate(prompt, max_tokens=800)
        
        phases = self._parse_phases_response(response)
        
        if not phases:
            phases = self._default_phases(role, readiness)
        
        return phases
    
    def _parse_phases_response(self, response: str) -> List[Dict]:
        """Parse LLM response into phases"""
        phases = []
        current_phase = None
        
        lines = response.split('\n')
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('Phase'):
                if current_phase:
                    phases.append(current_phase)
                
                parts = line.split('-')
                if len(parts) >= 2:
                    title = parts[0].replace('Phase', '').strip()
                    weeks_str = parts[1].strip().split()[0]
                    try:
                        weeks = int(weeks_str)
                    except:
                        weeks = 4
                    
                    current_phase = {
                        "title": title,
                        "weeks": weeks,
                        "topics": [],
                        "projects": []
                    }
            
            elif line.startswith('Topics:') and current_phase:
                topics_str = line.replace('Topics:', '').strip()
                current_phase["topics"] = [t.strip() for t in topics_str.split(';') if t.strip()]
            
            elif line.startswith('Projects:') and current_phase:
                projects_str = line.replace('Projects:', '').strip()
                current_phase["projects"] = [p.strip() for p in projects_str.split(';') if p.strip()]
        
        if current_phase:
            phases.append(current_phase)
        
        return phases
    
    def _default_phases(self, role: str, readiness: int) -> List[Dict]:
        """Default phases if parsing fails"""
        return [
            {
                "title": "Foundations",
                "weeks": 4,
                "topics": ["Core concepts", "Prerequisites", "Setup and tools"],
                "projects": ["Setup development environment"]
            },
            {
                "title": "Core Skills",
                "weeks": 8,
                "topics": ["Main technologies", "Key frameworks", "Best practices"],
                "projects": ["Build 1 beginner project"]
            },
            {
                "title": "Advanced Topics",
                "weeks": 8,
                "topics": ["System design", "Optimization", "Advanced patterns"],
                "projects": ["Build 1 intermediate project"]
            },
            {
                "title": "Specialization",
                "weeks": 4,
                "topics": ["Role-specific skills", "Industry practices", "Interview prep"],
                "projects": ["Build 1 portfolio project"]
            }
        ]
    
    def _get_learning_resources(self, role: str) -> Dict[str, List[str]]:
        """Get learning resources for role"""
        resources = {
            "Online Courses": [
                "Udemy",
                "Coursera",
                "Pluralsight",
                "LinkedIn Learning"
            ],
            "Documentation": [
                "Official documentation",
                "GitHub repositories",
                "Tech blogs",
                "Medium articles"
            ],
            "Practice Platforms": [
                "LeetCode",
                "HackerRank",
                "CodeSignal",
                "ProjectEuler"
            ],
            "Community": [
                "GitHub discussions",
                "Stack Overflow",
                "Reddit communities",
                "Discord servers"
            ]
        }
        return resources
    
    def _generate_milestones(self, phases: List[Dict]) -> List[str]:
        """Generate milestones"""
        milestones = []
        cumulative_weeks = 0
        
        for phase in phases:
            cumulative_weeks += phase["weeks"]
            milestone = f"Complete {phase['title']} - Week {cumulative_weeks}"
            milestones.append(milestone)
        
        return milestones