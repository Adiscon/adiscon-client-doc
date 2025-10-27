#!/usr/bin/env python3
"""
Prompt Maker GUI - Interactive Documentation Prompt Generator
Creates prompts for documentation articles with variable substitution
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
import sys
from pathlib import Path
import re
import subprocess
import venv
import threading

class PromptMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Prompt Maker - Documentation Generator")
        self.root.geometry("1000x800")

        # Config file paths
        self.config_dir = Path.home() / ".prompt_maker"
        self.config_file = self.config_dir / "config.json"
        self.templates_dir = self.config_dir / "templates"

        # Default values
        self.config = {
            "author_name": "adiscon team",
            "author_email": "",
            "default_article_type": "Step-by-Step Guide",
            "default_products": "MonitorWare Agent, EventReporter, WinSyslog",
            "created_date": "",
            "updated_date": ""
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
            "EventReporter",
            "MonitorWare Agent, EventReporter",
            "MonitorWare Agent, WinSyslog",
            "All Products"
        ]

        # Current template content
        self.current_template = self.get_default_template()

        # Load config
        self.load_config()

        # Create GUI
        self.create_gui()

        # Load last used template if available
        self.load_last_template()

    def get_default_template(self):
        """Get the default embedded template"""
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

## Article Type Selection
Choose the type of documentation article you want to create:

1. **FAQ Article** - Addresses specific questions, problems, or common issues
2. **Step-by-Step Guide** - Provides detailed procedural instructions
3. **Technical Article** - Explains concepts, features, or how things work
4. **Troubleshooting Guide** - Helps diagnose and resolve specific problems
5. **Best Practices Guide** - Recommends optimal approaches and methodologies
6. **Configuration Guide** - Explains how to set up and configure features
7. **Reference Documentation** - Detailed technical specifications and parameters

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

   For FAQ Articles:
   - Start with the question or problem statement
   - Provide clear, direct answer
   - Include step-by-step resolution if applicable
   - Add notes, warnings, or additional context as needed

   For Step-by-Step Guides:
   - Include numbered steps with clear actions
   - Add screenshots or code examples where helpful
   - Include prerequisites and requirements
   - Add verification steps and troubleshooting tips

   For Technical Articles:
   - Explain the concept or feature clearly
   - Provide examples and use cases
   - Include technical details and parameters
   - Reference related documentation

   For Troubleshooting Guides:
   - Describe the problem/symptom
   - List possible causes
   - Provide systematic diagnosis steps
   - Offer solutions for each cause

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

**Additional Instructions:**
- Ensure technical accuracy and consistency with existing documentation
- Use clear, professional language appropriate for technical users
- Include practical examples when possible
- Consider edge cases and error conditions
- Reference related articles and documentation sections

**File Placement:**
- FAQ articles: `/source/shared/faq/`
- Step-by-step guides: `/source/step-by-step/` or `/source/eventreporterspecific/stepbystepguides.rst`
- Technical articles: `/source/articles/`
- Product-specific guides: Appropriate product subdirectory
- Specific path: {{FILE_PATH}}
```'''

    def create_gui(self):
        """Create the main GUI interface"""
        # Create main notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create tabs
        self.create_variables_tab()
        self.create_template_tab()
        self.create_settings_tab()
        self.create_output_tab()

        # Create menu bar
        self.create_menu()

        # Create status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.status_var.set("Ready")

    def create_menu(self):
        """Create menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Template", command=self.new_template)
        file_menu.add_command(label="Load Template", command=self.load_template)
        file_menu.add_command(label="Save Template", command=self.save_template)
        file_menu.add_separator()
        file_menu.add_command(label="Export Prompt", command=self.export_prompt)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Reset to Defaults", command=self.reset_to_defaults)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_variables_tab(self):
        """Create the variables input tab"""
        variables_frame = ttk.Frame(self.notebook)
        self.notebook.add(variables_frame, text="📝 Variables")

        # Create main frame with scrollbar for variables
        main_frame = ttk.Frame(variables_frame)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Canvas and scrollbar for scrollable content
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack canvas and scrollbar
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # Create variable input fields
        self.create_variable_inputs(scrollable_frame)

        # Generate button
        button_frame = ttk.Frame(variables_frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)

        self.generate_btn = ttk.Button(
            button_frame,
            text="🚀 Generate Prompt",
            command=self.generate_prompt,
            style="Accent.TButton"
        )
        self.generate_btn.pack(side=tk.RIGHT, padx=(5, 0))

        # Auto-generate checkbox
        self.auto_generate_var = tk.BooleanVar(value=True)
        auto_gen_check = ttk.Checkbutton(
            button_frame,
            text="Auto-generate on changes",
            variable=self.auto_generate_var,
            command=self.toggle_auto_generate
        )
        auto_gen_check.pack(side=tk.LEFT)

    def create_variable_inputs(self, parent):
        """Create input fields for all variables"""
        # Variable definitions
        variables = [
            ("article_type", "Article Type:", self.article_types, self.config.get("default_article_type", "Step-by-Step Guide")),
            ("support_request", "Support Request:", None, ""),
            ("support_answer", "Support Answer:", None, ""),
            ("article_title", "Article Title:", None, ""),
            ("author_name", "Author Name:", None, self.config.get("author_name", "adiscon team")),
            ("created_date", "Created Date:", None, self.get_today_date()),
            ("updated_date", "Updated Date:", None, self.get_today_date()),
            ("applicable_products", "Applicable Products:", self.product_options, self.config.get("default_products", "MonitorWare Agent")),
            ("article_description", "Article Description:", None, ""),
            ("content_outline", "Content Outline:", None, ""),
            ("file_path", "File Path:", None, "/source/shared/faq/"),
            ("reference_label", "Reference Label:", None, "")
        ]

        self.var_entries = {}

        for i, (var_name, label_text, options, default_value) in enumerate(variables):
            # Label
            label = ttk.Label(parent, text=label_text, font=("Arial", 10, "bold"))
            label.grid(row=i, column=0, sticky="w", padx=5, pady=5)

            if options:
                # Combobox for options
                entry = ttk.Combobox(parent, values=options, state="normal")
                entry.set(default_value if default_value else options[0])
            else:
                # Text entry
                entry = ttk.Entry(parent, width=50)
                entry.insert(0, default_value)

            entry.grid(row=i, column=1, sticky="ew", padx=5, pady=2)
            self.var_entries[var_name] = entry

            # Bind change events for auto-generation
            if isinstance(entry, ttk.Entry):
                entry.bind('<KeyRelease>', self.on_variable_change)
            else:
                entry.bind('<<ComboboxSelected>>', self.on_variable_change)

        # Configure grid weights
        parent.grid_columnconfigure(1, weight=1)

    def create_template_tab(self):
        """Create the template management tab"""
        template_frame = ttk.Frame(self.notebook)
        self.notebook.add(template_frame, text="📄 Templates")

        # Template selection
        template_select_frame = ttk.LabelFrame(template_frame, text="Template Management")
        template_select_frame.pack(fill=tk.X, padx=5, pady=5)

        # Template list
        list_frame = ttk.Frame(template_select_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Template listbox
        self.template_listbox = tk.Listbox(list_frame, height=5)
        self.template_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for listbox
        list_scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.template_listbox.yview)
        list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.template_listbox.config(yscrollcommand=list_scrollbar.set)

        # Template buttons
        btn_frame = ttk.Frame(template_select_frame)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)

        ttk.Button(btn_frame, text="Load Selected", command=self.load_selected_template).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Save Current", command=self.save_current_template).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Delete", command=self.delete_template).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Refresh List", command=self.refresh_template_list).pack(side=tk.RIGHT)

        # Template editor
        editor_frame = ttk.LabelFrame(template_frame, text="Template Editor")
        editor_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Template text area
        self.template_text = tk.Text(editor_frame, wrap=tk.WORD)
        template_scrollbar = ttk.Scrollbar(editor_frame, orient=tk.VERTICAL, command=self.template_text.yview)
        self.template_text.config(yscrollcommand=template_scrollbar.set)

        self.template_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        template_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Insert default template
        self.template_text.insert(tk.END, self.current_template)

    def create_settings_tab(self):
        """Create the settings tab"""
        settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(settings_frame, text="⚙️ Settings")

        # User settings
        user_frame = ttk.LabelFrame(settings_frame, text="User Information")
        user_frame.pack(fill=tk.X, padx=5, pady=5)

        # Author name
        ttk.Label(user_frame, text="Author Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.author_entry = ttk.Entry(user_frame)
        self.author_entry.insert(0, self.config.get("author_name", "adiscon team"))
        self.author_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Author email
        ttk.Label(user_frame, text="Author Email:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.email_entry = ttk.Entry(user_frame)
        self.email_entry.insert(0, self.config.get("author_email", ""))
        self.email_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Default settings
        default_frame = ttk.LabelFrame(settings_frame, text="Default Settings")
        default_frame.pack(fill=tk.X, padx=5, pady=5)

        # Default article type
        ttk.Label(default_frame, text="Default Article Type:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.default_type_combo = ttk.Combobox(default_frame, values=self.article_types, state="readonly")
        self.default_type_combo.set(self.config.get("default_article_type", "Step-by-Step Guide"))
        self.default_type_combo.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Default products
        ttk.Label(default_frame, text="Default Products:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.default_products_entry = ttk.Entry(default_frame)
        self.default_products_entry.insert(0, self.config.get("default_products", "MonitorWare Agent, EventReporter, WinSyslog"))
        self.default_products_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Buttons frame
        btn_frame = ttk.Frame(settings_frame)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)

        ttk.Button(btn_frame, text="Save Settings", command=self.save_settings).pack(side=tk.RIGHT, padx=(5, 0))
        ttk.Button(btn_frame, text="Reset to Defaults", command=self.reset_settings).pack(side=tk.RIGHT)

        # Configure grid weights
        settings_frame.grid_columnconfigure(1, weight=1)

    def create_output_tab(self):
        """Create the output tab with generated prompt"""
        output_frame = ttk.Frame(self.notebook)
        self.notebook.add(output_frame, text="📋 Generated Prompt")

        # Output text area
        self.output_text = tk.Text(output_frame, wrap=tk.WORD, font=("Consolas", 10))
        output_scrollbar = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        self.output_text.config(yscrollcommand=output_scrollbar.set)

        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Output buttons
        btn_frame = ttk.Frame(output_frame)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)

        ttk.Button(btn_frame, text="📋 Copy to Clipboard", command=self.copy_to_clipboard).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="💾 Save as File", command=self.save_prompt_to_file).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="🔄 Refresh", command=self.generate_prompt).pack(side=tk.RIGHT)

    def get_today_date(self):
        """Get today's date in YYYY-MM-DD format"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d")

    def load_config(self):
        """Load configuration from file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    self.config.update(json.load(f))
        except Exception as e:
            print(f"Error loading config: {e}")

    def save_config(self):
        """Save configuration to file"""
        try:
            self.config_dir.mkdir(exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")

    def load_template_list(self):
        """Load list of saved templates"""
        self.template_listbox.delete(0, tk.END)
        if self.templates_dir.exists():
            for template_file in self.templates_dir.glob("*.json"):
                self.template_listbox.insert(tk.END, template_file.stem)

    def refresh_template_list(self):
        """Refresh the template list"""
        self.load_template_list()

    def load_selected_template(self):
        """Load the selected template"""
        selection = self.template_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a template to load.")
            return

        template_name = self.template_listbox.get(selection[0])
        template_file = self.templates_dir / f"{template_name}.json"

        try:
            with open(template_file, 'r') as f:
                template_data = json.load(f)

            # Load variables into form
            for var_name, value in template_data.get("variables", {}).items():
                if var_name in self.var_entries:
                    if isinstance(self.var_entries[var_name], ttk.Combobox):
                        self.var_entries[var_name].set(value)
                    else:
                        self.var_entries[var_name].delete(0, tk.END)
                        self.var_entries[var_name].insert(0, value)

            # Load template content
            self.template_text.delete(1.0, tk.END)
            self.template_text.insert(1.0, template_data.get("template", self.current_template))

            self.status_var.set(f"Template '{template_name}' loaded")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load template: {e}")

    def save_current_template(self):
        """Save current template"""
        template_name = tk.simpledialog.askstring("Save Template", "Enter template name:")
        if not template_name:
            return

        # Collect current variables
        variables = {}
        for var_name, entry in self.var_entries.items():
            if isinstance(entry, ttk.Combobox):
                variables[var_name] = entry.get()
            else:
                variables[var_name] = entry.get()

        # Get template content
        template_content = self.template_text.get(1.0, tk.END).strip()

        # Save template data
        template_data = {
            "variables": variables,
            "template": template_content
        }

        try:
            self.templates_dir.mkdir(exist_ok=True)
            template_file = self.templates_dir / f"{template_name}.json"

            with open(template_file, 'w') as f:
                json.dump(template_data, f, indent=2)

            self.refresh_template_list()
            self.status_var.set(f"Template '{template_name}' saved")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save template: {e}")

    def delete_template(self):
        """Delete selected template"""
        selection = self.template_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a template to delete.")
            return

        template_name = self.template_listbox.get(selection[0])
        if messagebox.askyesno("Confirm Delete", f"Delete template '{template_name}'?"):
            template_file = self.templates_dir / f"{template_name}.json"
            try:
                template_file.unlink()
                self.refresh_template_list()
                self.status_var.set(f"Template '{template_name}' deleted")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete template: {e}")

    def save_settings(self):
        """Save user settings"""
        self.config["author_name"] = self.author_entry.get()
        self.config["author_email"] = self.email_entry.get()
        self.config["default_article_type"] = self.default_type_combo.get()
        self.config["default_products"] = self.default_products_entry.get()

        self.save_config()
        self.status_var.set("Settings saved")

    def reset_settings(self):
        """Reset settings to defaults"""
        if messagebox.askyesno("Confirm Reset", "Reset all settings to defaults?"):
            self.author_entry.delete(0, tk.END)
            self.author_entry.insert(0, "adiscon team")
            self.email_entry.delete(0, tk.END)
            self.default_type_combo.set("Step-by-Step Guide")
            self.default_products_entry.delete(0, tk.END)
            self.default_products_entry.insert(0, "MonitorWare Agent, EventReporter, WinSyslog")

            self.save_settings()

    def on_variable_change(self, event=None):
        """Handle variable changes for auto-generation"""
        if self.auto_generate_var.get():
            self.root.after(1000, self.generate_prompt)  # Debounce for 1 second

    def toggle_auto_generate(self):
        """Toggle auto-generation on/off"""
        if self.auto_generate_var.get():
            self.generate_prompt()

    def generate_prompt(self):
        """Generate the prompt from current variables"""
        try:
            # Collect variables
            variables = {}
            for var_name, entry in self.var_entries.items():
                if isinstance(entry, ttk.Combobox):
                    variables[var_name] = entry.get()
                else:
                    variables[var_name] = entry.get()

            # Get template content
            template_content = self.template_text.get(1.0, tk.END).strip()

            # Substitute variables
            for var_name, var_value in variables.items():
                # Replace in template content
                template_content = re.sub(
                    r'\{\{(' + re.escape(var_name) + r')\}\}',
                    var_value,
                    template_content
                )

            # Update output text
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(1.0, template_content)

            self.status_var.set("Prompt generated successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate prompt: {e}")
            self.status_var.set("Error generating prompt")

    def copy_to_clipboard(self):
        """Copy generated prompt to clipboard"""
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.output_text.get(1.0, tk.END).strip())
            self.status_var.set("Prompt copied to clipboard")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy to clipboard: {e}")

    def save_prompt_to_file(self):
        """Save generated prompt to file"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".md",
            filetypes=[("Markdown files", "*.md"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.output_text.get(1.0, tk.END).strip())
                self.status_var.set(f"Prompt saved to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def export_prompt(self):
        """Export current prompt (alias for save to file)"""
        self.save_prompt_to_file()

    def new_template(self):
        """Create new template"""
        if messagebox.askyesno("New Template", "Create new template from current content?"):
            self.template_text.delete(1.0, tk.END)
            self.template_text.insert(1.0, self.get_default_template())

            # Reset variables to defaults
            self.reset_to_defaults()

    def load_template(self):
        """Load template from file"""
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'r') as f:
                    template_data = json.load(f)

                # Load into form
                for var_name, value in template_data.get("variables", {}).items():
                    if var_name in self.var_entries:
                        if isinstance(self.var_entries[var_name], ttk.Combobox):
                            self.var_entries[var_name].set(value)
                        else:
                            self.var_entries[var_name].delete(0, tk.END)
                            self.var_entries[var_name].insert(0, value)

                # Load template content
                self.template_text.delete(1.0, tk.END)
                self.template_text.insert(1.0, template_data.get("template", ""))

                self.status_var.set(f"Template loaded from {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load template: {e}")

    def save_template(self):
        """Save current template to file"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            try:
                # Collect current variables
                variables = {}
                for var_name, entry in self.var_entries.items():
                    if isinstance(entry, ttk.Combobox):
                        variables[var_name] = entry.get()
                    else:
                        variables[var_name] = entry.get()

                template_content = self.template_text.get(1.0, tk.END).strip()

                template_data = {
                    "variables": variables,
                    "template": template_content
                }

                with open(filename, 'w') as f:
                    json.dump(template_data, f, indent=2)

                self.status_var.set(f"Template saved to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save template: {e}")

    def reset_to_defaults(self):
        """Reset all variables to defaults"""
        # Reset author from config
        self.var_entries["author_name"].delete(0, tk.END)
        self.var_entries["author_name"].insert(0, self.config.get("author_name", "adiscon team"))

        # Reset dates
        today = self.get_today_date()
        self.var_entries["created_date"].delete(0, tk.END)
        self.var_entries["created_date"].insert(0, today)
        self.var_entries["updated_date"].delete(0, tk.END)
        self.var_entries["updated_date"].insert(0, today)

        # Reset article type
        self.var_entries["article_type"].set(self.config.get("default_article_type", "Step-by-Step Guide"))

        # Reset products
        self.var_entries["applicable_products"].set(self.config.get("default_products", "MonitorWare Agent"))

        # Clear other fields
        for var_name in ["support_request", "support_answer", "article_title",
                        "article_description", "content_outline", "file_path", "reference_label"]:
            self.var_entries[var_name].delete(0, tk.END)

        self.status_var.set("Variables reset to defaults")

    def load_last_template(self):
        """Load the last used template if available"""
        # This would be implemented to load from a "last_template.json" or similar
        pass

    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo(
            "About Prompt Maker",
            "Prompt Maker GUI v1.0\n\n"
            "Interactive Documentation Prompt Generator\n"
            "Creates prompts for documentation articles with variable substitution\n\n"
            "© 2024 Adiscon GmbH"
        )

