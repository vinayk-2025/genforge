# Education Agent - Workflow

## Steps
1. **Database Setup**
   - Run `create_db.sql` to create `genforge_education` DB with `faq` and `logs` tables.
   - Populate FAQ table using `generate_faq_csv.py` + `load_faq_csv.py`.
   - Populate Logs table using `generate_logs_csv.py` + `load_logs_csv.py`.

2. **Frontend (Streamlit)**
   - Run `streamlit run app.py`.
   - Student enters query → agent checks FAQ table.
   - Exact match → return answer.
   - No match → fuzzy match with `difflib`.
   - Still no match → fallback response.

3. **Logging**
   - Every query/response pair is inserted into `logs` table.

4. **Dashboard**
   - Run `streamlit run dashboard.py`.
   - View FAQ entries and logs with filters.

5. **Testing**
   - Use `test-cases.md` for validation.
