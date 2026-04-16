# 🤖 AI Resume Screening System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3.7-green?style=for-the-badge&logo=chainlink&logoColor=white)
![LangSmith](https://img.shields.io/badge/LangSmith-Tracing-orange?style=for-the-badge&logo=smith&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-FREE_AI-purple?style=for-the-badge&logo=groq&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-black?style=for-the-badge&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

### 🚀 An AI-powered Resume Screening System
### Built with LangChain + LangSmith + Groq/OpenAI

*Automatically evaluates candidates using*
*Skill Extraction → Matching → Scoring → Explanation*

---

[🚀 Features](#-features) •
[📁 Structure](#-project-structure) •
[⚙️ Installation](#️-installation) •
[▶️ Usage](#️-usage) •
[📊 Output](#-output) •
[🔧 Tech Stack](#-tech-stack) •
[🐛 Troubleshooting](#-troubleshooting)

</div>

---

## 📌 Project Overview

This project is an **AI-powered Resume Screening System** that automatically
evaluates job candidates by analyzing their resumes against a job description
using the power of **Large Language Models (LLMs)**.
INPUT → Resume Text + Job Description
PROCESS → AI extracts skills, matches, scores, explains
OUTPUT → Score (0-100) + Detailed Explanation + Recommendation

text


> 🎓 Built as part of **Data Science Internship - February 2026**
>
> 📌 Topic: **GenAI + LLM Engineering + Production AI Systems**

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 🧠 **AI Skill Extraction** | Automatically reads and extracts skills from any resume |
| 🔍 **Smart Matching** | Compares candidate profile with job requirements |
| 📊 **Scoring System** | Gives fair score out of 100 with full breakdown |
| 💡 **Explainable AI** | Tells you exactly WHY a score was given |
| 📡 **LangSmith Tracing** | Monitors and debugs every pipeline step |
| 🆓 **Free AI Support** | Works with FREE Groq API - no credit card needed |
| 💰 **OpenAI Support** | Also supports GPT-3.5-turbo for premium results |
| 📁 **Auto Save** | Saves all results to output files automatically |
| 🎯 **3 Candidates** | Tests Strong, Average, and Weak candidate profiles |
| 🔧 **Clean Code** | Modular, well-commented, beginner-friendly structure |

---

## 📁 Project Structure
ai-resume-screening/
│
├── 📂 prompts/
│ ├── init.py ← Package initializer
│ ├── extraction_prompt.py ← AI prompt to extract skills
│ ├── matching_prompt.py ← AI prompt to match skills
│ └── scoring_prompt.py ← AI prompt to score and explain
│
├── 📂 chains/
│ ├── init.py ← Package initializer
│ └── screening_chain.py ← Main pipeline - 3 steps
│
├── 📂 data/
│ ├── job_description.txt ← Data Scientist job post
│ ├── resume_strong.txt ← Strong candidate resume
│ ├── resume_average.txt ← Average candidate resume
│ └── resume_weak.txt ← Weak candidate resume
│
├── 📂 outputs/ ← Auto-generated result files
│ ├── result_Priya_Sharma.txt
│ ├── result_Rahul_Gupta.txt
│ └── result_Amit_Kumar.txt
│
├── 📂 screenshots/ ← LangSmith trace screenshots
│
├── 📄 main.py ← ▶️ Run this file!
├── 📄 config.py ← API keys and settings
├── 📄 requirements.txt ← All Python packages needed
├── 📄 .env ← 🔒 Secret keys - NOT on GitHub
├── 📄 .gitignore ← Files to ignore in Git
└── 📄 README.md ← You are reading this!

text


---

## 🔄 Pipeline Architecture
╔══════════════════════════════════════════════════════════╗
║ AI RESUME SCREENING PIPELINE ║
╠══════════════════════════════════════════════════════════╣
║ ║
║ 📄 Resume + 📋 Job Description ║
║ │ ║
║ ▼ ║
║ ┌─────────────────────────┐ ║
║ │ STEP 1 │ ║
║ │ Skill Extraction │ ║
║ │ (LangChain + LLM) │ ║
║ │ │ ║
║ │ Finds: Skills │ ║
║ │ Experience │ ║
║ │ Tools │ ║
║ │ Education │ ║
║ └────────────┬────────────┘ ║
║ │ ║
║ ▼ ║
║ ┌─────────────────────────┐ ║
║ │ STEP 2 │ ║
║ │ Skill Matching │ ║
║ │ (LangChain + LLM) │ ║
║ │ │ ║
║ │ Finds: Matched Skills │ ║
║ │ Missing Skills │ ║
║ │ Match Percent │ ║
║ └────────────┬────────────┘ ║
║ │ ║
║ ▼ ║
║ ┌─────────────────────────┐ ║
║ │ STEP 3 │ ║
║ │ Score and Explain │ ║
║ │ (LangChain + LLM) │ ║
║ │ │ ║
║ │ Gives: Score 0-100 │ ║
║ │ Strengths │ ║
║ │ Weaknesses │ ║
║ │ Recommendation │ ║
║ └────────────┬────────────┘ ║
║ │ ║
║ ▼ ║
║ 📊 Final Output + 📡 LangSmith Tracing ║
║ ║
╚══════════════════════════════════════════════════════════╝

text


---

## ⚙️ Installation

### Prerequisites
Make sure you have these installed:
✅ Python 3.10 or higher
✅ pip (comes with Python)
✅ Git
✅ VS Code (recommended)

text


### Step 1 - Clone Repository

```bash
git clone https://github.com/YourUsername/ai-resume-screening.git
cd ai-resume-screening
Step 2 - Create Virtual Environment
Bash

# Create virtual environment
python -m venv venv

# Activate on Windows CMD
venv\Scripts\activate

# Activate on Mac or Linux
source venv/bin/activate

# You will see (venv) at start of terminal - that means its working
Step 3 - Install All Packages
Bash

pip install -r requirements.txt
Step 4 - Get Your API Keys
🆓 Groq API Key - FREE and Recommended
text

1. Visit  : https://console.groq.com
2. Action : Sign up FREE with Google
3. Go to  : API Keys section
4. Click  : Create API Key
5. Copy   : your key and save it safely
💰 OpenAI API Key - Paid Option
text

1. Visit  : https://platform.openai.com
2. Action : Login to your account
3. Go to  : API Keys section
4. Click  : Create New Secret Key
5. Add    : minimum $5 in billing
6. Copy   : your key (starts with sk-)
📡 LangSmith API Key - FREE for Tracing
text

1. Visit  : https://smith.langchain.com
2. Action : Sign up FREE
3. Go to  : Settings → API Keys
4. Click  : Create API Key
5. Copy   : your key and save it safely
Step 5 - Setup Environment File
Bash

# Create .env file in project root
# Add your keys like this:
env

# ================================
# AI Provider Keys
# ================================
OPENAI_API_KEY=sk-your-openai-key-here
GROQ_API_KEY=your-groq-key-here

# ================================
# LangSmith Tracing - Required
# ================================
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your-langsmith-key-here
LANGCHAIN_PROJECT=ai-resume-screening

# ================================
# Model Settings
# ================================
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_TEMPERATURE=0.1
Step 6 - Choose AI Provider
Python

# Open config.py and set this line:

AI_PROVIDER = "groq"    # FREE - Best for beginners
# OR
AI_PROVIDER = "openai"  # Paid - Better quality results
▶️ Usage
Run the System
Bash

python main.py
What Happens When You Run
text

Phase 1 → Validates all API keys and configuration
Phase 2 → Loads job description and 3 resumes from data folder
Phase 3 → Initializes AI pipeline with chosen model
Phase 4 → Runs screening for each candidate:

          Candidate 1 → Priya Sharma  (Strong Profile)
          Candidate 2 → Rahul Gupta   (Average Profile)
          Candidate 3 → Amit Kumar    (Weak Profile)

Phase 5 → Displays complete results in terminal
Phase 6 → Saves results to outputs folder
Phase 7 → All steps traced in LangSmith dashboard
📊 Output
Terminal Output
text

🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟
   AI RESUME SCREENING SYSTEM
   Powered by LangChain + Groq + LangSmith
🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟

✅ Configuration loaded successfully!
✅ AI Provider  : GROQ (FREE)
✅ Tracing      : LangSmith Active

📄 Step 1: Extracting skills from resume...
✅ Skills extracted!

🔍 Step 2: Matching with job description...
✅ Matching completed!

📊 Step 3: Scoring and explaining...
✅ Scoring completed!

SCORE BREAKDOWN:
- Required Skills  : 40 / 40
- Experience       : 25 / 25
- Preferred Skills : 18 / 20
- Education        : 15 / 15

FINAL SCORE        : 98 / 100 ⭐
CANDIDATE LEVEL    : Excellent - Strong Hire 🌟
RECOMMENDATION     : STRONG HIRE ✅

📊 SCREENING COMPLETE!
Total Screened : 3
✅ Successful  : 3
❌ Failed      : 0
Results Summary Table
#	Candidate	Profile	Score	Level	Recommendation
1	Priya Sharma	Strong	98 / 100	⭐ Excellent	✅ STRONG HIRE
2	Rahul Gupta	Average	57 / 100	📚 Average	🤔 MAYBE
3	Amit Kumar	Weak	08 / 100	❌ Weak	❌ REJECT
🔧 Tech Stack
Technology	Version	Purpose
🐍 Python	3.10+	Core programming language
🔗 LangChain	0.3.7	LLM pipeline framework
🧩 LangChain Core	0.3.15	Prompts and core components
📡 LangSmith	0.1.147	Pipeline tracing and monitoring
🤖 LangChain Groq	0.2.1	FREE Groq AI model integration
🧠 LangChain OpenAI	0.2.9	OpenAI GPT model integration
🦙 Groq Llama3	Free	FREE large language model
💬 OpenAI GPT-3.5	Paid	Premium language model
🔐 Python Dotenv	1.0.1	Secure environment variables
🌐 httpx	0.27.2	HTTP client stable version
📡 LangSmith Tracing
text

Every pipeline run is automatically tracked in LangSmith.
No extra code needed - just set LANGCHAIN_TRACING_V2=true
How to View Traces
text

Step 1 → Go to  : https://smith.langchain.com
Step 2 → Login  : with your account
Step 3 → Click  : Projects in left sidebar
Step 4 → Find   : ai-resume-screening project
Step 5 → See    : all 3 candidate runs listed
Step 6 → Click  : any run to see all 3 steps inside
Step 7 → Debug  : check inputs outputs and errors
What LangSmith Shows
text

✅ Complete input sent to AI for each step
✅ Complete output received from AI
✅ Time taken for each LLM call
✅ Total tokens used and API cost
✅ All 3 pipeline steps clearly visible
✅ Error details if anything fails
✅ Side by side comparison of all runs
🎯 Scoring System
How Score is Calculated
Category	Max Points	How It Is Measured
✅ Required Skills	40 points	Core job skills present in resume
💼 Experience	25 points	Years of relevant work experience
⭐ Preferred Skills	20 points	Bonus skills beyond requirements
🎓 Education	15 points	Degree relevance and institution
🏆 Total	100 points	Final candidate score
Score Interpretation
text

╔══════════════════════════════════════════════╗
║  SCORE    LEVEL        RECOMMENDATION        ║
╠══════════════════════════════════════════════╣
║  80-100   Excellent    ✅ Strong Hire         ║
║  60-79    Good         🟡 Consider           ║
║  40-59    Average      🤔 Maybe with Training║
║  00-39    Weak         ❌ Reject             ║
╚══════════════════════════════════════════════╝
🐛 Troubleshooting
❌ Error	🔍 Cause	✅ Fix
No module named dotenv	venv not active	Run venv\Scripts\activate
No module named langchain.prompts	Wrong import path	Use langchain_core.prompts
Error 429 quota exceeded	No OpenAI credits	Switch to FREE Groq
proxies keyword argument	httpx version conflict	Run pip install httpx==0.27.2
list.remove not in list	LangSmith decorator bug	Remove @traceable decorators
FileNotFoundError	Wrong working directory	Run from project root folder
AuthenticationError	Wrong API key in .env	Double check your API keys
Connection refused	No internet connection	Check your internet connection
📋 Requirements File
txt

langchain==0.3.7
langchain-core==0.3.15
langchain-openai==0.2.9
langchain-community==0.3.7
langchain-groq==0.2.1
langsmith==0.1.147
openai==1.54.4
python-dotenv==1.0.1
tiktoken==0.8.0
httpx==0.27.2
⚡ Quick Start
Bash

# 1 - Clone and enter folder
git clone https://github.com/YourUsername/ai-resume-screening.git
cd ai-resume-screening

# 2 - Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 3 - Install all packages
pip install -r requirements.txt

# 4 - Add your API keys to .env file
# Get FREE key from https://console.groq.com
# Get FREE key from https://smith.langchain.com

# 5 - Run the project
python main.py
📚 Learning Outcomes
text

After completing this project you will know how to:

✅ Build LLM based evaluation systems from scratch
✅ Create modular AI pipelines using LangChain
✅ Implement skill extraction using prompt engineering
✅ Use LangSmith for tracing debugging and monitoring
✅ Build explainable AI outputs with clear reasoning
✅ Structure production level AI projects properly
✅ Use PromptTemplate and LCEL in LangChain
✅ Handle API errors and edge cases gracefully
✅ Work with environment variables and API keys safely
✅ Build beginner friendly yet powerful AI applications
🤝 Contributing
Bash

# Step 1 - Fork this repository on GitHub

# Step 2 - Clone your fork
git clone https://github.com/YourUsername/ai-resume-screening.git

# Step 3 - Create a new branch
git checkout -b feature/your-feature-name

# Step 4 - Make your changes and save

# Step 5 - Add and commit
git add .
git commit -m "Add: description of your changes"

# Step 6 - Push to your fork
git push origin feature/your-feature-name

# Step 7 - Open Pull Request on GitHub
📄 License
text

MIT License

Copyright (c) 2026 Your Name

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software to use, copy, modify, merge, publish, and
distribute freely, provided the above copyright notice is included.
👨‍💻 Author
<div align="center">
Field	Details
👤 Name	Your Full Name
🎓 Role	Data Science Intern - February 2026
💼 LinkedIn	linkedin.com/in/yourprofile
🐙 GitHub	github.com/YourUsername
📧 Email	your.email@gmail.com
</div>
🙏 Acknowledgements
text

Special thanks to these amazing tools and platforms:

🔗 LangChain     →  https://python.langchain.com
📡 LangSmith     →  https://smith.langchain.com
🤖 Groq          →  https://console.groq.com
🧠 OpenAI        →  https://platform.openai.com
🐍 Python        →  https://python.org
<div align="center">
⭐ Found this helpful? Please give it a Star! ⭐
text

🚀 From Prompt Usage to Production AI Systems 🚀
Built with ❤️ for Data Science Internship February 2026

</div> ```