# ============================================================
# main.py - FULLY FIXED VERSION
# ============================================================

import os
import sys

from dotenv import load_dotenv
load_dotenv()

from config import validate_config, OPENAI_MODEL, OPENAI_TEMPERATURE
from chains.screening_chain import ResumeScreeningChain


def load_file(filepath: str) -> str:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"  ✅ Loaded: {filepath}")
        return content
    except FileNotFoundError:
        print(f"  ❌ File not found: {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"  ❌ Error loading {filepath}: {str(e)}")
        sys.exit(1)


def display_separator(title: str = ""):
    if title:
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}")
    else:
        print(f"\n{'='*60}")


def display_results(results: dict):
    candidate = results.get("candidate_name", "Unknown")
    status = results.get("status", "UNKNOWN")
    
    display_separator(f"RESULTS: {candidate}")
    
    if status == "FAILED":
        print(f"\n❌ Pipeline FAILED for {candidate}")
        print(f"Error: {results.get('error', 'Unknown error')}")
        return
    
    print("\n📄 STEP 1 - EXTRACTED INFORMATION:")
    print("-" * 40)
    print(results.get("extracted_info", "No data"))
    
    print("\n🔍 STEP 2 - MATCH ANALYSIS:")
    print("-" * 40)
    print(results.get("match_analysis", "No data"))
    
    print("\n📊 STEP 3 - SCORE AND EXPLANATION:")
    print("-" * 40)
    print(results.get("score_explanation", "No data"))


def save_results(results: dict, output_dir: str = "outputs"):
    os.makedirs(output_dir, exist_ok=True)
    
    candidate = results.get("candidate_name", "unknown")
    filename = f"{output_dir}/result_{candidate.replace(' ', '_')}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"RESUME SCREENING RESULTS\n")
            f.write(f"{'='*60}\n")
            f.write(f"Candidate: {candidate}\n")
            f.write(f"Status: {results.get('status')}\n")
            f.write(f"{'='*60}\n\n")
            
            if results.get("status") == "SUCCESS":
                f.write("STEP 1 - EXTRACTED INFORMATION:\n")
                f.write("-"*40 + "\n")
                f.write(results.get("extracted_info", "") + "\n\n")
                
                f.write("STEP 2 - MATCH ANALYSIS:\n")
                f.write("-"*40 + "\n")
                f.write(results.get("match_analysis", "") + "\n\n")
                
                f.write("STEP 3 - SCORE AND EXPLANATION:\n")
                f.write("-"*40 + "\n")
                f.write(results.get("score_explanation", "") + "\n\n")
        
        print(f"  💾 Results saved to: {filename}")
        
    except Exception as e:
        print(f"  ⚠️  Could not save results: {str(e)}")


def main():
    print("\n" + "🌟"*30)
    print("   AI RESUME SCREENING SYSTEM")
    print("   Powered by LangChain + OpenAI + LangSmith")
    print("🌟"*30)
    
    display_separator("PHASE 1: Configuration Check")
    if not validate_config():
        print("\n❌ Please fix configuration errors and try again.")
        sys.exit(1)
    
    display_separator("PHASE 2: Loading Data Files")
    print("\nLoading job description...")
    job_description = load_file("data/job_description.txt")
    
    print("\nLoading resumes...")
    resume_strong = load_file("data/resume_strong.txt")
    resume_average = load_file("data/resume_average.txt")
    resume_weak = load_file("data/resume_weak.txt")
    
    print("\n✅ All files loaded successfully!")
    
    display_separator("PHASE 3: Initializing AI Pipeline")
    pipeline = ResumeScreeningChain(
        model_name=OPENAI_MODEL,
        temperature=OPENAI_TEMPERATURE
    )
    
    candidates = [
        {
            "name": "Priya Sharma",
            "resume": resume_strong,
            "type": "Strong Candidate"
        },
        {
            "name": "Rahul Gupta",
            "resume": resume_average,
            "type": "Average Candidate"
        },
        {
            "name": "Amit Kumar",
            "resume": resume_weak,
            "type": "Weak Candidate"
        }
    ]
    
    display_separator("PHASE 5: Running AI Screening Pipeline")
    print("\n📋 Will screen these candidates:")
    for i, candidate in enumerate(candidates, 1):
        print(f"  {i}. {candidate['name']} ({candidate['type']})")
    
    print("\n⏳ Starting pipeline... (This takes 1-2 minutes)")
    print("📡 All runs will be traced in LangSmith automatically\n")
    
    all_results = []
    
    for i, candidate in enumerate(candidates, 1):
        print(f"\n{'🔄'*20}")
        print(f"Processing Candidate {i}/3: {candidate['name']}")
        print(f"Type: {candidate['type']}")
        print(f"{'🔄'*20}")
        
        results = pipeline.run_pipeline(
            resume_text=candidate["resume"],
            job_description=job_description,
            candidate_name=candidate["name"]
        )
        
        all_results.append(results)
        display_results(results)
        
        print(f"\n💾 Saving results...")
        save_results(results)
    
    display_separator("PHASE 6: FINAL SUMMARY")
    
    print("\n📊 SCREENING COMPLETE!")
    print(f"\nTotal candidates screened: {len(all_results)}")
    
    successful = sum(1 for r in all_results if r["status"] == "SUCCESS")
    failed = sum(1 for r in all_results if r["status"] == "FAILED")
    
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    
    print("\n💡 Check your LangSmith dashboard for traces:")
    print("   https://smith.langchain.com")
    print("   Project: ai-resume-screening")
    
    print("\n📁 Results saved in: outputs/ folder")
    
    print("\n" + "🎉"*30)
    print("   AI RESUME SCREENING COMPLETED!")
    print("🎉"*30 + "\n")


if __name__ == "__main__":
    main()