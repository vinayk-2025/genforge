"""
test_langchain_prompt.py

Purpose:
    Demonstrate a simple LangChain pipeline using a local Ollama model.
    Builds a prompt template, chains it to the model, and prints the response.

Prerequisites:
    1. Install Python 3.10+ and required packages:
         pip install langchain langchain-core langchain-ollama
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

Usage:
    1. Run the script:
         python test_langchain_prompt.py

    2. Expected output:
         🧠 LangChain Response:
         (Model’s answer to the test question)

Notes:
    - Uses LangChain PromptTemplate + OllamaLLM.
    - This script runs a single test prompt and prints the response.
    - Students can edit the question in the script to experiment with different prompts.
"""

from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Load local Ollama model (ensure it's pulled and running via `ollama serve`)
llm = OllamaLLM(model="tinyllama")

# Define prompt template
template = PromptTemplate.from_template("""
You are a helpful assistant.

Question: {question}

Answer:""")

# Chain prompt → LLM
chain = template | llm

# Run the chain with a sample question
response = chain.invoke({"question": "Explain artificial intelligence using a cooking analogy."})

# Print result
print("\n🧠 LangChain Response:\n")
print(response)
