#!/bin/bash
# -----------------------------------------------------------------------------
# test_gemini_cli.sh
#
# Purpose:
#   Validate installation and basic usage of the Gemini CLI.
#   Ensures Node.js and npm are installed, Gemini CLI is available,
#   and a sample prompt runs successfully in non-interactive mode.
#
# Usage:
#   ./test_gemini_cli.sh
#
# Expected Output:
#   - Node.js and npm version numbers
#   - Gemini CLI help message
#   - Response to test prompt ("The capital of Karnataka is Bengaluru.")
# -----------------------------------------------------------------------------

set -e  # Exit immediately if a command exits with a non-zero status

echo "🔍 Checking Node.js and npm installation..."
node -v || { echo "❌ Node.js not installed"; exit 1; }
npm -v || { echo "❌ npm not installed"; exit 1; }
echo "✅ Node.js and npm are installed"

echo "🔍 Checking Gemini CLI installation..."
if ! command -v gemini &> /dev/null; then
    echo "❌ Gemini CLI not found. Install with: npm install -g @google/gemini-cli"
    exit 1
fi
echo "✅ Gemini CLI is installed"

echo "🔍 Running Gemini CLI help..."
gemini --help | head -n 5

echo "🔍 Creating test prompt file..."
cat <<EOF > test-prompt.txt
You are a helpful assistant. What is the capital of Karnataka?
EOF

echo "🔍 Running test prompt with Gemini CLI (non-interactive mode)..."
gemini -p "$(cat test-prompt.txt)" || { echo "❌ Gemini CLI test failed"; exit 1; }

echo "✅ Gemini CLI test completed successfully"
