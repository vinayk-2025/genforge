"""
test_gemini_fastapi.py

Purpose:
    Expose Gemini CLI as a FastAPI service.
    Provides a /ask endpoint that accepts a prompt and returns the Gemini response.

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
    1. Start the FastAPI server:
         uvicorn test_gemini_fastapi:app --reload

    2. Test the health check endpoint:
         curl http://127.0.0.1:8000/
       Expected output:
         {"message":"✅ Gemini FastAPI is running. Use /ask endpoint to send a prompt."}

    3. Send a prompt to the /ask endpoint:

       Linux/macOS (bash):
         curl -X POST "http://127.0.0.1:8000/ask" \
              -H "Content-Type: application/json" \
              -d '{"prompt": "What is the capital of Karnataka?"}'

       Windows Git Bash:
         curl -X POST "http://127.0.0.1:8000/ask" \
              -H "Content-Type: application/json" \
              -d '{"prompt": "What is the capital of Karnataka?"}'

       Windows PowerShell (Invoke-WebRequest):
         Invoke-WebRequest -Uri "http://127.0.0.1:8000/ask" `
           -Method POST `
           -ContentType "application/json" `
           -Body '{"prompt": "What is the capital of Karnataka?"}'

       Python alternative (cross-platform):
         import requests
         resp = requests.post("http://127.0.0.1:8000/ask",
                              json={"prompt": "What is the capital of Karnataka?"})
         print(resp.json())

    Expected output:
         {"response":"The capital of Karnataka is Bengaluru."}

Notes:
    - Uses subprocess to invoke Gemini CLI in non-interactive mode (-p).
    - Error handling included for missing CLI or unexpected failures.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import shutil

app = FastAPI(title="GenAI Agentic Course — Gemini CLI API")


class PromptRequest(BaseModel):
    """Schema for incoming prompt requests."""
    prompt: str


@app.get("/")
def read_root():
    """Health check endpoint."""
    return {
        "message": "✅ Gemini FastAPI is running. Use /ask endpoint to send a prompt."
    }


@app.post("/ask")
def ask_model(request: PromptRequest):
    """
    Accepts a prompt and runs Gemini CLI in non-interactive mode (-p).
    Returns the CLI output or an error message.
    """
    try:
        gemini_path = shutil.which("gemini")
        if not gemini_path:
            return {
                "error": "❌ Gemini CLI not found in PATH. Ensure npm global bin is added."
            }

        process = subprocess.run(
            [gemini_path, "-p", request.prompt],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        if process.returncode == 0 and process.stdout.strip():
            return {"response": process.stdout.strip()}
        return {"error": process.stderr.strip() or "⚠️ No response received"}

    except Exception as exc:
        return {"error": f"⚠️ Unexpected error: {str(exc)}"}
