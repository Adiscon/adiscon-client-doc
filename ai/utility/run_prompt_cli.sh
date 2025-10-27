#!/bin/bash
# Wrapper script to run Prompt Maker CLI

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Run the CLI script
python3 "$SCRIPT_DIR/prompt_maker_cli.py" "$@"