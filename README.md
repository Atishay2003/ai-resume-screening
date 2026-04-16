# AI Resume Screening System

This project screens text resumes against a job description using a simple
three-step LangChain pipeline:

1. Extract candidate skills and background from the resume
2. Compare the extracted information with the job description
3. Generate a final score, recommendation, and explanation

The current implementation uses `ChatOpenAI` for inference and LangSmith for
trace collection.

## Features

- End-to-end resume screening pipeline in plain Python
- Modular prompt files for extraction, matching, and scoring
- LangSmith tracing support for every LLM call
- Sample job description and three sample resumes included
- Result files saved automatically under `outputs/`

## Project Structure

```text
ai-resume-screening/
|-- chains/
|   |-- __init__.py
|   `-- screening_chain.py
|-- data/
|   |-- job_description.txt
|   |-- resume_average.txt
|   |-- resume_strong.txt
|   `-- resume_weak.txt
|-- outputs/
|   |-- result_Amit_Kumar.txt
|   |-- result_Priya_Sharma.txt
|   `-- result_Rahul_Gupta.txt
|-- prompts/
|   |-- __init__.py
|   |-- extraction_prompt.py
|   |-- matching_prompt.py
|   `-- scoring_prompt.py
|-- screenshots/
|-- config.py
|-- main.py
`-- requirements.txt
```

## Requirements

- Python 3.10 or newer
- An OpenAI API key
- A LangSmith API key

Install dependencies:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

On macOS or Linux, activate the environment with:

```bash
source venv/bin/activate
```

## Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-your-openai-key-here
LANGCHAIN_API_KEY=your-langsmith-key-here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ai-resume-screening

# Optional overrides
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_TEMPERATURE=0.1
```

Notes:

- `OPENAI_API_KEY` is required by `config.py`
- `LANGCHAIN_API_KEY` is also required by `config.py`
- `LANGCHAIN_TRACING_V2` defaults to `true` if omitted, but setting it
  explicitly is clearer

## How It Works

### Step 1: Extraction

`prompts/extraction_prompt.py` asks the model to identify:

- Candidate name
- Technical skills
- Years of experience
- Tools and technologies
- Education
- Certifications
- Key projects

### Step 2: Matching

`prompts/matching_prompt.py` compares the extracted information with
`data/job_description.txt` and produces:

- Matched required skills
- Missing required skills
- Matched preferred skills
- Experience and education fit
- Overall match percentage
- Short match summary

### Step 3: Scoring

`prompts/scoring_prompt.py` converts the match analysis into:

- Final score out of 100
- Hiring recommendation
- Strengths
- Weaknesses
- Interview recommendation
- Detailed explanation

## Running the Project

Run the pipeline from the project root:

```bash
python main.py
```

The script will:

1. Validate the environment configuration
2. Load the job description from `data/job_description.txt`
3. Load three sample resumes from `data/`
4. Run the three-step screening pipeline for each candidate
5. Print the results in the terminal
6. Save one output file per candidate in `outputs/`

## Output Files

Each generated result file contains:

- Candidate name
- Pipeline status
- Extracted information
- Match analysis
- Final score and explanation

Example output files:

- `outputs/result_Priya_Sharma.txt`
- `outputs/result_Rahul_Gupta.txt`
- `outputs/result_Amit_Kumar.txt`

## LangSmith Tracing

If your LangSmith environment variables are set, LangChain will automatically
trace the model calls. After running the project, open your LangSmith account
and inspect the `ai-resume-screening` project to review the pipeline runs.

## Troubleshooting

### `OPENAI_API_KEY is missing in .env file`

Add `OPENAI_API_KEY` to `.env` and rerun the script.

### `LANGCHAIN_API_KEY is missing in .env file`

Add your LangSmith API key to `.env`.

### `File not found: data/...`

Run the program from the repository root:

```bash
python main.py
```

### `No module named 'dotenv'`

Activate your virtual environment and reinstall dependencies:

```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### `No module named 'langchain_core'` or related import errors

Your environment is likely missing dependencies or using incompatible versions.
Reinstall from `requirements.txt`.

### OpenAI authentication or quota errors

Check that your API key is valid and that your OpenAI account has access to the
selected model.

## Tech Stack

- Python
- LangChain
- LangChain OpenAI
- LangSmith
- OpenAI
- python-dotenv

## Current Limitations

- The project reads resumes from plain text files only
- The candidate list is currently hard-coded in `main.py`
- The pipeline runs sequentially rather than in parallel
- Groq support is not part of the current checked-in implementation

## Suggested Next Improvements

- Add PDF and DOCX resume parsing
- Support batch input from a folder or spreadsheet
- Export structured JSON alongside text reports
- Add tests for prompt formatting and pipeline behavior
- Make the candidate list configurable
