 
---
title: "Ollama Installation Checklist"
description: "Guide to install Ollama, pull local LLMs, and verify prompt execution offline"
author: Satya Prakash Nigam
tags: [GenAI, Environment Setup, Ollama, Local LLM, Installation]
layout: post
permalink: /labs/lab-1/phase-1-checklists/ollama-installation-checklist/
---

# 🧠 Ollama Installation Checklist
This guide walks you through installing Ollama, pulling local LLMs, and verifying prompt execution — all offline and free.

---

## ✅ Step 1: Install Ollama
- Visit [https://ollama.com/download](https://ollama.com/download)  
- Download and install for your OS (Windows, macOS, Linux)  
- Restart your terminal after installation  

Verify installation:

```bash
ollama --version
```

Expected output: Ollama CLI version number  

---

## ✅ Step 2: Pull a Local Model
Example: Pull TinyLLaMA (lightweight model for testing):

```bash
ollama pull tinyllama
```

Other available models:

```bash
ollama list
```

---

## ✅ Step 3: Run a Test Prompt
```bash
ollama run tinyllama
```

Type your prompt:

```
What is the capital of India?
```

Expected output:  

```
The capital of India is New Delhi.
```

---

## ✅ Step 4: Use Ollama via Python (Optional)
Install Python bindings:

```bash
pip install ollama
```

Sample script:

```python
import ollama
response = ollama.chat(model='tinyllama', messages=[{'role': 'user', 'content': 'Tell me a joke'}])
print(response['message']['content'])
```

---

## 🧪 Outcome
- Ollama is installed and working  
- Local models are pulled and ready  
- Prompts can be executed offline  
- Python integration is optional for chaining and logging  

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
 

