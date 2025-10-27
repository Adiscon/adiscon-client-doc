#!/usr/bin/env python3
"""
Interactive Documentation Prompt Workflow
Helps users fill in template variables step by step
"""

import re
import sys
from typing import Dict, List, Tuple


def parse_template_variables(template_content: str) -> Dict[str, str]:
    """
    Parse template to find all variables and their current values.
    Returns a dictionary of variable_name -> current_value
    """
    # Find all {{VARIABLE_NAME}} patterns
    variable_pattern = r'\{\{([^}]+)\}\}'
    variables = {}

    for match in re.finditer(variable_pattern, template_content):
        var_name = match.group(1).strip()
        variables[var_name] = ""

    return variables


def identify_unfilled_variables(variables: Dict[str, str], template_content: str) -> List[str]:
    """
    Identify variables that still need to be filled.
    Variables that are empty or contain placeholder text are considered unfilled.
    """
    unfilled = []

    for var_name, current_value in variables.items():
        # Check if variable is empty or contains placeholder patterns
        if not current_value.strip() or current_value.startswith('[') and current_value.endswith(']'):
            unfilled.append(var_name)

    return unfilled


def ask_user_for_variable(var_name: str, template_content: str) -> str:
    """Ask user to fill in a specific variable with context from the template."""
    print(f"\n{'='*60}")
    print(f"📝 Please fill in: {var_name}")
    print(f"{'='*60}")

    # Try to find context for this variable in the template
    var_pattern = r'\*\*' + re.escape(var_name) + r'\*\* = (.+)'
    context_match = re.search(var_pattern, template_content)

    if context_match:
        context = context_match.group(1).strip()
        print(f"💡 Context: {context}")

    print(f"\nEnter value for {var_name}:")
    print("(Leave empty to skip this variable)")

    value = input("> ").strip()

    return value if value else ""


def substitute_variables(template_content: str, variables: Dict[str, str]) -> str:
    """Substitute all variables in the template with their values."""
    result = template_content

    for var_name, var_value in variables.items():
        # Replace both {{VAR_NAME}} and **VAR_NAME** = [value] patterns
        result = re.sub(r'\{\{' + re.escape(var_name) + r'\}\}', var_value, result)
        # Also replace the variable definition line
        var_def_pattern = r'(\*\*' + re.escape(var_name) + r'\*\* = )\[([^\]]+)\]'
        result = re.sub(var_def_pattern, r'\1' + var_value, result)

    return result


def main():
    """Main workflow function."""
    print("🚀 Interactive Documentation Prompt Workflow")
    print("=" * 60)
    print("This tool will help you fill in template variables step by step.")
    print("Please paste your template content below (press Ctrl+D when finished on Unix/Linux):")
    print()

    # Read template content
    if sys.platform == "win32":
        print("📋 Paste your template content and press Enter, then Ctrl+Z, then Enter:")
        template_lines = []
        try:
            while True:
                line = input()
                template_lines.append(line)
        except EOFError:
            pass
        template_content = "\n".join(template_lines)
    else:
        print("📋 Paste your template content and press Ctrl+D when finished:")
        template_content = sys.stdin.read()

    if not template_content.strip():
        print("❌ No template content provided. Exiting.")
        return

    print(f"\n✅ Template loaded ({len(template_content)} characters)")
    print("=" * 60)

    # Parse variables
    variables = parse_template_variables(template_content)
    print(f"🔍 Found {len(variables)} variables: {', '.join(variables.keys())}")

    # Identify unfilled variables
    unfilled = identify_unfilled_variables(variables, template_content)
    print(f"📝 Found {len(unfilled)} unfilled variables: {', '.join(unfilled)}")

    if not unfilled:
        print("✅ All variables are already filled! Template is ready to use.")
        print("\n" + "=" * 60)
        print("COMPLETED PROMPT:")
        print("=" * 60)
        print(substitute_variables(template_content, variables))
        return

    print(f"\n❓ I need to ask you about {len(unfilled)} variables.")
    print("Let's fill them in one by one...")

    # Ask for each unfilled variable
    for var_name in unfilled:
        value = ask_user_for_variable(var_name, template_content)
        if value:
            variables[var_name] = value
            print(f"✅ Set {var_name} = '{value}'")
        else:
            print(f"⏭️  Skipped {var_name}")

    # Show summary
    print(f"\n{'='*60}")
    print("📊 SUMMARY")
    print(f"{'='*60}")
    print(f"Total variables: {len(variables)}")
    print(f"Filled: {len([v for v in variables.values() if v.strip()])}")
    print(f"Skipped: {len([v for v in variables.values() if not v.strip()])}")

    # Generate completed prompt
    completed_prompt = substitute_variables(template_content, variables)

    print(f"\n{'='*60}")
    print("🎉 COMPLETED PROMPT")
    print(f"{'='*60}")
    print(completed_prompt)

    # Optionally save to file
    save_option = input("\n💾 Save completed prompt to file? (y/n): ").lower().strip()
    if save_option == 'y':
        filename = input("Enter filename (default: completed_prompt.md): ").strip()
        if not filename:
            filename = "completed_prompt.md"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(completed_prompt)
            print(f"✅ Saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving file: {e}")


if __name__ == "__main__":
    main()