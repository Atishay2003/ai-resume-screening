# ============================================================
# prompts/matching_prompt.py - FULLY FIXED
# ============================================================

# ✅ FIXED: Changed from langchain.prompts to langchain_core.prompts
from langchain_core.prompts import PromptTemplate


def get_matching_prompt():
    """
    Creates and returns a prompt template for skill matching.
    """
    
    matching_template = """
You are an expert technical recruiter. Your job is to compare a 
candidate's extracted skills with job requirements and find matches.

CANDIDATE INFORMATION (Extracted from Resume):
===============================================
{extracted_info}
===============================================

JOB DESCRIPTION AND REQUIREMENTS:
===================================
{job_description}
===================================

MATCHING TASK:
Compare the candidate information with the job requirements carefully.
Only match skills that are EXPLICITLY mentioned in the candidate info.
Do NOT assume the candidate has skills not mentioned.

Please analyze and provide:

1. MATCHED REQUIRED SKILLS:
   Skills from job requirements that the candidate HAS

2. MISSING REQUIRED SKILLS:
   Skills from job requirements that the candidate DOES NOT have or 
   it's unclear

3. MATCHED PREFERRED SKILLS:
   Preferred/bonus skills that the candidate has

4. EXPERIENCE MATCH:
   Does the candidate meet the experience requirement?
   (Required: 2-5 years)

5. EDUCATION MATCH:
   Does the candidate meet education requirements?

6. OVERALL MATCH PERCENTAGE:
   Your estimate: what percentage of requirements are met?
   (Give a number between 0-100)

FORMAT YOUR RESPONSE EXACTLY LIKE THIS:
=========================================
MATCHED REQUIRED SKILLS:
- [matched skill 1]
- [matched skill 2]
(list all matches, or write "None" if no matches)

MISSING REQUIRED SKILLS:
- [missing skill 1]
- [missing skill 2]
(list all missing skills)

MATCHED PREFERRED SKILLS:
- [preferred skill 1]
- [preferred skill 2]
(list matched preferred skills, or write "None")

EXPERIENCE MATCH: [Yes/No/Partial] - [brief explanation]

EDUCATION MATCH: [Yes/No] - [brief explanation]

OVERALL MATCH PERCENTAGE: [number]%

MATCH SUMMARY:
[Write 2-3 sentences explaining the overall match quality]
=========================================

RULES:
- Be objective and accurate
- Base matching ONLY on what is in the candidate info
- Do not give benefit of doubt for missing skills
"""
    
    # ✅ FIXED import is at top of file
    prompt = PromptTemplate(
        input_variables=["extracted_info", "job_description"],
        template=matching_template
    )
    
    return prompt


if __name__ == "__main__":
    prompt = get_matching_prompt()
    print("✅ Matching prompt created successfully!")
    print(f"Input variables needed: {prompt.input_variables}")