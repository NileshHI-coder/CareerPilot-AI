import re
from typing import Dict, List
from PyPDF2 import PdfReader
from docx import Document

class ResumeAnalystAgent:
    
    TECHNICAL_SKILLS_KEYWORDS = {
        "Programming Languages": [
            "Python", "Java", "JavaScript", "C++", "C#", "Go", "Rust", "Ruby", "PHP", "Swift", "Kotlin"
        ],
        "Web Technologies": [
            "HTML", "CSS", "React", "Vue", "Angular", "Node.js", "Express", "Django", "Flask", "ASP.NET"
        ],
        "Databases": [
            "SQL", "MongoDB", "PostgreSQL", "MySQL", "Redis", "Cassandra", "Firebase", "DynamoDB"
        ],
        "Cloud & DevOps": [
            "AWS", "Azure", "GCP", "Docker", "Kubernetes", "Jenkins", "GitLab", "Terraform", "Ansible"
        ],
        "Data & ML": [
            "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Scikit-learn", "Pandas", "NumPy", "Spark"
        ],
        "Tools": [
            "Git", "GitHub", "Linux", "Windows", "Jira", "Figma", "Adobe XD", "VS Code"
        ]
    }
    
    SOFT_SKILLS_KEYWORDS = [
        "Leadership", "Communication", "Problem Solving", "Team Player", "Adaptable", 
        "Project Management", "Critical Thinking", "Creativity", "Time Management"
    ]
    
    def run(self, resume_text: str) -> Dict:
        """Analyze resume and extract skills"""
        technical_skills = self._extract_technical_skills(resume_text)
        soft_skills = self._extract_soft_skills(resume_text)
        education = self._extract_education(resume_text)
        projects = self._extract_projects(resume_text)
        experience = self._extract_experience(resume_text)
        
        return {
            "technical_skills": technical_skills,
            "soft_skills": soft_skills,
            "education": education,
            "projects": projects,
            "experience": experience,
            "raw_text": resume_text[:500]
        }
    
    def _extract_technical_skills(self, text: str) -> List[str]:
        """Extract technical skills from resume"""
        skills = []
        text_lower = text.lower()
        
        for category, keywords in self.TECHNICAL_SKILLS_KEYWORDS.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    skills.append(keyword)
        
        return list(set(skills))
    
    def _extract_soft_skills(self, text: str) -> List[str]:
        """Extract soft skills from resume"""
        skills = []
        text_lower = text.lower()
        
        for skill in self.SOFT_SKILLS_KEYWORDS:
            if skill.lower() in text_lower:
                skills.append(skill)
        
        return list(set(skills))
    
    def _extract_education(self, text: str) -> str:
        """Extract education information"""
        education_keywords = ["Bachelor", "Master", "PhD", "B.Tech", "M.Tech", "B.S", "M.S"]
        lines = text.split('\n')
        
        for line in lines:
            for keyword in education_keywords:
                if keyword in line:
                    return line.strip()
        
        return "Education information not clearly specified"
    
    def _extract_projects(self, text: str) -> List[str]:
        """Extract projects from resume"""
        projects = []
        
        project_keywords = ["Project", "Built", "Developed", "Created", "Designed"]
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            for keyword in project_keywords:
                if keyword in line and len(line) > 10:
                    projects.append(line.strip())
        
        return projects[:5]
    
    def _extract_experience(self, text: str) -> List[str]:
        """Extract work experience"""
        experience = []
        
        experience_keywords = ["Experience", "Worked", "Employed", "Engineer", "Developer", "Manager"]
        lines = text.split('\n')
        
        for line in lines:
            for keyword in experience_keywords:
                if keyword in line and len(line) > 10:
                    experience.append(line.strip())
        
        return experience[:5]
    
    @staticmethod
    def extract_from_pdf(pdf_path: str) -> str:
        """Extract text from PDF"""
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            return f"Error reading PDF: {e}"
    
    @staticmethod
    def extract_from_docx(docx_path: str) -> str:
        """Extract text from DOCX"""
        try:
            doc = Document(docx_path)
            text = ""
            for para in doc.paragraphs:
                text += para.text + "\n"
            return text
        except Exception as e:
            return f"Error reading DOCX: {e}"