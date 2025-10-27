#!/usr/bin/env python3
"""
Prompt Maker CLI - Command Line Documentation Prompt Generator
Creates prompts for documentation articles with variable substitution
"""

import sys
import os
import json
from pathlib import Path
import re
import argparse


class PromptMakerCLI:
    def __init__(self):
        self.config_dir = Path.home() / ".prompt_maker"
        self.config_file = self.config_dir / "config.json"

        # Default values
        self.config = {
            "author_name": "Adiscon Team",
            "author_email": "",
            "default_article_type": "Step-by-Step Guide",
            "default_products": "MonitorWare Agent, EventReporter, WinSyslog"
        }

        # Article type options
        self.article_types = [
            "FAQ Article",
            "Step-by-Step Guide",
            "Technical Article",
            "Troubleshooting Guide",
            "Best Practices Guide",
            "Configuration Guide",
            "Reference Documentation"
        ]

        # Common product options
        self.product_options = [
            "EventReporter",
            "MonitorWare Agent",
            "WinSyslog",
            "Rsyslog Windows Agent",
            "EventReporter, MonitorWare Agent",
            "MonitorWare Agent, WinSyslog",
            "All Products"
        ]

        # Load config
        self.load_config()

    def load_config(self):
        """Load configuration from file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    self.config.update(json.load(f))
        except Exception as e:
            print(f"Warning: Could not load config: {e}")

    def save_config(self):
        """Save configuration to file"""
        try:
            self.config_dir.mkdir(exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save config: {e}")

    def get_user_input(self, prompt_text, default_value="", options=None, required=False):
        """Get user input with optional validation"""
        while True:
            if options:
                print(f"\n{prompt_text}")
                for i, option in enumerate(options, 1):
                    marker = "*" if option == default_value else " "
                    print(f"  {i}. {option} {marker}")
                print(f"\nEnter choice (1-{len(options)}) or custom value")

                try:
                    choice = input("> ").strip()
                    if choice.isdigit() and 1 <= int(choice) <= len(options):
                        return options[int(choice) - 1]
                    elif choice:
                        return choice
                    elif default_value:
                        return default_value
                except (ValueError, KeyboardInterrupt):
                    pass
            else:
                default_display = f" (default: {default_value})" if default_value else ""
                response = input(f"{prompt_text}{default_display}: ").strip()
                if response:
                    return response
                elif default_value:
                    return default_value

            if required and not (default_value if not options else False):
                print("This field is required.")
            else:
                break

        return default_value

    def get_template_content(self):
        """Get the template content"""
        return '''# Documentation Article Creation Prompt Template

## Variables Section
Fill in these variables at the top - they will be used throughout the prompt:

**ARTICLE_TYPE** = [{{article_type}}]

**SUPPORT_REQUEST** = [{{support_request}}]

**SUPPORT_ANSWER** = [{{support_answer}}]

**ARTICLE_TITLE** = [{{article_title}}]

**AUTHOR_NAME** = [{{author_name}}]

**CREATED_DATE** = [{{created_date}}]

**UPDATED_DATE** = [{{updated_date}}]

**APPLICABLE_PRODUCTS** = [{{applicable_products}}]

**ARTICLE_DESCRIPTION** = [{{article_description}}]

**CONTENT_OUTLINE** = [{{content_outline}}]

**FILE_PATH** = [{{file_path}}]

**REFERENCE_LABEL** = [{{reference_label}}]

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

**Agent Instructions:**
- For any variables marked as optional above, if not provided by the user, the Agent should decide appropriate values based on the context
- Generate meaningful titles, descriptions, and outlines based on the support request and answer
- Choose appropriate file paths based on the article type and content
- Create relevant reference labels for cross-referencing
- Select applicable products based on the content and context
```'''

    def collect_variables(self):
        """Collect all variables from user input"""
        print("Prompt Maker CLI - Documentation Prompt Generator")
        print("=" * 60)

        variables = {}

        # MANDATORY: Article type
        variables['article_type'] = self.get_user_input(
            "Article Type (MANDATORY)",
            self.config.get("default_article_type", "Step-by-Step Guide"),
            self.article_types,
            required=True
        )

        # MANDATORY: Support request
        variables['support_request'] = self.get_user_input(
            "Support Request (MANDATORY)",
            "",
            required=True
        )

        # MANDATORY: Support answer
        variables['support_answer'] = self.get_user_input(
            "Support Answer (MANDATORY)",
            "",
            required=True
        )

        # OPTIONAL: Article title (Agent decides if not specified)
        article_title = self.get_user_input(
            "Article Title (optional - Agent will generate if not specified)",
            "",
            required=False
        )
        if article_title:
            variables['article_title'] = article_title

        # OPTIONAL: Author name (Agent decides if not specified)
        author_name = self.get_user_input(
            "Author Name (optional - Agent will use default if not specified)",
            self.config.get("author_name", "adiscon team"),
            required=False
        )
        if author_name:
            variables['author_name'] = author_name

        # OPTIONAL: Dates (Agent decides if not specified)
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        
        created_date = self.get_user_input(
            "Created Date (optional - Agent will use today if not specified)",
            today,
            required=False
        )
        if created_date:
            variables['created_date'] = created_date

        updated_date = self.get_user_input(
            "Updated Date (optional - Agent will use today if not specified)",
            today,
            required=False
        )
        if updated_date:
            variables['updated_date'] = updated_date

        # OPTIONAL: Applicable products (Agent decides if not specified)
        applicable_products = self.get_user_input(
            "Applicable Products (optional - Agent will choose appropriate products)",
            self.config.get("default_products", "MonitorWare Agent"),
            self.product_options,
            required=False
        )
        if applicable_products:
            variables['applicable_products'] = applicable_products

        # OPTIONAL: Article description (Agent decides if not specified)
        article_description = self.get_user_input(
            "Article Description (optional - Agent will generate if not specified)",
            "",
            required=False
        )
        if article_description:
            variables['article_description'] = article_description

        # OPTIONAL: Content outline (Agent decides if not specified)
        content_outline = self.get_user_input(
            "Content Outline (optional - Agent will generate if not specified)",
            "",
            required=False
        )
        if content_outline:
            variables['content_outline'] = content_outline

        # OPTIONAL: File path (Agent decides if not specified)
        file_path = self.get_user_input(
            "File Path (optional - Agent will choose appropriate path)",
            "/source/shared/faq/",
            required=False
        )
        if file_path:
            variables['file_path'] = file_path

        # OPTIONAL: Reference label (Agent decides if not specified)
        reference_label = self.get_user_input(
            "Reference Label (optional - Agent will generate if not specified)",
            "",
            required=False
        )
        if reference_label:
            variables['reference_label'] = reference_label

        return variables

    def substitute_variables(self, template_content, variables):
        """Substitute variables in template"""
        result = template_content

        for var_name, var_value in variables.items():
            # Replace in template content using simple string replacement to avoid regex issues
            placeholder = f"{{{{{var_name}}}}}"
            result = result.replace(placeholder, var_value)

        return result

    def generate_prompt(self, variables):
        """Generate the final prompt"""
        template_content = self.get_template_content()
        completed_prompt = self.substitute_variables(template_content, variables)

        return completed_prompt

    def run_interactive(self):
        """Run the interactive CLI mode"""
        try:
            # Collect variables
            variables = self.collect_variables()

            # Update config with new defaults
            if variables.get('author_name'):
                self.config['author_name'] = variables['author_name']
            if variables.get('article_type'):
                self.config['default_article_type'] = variables['article_type']
            if variables.get('applicable_products'):
                self.config['default_products'] = variables['applicable_products']

            self.save_config()

            # Generate prompt
            print("\n" + "=" * 60)
            print("GENERATING PROMPT...")
            print("=" * 60)

            completed_prompt = self.generate_prompt(variables)

            # Display results
            print("\n" + "=" * 80)
            print("GENERATED PROMPT")
            print("=" * 80)
            print(completed_prompt)

            # Offer to save to file
            save_option = self.get_user_input(
                "\nSave prompt to file? (y/n)",
                "n",
                required=False
            )

            if save_option.lower() in ['y', 'yes']:
                filename = self.get_user_input(
                    "Enter filename",
                    "generated_prompt.md"
                )

                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(completed_prompt)
                    print(f"Prompt saved to {filename}")
                except Exception as e:
                    print(f"Error saving file: {e}")

            print("\nPrompt generation completed!")
            return completed_prompt

        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user")
            return None
        except Exception as e:
            print(f"\nError: {e}")
            return None

    def run_batch(self, args):
        """Run in batch mode with provided arguments"""
        variables = {}

        # Map command line arguments to variables
        arg_mapping = {
            '--article-type': 'article_type',
            '--support-request': 'support_request',
            '--support-answer': 'support_answer',
            '--title': 'article_title',
            '--author': 'author_name',
            '--created-date': 'created_date',
            '--updated-date': 'updated_date',
            '--products': 'applicable_products',
            '--description': 'article_description',
            '--outline': 'content_outline',
            '--file-path': 'file_path',
            '--reference': 'reference_label'
        }

        # Parse arguments
        for i in range(0, len(args), 2):
            if i + 1 < len(args) and args[i] in arg_mapping:
                variables[arg_mapping[args[i]]] = args[i + 1]

        # Check for mandatory fields
        mandatory_fields = ['article_type', 'support_request', 'support_answer']
        missing_mandatory = [field for field in mandatory_fields if field not in variables]
        
        if missing_mandatory:
            print(f"Error: Missing mandatory fields: {', '.join(missing_mandatory)}")
            print("Mandatory fields are: --article-type, --support-request, --support-answer")
            return None

        # Optional fields - Agent will decide if not provided
        # Only add defaults for fields that were explicitly provided or have sensible defaults
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")

        # Only set defaults for fields that weren't provided and have reasonable defaults
        if 'author_name' not in variables:
            variables['author_name'] = self.config.get("author_name", "adiscon team")
        if 'created_date' not in variables:
            variables['created_date'] = today
        if 'updated_date' not in variables:
            variables['updated_date'] = today

        # Generate and return prompt
        return self.generate_prompt(variables)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Prompt Maker CLI - Generate documentation prompts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                    # Interactive mode
  %(prog)s --article-type "Step-by-Step Guide" --support-request "How to configure log forwarding?" --support-answer "Use the configuration wizard to set up forwarding rules" --title "How to Configure MonitorWare Agent" --author "adiscon team"
  %(prog)s --article-type "FAQ Article" --support-request "How do I configure log forwarding?" --support-answer "Navigate to Settings > Forwarding and configure your rules"

Note: --article-type, --support-request, and --support-answer are MANDATORY.
All other fields are optional and the Agent will decide appropriate values if not specified.
        """
    )

    parser.add_argument(
        '--article-type',
        help='Type of documentation article (MANDATORY for batch mode)'
    )
    parser.add_argument(
        '--support-request',
        help='Original support request or question (MANDATORY for batch mode)'
    )
    parser.add_argument(
        '--support-answer',
        help='Original support answer or solution (MANDATORY for batch mode)'
    )
    parser.add_argument(
        '--title',
        help='Article title'
    )
    parser.add_argument(
        '--author',
        help='Author name'
    )
    parser.add_argument(
        '--created-date',
        help='Creation date (YYYY-MM-DD)'
    )
    parser.add_argument(
        '--updated-date',
        help='Last update date (YYYY-MM-DD)'
    )
    parser.add_argument(
        '--products',
        help='Applicable products'
    )
    parser.add_argument(
        '--description',
        help='Article description'
    )
    parser.add_argument(
        '--outline',
        help='Content outline'
    )
    parser.add_argument(
        '--file-path',
        help='File path in documentation'
    )
    parser.add_argument(
        '--reference',
        help='RST reference label'
    )

    args = parser.parse_args()

    # Create prompt maker instance
    prompt_maker = PromptMakerCLI()

    # If no arguments provided, run interactive mode
    if len(sys.argv) == 1:
        result = prompt_maker.run_interactive()
    else:
        # Run batch mode with provided arguments
        result = prompt_maker.run_batch(sys.argv[1:])

        if result:
            print("\n" + "=" * 80)
            print("GENERATED PROMPT")
            print("=" * 80)
            print(result)

    return 0 if result else 1


if __name__ == "__main__":
    sys.exit(main())