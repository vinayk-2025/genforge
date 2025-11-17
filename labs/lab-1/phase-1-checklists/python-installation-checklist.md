
---
title: "Python Installation Checklist (Python 3.11.x + Requirements)"
description: "Guide to install Python 3.11.x, set up a virtual environment, install packages, and verify GenAI development setup"
author: Satya Prakash Nigam
tags: [GenAI, Environment Setup, Python, Virtual Environment, Installation, Requirements]
layout: post
permalink: /labs/lab-1/phase-1-checklists/python-installation-checklist/
---

# 🐍 Python Installation Checklist (Python 3.11.x + Requirements)
This guide walks you through installing Python 3.11.x, setting up a virtual environment, installing required packages, and verifying your GenAI development setup.

---

## ✅ Step 1: Download & Install Python 3.11.x
1. Visit [https://www.python.org/downloads/](https://www.python.org/downloads/)  
2. Download the latest **Python 3.11.x** installer for your OS  
3. During installation:  
   - ✅ Check **"Add Python to PATH"**  
   - ✅ Choose **"Customise installation"** and enable `pip`  
4. Complete the installation  

---

## ✅ Step 2: Verify Installation
Open your terminal or command prompt and run:

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

## ✅ Step 3: Create a Virtual Environment
Navigate to your project folder and run:

```bash
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

---

## ✅ Step 4: Install Dependencies
Ensure your `requirements.txt` file includes:

```
streamlit
langchain
requests
huggingface_hub
```

Then install all packages:

```bash
pip install -r requirements.txt
```

---

## ✅ Step 5: Test Your Setup
Create a file named `test-genai.py`:

```python
import requests
print("Python environment is ready for GenAI development!")
```

Run it:

```bash
python test-genai.py
```

Expected output:

```
Python environment is ready for GenAI development!
```

---

## 🧪 Outcome
- Python 3.11.x is installed and working  
- Virtual environment is active  
- Required packages are installed  
- Your GenAI Python environment is ready for CLI, scripting, and Streamlit workflows  

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
 

