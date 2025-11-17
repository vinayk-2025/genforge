"""
test_requirements.py

Purpose:
    Validate that all mandatory Python packages for Agentic AI labs are installed.
    Prints ✅ if installed, ❌ with pip install hint if missing.

Prerequisites:
    - Python 3.10+
    - Virtual environment activated (recommended):
         python -m venv venv
         source venv/bin/activate   # Linux/macOS
         venv\Scripts\activate      # Windows PowerShell

Usage:
    1. Run the script:
         python test_requirements.py
    2. Expected output:
         🔍 Checking required Python packages...

         ✅ fastapi is installed.
         ❌ tensorflow is missing. Run: pip install tensorflow
         ✅ torch is installed.
         ...

Notes:
    - This script does not install packages automatically.
    - Students must copy/paste the suggested pip install commands.
    - Always re‑run after installation to confirm.
"""

import importlib

# Comprehensive list of mandatory packages for Agentic AI labs
required = [
    # Web frameworks
    "fastapi", "flask", "uvicorn", "streamlit",

    # HTTP utilities
    "requests",

    # Data validation
    "pydantic",

    # LangChain ecosystem
    "langchain", "langchain_core", "langchain_community", "langchain_ollama",

    # Ollama bindings (Python client)
    "ollama",

    # Environment and configuration
    "python-dotenv",

    # Core ML/AI frameworks
    "tensorflow", "torch", "scikit-learn",

    # NLP and text processing
    "nltk", "spacy",

    # Computer vision
    "opencv-python", "scikit-image",

    # Agentic frameworks (open-source only)
    "crewai",

    # Scientific computing
    "numpy", "pandas", "matplotlib"
] 

print("🔍 Checking required Python packages...\n")
for pkg in required:
    try:
        importlib.import_module(pkg)
        print(f"✅ {pkg} is installed.")
    except ImportError:
        print(f"❌ {pkg} is missing. Run: pip install {pkg}")
