import streamlit as st
import requests
import re
import os
import pandas as pd
import json

# --- Ensure logs directory exists ---
os.makedirs("logs", exist_ok=True)

# --- Ollama query function (robust streaming parser) ---
def query_ollama(prompt, model="tinyllama:latest"):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt},
            stream=True
        )
        output = ""
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    if "response" in data:
                        output += data["response"]
                except json.JSONDecodeError:
                    continue
        return output.strip()
    except Exception as e:
        return f"⚠️ Error contacting Ollama: {e}"

# --- Intent detection ---
def detect_intent(user_query):
    if "def " in user_query or "class " in user_query or "import " in user_query or re.search(r":\n", user_query):
        return "debug"
    if "quiz" in user_query.lower() or "mcq" in user_query.lower():
        return "quiz"
    if "code" in user_query.lower() or "program" in user_query.lower() or "script" in user_query.lower():
        return "code"
    return "explain"

# --- Streamlit UI ---
st.set_page_config(page_title="Python Tutor", layout="wide")

st.markdown(
    "<h2 style='color:#2E86C1; text-align:center;'>🐍 Python Tutor Agent</h2>",
    unsafe_allow_html=True
)

tab1, tab2 = st.tabs(["Tutor", "Dashboard"])

# --- Tutor Tab ---
with tab1:
    st.write("Ask me a Python question, request code, generate a quiz, or paste code to debug!")

    user_query = st.text_area("Enter your query or code snippet:", height=150)
    model_choice = st.selectbox("Choose model:", ["tinyllama:latest", "phi3:mini", "mistral:7b"])

    if st.button("Submit") and user_query.strip():
        intent = detect_intent(user_query)

        # Simplified prompts
        if intent == "explain":
            prompt = f"Explain clearly with examples: {user_query}"
        elif intent == "code":
            prompt = f"Write clean Python code with comments for: {user_query}"
        elif intent == "quiz":
            prompt = f"Generate 5 beginner-friendly MCQs on: {user_query}"
        elif intent == "debug":
            prompt = f"Debug this Python code and explain fixes:\n{user_query}"
        else:
            prompt = user_query

        st.info(f"🔎 Detected intent: **{intent.capitalize()}** | Model: {model_choice}")

        response = query_ollama(prompt, model=model_choice)
        if response:
            st.success(response)
        else:
            st.warning("⚠️ No response generated. Try rephrasing your query or switch to a stronger model.")

        # Log interaction
        with open("logs/python_tutor_logs.csv", "a", encoding="utf-8") as f:
            f.write(f"{intent},{user_query.replace(',', ' ')},{response.replace(',', ' ')}\n")

# --- Dashboard Tab ---
with tab2:
    st.subheader("📊 Tutor Logs")

    try:
        df = pd.read_csv("logs/python_tutor_logs.csv", names=["Intent", "Query", "Response"])
        st.dataframe(df)
        filter_intent = st.selectbox("Filter by intent:", ["All", "Explain", "Code", "Quiz", "Debug"])
        if filter_intent != "All":
            st.dataframe(df[df["Intent"].str.lower() == filter_intent.lower()])
    except FileNotFoundError:
        st.warning("No logs found yet. Interact with the Tutor to generate logs.")
