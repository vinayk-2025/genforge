---
title: ""Phase 1 - Environment Setup README""
description: "Overview and objectives for Phase 1 environment setup labs"
author: "Satya Prakash Nigam"
tags: [GenAI, Environment Setup, Installation, Checklist, Reproducibility]
layout: post
permalink: /labs/lab-1/phase-1-checklists/readme/
---

# 🛠️ Phase 1 - Environment Setup
📅 **Date**: 17-11-2025  
👨‍🏫 Curated by: Satya Prakash Nigam  

---

## 🎯 Objectives
Phase 1 ensures every student has a reproducible, working environment for GenAI labs.  
By completing this phase, students will:
- Install and validate **core tools** (Python, Node.js, Git, Ollama, LM Studio, Jupyter, XAMPP)  
- Configure GitHub identity and workspace hygiene  
- Establish reproducibility habits with `requirements.txt` and `README.md`  
- Prepare for Phase 2 online labs and Phase 3 validation scripts  

---

## 📂 Structure
This folder contains individual installation checklists and a master checklist:

- [00-master-installation-checklist.md](./00-master-installation-checklist.md) - consolidated view of all tasks  
- [python-installation-checklist.md](./python-installation-checklist.md)  
- [nodejs-installation-checklist.md](./nodejs-installation-checklist.md)  
- [notepad-git-installation-checklist.md](./notepad-git-installation-checklist.md)  
- [ollama-installation-checklist.md](./ollama-installation-checklist.md)  
- [lmstudio-installation-checklist.md](./lmstudio-installation-checklist.md)  
- [jupyter-installation-checklist.md](./jupyter-installation-checklist.md)  
- [xampp-installation-checklist.md](./xampp-installation-checklist.md)  

---

## 📑 Sequence
1. Install **Python 3.11** and verify with `python --version`  
2. Install **Node.js** and verify with `node --version`  
3. Configure **Git** identity and link to GitHub  
4. Install **Ollama** and run `ollama run tinyllama`  
5. Install **LM Studio** and test a local model  
6. Install **Jupyter Notebook** and launch `jupyter notebook`  
7. Install **XAMPP** and verify Apache/MySQL services  

---

## ✅ Expected Outcomes
- Each tool runs successfully from the command line  
- GitHub identity configured (`git config --global user.name`, `git config --global user.email`)  
- Ollama and LM Studio can run a lightweight model locally  
- Jupyter Notebook launches in browser  
- XAMPP services start without errors  

---

## 🛠️ Troubleshooting
- **PATH issues**: Ensure Python, Node.js, Git executables are added to system PATH  
- **Git identity missing**: Run `git config --global` commands with correct name/email  
- **Ollama model download fails**: Check internet connectivity and retry `ollama pull tinyllama`  
- **XAMPP MySQL not starting**: Ensure no conflicting services (e.g., MySQL from other installs)  

---

## 📜 License
This README is licensed under **CC BY-NC 4.0**  
You may share and adapt with attribution - but commercial use is prohibited  
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
