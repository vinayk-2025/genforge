"""
test_ollama.py

Purpose:
    Demonstrate how to run a local Ollama model (tinyllama) from Python using subprocess.
    Sends a simple prompt and prints the model’s response.

Prerequisites:
    1. Install Python 3.10+.
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
    1. Run the script:
         python test_ollama.py

    2. Expected output:
         🔍 Sending prompt to 'tinyllama' via Ollama...

         ✅ Ollama responded:
         (Model’s generated answer, e.g. "Hello GenAI Agentic Course students!")

Notes:
    - Uses subprocess to call Ollama CLI directly.
    - Includes error handling for:
         • Ollama not installed or not in PATH
         • Timeout if Ollama does not respond
         • Other unexpected errors
    - Students can edit the `prompt` variable to experiment with different inputs.
"""

import subprocess

def run_ollama_hello_world():
    """Send a simple prompt to Ollama and print the response."""
    prompt = "Say hello to the GenAI Agentic Course students."
    print("🔍 Sending prompt to 'tinyllama' via Ollama...\n")

    try:
        # Launch Ollama process with the tinyllama model
        process = subprocess.Popen(
            ["ollama", "run", "tinyllama"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8"
        )

        # Send the prompt and capture output
        stdout, stderr = process.communicate(input=prompt, timeout=30)

        # Check exit code and print result
        if process.returncode == 0:
            print("✅ Ollama responded:")
            print(stdout.strip())
        else:
            print("❌ Ollama returned an error:")
            print(stderr.strip())

    except subprocess.TimeoutExpired:
        print("⚠️ Ollama timed out. Try running manually.")
    except FileNotFoundError:
        print("❌ Ollama is not installed or not in PATH.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    run_ollama_hello_world()

