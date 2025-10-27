# 📝 Prompt Maker GUI

A comprehensive GUI application for generating documentation prompts with variable substitution. Perfect for creating consistent documentation articles for Adiscon products.

## ✨ Features

- **🎨 Modern GUI Interface**: Clean, intuitive interface built with tkinter
- **📝 Variable Management**: Fill in template variables with comboboxes for common values
- **💾 Config Persistence**: Save user preferences (author, email, defaults) locally
- **📄 Template Management**: Save and load custom prompt templates
- **🔄 Auto-Generation**: Real-time prompt generation as you type
- **📋 Multiple Outputs**: Copy to clipboard, save to file, or export
- **🐍 Virtual Environment**: Auto-creates and manages Python venv
- **⚡ Cross-Platform**: Works on Windows, Linux, and macOS

## 🚀 Quick Start

### Windows
Double-click `run_prompt_maker.bat` or run in Command Prompt:
```cmd
run_prompt_maker.bat
```

### Linux/macOS
Make executable and run:
```bash
chmod +x run_prompt_maker.sh
./run_prompt_maker.sh
```

### Python Direct
```bash
python3 prompt_maker.py
```

## 📋 How to Use

1. **Launch the application** using one of the starter scripts
2. **Fill in variables** in the "Variables" tab:
   - Use comboboxes for common options (Article Type, Products)
   - Enter custom values for other fields
   - Enable auto-generation for real-time updates

3. **Customize template** in the "Templates" tab if needed

4. **Review generated prompt** in the "Generated Prompt" tab

5. **Copy or save** the completed prompt

## 🗂️ Project Structure

```
├── prompt_maker.py          # Main GUI application
├── run_prompt_maker.bat     # Windows starter script
├── run_prompt_maker.sh      # Unix starter script
├── requirements.txt         # Python dependencies (minimal)
├── README_PromptMaker.md    # This file
└── venv/                    # Auto-created virtual environment
    ├── bin/python3          # Linux/macOS Python
    └── Scripts/python.exe   # Windows Python
```

## ⚙️ Configuration

### User Settings (Saved locally in `~/.prompt_maker/config.json`)
- **Author Name**: Default author for documentation
- **Author Email**: Contact email
- **Default Article Type**: Preferred documentation type
- **Default Products**: Commonly used products

### Template Storage (Saved locally in `~/.prompt_maker/templates/`)
- Custom prompt templates saved as JSON files
- Variables and template content preserved
- Easy loading for reuse

## 🎯 Variable Types

The application handles these variable types intelligently:

### Combobox Variables (Dropdown Selection)
- **Article Type**: FAQ Article, Step-by-Step Guide, Technical Article, etc.
- **Applicable Products**: EventReporter, MonitorWare Agent, WinSyslog, etc.

### Text Input Variables
- **Support Request**: Original support question
- **Support Answer**: Original support answer
- **Article Title**: Descriptive title for the documentation
- **Author Name**: Document author
- **Created/Updated Dates**: Publication dates
- **Article Description**: Brief summary
- **Content Outline**: Structure overview
- **File Path**: Target location in documentation
- **Reference Label**: RST reference for cross-linking

## 🔧 Template Format

Templates use `{{VARIABLE_NAME}}` syntax for substitution:

```markdown
**ARTICLE_TYPE** = [{{article_type}}]

**SUPPORT_REQUEST** = [{{support_request}}]

Create a **{{ARTICLE_TYPE}}** for the Adiscon product documentation.

**Context Information:**
**{{SUPPORT_REQUEST}}** - Insert the original support request or question here if applicable
```

## 🛠️ Advanced Features

### Template Management
- **Save Current**: Save current variable values and template as a named template
- **Load Template**: Load previously saved templates
- **Delete Template**: Remove unwanted templates
- **New Template**: Start fresh with default template

### Auto-Generation
- Enable/disable real-time prompt generation
- Debounced updates (waits 1 second after last change)
- Instant feedback as you fill in variables

### Export Options
- **Copy to Clipboard**: Quick copy for immediate use
- **Save as File**: Export as Markdown or text file
- **Template Export**: Save current setup as reusable template

## 🔒 Local Storage

All user data is stored locally and NOT added to git:

- **Config**: `~/.prompt_maker/config.json` - User preferences
- **Templates**: `~/.prompt_maker/templates/` - Custom templates
- **Virtual Environment**: `./venv/` - Python environment

## 🐛 Troubleshooting

### Common Issues

**Application won't start:**
- Ensure Python 3.8+ is installed
- On Linux/macOS, install tkinter: `sudo apt install python3-tk` (Ubuntu/Debian)
- Try running directly: `python3 prompt_maker.py`

**GUI looks different on different systems:**
- Uses system-native tkinter theming
- Appearance varies by OS and desktop environment

**Virtual environment issues:**
- Delete `./venv/` folder and restart
- The application will recreate it automatically

**Template not loading:**
- Check file permissions in `~/.prompt_maker/templates/`
- Ensure JSON format is valid

## 🆘 Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Ensure all dependencies are installed
3. Try deleting the virtual environment and restarting
4. Check that you're using Python 3.8 or later

## 📝 License

This tool is part of the Adiscon documentation workflow and is intended for internal use in creating consistent documentation prompts.

---

**Happy Documentation Writing! 🚀**