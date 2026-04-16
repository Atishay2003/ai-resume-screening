# ============================================================
# prompts/scoring_prompt.py - NEW FIXED FILE
# This was MISSING from your project - Added now!
# ============================================================

from langchain_core.prompts import PromptTemplate


def get_scoring_prompt():
    """
    Creates and returns a prompt template for scoring candidates.
    """
    
    scoring_template = """
You are an expert HR recruiter. Based on the match analysis below,
provide a final score and detailed explanation for this candidate.

MATCH ANALYSIS:
===============
{match_analysis}
===============

SCORING TASK:
Based on the match analysis above, provide:

1. FINAL SCORE (0-100):
   Calculate based on:
   - Required skills match (50% weight)
   - Experience match (25% weight)
   - Education match (15% weight)
   - Preferred skills match (10% weight)

2. RECOMMENDATION:
   - STRONG HIRE (Score 80-100)
   - CONSIDER (Score 60-79)
   - MAYBE (Score 40-59)
   - REJECT (Score 0-39)

3. STRENGTHS:
   What makes this candidate good for the role?

4. WEAKNESSES:
   What is this candidate missing?

5. INTERVIEW RECOMMENDATION:
   Should we interview this candidate? Why?

FORMAT YOUR RESPONSE EXACTLY LIKE THIS:
=========================================
FINAL SCORE: [number]/100

RECOMMENDATION: [STRONG HIRE / CONSIDER / MAYBE / REJECT]

STRENGTHS:
- [strength 1]
- [strength 2]
- [strength 3]

WEAKNESSES:
- [weakness 1]
- [weakness 2]

INTERVIEW RECOMMENDATION:
[Yes/No] - [2-3 sentences explaining why]

DETAILED EXPLANATION:
[Write 3-4 sentences with complete evaluation summary]
=========================================

RULES:
- Be fair and objective
- Base score ONLY on the match analysis provided
- Give specific reasons for your score
"""
    
    prompt = PromptTemplate(
        input_variables=["match_analysis"],
        template=scoring_template
    )
    
    return prompt


if __name__ == "__main__":
    prompt = get_scoring_prompt()
    print("✅ Scoring prompt created successfully!")
    print(f"Input variables needed: {prompt.input_variables}")