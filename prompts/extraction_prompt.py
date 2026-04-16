# ============================================================
# prompts/extraction_prompt.py - FULLY FIXED
# ============================================================

from langchain_core.prompts import PromptTemplate  # ✅ Already correct


def get_extraction_prompt():
    """
    Creates and returns a prompt template for skill extraction.
    """
    
    extraction_template = """
You are an expert HR analyst and resume parser. Your job is to carefully 
read a resume and extract specific information.

RESUME TO ANALYZE:
==================
{resume_text}
==================

EXTRACTION TASK:
Extract the following information from the resume above.
Be ACCURATE and only include what is ACTUALLY mentioned in the resume.
Do NOT add skills or experience that are not present.
Do NOT make assumptions or hallucinate information.

Please extract and list:

1. TECHNICAL SKILLS:
   List all technical skills mentioned (programming languages, frameworks, 
   libraries, tools, platforms)

2. YEARS OF EXPERIENCE:
   Total years of professional work experience in data science / tech field
   (Write "0 years" if no experience)

3. TOOLS AND TECHNOLOGIES:
   Specific tools, software, platforms mentioned 
   (e.g., Jupyter, Git, AWS, Docker, MySQL)

4. EDUCATION:
   Highest degree and field of study

5. CERTIFICATIONS:
   Any certifications or courses mentioned

6. KEY PROJECTS:
   Brief list of projects mentioned

FORMAT YOUR RESPONSE EXACTLY LIKE THIS:
========================================
CANDIDATE NAME: [name from resume]

TECHNICAL SKILLS:
- [skill 1]
- [skill 2]
- [skill 3]
(list all skills found)

YEARS OF EXPERIENCE: [number] years

TOOLS AND TECHNOLOGIES:
- [tool 1]
- [tool 2]
(list all tools found)

EDUCATION: [degree and field]

CERTIFICATIONS:
- [cert 1]
- [cert 2]
(write "None" if no certifications)

KEY PROJECTS:
- [project 1]
- [project 2]
(list projects found)
========================================

IMPORTANT RULES:
- Only include what is ACTUALLY in the resume
- Do not assume or hallucinate any information
- If something is not mentioned, write "Not mentioned"
- Be specific and accurate
"""
    
    prompt = PromptTemplate(
        input_variables=["resume_text"],
        template=extraction_template
    )
    
    return prompt


if __name__ == "__main__":
    prompt = get_extraction_prompt()
    print("✅ Extraction prompt created successfully!")
    print(f"Input variables needed: {prompt.input_variables}")