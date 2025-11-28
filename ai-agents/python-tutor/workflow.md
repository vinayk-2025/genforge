
---
 
 
# 🐍 Python Tutor Agent Workflow

## 1. Setup Environment
- Ensure Python 3.9+ is installed.
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Verify Ollama is installed and running locally:
  ```bash
  ollama list
  ```
  Confirm that `tinyllama:latest` is available.

---

## 2. Project Structure
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

---

## 3. Running the Tutor
Start the Streamlit app:
```bash
streamlit run app.py
```

Open the browser at `http://localhost:8501`.

---

## 4. Using the Agent
### Agent Tab
- **Concept Explanations**: Enter queries like *"Explain recursion in Python"*.
- **Code Generation**: Enter queries like *"Write Python code for bubble sort"*.
- **Quiz Creation**: Enter queries like *"Generate 5 MCQs on Python lists"*.

The agent will:
1. Detect intent (Explanation / Code / Quiz).
2. Load the appropriate prompt template.
3. Query Ollama (`tinyllama:latest`).
4. Display the response.

### Dashboard Tab
- View logs of queries and responses.
- Filter by type (Explanation / Code / Quiz).
- Monitor usage statistics.

---

## 5. Logging
- Each query and response is logged automatically.
- Logs can be exported later for analysis (CSV option to be added).

---

## 6. Validation
Use `test-cases.md` to validate:
- Correct handling of typos (e.g., *"recusrion"* → *recursion*).
- Runnable Python code snippets.
- MCQs with correct answers and plausible distractors.

---

## 7. Maintenance
- Update prompt templates in `/prompts/` for improved clarity.
- Switch Ollama model if needed (e.g., `phi3:mini` for richer responses).
- Keep dependencies updated via `requirements.txt`.
 