"""
test_langchain_fastapi.py

Purpose:
    Expose a local Ollama model via LangChain as a FastAPI service.
    Provides a /ask endpoint that accepts a question and returns the model response.

Prerequisites:
    1. Install Python 3.10+ and FastAPI:
         pip install fastapi uvicorn langchain langchain-core langchain-ollama pydantic
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
    1. Start the FastAPI server:
         uvicorn test_langchain_fastapi:app --reload

    2. Test the health check endpoint:
         curl http://127.0.0.1:8000/
       Expected output:
         {"message":"✅ LangChain FastAPI is running. Use /ask endpoint to send a question."}

    3. Send a question to the /ask endpoint:

       Linux/macOS (bash):
         curl -X POST "http://127.0.0.1:8000/ask" \
              -H "Content-Type: application/json" \
              -d '{"question": "What is the capital of Karnataka?"}'

       Windows Git Bash:
         curl -X POST "http://127.0.0.1:8000/ask" \
              -H "Content-Type: application/json" \
              -d '{"question": "What is the capital of Karnataka?"}'

       Windows PowerShell (Invoke-WebRequest):
         Invoke-WebRequest -Uri "http://127.0.0.1:8000/ask" `
           -Method POST `
           -ContentType "application/json" `
           -Body '{"question": "What is the capital of Karnataka?"}'

       Python alternative (cross-platform):
         import requests
         resp = requests.post("http://127.0.0.1:8000/ask",
                              json={"question": "What is the capital of Karnataka?"})
         print(resp.json())

    Expected output:
         {"response":"The capital of Karnataka is Bengaluru."}

Notes:
    - Uses LangChain PromptTemplate + OllamaLLM.
    - Error handling included for unexpected failures.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Initialize FastAPI app
app = FastAPI(title="GenAI Agentic Course — LangChain API")

# Load local Ollama model (ensure it's pulled and running)
llm = OllamaLLM(model="tinyllama")

# Define prompt template
template = PromptTemplate.from_template("""
You are a helpful assistant.

Question: {question}

Answer:""")

# Chain prompt → LLM
chain = template | llm

# Request schema
class PromptRequest(BaseModel):
    question: str

@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"message": "✅ LangChain FastAPI is running. Use /ask endpoint to send a question."}

@app.post("/ask")
def ask_model(request: PromptRequest):
    """
    Accepts a question and runs it through the LangChain → Ollama pipeline.
    Returns the model response or an error message.
    """
    try:
        response = chain.invoke({"question": request.question})
        return {"response": response}
    except Exception as e:
        return {"error": f"⚠️ Unexpected error: {str(e)}"}
