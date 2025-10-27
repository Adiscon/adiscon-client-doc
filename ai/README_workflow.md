# Interactive Documentation Prompt Workflow

This workflow system helps you fill in template variables step by step for creating documentation articles.

## Features

- 🔍 **Automatic Variable Detection**: Finds all `{{VARIABLE_NAME}}` patterns in your template
- 📝 **Interactive Questioning**: Asks you to fill in unfilled variables one by one
- ✅ **Smart Validation**: Identifies which variables still need values
- 🔄 **Template Substitution**: Automatically replaces variables in the final prompt
- 💾 **File Export**: Optionally save the completed prompt to a file

## Quick Start

### Method 1: Interactive Mode (Recommended)

1. **Run the workflow script:**
   ```bash
   python3 variable_prompt_workflow.py
   ```

2. **Paste your template** when prompted (the entire template content)

3. **Answer questions** for each unfilled variable

4. **Review the completed prompt**

5. **Optionally save** to a file

### Method 2: Programmatic Usage

```python
from variable_prompt_workflow import (
    parse_template_variables,
    identify_unfilled_variables,
    substitute_variables
)

# Parse your template
variables = parse_template_variables(your_template_content)

# Fill in some variables
variables['ARTICLE_TYPE'] = 'Step-by-Step Guide'
variables['ARTICLE_TITLE'] = 'Your Article Title'

# Generate completed prompt
completed_prompt = substitute_variables(your_template_content, variables)
```

## Template Format

Your template should use this format for variables:

```markdown
## Variables Section

**VARIABLE_NAME** = [Description or current value]

**ARTICLE_TYPE** = [FAQ Article | Step-by-Step Guide | Technical Article]

**SUPPORT_REQUEST** = [Original support request or question]

## Prompt Template

```
Create a **{{ARTICLE_TYPE}}** for the Adiscon product documentation.

**Context Information:**
**{{SUPPORT_REQUEST}}** - Insert the original support request or question here if applicable
```

## Variable Types

The system recognizes these variable patterns:

- `{{VARIABLE_NAME}}` - Variables used in the prompt content
- `**VARIABLE_NAME** = [value]` - Variable definitions in the Variables Section

## Example Workflow

```bash
$ python3 variable_prompt_workflow.py

🚀 Interactive Documentation Prompt Workflow
============================================================
This tool will help you fill in template variables step by step.
Please paste your template content below (press Ctrl+D when finished on Unix/Linux):

📋 Paste your template content and press Ctrl+D when finished:
**ARTICLE_TYPE** = [FAQ Article | Step-by-Step Guide | Technical Article]

**SUPPORT_REQUEST** = [Original support request or question]

Create a **{{ARTICLE_TYPE}}** for documentation.

✅ Template loaded (512 characters)
============================================================
🔍 Found 2 variables: ARTICLE_TYPE, SUPPORT_REQUEST
📝 Found 2 unfilled variables: ARTICLE_TYPE, SUPPORT_REQUEST

❓ I need to ask you about 2 variables.
Let's fill them in one by one...

===========================================================
📝 Please fill in: ARTICLE_TYPE
===========================================================
💡 Context: [FAQ Article | Step-by-Step Guide | Technical Article]

Enter value for ARTICLE_TYPE:
> Step-by-Step Guide
✅ Set ARTICLE_TYPE = 'Step-by-Step Guide'

===========================================================
📝 Please fill in: SUPPORT_REQUEST
===========================================================
💡 Context: [Original support request or question]

Enter value for SUPPORT_REQUEST:
> How do I configure log forwarding?
✅ Set SUPPORT_REQUEST = 'How do I configure log forwarding?'

===========================================================
📊 SUMMARY
===========================================================
Total variables: 2
Filled: 2
Skipped: 0

===========================================================
🎉 COMPLETED PROMPT
===========================================================
**ARTICLE_TYPE** = Step-by-Step Guide

**SUPPORT_REQUEST** = How do I configure log forwarding?

Create a **Step-by-Step Guide** for documentation.

💾 Save completed prompt to file? (y/n): y
Enter filename (default: completed_prompt.md): my_article_prompt.md
✅ Saved to my_article_prompt.md
```

## Integration Ideas

### With Documentation Generator
You could integrate this workflow with a documentation generator:

```python
# After completing the workflow
completed_prompt = substitute_variables(template, variables)

# Use the completed prompt with your AI documentation generator
response = ai_generate_documentation(completed_prompt)
```

### With Batch Processing
Process multiple templates:

```python
import glob

for template_file in glob.glob("templates/*.md"):
    with open(template_file, 'r') as f:
        template_content = f.read()

    variables = parse_template_variables(template_content)
    # ... fill variables ...
    completed = substitute_variables(template_content, variables)

    output_file = f"completed/{template_file}"
    with open(output_file, 'w') as f:
        f.write(completed)
```

## Troubleshooting

### Common Issues

1. **No variables detected**: Make sure you're using `{{VARIABLE_NAME}}` format
2. **Wrong variables identified**: Check that your Variables Section format matches the expected pattern
3. **Template not loading**: Ensure you're pasting the complete template content

### Variable Name Rules

- Variable names should be uppercase with underscores: `ARTICLE_TYPE`
- Use descriptive names: `SUPPORT_REQUEST`, `AUTHOR_NAME`
- Avoid special characters in variable names

## Advanced Usage

### Custom Variable Detection

You can customize the variable detection pattern:

```python
import re

# Custom pattern for different variable formats
custom_pattern = r'<<([^>]+)>>'  # For <<VARIABLE>> format
variables = {}

for match in re.finditer(custom_pattern, template_content):
    var_name = match.group(1).strip()
    variables[var_name] = ""
```

### Batch Variable Filling

Pre-fill multiple variables at once:

```python
# Pre-fill common variables
common_variables = {
    'AUTHOR_NAME': 'adiscon team',
    'CREATED_DATE': '2024-01-15',
    'UPDATED_DATE': '2024-01-15'
}

variables.update(common_variables)
```

This workflow system makes it easy to maintain consistent documentation templates while allowing flexible customization for each specific use case.