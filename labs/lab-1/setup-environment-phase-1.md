# 🐍 Environment Setup: Phase 1 (Lectures 1–10)

This guide walks you through setting up your Python environment for the first phase of the GenAI course. You’ll install required packages, configure a virtual environment, and verify your setup with a test script.

---

## ✅ Step 1: Install Python 3.11.x

- Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)
- During installation:
  - ✅ Check **"Add Python to PATH"**
  - ✅ Enable `pip` in optional features

Verify installation:

```bash
python --version
pip --version
```

Expected output:

```
Python 3.11.x  
pip 23.x.x or higher
```

---

## ✅ Step 2: Create a Virtual Environment

Navigate to your project folder:

```bash
mkdir genai-phase-1
cd genai-phase-1
python -m venv venv
```

Activate the environment:

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

## ✅ Step 3: Install Required Packages

Create a file named `requirements-phase-1.txt` with the following contents:

```
streamlit
requests
langchain
huggingface_hub
sentence-transformers
tiktoken
ollama
openai  # used for dummy key simulation only
notebook
pandas
numpy
rich
colorama
```

Install all dependencies:

```bash
pip install -r requirements-phase-1.txt
```

---

## ✅ Step 4: Test Your Setup

Create a file named `test-env.py`:

```python
import streamlit as st
import langchain
import requests
import huggingface_hub
from rich import print
from colorama import init, Fore

init(autoreset=True)

print("[bold green]✅ Phase 1 environment is ready![/bold green]")
print(Fore.CYAN + "Colorama is active — CLI UX enhancements are working.")
```

Run it:

```bash
python test-env.py
```

Expected output:

```
✅ Phase 1 environment is ready!
Colorama is active — CLI UX enhancements are working.
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

- Python 3.11.x is installed and verified  
- Virtual environment is active and isolated  
- Phase 1 packages are installed and tested  
- `rich` and `colorama` enhance CLI feedback and UX from day one  
- You’re ready for CLI labs, prompt workflows, and Streamlit deployment
