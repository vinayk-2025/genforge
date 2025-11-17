 
---
title: "Phase 3 Validation Labs Overview"
description: "Validation scripts and environment setup guide for Phase 3 labs in the GenAI Agentic Course"
date: 2025-11-17
author: Satya Prakash Nigam
tags: [GenAI, Validation Labs, Phase 3, Environment Setup, Agentic AI]
layout: post
permalink: /labs/lab-1/phase-3-validation/
---

# Phase-3 Validation Labs — GenAI Agentic Course

This folder contains validation scripts to ensure your environment is correctly set up for the **GenAI Agentic Course**. Each script demonstrates a framework, library, or tool integration. Follow the instructions carefully — no assumptions are made.

---

## 📂 Contents

- `check_mysql_connection.php` — Validate PHP + MySQL connectivity  
- `test-prompt.txt` — Sample prompt file for CLI/LLM testing  
- `test_gemini_cli.sh` — Run Gemini CLI directly from shell  
- `test_gemini_fastapi.py` — Expose Gemini CLI via FastAPI  
- `test_gemini_flask.py` — Expose Gemini CLI via Flask  
- `test_gemini_streamlit.py` — Expose Gemini CLI via Streamlit  
- `test_git_config.sh` — Validate Git installation and configuration  
- `test_langchain_fastapi.py` — LangChain + Ollama via FastAPI  
- `test_langchain_prompt.py` — LangChain prompt template demo  
- `test_langchain_streamlit.py` — LangChain + FastAPI via Streamlit frontend  
- `test_node_hello_world.js` — Node.js Hello World validation  
- `test_ollama.py` — Run Ollama model (tinyllama) via Python subprocess  
- `test_ollama_fastapi.py` — Expose Ollama via FastAPI  
- `test_requirements.py` — Validate mandatory Python packages  
- `test_streamlit.py` — Minimal Streamlit dashboard validation  

---

## 🛠️ Prerequisites

1. **Python 3.10+**  
   - Verify: `python --version`

2. **Virtual Environment (recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows PowerShell
   ```

3. **Install mandatory packages**  
   Run the validator:
   ```bash
   python test_requirements.py
   ```
   Install missing packages as instructed (`pip install <package>`).

4. **Node.js v18+**  
   - Verify: `node -v` and `npm -v`

5. **Git**  
   - Verify: `git --version`

6. **Ollama (local LLM runner)**  
   - Install: [https://ollama.com/download](https://ollama.com/download)  
   - Verify: `ollama --version`  
   - Pull model: `ollama pull tinyllama`  
   - Start service: `ollama serve`

---

## 🚀 Usage Instructions

(Examples for each script: Gemini CLI, FastAPI, Flask, Streamlit, Git config, LangChain, Node.js, Ollama, Requirements validator, Streamlit Hello World — see detailed commands above.)

---

## ⚠️ Notes

- **Gemini Developer API (`google-genai`) requires paid subscription.**  
  Excluded from this course. We use **Ollama** and other open‑source backends instead.  
- **AutoGen** also requires paid OpenAI/Azure APIs. Dropped from labs.  
- Always start **FastAPI backend first**, then **Streamlit frontend**.  
- If you see `WinError 10061` → backend not running.  
- If you see `Could not import module` → remove `.py` from uvicorn command.  

---

## ✅ Validation Checklist

- [ ] Python 3.10+ installed  
- [ ] Virtual environment activated  
- [ ] All mandatory packages installed (`test_requirements.py`)  
- [ ] Node.js + npm installed  
- [ ] Git installed and configured  
- [ ] Ollama installed, model pulled, service running  
- [ ] FastAPI/Flask/Streamlit scripts tested successfully  

---

🎓 With this README, students have **one authoritative guide** to validate their environment before moving into advanced Agentic AI labs.

---

## License
This guide is licensed under **CC BY-NC 4.0**  
You may share and adapt with attribution — but commercial use is prohibited  
🔗 [License Details](https://creativecommons.org/licenses/by-nc/4.0)

---

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
 
 