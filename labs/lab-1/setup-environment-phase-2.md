# 🧠 Environment Setup: Phase 2 (Lectures 11–18)

This guide prepares your Python environment for agentic workflows, mini-agent construction, and ethical deployment labs — using only free, local, and open-source tools.

---

## ✅ Step 1: Create a Dedicated Workspace Folder

```bash
mkdir genai-phase-2
cd genai-phase-2
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

You should see `(venv)` prefix in your terminal — this means the environment is active.

---

## ✅ Step 2: Install Phase 2 Dependencies

Create a file named `requirements-phase-2.txt` with the following contents:

```
python-dotenv
nltk
spacy
faker
scikit-learn
rich
```

Install all packages:

```bash
pip install -r requirements-phase-2.txt
```

---

## ✅ Step 3: Download NLP Models

For `nltk`:

```bash
python -m nltk.downloader punkt stopwords wordnet
```

For `spacy`:

```bash
python -m spacy download en_core_web_sm
```

---

## ✅ Step 4: Test Your Setup

Create a file named `test-agentic-env.py`:

```python
import nltk
import spacy
import faker
from dotenv import load_dotenv
from sklearn.feature_extraction.text import CountVectorizer
from rich import print

print("[bold green]✅ Phase 2 environment is ready for agentic workflows![/bold green]")
```

Run it:

```bash
python test-agentic-env.py
```

Expected output:

```
✅ Phase 2 environment is ready for agentic workflows!
```

---

## ✅ Step 5: Deactivate the Environment

When you're done working:

```bash
deactivate
```

This will return your terminal to the global Python context.

---

## 🧪 Outcome

- Your virtual environment now supports agentic AI labs  
- NLP tools (`nltk`, `spacy`) are installed and configured  
- Faker and dotenv are ready for test data and memory workflows  
- `scikit-learn` supports evaluation and vectorization  
- `rich` enables styled CLI output for agent feedback and logging  
- You’re equipped for mini-agent construction and ethical deployment labs — with no paid dependencies
