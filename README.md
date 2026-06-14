CareerPilot AI 🚀
Overview
CareerPilot AI is an AI-powered career guidance platform that helps students and job seekers discover the skills required for their dream role, identify skill gaps, and generate personalized career roadmaps.

The platform supports approximately 15 predefined career roles, including:

AI Engineer
Data Scientist
Full Stack Developer
Cloud Engineer
Cybersecurity Analyst
DevOps Engineer
Machine Learning Engineer
Frontend Developer
Backend Developer
Data Analyst
Product Manager
UI/UX Designer
Android Developer
Blockchain Developer
Software Engineer
Users can either upload their resume or continue without a resume to receive:

Skill Gap Analysis
Career Strategy
Personalized Learning Roadmap
Career Report
Tech Stack
Frontend
Streamlit
Backend
Python 3.11
AI Architecture
Multi-Agent AI Architecture
Prompt Engineering
Role-based LLM workflows
Database
Firebase Realtime Database
Development Tools
GitHub Copilot
Visual Studio Code
Git & GitHub
Why Groq API?
This project uses Groq API with Llama 3.3 70B Versatile for intelligent AI-powered career guidance and roadmap generation.

Benefits:
✅ Fast inference with Groq's high-performance infrastructure ✅ Powerful open-source LLM – Llama 3.3 70B Versatile ✅ Easy API integration ✅ Cost-effective for development and prototyping ✅ Reliable and scalable AI inference

Groq API Usage
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = "llama-3.3-70b-versatile"
        self.client = Groq(api_key=self.api_key)
Groq API is used for:
Resume Analysis Skill Gap Identification Career Strategy Generation Personalized Learning Roadmap Creation Career Report Generation

Get your Groq API Key: https://console.groq.com/keys

AI & LLM Integration
Groq API – High-Speed LLM Inference Llama 3.3 70B Versatile – Large Language Model Groq API Key – Authentication Multi-Agent AI Architecture Prompt Engineering Role-based LLM Workflows

Microsoft AI Stack Usage
This project uses GitHub Copilot, a Microsoft AI-powered coding assistant, during development.

GitHub Copilot was used for:

Generating boilerplate code
Improving developer productivity
Assisting with code suggestions
Documentation assistance
All final architecture, prompts, business logic, UI design, and engineering decisions were designed and implemented by the development team.

Multi-Agent Workflow
CareerPilot AI follows a Multi-Agent Architecture:

Resume Upload / Quick Start ↓ Resume Analyst Agent ↓ Skill Gap Agent ↓ Career Strategist Agent ↓ Learning Roadmap Agent ↓ Career Report

Each agent performs a specialized task and communicates through a centralized orchestrator.

Features
✅ Resume Upload & Analysis (PDF/DOCX) ✅ Quick Start (No Resume Required) ✅ AI-Powered Skill Gap Identification ✅ LLM-Generated Career Strategy ✅ Personalized Learning Roadmap ✅ Interactive Career Report ✅ Multi-Agent AI Workflow ✅ GROQ API KEY ✅ Streamlit Interactive UI
Future Enhancements
Azure AI / Azure OpenAI Integration
Real-time Job Market Analysis
Adaptive Learning Recommendations
User Authentication
Resume Builder
Installation & Setup
Prerequisites
Python 3.12+
Groq Account
Groq API Key
Installation Steps
# 1. Clone repository
git clone https://github.com/NileshHI-coder/CareerPilot-AI.git
cd CareerPilot-AI

# 2. Create virtual environment
python -m venv venv

# Activate virtual environment

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file

# Windows
echo GROQ_API_KEY=your_api_key_here > .env
echo MODEL_NAME=llama-3.3-70b-versatile >> .env

# Linux / macOS
echo "GROQ_API_KEY=your_api_key_here" > .env
echo "MODEL_NAME=llama-3.3-70b-versatile" >> .env

# 5. Run application
streamlit run app.py
How to Get Groq API Key
Create an account on Groq.
Visit the API Keys dashboard.
Generate a new API Key.
Copy the key and paste it into the .env file.
Example:

GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxx
MODEL_NAME=llama-3.3-70b-versatile
License
MIT License - Free to use and modify

Author
Nilesh HI GitHub: @NileshHI-coder

Built with:

❤️ GitHub Copilot (AI-assisted development) 🤖 GitHub Models (LLM inference) 🧠 Llama 4 Scout (Open-source AI model by Meta) Status: ✅ Production Ready | Version: 1.0.0
