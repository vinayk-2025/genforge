"""
test_langchain_streamlit.py

Purpose:
    Provide a Streamlit web UI that connects to the LangChain FastAPI service.
    Students can type a question in the browser and see the response from a local LLM.

Prerequisites:
    1. Install Python 3.10+ and required packages:
         pip install streamlit requests
    2. Install Ollama (local LLM runner):
         - Windows: https://ollama.com/download
         - macOS: brew install ollama
         - Linux: follow instructions at https://ollama.com/download
    3. Verify Ollama installation:
         ollama --version
    4. Pull the required model (tinyllama in this example):
         ollama pull tinyllama
    5. Ensure Ollama service is running:
         ollama serve
    6. Ensure LangChain FastAPI service is running (see test_langchain_fastapi.py):
         uvicorn test_langchain_fastapi:app --reload

Usage:
    Step 1: Start the FastAPI backend
        uvicorn test_langchain_fastapi:app --reload

    Step 2: Verify FastAPI health check
        curl http://127.0.0.1:8000/
        Expected output:
            {"message":"✅ LangChain FastAPI is running. Use /ask endpoint to send a question."}

    Step 3: Start the Streamlit frontend
        streamlit run test_langchain_streamlit.py

    Step 4: Open the browser (default: http://localhost:8501).
        You will see:
            - A text area to enter your question
            - An "Ask" button
            - The model’s response displayed below

    Example question:
        Tell me how to prepare French Onion soup.

    Expected output:
        Response:
        (Model’s generated answer)

Notes:
    - This script connects to the FastAPI backend at http://127.0.0.1:8000/ask.
    - Students must ensure the FastAPI service is running before using Streamlit.
    - Streamlit provides a student-friendly UI, no need for curl/Postman.
"""

import streamlit as st
import requests

# Configure Streamlit page
st.set_page_config(page_title="LangChain Assistant", page_icon="🧠", layout="centered")

# Page title and description
st.title("🧠 LangChain Assistant")
st.markdown("Ask a question and get a response from your local LLM via FastAPI.")

# Input box for question
question = st.text_area("Enter your question:", height=100)

# Submit button
if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            try:
                # Send question to FastAPI backend
                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={"question": question},
                    headers={"Content-Type": "application/json"}
                )
                data = response.json()

                # Display response or error
                if "response" in data:
                    st.success("Response:")
                    st.markdown(data["response"])
                else:
                    st.error(data.get("error", "Unknown error occurred."))
            except Exception as e:
                st.error(f"⚠️ Failed to connect to FastAPI: {str(e)}")
    else:
        st.warning("Please enter a question before submitting.")
