# ============================================================
# chains/screening_chain.py
# FIXED VERSION - No traceable decorator conflict
# Pipeline: Resume → Extract → Match → Score → Explain
# ============================================================

import os
from langchain_openai import ChatOpenAI
# NEW - works perfectly
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage

# Import our custom prompts
from prompts.extraction_prompt import get_extraction_prompt
from prompts.matching_prompt import get_matching_prompt
from prompts.scoring_prompt import get_scoring_prompt


class ResumeScreeningChain:
    """
    Main Resume Screening Pipeline Class
    
    Steps:
    Step 1: Extract skills from resume
    Step 2: Match with job description  
    Step 3: Score and explain
    """
    
    def __init__(self, model_name="gpt-3.5-turbo", temperature=0.1):
        """
        Initialize the pipeline with AI model settings
        
        Args:
            model_name: Which OpenAI model to use
            temperature: 0.1 = accurate and consistent results
        """
        print(f"\n🤖 Initializing AI Model: {model_name}")
        
        # Create the AI model
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=temperature
        )
        
        # Load all prompt templates
        self.extraction_prompt = get_extraction_prompt()
        self.matching_prompt = get_matching_prompt()
        self.scoring_prompt = get_scoring_prompt()
        
        print("✅ Pipeline initialized successfully!")
        print("✅ All prompts loaded!")

    def _call_ai(self, prompt_text: str) -> str:
        """
        Helper method to call OpenAI API
        
        Args:
            prompt_text: The complete prompt to send
            
        Returns:
            str: AI response text
        """
        # Create message and call AI
        messages = [HumanMessage(content=prompt_text)]
        response = self.llm.invoke(messages)
        return response.content

    def extract_skills(self, resume_text: str) -> str:
        """
        STEP 1: Extract skills and information from resume
        
        Args:
            resume_text: The full resume text
            
        Returns:
            str: Extracted information
        """
        print("\n  📄 Step 1: Extracting skills from resume...")
        
        # Format prompt with resume text
        formatted_prompt = self.extraction_prompt.format(
            resume_text=resume_text
        )
        
        # Call AI
        result = self._call_ai(formatted_prompt)
        
        print("  ✅ Skills extracted successfully!")
        return result

    def match_skills(self, extracted_info: str, job_description: str) -> str:
        """
        STEP 2: Match extracted skills with job requirements
        
        Args:
            extracted_info: Output from extract_skills()
            job_description: The job description text
            
        Returns:
            str: Match analysis
        """
        print("\n  🔍 Step 2: Matching skills with job description...")
        
        # Format prompt with both inputs
        formatted_prompt = self.matching_prompt.format(
            extracted_info=extracted_info,
            job_description=job_description
        )
        
        # Call AI
        result = self._call_ai(formatted_prompt)
        
        print("  ✅ Matching completed successfully!")
        return result

    def score_and_explain(self, match_analysis: str) -> str:
        """
        STEP 3: Score the candidate and provide explanation
        
        Args:
            match_analysis: Output from match_skills()
            
        Returns:
            str: Score and explanation
        """
        print("\n  📊 Step 3: Scoring candidate and generating explanation...")
        
        # Format prompt with match analysis
        formatted_prompt = self.scoring_prompt.format(
            match_analysis=match_analysis
        )
        
        # Call AI
        result = self._call_ai(formatted_prompt)
        
        print("  ✅ Scoring completed successfully!")
        return result

    def run_pipeline(
        self,
        resume_text: str,
        job_description: str,
        candidate_name: str = "Unknown"
    ) -> dict:
        """
        MAIN PIPELINE: Runs all 3 steps together
        
        Args:
            resume_text: Full resume text
            job_description: Job description text
            candidate_name: Name of candidate
            
        Returns:
            dict: Complete results with all steps
        """
        print(f"\n{'='*60}")
        print(f"🚀 Starting Pipeline for: {candidate_name}")
        print(f"{'='*60}")
        
        try:
            # STEP 1: Extract
            extracted_info = self.extract_skills(resume_text)
            
            # STEP 2: Match
            match_analysis = self.match_skills(
                extracted_info, 
                job_description
            )
            
            # STEP 3: Score
            score_explanation = self.score_and_explain(match_analysis)
            
            # Return all results
            results = {
                "candidate_name": candidate_name,
                "status": "SUCCESS",
                "extracted_info": extracted_info,
                "match_analysis": match_analysis,
                "score_explanation": score_explanation
            }
            
            print(f"\n✅ Pipeline completed for: {candidate_name}")
            return results

        except Exception as e:
            print(f"\n❌ Pipeline failed for {candidate_name}: {str(e)}")
            return {
                "candidate_name": candidate_name,
                "status": "FAILED",
                "error": str(e),
                "extracted_info": None,
                "match_analysis": None,
                "score_explanation": None
            }