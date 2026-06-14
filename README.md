# CareerPilot AI 🚀

## Overview

CareerPilot AI is an AI-powered career guidance platform that helps students and job seekers discover the skills required for their dream role, identify skill gaps, and generate personalized career roadmaps.

The platform supports approximately **15 predefined career roles**, including:

* AI Engineer
* Data Scientist
* Full Stack Developer
* Cloud Engineer
* Cybersecurity Analyst
* DevOps Engineer
* Machine Learning Engineer
* Frontend Developer
* Backend Developer
* Data Analyst
* Product Manager
* UI/UX Designer
* Android Developer
* Blockchain Developer
* Software Engineer

Users can either upload their resume or continue without a resume to receive:

* Skill Gap Analysis
* Career Strategy
* Personalized Learning Roadmap
* Career Report

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python 3.12+

### AI Architecture

* Multi-Agent AI Architecture
* Prompt Engineering
* Role-based LLM Workflows

### LLM & AI Integration

* Groq API
* Llama 3.3 70B Versatile
* Environment Variable based API Authentication

### Database

* Firebase Realtime Database

### Development Tools

* GitHub Copilot
* Visual Studio Code
* Git & GitHub

---

## Groq API & LLM Integration

### Why Groq API?

This project uses **Groq API** with **Llama 3.3 70B Versatile** for intelligent AI-powered career guidance and roadmap generation.

### Benefits

* ✅ High-speed AI inference
* ✅ Powerful open-source LLM
* ✅ Easy API integration
* ✅ Cost-effective
* ✅ Scalable architecture

### Groq API Usage

```python
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = "llama-3.3-70b-versatile"
        self.client = Groq(api_key=self.api_key)
```

Groq API is used for:

* Resume Analysis
* Skill Gap Identification
* Career Strategy Generation
* Personalized Learning Roadmap Creation
* Career Report Generation

---

## Microsoft AI Stack Usage

This project uses **GitHub Copilot**, a Microsoft AI-powered coding assistant, during development.

GitHub Copilot was used for:

* Generating boilerplate code
* Improving developer productivity
* Assisting with code suggestions
* Documentation assistance

All final architecture, prompts, business logic, UI design, and engineering decisions were designed and implemented by the development team.

---

## Multi-Agent Workflow

CareerPilot AI follows a Multi-Agent Architecture:

```text
Resume Upload / Quick Start
          ↓
Resume Analyst Agent
          ↓
Skill Gap Agent
          ↓
Career Strategist Agent
          ↓
Learning Roadmap Agent
          ↓
Career Report
```

Each agent performs a specialized task and communicates through a centralized orchestrator.

---

## Features

✅ Resume Upload & Analysis (PDF/DOCX)

✅ Quick Start (No Resume Required)

✅ AI-Powered Skill Gap Identification

✅ LLM-Generated Career Strategy

✅ Personalized Learning Roadmap

✅ Interactive Career Report

✅ Multi-Agent AI Workflow

✅ Groq API Integration

✅ Firebase Realtime Database

✅ Streamlit Interactive UI

---

## Installation & Setup

### Prerequisites

* Python 3.12+
* Groq Account
* Groq API Key

---

### Installation Steps

```bash
# 1. Clone Repository

git clone https://github.com/NileshHI-coder/CareerPilot-AI.git

cd CareerPilot-AI


# 2. Create Virtual Environment

python -m venv venv


# Activate Virtual Environment

# Windows

venv\Scripts\activate

# Linux/macOS

source venv/bin/activate


# 3. Install Dependencies

pip install -r requirements.txt


# 4. Create .env File

# Windows

echo GROQ_API_KEY=your_api_key_here > .env
echo MODEL_NAME=llama-3.3-70b-versatile >> .env


# Linux/macOS

echo "GROQ_API_KEY=your_api_key_here" > .env
echo "MODEL_NAME=llama-3.3-70b-versatile" >> .env


# 5. Run Application

streamlit run app.py
```

---

## How to Get Groq API Key

1. Create a Groq account.

2. Open the API Keys Dashboard.

3. Generate a new API Key.

4. Copy the key into your `.env` file.

Example:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxx
MODEL_NAME=llama-3.3-70b-versatile
```

---

## Deployment

This application can be deployed on:

* Render
* Streamlit Community Cloud
* Azure App Service
* Docker Containers

---

## Future Enhancements

* Azure AI / Azure OpenAI Integration
* Real-time Job Market Analysis
* Adaptive Learning Recommendations
* User Authentication
* Resume Builder
* Job Matching Engine

---

## License

MIT License

Free to use, modify, and distribute.

---

## Author

**Nilesh HI**

GitHub: @NileshHI-coder

---

## Built With

❤️ GitHub Copilot (AI-assisted development)

⚡ Groq API (High-speed LLM inference)

🧠 Llama 3.3 70B Versatile

🚀 Streamlit

🔥 Firebase Realtime Database

---

**Status:** ✅ Production Ready

**Version:** 1.0.0
