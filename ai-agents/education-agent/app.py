import streamlit as st
import pymysql
import pandas as pd
from difflib import SequenceMatcher
from sqlalchemy import create_engine

# --- Utility to load prompt text files ---
def load_prompt(filename):
    try:
        with open(f"prompts/{filename}", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

# Load prompt templates
faq_template = load_prompt("faq_response.txt")
fallback_template = load_prompt("fallback_response.txt")
escalation_template = load_prompt("escalation_response.txt")
polite_prefix = load_prompt("polite_prefix.txt")

# --- SQLAlchemy engine for pandas reads ---
def get_engine():
    return create_engine("mysql+pymysql://root:@localhost/genforge_education")

# --- PyMySQL connection for inserts ---
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="genforge_education"
    )

# --- Exact match search in DB ---
def fetch_exact_answer(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM faq WHERE LOWER(question) LIKE %s", ("%" + query.lower() + "%",))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# --- Fetch all FAQs for fuzzy matching ---
def fetch_all_questions():
    engine = get_engine()
    df = pd.read_sql("SELECT question, answer FROM faq", engine)
    return list(df.itertuples(index=False, name=None))

# --- Fuzzy match with academic keyword guard ---
def find_best_match(user_query, faqs):
    academic_keywords = [
        "exam", "grading", "attendance", "library", "registration", "register",
        "internship", "scholarship", "labs", "projects", "faculty"
    ]

    best_score = 0
    best_answer = None
    best_question = None

    for q, a in faqs:
        score = SequenceMatcher(None, user_query.lower(), q.lower()).ratio()
        if score > best_score:
            best_score = score
            best_answer = a
            best_question = q

    # Only accept if similarity is high enough AND the matched FAQ contains academic keywords
    if best_score >= 0.6 and any(kw in best_question.lower() for kw in academic_keywords):
        return best_answer
    else:
        return None

# --- Log interaction ---
def log_interaction(query, response):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (query, response) VALUES (%s, %s)", (query, response))
    conn.commit()
    conn.close()

# --- Fetch logs for dashboard ---
def fetch_logs():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM logs ORDER BY timestamp DESC", engine)
    return df

# --- Fetch FAQ for dashboard ---
def fetch_faq():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM faq ORDER BY id ASC", engine)
    return df

# --- Streamlit UI ---
st.set_page_config(page_title="Education Agent", layout="wide")

# Custom styled title
st.markdown(
    "<h2 style='color:#117A65; text-align:center;'>🎓 Education Agent (Hybrid Intelligent)</h2>",
    unsafe_allow_html=True
)

# Tabs: Agent and Dashboard
tab1, tab2 = st.tabs(["Agent", "Dashboard"])

with tab1:
    st.write("Ask me an academic question and I'll try to help!")
    user_query = st.text_input("Enter your query:")

    if user_query:
        # Step 1: Exact DB match
        answer = fetch_exact_answer(user_query)

        # Step 2: Fuzzy match if no exact answer
        if not answer:
            faqs = fetch_all_questions()
            answer = find_best_match(user_query, faqs)

        # Step 3: Display + log
        if answer:
            response_text = f"{polite_prefix}\n\n{answer}"
            st.success(response_text)
            log_interaction(user_query, response_text)
        else:
            st.info(fallback_template)
            log_interaction(user_query, fallback_template)

with tab2:
    st.subheader("📊 Dashboard")

    faq_df = fetch_faq()
    logs_df = fetch_logs()

    # Classify responses
    logs_df["Status"] = logs_df["response"].apply(
        lambda r: "Fallback" if r.strip() == fallback_template.strip() else "Matched"
    )

    # Summary panel
    total_queries = len(logs_df)
    matched = (logs_df["Status"] == "Matched").sum()
    fallback = (logs_df["Status"] == "Fallback").sum()

    st.markdown(f"**Total Queries:** {total_queries} | **Matched:** {matched} | **Fallback:** {fallback}")

    subtab1, subtab2 = st.tabs(["FAQ Table", "Logs Table"])

    with subtab1:
        st.dataframe(faq_df)
        keyword = st.text_input("Filter FAQs by keyword:")
        if keyword:
            filtered = faq_df[faq_df['question'].str.contains(keyword, case=False)]
            st.dataframe(filtered)

    with subtab2:
        st.dataframe(logs_df)
        keyword = st.text_input("Filter Logs by keyword:")
        if keyword:
            filtered = logs_df[logs_df['query'].str.contains(keyword, case=False)]
            st.dataframe(filtered)

        status_filter = st.selectbox("Filter by Status:", ["All", "Matched", "Fallback"])
        if status_filter != "All":
            filtered = logs_df[logs_df["Status"] == status_filter]
            st.dataframe(filtered)
