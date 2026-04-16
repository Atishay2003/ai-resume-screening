# ============================================================
# config.py - Configuration and Settings
# This file loads all API keys and settings from .env file
# ============================================================

import os
from dotenv import load_dotenv

# Load all values from .env file
load_dotenv()

# ============================================================
# OpenAI Settings
# ============================================================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.1"))

# ============================================================
# LangSmith Settings (for tracing and monitoring)
# ============================================================
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "true")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "ai-resume-screening")

# ============================================================
# Validation - Check if keys are present
# ============================================================
def validate_config():
    """
    This function checks if all required API keys are set.
    If any key is missing, it shows an error message.
    """
    errors = []
    
    if not OPENAI_API_KEY:
        errors.append("❌ OPENAI_API_KEY is missing in .env file")
    
    if not LANGCHAIN_API_KEY:
        errors.append("❌ LANGCHAIN_API_KEY is missing in .env file")
    
    if errors:
        print("\n" + "="*50)
        print("CONFIGURATION ERRORS FOUND:")
        print("="*50)
        for error in errors:
            print(error)
        print("="*50)
        print("Please add the missing keys to your .env file")
        print("="*50 + "\n")
        return False
    
    print("✅ Configuration loaded successfully!")
    print(f"✅ Model: {OPENAI_MODEL}")
    print(f"✅ LangSmith Project: {LANGCHAIN_PROJECT}")
    print(f"✅ Tracing: {LANGCHAIN_TRACING_V2}")
    return True


# ============================================================
# Job Requirements (what skills we look for)
# ============================================================
JOB_REQUIREMENTS = {
    "required_skills": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "Data Analysis",
        "SQL",
        "Statistics"
    ],
    "preferred_skills": [
        "TensorFlow",
        "PyTorch",
        "Scikit-learn",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "AWS",
        "Docker"
    ],
    "required_experience_years": 2,
    "preferred_tools": [
        "Jupyter Notebook",
        "Git",
        "VS Code"
    ]
}