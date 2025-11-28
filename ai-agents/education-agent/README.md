# 🎓 Education Agent

An AI Agent built with **Streamlit + MySQL (PyMySQL)** to provide intelligent support for student queries.  
It retrieves FAQ answers, handles fuzzy queries, and logs interactions.

---

## 📌 Features
- Streamlit frontend for student queries
- MySQL backend (XAMPP, root/no password)
- Hybrid retrieval: exact SQL match + fuzzy matching (`difflib`)
- Synthetic dataset generation with Faker
- Bulk CSV loaders for FAQs and logs
- Dashboard to view FAQs and query logs
- Prompt templates for modular responses
- Test cases for validation

---

## 🚀 Setup Instructions
1. **Database**
   - Run `create_db.sql` in MySQL.
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
