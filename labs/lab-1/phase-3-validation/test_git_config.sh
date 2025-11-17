#!/bin/bash
# -----------------------------------------------------------------------------
# test_git_config.sh
#
# Purpose:
#   Validate Git installation and configuration for student labs.
#   Ensures Git is installed, shows current configuration, and suggests setup.
#
# Prerequisites:
#   - Git must be installed:
#       Linux/macOS:   sudo apt install git   OR   brew install git
#       Windows Git Bash: Git is bundled with Git for Windows (https://git-scm.com/download/win)
#       Windows PowerShell: Install Git for Windows and ensure git.exe is in PATH
#
# Usage:
#   1. Run this script:
#        ./test_git_config.sh
#
#   2. Expected output:
#        🔍 Checking Git configuration...
#        (list of current git config values)
#
#        🔧 Suggested setup:
#        git config --global user.name "Your Name"
#        git config --global user.email "you@example.com"
#
# Notes:
#   - Students must replace "Your Name" and "you@example.com" with their actual name/email.
#   - These values are used for commit metadata in Git repositories.
#   - Run the suggested commands once; they persist globally.
# -----------------------------------------------------------------------------

echo "🔍 Checking Git installation..."
if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Please install Git and ensure it is in your PATH."
    exit 1
fi

echo "✅ Git is installed"

echo "🔍 Checking Git configuration..."
git config --list || echo "⚠️ No Git configuration found."

echo -e "\n🔧 Suggested setup:"
echo "git config --global user.name \"Your Name\""
echo "git config --global user.email \"you@example.com\""
