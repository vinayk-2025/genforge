"""
test_gemini_flask.py

Purpose:
    Expose Gemini CLI as a Flask service.
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
    1. Start the Flask server:
         python test_gemini_flask.py

    2. Test the health check endpoint:
         curl http://127.0.0.1:5000/
       Expected output:
         ✅ Gemini Flask API is running.

    3. Send a prompt to the /ask endpoint:

       Linux/macOS (bash):
         curl -X POST "http://127.0.0.1:5000/ask" \
              -H "Content-Type: application/json" \
              -d '{"prompt": "What is the capital of Karnataka?"}'

       Windows Git Bash:
         curl -X POST "http://127.0.0.1:5000/ask" \
              -H "Content-Type: application/json" \
              -d '{"prompt": "What is the capital of Karnataka?"}'

       Windows PowerShell (Invoke-WebRequest):
         Invoke-WebRequest -Uri "http://127.0.0.1:5000/ask" `
           -Method POST `
           -ContentType "application/json" `
           -Body '{"prompt": "What is the capital of Karnataka?"}'

       Python alternative (cross-platform):
         import requests
         resp = requests.post("http://127.0.0.1:5000/ask",
                              json={"prompt": "What is the capital of Karnataka?"})
         print(resp.json())

    Expected output:
         {"response":"The capital of Karnataka is Bengaluru."}

Notes:
    - Uses subprocess to invoke Gemini CLI in non-interactive mode (-p).
    - Error handling included for missing CLI or unexpected failures.
"""

from flask import Flask, request, jsonify
import subprocess
import shutil

app = Flask(__name__)


@app.route("/ask", methods=["POST"])
def ask():
    """Accepts a prompt and runs Gemini CLI in non-interactive mode (-p)."""
    data = request.get_json()
    prompt = data.get("prompt", "")

    try:
        gemini_path = shutil.which("gemini")
        if not gemini_path:
            return jsonify({
                "error": "❌ Gemini CLI not found in PATH. Ensure npm global bin is added."
            }), 500

        process = subprocess.run(
            [gemini_path, "-p", prompt],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        if process.returncode == 0 and process.stdout.strip():
            return jsonify({"response": process.stdout.strip()})
        return jsonify({"error": process.stderr.strip() or "⚠️ No response received"}), 500

    except Exception as exc:
        return jsonify({"error": f"⚠️ Unexpected error: {str(exc)}"}), 500


@app.route("/")
def home():
    """Health check endpoint."""
    return "✅ Gemini Flask API is running."


if __name__ == "__main__":
    app.run(debug=True)
