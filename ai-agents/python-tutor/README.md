
# 🐍 Python Tutor Agent

## Overview
Python Tutor is a lightweight AI agent designed to help students and developers learn Python concepts, generate code snippets, and practice through quizzes.  
It runs locally using [Ollama](https://ollama.ai/) with the **tinyllama** model (637 MB), ensuring fast responses without heavy resource usage.

## Features
- 📘 **Concept Explanations**: Ask any Python question and get clear, step-by-step answers.
- 💻 **Code Generation**: Request Python code snippets for algorithms, data structures, or tasks.
- 🎯 **Quiz Mode**: Generate multiple-choice questions (MCQs) on specific Python topics for practice.
- 📊 **Dashboard**: View logs of queries and responses, filter by type (Explanation / Code / Quiz).

## Project Structure
```
python-tutor/
│
├── app.py                  # Streamlit frontend
├── tutor-spec.md            # Specification of the Python Tutor agent
├── workflow.md              # Step-by-step workflow
├── README.md                # Overview and setup instructions
├── requirements.txt         # Dependencies
├── test-cases.md            # Sample queries for validation
└── prompts/
    ├── code_generation.txt
    ├── quiz_generation.txt
    └── explanation.txt
```

## Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure Ollama is installed and running locally:
   ```bash
   ollama list
   ```
   Confirm that `tinyllama:latest` is available.
3. Start the tutor:
   ```bash
   streamlit run app.py
   ```

## Example Queries
- **Explanation**: "Explain recursion in Python."
- **Code Generation**: "Write Python code for bubble sort."
- **Quiz**: "Generate 5 MCQs on Python lists."

---

## Next Steps
- Populate `app.py` with Streamlit + Ollama integration.
- Define prompt templates in `prompts/`.
- Add test cases in `test-cases.md` for validation.
```
