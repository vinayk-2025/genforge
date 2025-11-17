 

# Phase-3 Validation Labs - GenAI Agentic Course

This folder contains validation scripts to ensure your environment is correctly set up for the **GenAI Agentic Course**. Each script demonstrates a framework, library, or tool integration. Follow the instructions carefully - no assumptions are made.


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


## ⚠️ Notes

- **Gemini Developer API (`google-genai`) requires paid subscription.**  
  Excluded from this course. We use **Ollama** and other open‑source backends instead.  
- **AutoGen** also requires paid OpenAI/Azure APIs. Dropped from labs.  
- Always start **FastAPI backend first**, then **Streamlit frontend**.  
- If you see `WinError 10061` → backend not running.  
- If you see `Could not import module` → remove `.py` from uvicorn command.  


🎓 With this README, students have **one authoritative guide** to validate their environment before moving into advanced Agentic AI labs.


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
 
 