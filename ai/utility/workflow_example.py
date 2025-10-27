#!/usr/bin/env python3
"""
Example usage of the variable prompt workflow
"""

from variable_prompt_workflow import (
    parse_template_variables,
    identify_unfilled_variables,
    substitute_variables
)

# Example template with some variables already filled
example_template = """
# Documentation Article Creation Prompt Template

## Variables Section
Fill in these variables at the top - they will be used throughout the prompt:

**ARTICLE_TYPE** = [FAQ Article | Step-by-Step Guide | Technical Article | Troubleshooting Guide | Best Practices Guide | Configuration Guide | Reference Documentation]

**SUPPORT_REQUEST** = [Original support request or question if applicable - leave empty if not relevant]

**SUPPORT_ANSWER** = How do I configure MonitorWare Agent to forward logs to a remote syslog server?

**ARTICLE_TITLE** = [Clear, descriptive title following Adiscon documentation conventions]

**AUTHOR_NAME** = [Your name or "adiscon team"]

**CREATED_DATE** = [Creation date in YYYY-MM-DD format]

**UPDATED_DATE** = [Last update date in YYYY-MM-DD format]

**APPLICABLE_PRODUCTS** = [List of relevant products: EventReporter, MonitorWare Agent, WinSyslog, Rsyslog Windows Agent, etc.]

**ARTICLE_DESCRIPTION** = [Brief description of what the article covers]

**CONTENT_OUTLINE** = [Specific content structure for your article type]

**FILE_PATH** = [Target file path in the documentation structure]

**REFERENCE_LABEL** = [RST reference label for cross-references, e.g., descriptive-label]

## Prompt Template

```
Create a **{{ARTICLE_TYPE}}** for the Adiscon product documentation.

**Context Information:**
**{{SUPPORT_REQUEST}}** - Insert the original support request or question here if applicable
**{{SUPPORT_ANSWER}}** - Insert the original support answer or solution here if applicable

**Article Requirements:**

1. **Title:** {{ARTICLE_TITLE}}
   - Use title case
   - Include relevant product names (EventReporter, MonitorWare Agent, WinSyslog, Rsyslog Windows Agent)
   - Be specific about the topic or problem being addressed

2. **Metadata:**
   - Author: {{AUTHOR_NAME}}
   - Created/Updated dates: {{CREATED_DATE}} / {{UPDATED_DATE}}
   - Applicable products: {{APPLICABLE_PRODUCTS}}

3. **Content Structure:**
   {{CONTENT_OUTLINE}}

4. **Documentation Standards:**
   - Use proper RST (reStructuredText) formatting
   - Include cross-references using `:doc:` directive
   - Add images with proper paths (../images/filename.png)
   - Use appropriate admonitions (note, warning, important, tip)
   - Follow existing documentation patterns and terminology

5. **SEO and Navigation:**
   - Include reference label (`.. _{{REFERENCE_LABEL}}:`)
   - Use descriptive section headers
   - Include relevant keywords for search

**File Placement:**
- Specific path: {{FILE_PATH}}
```
"""

def demo_workflow():
    """Demonstrate the workflow with the example template."""

    print("🔍 Parsing template variables...")
    variables = parse_template_variables(example_template)

    print(f"Found variables: {list(variables.keys())}")

    print("\n📝 Identifying unfilled variables...")
    unfilled = identify_unfilled_variables(variables, example_template)

    print(f"Unfilled variables: {unfilled}")

    # Simulate user input for some variables
    print("\n🎯 Simulating user input for variables...")
    user_inputs = {
        "ARTICLE_TYPE": "Step-by-Step Guide",
        "SUPPORT_REQUEST": "How do I configure MonitorWare Agent to forward logs to a remote syslog server?",
        "ARTICLE_TITLE": "How to Configure MonitorWare Agent to Forward Logs to a Remote Syslog Server",
        "AUTHOR_NAME": "adiscon team",
        "CREATED_DATE": "2024-01-15",
        "UPDATED_DATE": "2024-01-15",
        "APPLICABLE_PRODUCTS": "MonitorWare Agent",
        "ARTICLE_DESCRIPTION": "This step-by-step guide explains how to configure MonitorWare Agent to forward logs to a remote syslog server.",
        "CONTENT_OUTLINE": "**Prerequisites:** MonitorWare Agent installed and running, Network connectivity to target syslog server. **Step 1:** Access the Configuration Client. **Step 2:** Create a New Rule. **Step 3:** Add Send Syslog Action.",
        "FILE_PATH": "/source/mwagentspecific/",
        "REFERENCE_LABEL": "configure-remote-syslog"
    }

    # Update variables with user input
    for var_name, value in user_inputs.items():
        if var_name in variables:
            variables[var_name] = value

    print(f"\n✅ Updated {len(user_inputs)} variables")

    print(f"\n🔄 Generating completed prompt...")
    completed_prompt = substitute_variables(example_template, variables)

    print("\n" + "="*60)
    print("COMPLETED PROMPT:")
    print("="*60)
    print(completed_prompt[:500] + "..." if len(completed_prompt) > 500 else completed_prompt)

    return completed_prompt

if __name__ == "__main__":
    demo_workflow()