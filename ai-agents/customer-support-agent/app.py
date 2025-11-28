import streamlit as st
import pymysql
from difflib import get_close_matches
from difflib import SequenceMatcher

# --- Fuzzy match with confidence check ---
def find_best_match(user_query, faqs):
    best_score = 0
    best_answer = None
    for q, a in faqs:
        score = SequenceMatcher(None, user_query.lower(), q.lower()).ratio()
        if score > best_score:
            best_score = score
            best_answer = a
    # Only accept if similarity is reasonably high
    return best_answer if best_score >= 0.6 else None


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

# --- MySQL connection ---
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="genforge_customer_support"
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
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM faq")
    results = cursor.fetchall()
    conn.close()
    return results

# --- Fuzzy match with confidence check ---
def find_best_match(user_query, faqs):
    best_score = 0
    best_answer = None
    for q, a in faqs:
        score = SequenceMatcher(None, user_query.lower(), q.lower()).ratio()
        if score > best_score:
            best_score = score
            best_answer = a
    # Only accept if similarity is reasonably high
    return best_answer if best_score >= 0.6 else None


# --- Log interaction ---
def log_interaction(query, response):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (query, response) VALUES (%s, %s)", (query, response))
    conn.commit()
    conn.close()

# --- Streamlit UI ---
st.set_page_config(page_title="Customer Support Agent", layout="centered")

# Custom styled title (50% smaller, colored)
st.markdown(
    "<h3 style='color:#2E86C1; text-align:center;'>🤖 Customer Support Agent (Hybrid Intelligent)</h3>",
    unsafe_allow_html=True
)

st.markdown(
    "<HR>",
    unsafe_allow_html=True
)
st.write("Ask me a question and I'll try to help!")

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
        # Cleaned response: prefix + answer only
        response_text = f"{polite_prefix}\n\n{answer}"
        st.success(response_text)
        log_interaction(user_query, response_text)
    else:
        st.info(fallback_template)
        log_interaction(user_query, fallback_template)
