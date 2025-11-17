"""
test_ollama_fastapi.py

Purpose:
    Expose a local Ollama model (tinyllama) via FastAPI.
    Provides a /ask endpoint that accepts a prompt and returns the model response.

Prerequisites:
    1. Install Python 3.10+ and required packages:
         pip install fastapi uvicorn pydantic
    2. Install Ollama (local LLM runner):
         - Windows: https://ollama.com/download
         - macOS:   brew install ollama
         - Linux:   follow instructions at https://ollama.com/download
    3. Verify Ollama installation:
         ollama --version
    4. Pull the required model (tinyllama in this example):
         ollama pull tinyllama
    5. Ensure Ollama service is running:
         ollama serve

Usage:
    Step 1: Start the FastAPI server
        uvicorn test_ollama_fastapi:app --reload

    Step 2: Verify FastAPI health check
        curl http://127.0.0.1:8000/
        Expected output:
            {"message":"✅ Ollama FastAPI is running. Use /ask endpoint to send a prompt."}

    Step 3: Send a prompt to the /ask endpoint

        Linux/macOS (bash):
            curl -X POST "http://127.0.0.1:8000/ask" \
                 -H "Content-Type: application/json" \
                 -d '{"prompt": "Say hello to the GenAI Agentic Course students."}'

        Windows Git Bash:
            curl -X POST "http://127.0.0.1:8000/ask" \
                 -H "Content-Type: application/json" \
                 -d '{"prompt": "Say hello to the GenAI Agentic Course students."}'

        Windows PowerShell (Invoke-WebRequest):
            Invoke-WebRequest -Uri "http://127.0.0.1:8000/ask" `
              -Method POST `
              -ContentType "application/json" `
              -Body '{"prompt": "Say hello to the GenAI Agentic Course students."}'

        Python alternative (cross-platform):
            import requests
            resp = requests.post("http://127.0.0.1:8000/ask",
                                 json={"prompt": "Say hello to the GenAI Agentic Course students."})
            print(resp.json())

    Expected output:
        {"response":"Hello GenAI Agentic Course students!"}

Notes:
    - Uses subprocess to call Ollama CLI directly.
    - Reads output line by line to capture streaming responses.
    - Includes error handling for unexpected failures.
    - Students can edit the 'prompt' field in the request to experiment with different inputs.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

# Initialize FastAPI app
app = FastAPI(title="GenAI Agentic Course — Ollama API")

# Request schema
class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"message": "✅ Ollama FastAPI is running. Use /ask endpoint to send a prompt."}

@app.post("/ask")
def ask_model(request: PromptRequest):
    """
    Accepts a prompt and runs it through Ollama (tinyllama model).
    Returns the model response or an error message.
    """
    try:
        # Launch Ollama process
        process = subprocess.Popen(
            ["ollama", "run", "tinyllama"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8"
        )

        # Send prompt to Ollama
        process.stdin.write(request.prompt)
        process.stdin.close()

        # Read output line by line
        response_lines = []
        for line in process.stdout:
            response_lines.append(line.strip())

        # Wait for process to finish
        process.wait()

        if process.returncode == 0:
            return {"response": "\n".join(response_lines)}
        else:
            return {"error": process.stderr.read().strip()}

    except Exception as e:
        return {"error": f"⚠️ Unexpected error: {str(e)}"}
