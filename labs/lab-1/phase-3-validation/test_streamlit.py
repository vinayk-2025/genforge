"""
test_streamlit.py

Purpose:
    Validate that Streamlit is installed and working by launching a simple dashboard.
    Displays a title, subheader, and confirmation message.

Prerequisites:
    1. Install Python 3.10+.
    2. Install Streamlit:
         pip install streamlit
    3. Verify installation:
         streamlit --version

Usage:
    1. Run the Streamlit app:
         streamlit run test_streamlit.py
    2. The browser will open automatically (default: http://localhost:8501).
       You will see:
         - A page title
         - A subheader confirming Streamlit installation
         - A success message

Expected Output:
    🎓 GenAI Agentic Course — Hello Streamlit!
    ✅ Streamlit is installed and working
    Streamlit is ready for GenAI experimentation!

Notes:
    - This script is a minimal validation step.
    - Students can extend it by:
         • Adding a prompt input box
         • Connecting to Ollama or LangChain FastAPI backend
         • Deploying to Streamlit Cloud
"""

import streamlit as st

# Configure Streamlit page
st.set_page_config(page_title="GenAI Agentic Course", layout="centered")

# Page title and subheader
st.title("🎓 GenAI Agentic Course — Hello Streamlit!")
st.subheader("✅ Streamlit is installed and working")

# Markdown content with instructions
st.markdown("""
Welcome to your first GenAI dashboard.  
This confirms that **Streamlit** is installed and functional on your system.

---

### 🧠 Next Steps
- Try adding a prompt input box
- Connect to Ollama or LangChain FastAPI backend
- Deploy to Streamlit Cloud
""")

# Success message
st.success("Streamlit is ready for GenAI experimentation!")
