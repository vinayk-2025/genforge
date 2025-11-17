
---
title: "Node.js Installation Checklist (for Gemini CLI)"
description: "Guide to install Node.js, verify setup, and prepare environment for Gemini CLI usage"
author: Satya Prakash Nigam
tags: [GenAI, Environment Setup, Node.js, npm, Gemini CLI, Installation]
layout: post
permalink: /labs/lab-1/phase-1-checklists/nodejs-installation-checklist/
---

# 🛠️ Node.js Installation Checklist (for Gemini CLI)
This guide walks you through installing Node.js, verifying the setup, and preparing your environment for Gemini CLI usage.

---

## ✅ Step 1: Download & Install Node.js
1. Visit [https://nodejs.org](https://nodejs.org)  
2. Download the **LTS version** for your operating system (recommended for stability)  
3. Run the installer and follow default prompts  
4. Restart your terminal or command prompt  

---

## ✅ Step 2: Verify Installation
Open your terminal and run:

```bash
node -v
npm -v
```

Expected output:

```
node: v18.x.x or higher
npm: 9.x.x or higher
```

---

## ✅ Step 3: Install Gemini CLI
Gemini CLI requires Node.js for its runtime. To install:

```bash
npm install -g @google/gemini-cli
```

Verify installation:

```bash
gemini --help
```

Expected output: Gemini CLI usage instructions  

---

## ✅ Step 4: Create a Test Prompt
Create a file named `test-prompt.txt` with the following content:

```
You are a helpful assistant. What is the capital of Karnataka?
```

Run the prompt:

```bash
gemini test-prompt.txt
```

Expected output:  

```
The capital of Karnataka is Bengaluru.
```

---

## 🧪 Outcome
- Node.js and npm are installed and working  
- Gemini CLI is installed globally  
- You have successfully run a test prompt using Gemini CLI  
- Your environment is ready for CLI‑based GenAI workflows  

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
 

