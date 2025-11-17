 

# 🔥 GenForge - GenAI, Agentic AI & Prompt Engineering

Welcome to **GenForge**, the flagship repository of [AI Alchemy Hub](https://aialchemyhub.in).  
This course empowers learners to **forge reproducible GenAI workflows**, master **prompt engineering**, and design **agentic AI systems** with professional rigour.

Curated and delivered by **Satya Prakash Nigam**, Independent AI Consultant · Fractional CTO · Product Architect · Technical Enablement Strategist.


## 📁 Repository Structure

| Folder                  | Purpose                                                  |
|-------------------------|----------------------------------------------------------|
| `lectures/`             | Markdown lecture scripts (33 total)                      |
| `labs/`                 | Environment setup, online labs, validation scripts       |
| `quizzes/`              | Lecture‑specific MCQs and answer keys                    |
| `slide-decks/`          | Modular slide decks for classroom delivery               |
| `student-notes/`        | Student‑facing summaries (Markdown source)               |
| `pdf-quizzes/`          | Exported PDFs of all quizzes                             |
| `pdf-student-notes/`    | Exported PDFs of all student notes                       |
| `capstone-templates/`   | Project scaffolds, dashboards, and starter kits          |
| `assets/`               | Diagrams, visuals, and screenshots                       |
| `proposal/`             | Approved proposal documents and schedules                |
| `temp/`                 | Drafts and experimental scaffolds (excluded via `.gitignore`) |
| `utilities/`            | Helper scripts, environment validators, and automation   |

> ✅ `proposal/` and `temp/` are retained locally and excluded from GitHub sync

 
## 🛠️ Troubleshooting Environment Setup

Even with clear instructions, students may face common issues when creating a virtual environment or installing packages. Use this section to quickly resolve them.

### 1. Virtual Environment Issues
- **`venv` not found**  
  Ensure Python 3.10+ is installed. On Linux/macOS, install `python3-venv` if missing:  
  ```bash
  sudo apt install python3-venv
  ```
- **Activation script errors (Windows)**  
  If PowerShell blocks activation with *"execution of scripts is disabled"*, run:  
  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  ```
  Then retry activation.

### 2. Pip & Package Installation
- **`pip` not recognized**  
  Use `python -m pip install --upgrade pip` to ensure pip is available.  
- **SSL or certificate errors (macOS/Linux)**  
  Update certificates or run:  
  ```bash
  python -m pip install --upgrade certifi
  ```
- **Permission denied (Linux/macOS)**  
  Always install inside venv. If outside, use `--user` flag:  
  ```bash
  pip install --user <package>
  ```

### 3. Dependency Conflicts
- **Version mismatch**  
  If TensorFlow or PyTorch fails, check Python version (must be 3.10+).  
- **Reinstall cleanly**  
  Delete `venv/` folder and recreate:  
  ```bash
  rm -rf venv
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

### 4. Streamlit / Uvicorn Errors
- **`WinError 10061` (Connection refused)**  
  Backend (FastAPI/Flask) not running. Start backend before frontend.  
- **`Could not import module` with uvicorn**  
  Remove `.py` extension when running:  
  ```bash
  uvicorn test_langchain_fastapi:app --reload
  ```

### 5. Ollama Issues
- **`FileNotFoundError: ollama not found`**  
  Ollama not installed or not in PATH. Install from [ollama.com/download](https://ollama.com/download).  
- **Timeouts**  
  Ensure `ollama serve` is running before sending prompts.  
- **Model missing**  
  Run `ollama pull tinyllama` before testing.


## 🧠 Highlights of GenForge

- **Zero-cost infrastructure**: All tools are free and open‑source  
- **Local-first experimentation**: Ollama‑powered LLMs on student laptops  
- **Modular design**: Reusable templates, labs, and dashboards  
- **Student-first delivery**: Beginner‑friendly, reproducible, no LMS lock‑in  
- **Professional tooling**: GitHub workflows, Markdown documentation, reproducible environments  
- **Validation discipline**: Phase-3 labs ensure all dependencies and frameworks are tested before capstones  
- **Cross-platform onboarding**: Explicit instructions for Windows, Linux, and macOS  


Curated by **Satya Prakash Nigam**  
Independent AI Consultant · Fractional CTO · Product Architect · Technical Enablement Strategist  

🌐 Personal: [spnigam.in](https://spnigam.in)  
🧪 Platform: [aialchemyhub.in](https://www.aialchemyhub.in)  
📺 YouTube: [AI Alchemy Hub](https://www.youtube.com/@AIAlchemyHub-zx6lz)  
💬 Community (Coming Soon): [community.aialchemyhub.in](https://community.aialchemyhub.in)  
💬 Zulip: [aialchemyhub.zulipchat.com](https://aialchemyhub.zulipchat.com)  
📧 Email: spnigam25@yahoo.com  
🔗 LinkedIn: [linkedin.com/in/spn25](https://www.linkedin.com/in/spn25)  
💻 GitHub: [github.com/satya25](https://github.com/satya25)  
🤖 Hugging Face: [huggingface.co/satya25](https://huggingface.co/satya25)  

_Last updated: November 2025_
```

