# 🧩 Environment Setup: Phase 3 (Lectures 19–33)

This guide prepares your Python environment for LangChain integration, model hosting, embeddings, evaluation pipelines, and capstone development — using only free and local tools.

---

## ✅ Step 1: Create a Dedicated Workspace Folder

```bash
mkdir genai-phase-3
cd genai-phase-3
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

## ✅ Step 2: Install Phase 3 Dependencies

Create a file named `requirements-phase-3.txt` with the following contents:

```
streamlit
langchain
huggingface_hub
sentence-transformers
scikit-learn
matplotlib
pandas
jupyterlab
gradio
rich
colorama
```

Install all packages:

```bash
pip install -r requirements-phase-3.txt
```

---

## ✅ Step 3: Test Your Setup

Create a file named `test-phase3-env.py`:

```python
import streamlit
import langchain
import huggingface_hub
import sentence_transformers
import sklearn
import matplotlib
import pandas
import gradio
from rich import print
from colorama import init, Fore

init(autoreset=True)

print("[bold green]✅ Phase 3 environment is ready for integration and capstone development![/bold green]")
print(Fore.CYAN + "Colorama is active — CLI UX enhancements are working.")
```

Run it:

```bash
python test-phase3-env.py
```

Expected output:

```
✅ Phase 3 environment is ready for integration and capstone development!
Colorama is active — CLI UX enhancements are working.
```

---

## ✅ Step 4: Launch Jupyter Lab

To use notebooks for evaluation and capstone workflows:

```bash
jupyter lab
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

- Your virtual environment supports LangChain, Hugging Face, and Streamlit integration  
- Embedding models and vector search tools are installed  
- Evaluation and visualization libraries are ready  
- `rich` and `colorama` enhance CLI feedback and UX  
- You’re equipped for capstone development, peer review, and final showcase — with no paid dependencies
