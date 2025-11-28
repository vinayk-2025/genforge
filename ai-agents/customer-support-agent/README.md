
---
 
# 🤖 Customer Support Agent

A fully functional AI Agent built with **Streamlit + FastAPI + MySQL (PyMySQL)**.  
This agent provides intelligent customer support by retrieving FAQ answers, handling fuzzy queries, and logging interactions.

---

## 📌 Features
- **Streamlit frontend** for user queries
- **MySQL backend** (XAMPP, root/no password)
- **Hybrid retrieval**: exact SQL match + fuzzy matching (`difflib`)
- **Synthetic dataset generation** with Faker
- **Bulk CSV loaders** for FAQs and logs
- **Dashboard** to view FAQs and query logs
- **Test cases** for validation
- **Prompt templates** for modular responses

---

## 📂 Project Structure
```
customer-support-agent/
├── agent-spec.md
├── app.py
├── create_db.sql
├── dashboard.py
├── generate_faq_csv.py
├── generate_logs_csv.py
├── load_faq_csv.py
├── load_logs_csv.py
├── prompts/
│   ├── faq_response.txt
│   ├── fallback_response.txt
│   ├── escalation_response.txt
│   └── polite_prefix.txt
├── requirements.txt
├── test-cases.md
└── workflow.md
```

---

## 🚀 Setup Instructions
1. **Database**
   - Run `create_db.sql` in MySQL (XAMPP).
   - Generate FAQ dataset:
     ```bash
     python generate_faq_csv.py
     python load_faq_csv.py
     ```
   - Generate Logs dataset:
     ```bash
     python generate_logs_csv.py
     python load_logs_csv.py
     ```

2. **Run Agent**
   ```bash
   streamlit run app.py
   ```

3. **Run Dashboard**
   ```bash
   streamlit run dashboard.py
   ```

4. **Test**
   - Use queries from `test-cases.md`.

---

## 📝 Answer Prompt Templates

The agent uses modular text templates stored in the `prompts/` folder. These allow customization of tone and style without editing Python code.

- **`faq_response.txt`** → Template for successful FAQ retrieval.  
  Example:  
  ```
  📖 FAQ Answer: {answer}
  ```

- **`fallback_response.txt`** → Used when no FAQ or fuzzy match is found.  
  Example:  
  ```
  🤔 Sorry, I don't have an answer. Please contact support.
  ```

- **`escalation_response.txt`** → Optional escalation template for complex queries.  
  Example:  
  ```
  🚨 This query requires human support. Please escalate to the support team.
  ```

- **`polite_prefix.txt`** → Prepended to answers for a more customer‑friendly tone.  
  Example:  
  ```
  Thank you for reaching out! Here’s what I found:
  ```

---

## ✅ Notes
- No paid APIs (OpenAI, etc.) are used.
- All dependencies are free/open‑source.
- DB name: `genforge_customer_support` (avoids conflicts).
```

---

