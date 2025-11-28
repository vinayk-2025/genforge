# Customer Support Agent - Workflow

## Overview
This agent provides automated customer support using a local MySQL backend.  
It retrieves FAQ answers, handles fuzzy queries, and logs all interactions.

---

## Steps

1. **User Interaction**
   - User enters query in the Streamlit UI.

2. **Backend Processing**
   - Query is sent to backend.
   - Step 1: Check FAQ table in MySQL for **exact keyword match**.
   - Step 2: If no exact match → perform **fuzzy matching** using `difflib` with confidence threshold.
   - Step 3: If fuzzy match found → return stored answer.
   - Step 4: If no match at all → return **polite fallback** (from prompt templates).

3. **Response Display**
   - Response is displayed in Streamlit.
   - Uses modular **prompt templates** (`faq_response.txt`, `fallback_response.txt`, `polite_prefix.txt`) for consistent tone.

4. **Logging**
   - Query + final rendered response are logged into MySQL `logs` table.

5. **Dashboard**
   - Faculty/students can view FAQs and logs via `dashboard.py`.
   - Includes keyword filters for monitoring.

6. **Testing**
   - Validation queries are documented in `test-cases.md`.
