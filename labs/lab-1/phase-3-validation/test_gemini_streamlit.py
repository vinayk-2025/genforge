"""
test_gemini_streamlit.py

Purpose:
    Expose Gemini CLI as a Streamlit app.
    Provides a simple web UI where students can enter a prompt and see the Gemini response.

Prerequisites:
    1. Install Node.js v18+ (check with: node -v)
    2. Install Gemini CLI globally:
         npm install -g @google/gemini-cli
    3. Verify installation:
         gemini --version
    4. Ensure npm global bin directory is in PATH:
         - Windows (default): C:/Users/<username>/AppData/Roaming/npm
           Add this to PATH via System Environment Variables.
         - Git Bash: add to ~/.bashrc
             export PATH=$PATH:/c/Users/<username>/AppData/Roaming/npm
         - PowerShell: temporarily add
             $env:PATH += ";C:/Users/<username>/AppData/Roaming/npm"
         - Linux/macOS: npm global bin is usually /usr/local/bin or ~/.npm-global/bin
             export PATH=$PATH:$(npm root -g)/../bin

Usage:
    1. Start the Streamlit app:
         streamlit run test_gemini_streamlit.py

    2. The browser will open automatically (default: http://localhost:8501).
       You will see:
         - A text input box for your prompt
         - A "Submit" button
         - The Gemini CLI response displayed below

    Example prompt:
         What is the capital of Karnataka?

    Expected output:
         The capital of Karnataka is Bengaluru.

Notes:
    - Uses subprocess to invoke Gemini CLI in non-interactive mode (-p).
    - Error handling included for missing CLI or unexpected failures.
    - Streamlit provides a student-friendly UI, no need for curl/Postman.
"""

import streamlit as st
import subprocess
import shutil

st.title("GenAI Agentic Course — Gemini CLI Streamlit App")
st.write("✅ Enter a prompt below and get a response from Gemini CLI.")

# Input box for prompt
prompt = st.text_input("Enter your prompt:")

if st.button("Submit"):
    if not prompt.strip():
        st.error("⚠️ Please enter a prompt before submitting.")
    else:
        try:
            gemini_path = shutil.which("gemini")
            if not gemini_path:
                st.error("❌ Gemini CLI not found in PATH. Ensure npm global bin is added.")
            else:
                process = subprocess.run(
                    [gemini_path, "-p", prompt],
                    capture_output=True,
                    text=True,
                    encoding="utf-8"
                )

                if process.returncode == 0 and process.stdout.strip():
                    st.success("✅ Gemini CLI Response:")
                    st.write(process.stdout.strip())
                else:
                    st.error(process.stderr.strip() or "⚠️ No response received")

        except Exception as exc:
            st.error(f"⚠️ Unexpected error: {str(exc)}")