def create_venv_and_run():
    """Create virtual environment and run the application"""
    script_dir = Path(__file__).parent
    venv_dir = script_dir / "venv"

    # Check if we're already in a venv
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Already running in virtual environment")
        return run_gui()

    # Create venv if it doesn't exist
    if not venv_dir.exists():
        print("Creating virtual environment...")
        venv.create(venv_dir, with_pip=True)

        # Upgrade pip in venv
        pip_path = venv_dir / "bin" / "pip" if os.name != "nt" else venv_dir / "Scripts" / "pip.exe"
        if os.name == "nt":
            pip_cmd = [str(pip_path), "install", "--upgrade", "pip"]
        else:
            pip_cmd = [str(pip_path), "install", "--upgrade", "pip"]

        try:
            subprocess.check_call(pip_cmd)
            print("Virtual environment created successfully")
        except subprocess.CalledProcessError:
            print("Failed to upgrade pip in virtual environment")
            return

    # Activate venv and run script
    if os.name == "nt":
        python_path = venv_dir / "Scripts" / "python.exe"
        script_cmd = [str(python_path), __file__]
    else:
        python_path = venv_dir / "bin" / "python"
        script_cmd = [str(python_path), __file__]

    try:
        os.execv(python_path, script_cmd)
    except OSError:
        print(f"Failed to execute {python_path}")
        return

def run_gui():
    """Run the GUI application"""
    root = tk.Tk()

    # Set up styles
    style = ttk.Style()

    # Try to use a modern theme if available
    try:
        style.theme_use('clam')
    except:
        pass

    # Configure accent button style
    style.configure("Accent.TButton", background="#4CAF50", foreground="white")
    style.map("Accent.TButton",
              background=[("active", "#45a049"), ("pressed", "#4CAF50")])

    app = PromptMaker(root)
    root.mainloop()

if __name__ == "__main__":
    create_venv_and_run()