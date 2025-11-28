import streamlit as st
import pymysql
import pandas as pd

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="genforge_customer_support"
    )

def fetch_faq():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM faq ORDER BY id ASC", conn)
    conn.close()
    return df

def fetch_logs():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM logs ORDER BY timestamp DESC", conn)
    conn.close()
    return df

st.set_page_config(page_title="Customer Support Dashboard", layout="wide")
st.title("📊 Customer Support Agent Dashboard")

tab1, tab2 = st.tabs(["FAQ Table", "Logs Table"])

with tab1:
    st.subheader("FAQ Entries")
    faq_df = fetch_faq()
    st.dataframe(faq_df)

    keyword = st.text_input("Filter FAQs by keyword:")
    if keyword:
        filtered = faq_df[faq_df['question'].str.contains(keyword, case=False)]
        st.dataframe(filtered)

with tab2:
    st.subheader("Logs History")
    logs_df = fetch_logs()
    st.dataframe(logs_df)

    keyword = st.text_input("Filter Logs by keyword:")
    if keyword:
        filtered = logs_df[logs_df['query'].str.contains(keyword, case=False)]
        st.dataframe(filtered)
