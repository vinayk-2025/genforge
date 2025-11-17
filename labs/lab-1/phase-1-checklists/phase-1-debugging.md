 
---
title: "Phase 1 — Debugging Installation Issues"
description: "Troubleshooting guide for common environment setup problems in Phase 1"
author: Satya Prakash Nigam
tags: [GenAI, Environment Setup, Debugging, Troubleshooting, PATH, Installation]
layout: post
permalink: /labs/lab-1/phase-1-checklists/debugging/
---

# 🐞 Phase 1 — Debugging Installation Issues
📅 **Date**: 17-11-2025  
👨‍🏫 Curated by: Satya Prakash Nigam  

This guide helps students resolve common installation and configuration errors encountered during Phase 1 environment setup.

---

## ⚙️ PATH Not Set
**Symptom:** Running `python`, `node`, or `git` shows *command not found*.  
**Fix:**  
- Add executable paths to system environment variables.  
- Example (Windows):  
  - Open *System Properties → Environment Variables*.  
  - Add `C:\Python311\` to PATH.  
  - Add `C:\Program Files\nodejs\` to PATH.  
- Restart terminal and re-run version commands.

---

## 👤 Git Identity Missing
**Symptom:** Commits show “unknown author” or push fails.  
**Fix:**  
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```
Verify with `git config --list`.

---

## 📦 Pip / npm Package Errors
**Symptom:** `pip install` or `npm install` fails.  
**Fix:**  
- Upgrade package managers:  
  - `python -m pip install --upgrade pip`  
  - `npm install -g npm@latest`  
- Check internet connectivity and proxy settings.  
- Use `--user` flag if permission denied.

---

## 🤖 Ollama Model Download Fails
**Symptom:** `ollama run tinyllama` errors out.  
**Fix:**  
- Run `ollama pull tinyllama` explicitly.  
- Check firewall/proxy settings.  
- Ensure disk space is available.  

---

## 🗄️ XAMPP MySQL Not Starting
**Symptom:** MySQL service fails to start.  
**Fix:**  
- Stop conflicting MySQL services from other installs.  
- Change port in `my.ini` (e.g., from 3306 to 3307).  
- Restart XAMPP Control Panel.

---

## 🧪 Jupyter Notebook Issues
**Symptom:** `jupyter notebook` fails to launch.  
**Fix:**  
- Ensure `pip install notebook` is run.  
- Add `%USERPROFILE%\AppData\Roaming\Python\Scripts` to PATH (Windows).  
- Try `jupyter lab` as alternative.

---

## 📜 Notes
- Document every fix in your personal notes for reproducibility.  
- Share unresolved issues with faculty or community portal for support.  
- Push updated environment notes to GitHub for peer reference.

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
 
 