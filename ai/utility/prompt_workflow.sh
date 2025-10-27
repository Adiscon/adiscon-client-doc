#!/bin/bash
# Simple launcher for the documentation prompt workflow

echo "🚀 Starting Documentation Prompt Workflow..."
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    python3 variable_prompt_workflow.py
elif command -v python &> /dev/null; then
    python variable_prompt_workflow.py
else
    echo "❌ Python is not installed or not in PATH"
    echo "Please install Python 3 and try again"
    exit 1
fi