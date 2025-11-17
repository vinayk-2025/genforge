
---
title: "Jupyter Installation Checklist"
description: "Guide to install and launch Jupyter Notebook and Jupyter Lab for GenAI experimentation"
author: Satya Prakash Nigam
tags: [GenAI, Environment Setup, Jupyter, Notebook, Lab, Installation]
layout: post
permalink: /labs/lab-1/phase-1-checklists/jupyter-installation-checklist/
---

# 📓 Jupyter Installation Checklist
This guide helps you install and launch Jupyter Notebook and Jupyter Lab — essential tools for GenAI experimentation, evaluation pipelines, and capstone workflows.

---

## ✅ Step 1: Activate Your Virtual Environment

```bash
cd day-01
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # macOS/Linux
#nstall required packages (e.g. Jupyter, LangChain, Streamlit) 
pip install -r requirements.txt
```

---

## ✅ Step 2: Install Jupyter and Jupyter Lab

```bash
pip install jupyterlab notebook
```

---

## ✅ Step 3: Launch Jupyter Notebook

```bash
jupyter notebook
```

- Opens in your browser at `http://localhost:8888`
- Create `.ipynb` files for prompt chaining, evaluation, and logging

---

## ✅ Step 4: Launch Jupyter Lab (Recommended)

```bash
jupyter lab
```

- Opens in your browser at `http://localhost:8888/lab`
- Modern interface with file browser, terminals, and markdown support

---

## ✅ Step 5: Test Your Setup

Create a notebook and run:

```python
print("Jupyter is working!")
```

Expected output:

```
Jupyter is working!
```

---

## 🧪 Outcome
- Jupyter Notebook and Lab are installed  
- You can run GenAI experiments in browser‑based notebooks  
- Ready for evaluation pipelines and capstone workflows  

---

## License
This checklist is licensed under **CC BY-NC 4.0**  
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
 

---
 