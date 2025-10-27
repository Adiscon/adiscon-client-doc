# 🤖 AI Tools Directory

This directory contains AI-powered tools for documentation and content generation.

## 📁 Structure

```
ai/
├── utility/              # Utility scripts and tools
│   ├── prompt_maker.py      # Main GUI for prompt generation
│   ├── run_prompt_maker.bat # Windows launcher
│   ├── run_prompt_maker.sh  # Unix/Linux launcher
│   ├── variable_prompt_workflow.py  # Command-line workflow tool
│   ├── workflow_example.py   # Usage examples
│   └── documentation-prompt-template.md  # Template documentation
└── README.md            # This file
```

## 🚀 Quick Start

### GUI Application (Recommended)
**Windows:**
```cmd
run_prompt_maker.bat
```

**Linux/macOS:**
```bash
./run_prompt_maker.sh
```

### Command Line Interface
**Interactive Mode:**
```bash
./prompt_maker_cli.py                    # Interactive prompts
# or
./run_prompt_cli.sh                      # Using wrapper script
```

**Batch Mode (with arguments):**
```bash
./prompt_maker_cli.py --article-type "Step-by-Step Guide" --title "How to Configure MonitorWare Agent"
```

## 📖 CLI Arguments

### Interactive Mode
Run without arguments for guided prompts:
```bash
./prompt_maker_cli.py
```

### Batch Mode Arguments
```bash
./prompt_maker_cli.py [OPTIONS]

Options:
  --article-type TYPE     Article type (FAQ Article, Step-by-Step Guide, etc.)
  --support-request TEXT  Original support request/question
  --support-answer TEXT   Original support answer/solution
  --title TEXT           Article title (required)
  --author TEXT          Author name
  --created-date DATE    Creation date (YYYY-MM-DD)
  --updated-date DATE    Last update date (YYYY-MM-DD)
  --products TEXT        Applicable products
  --description TEXT     Article description
  --outline TEXT         Content outline
  --file-path PATH       File path in documentation
  --reference TEXT       RST reference label
```

### Examples

**Interactive Mode:**
```bash
./prompt_maker_cli.py
# Will prompt for each field interactively
```

**Batch Mode - Step-by-Step Guide:**
```bash
./prompt_maker_cli.py \
  --article-type "Step-by-Step Guide" \
  --title "How to Configure MonitorWare Agent Log Forwarding" \
  --author "adiscon team" \
  --products "MonitorWare Agent"
```

**Batch Mode - FAQ Article:**
```bash
./prompt_maker_cli.py \
  --article-type "FAQ Article" \
  --title "How do I configure log forwarding in MonitorWare Agent?" \
  --support-request "How do I configure MonitorWare Agent to forward logs to a remote server?" \
  --support-answer "Configure a Send Syslog action in MonitorWare Agent and set the destination server details."
```

## 🛠️ Legacy Command Line Tools

**Interactive Workflow:**
```bash
cd ai/utility
python3 variable_prompt_workflow.py
```

## 🛠️ Available Tools

### Prompt Maker GUI (`prompt_maker.py`)
- **Interactive GUI** for creating documentation prompts
- **Variable substitution** with comboboxes for common values
- **Template management** - save and load custom templates
- **Real-time generation** with auto-update
- **Cross-platform** (Windows, Linux, macOS)

**Features:**
- Article type selection (FAQ, Step-by-Step, Technical, etc.)
- Product selection (EventReporter, MonitorWare Agent, WinSyslog, etc.)
- Support request/answer context
- Author information and dates
- Content outline and file paths

### Prompt Maker CLI (`prompt_maker_cli.py`)
- **Command-line interface** for headless environments
- **Interactive prompts** guide you through variable entry
- **Batch mode** with command-line arguments
- **Template-based** prompt generation
- **Config persistence** saves preferences

**Features:**
- All GUI variables available via CLI
- Choice menus for article types and products
- Optional field handling
- File output capability
- Cross-platform compatibility

**Usage Modes:**
- **Interactive**: `./prompt_maker_cli.py` (asks questions)
- **Batch**: `./prompt_maker_cli.py --article-type "FAQ" --title "How to..."`

### Command Line Workflow (`variable_prompt_workflow.py`)
- **Interactive questioning** for template variables
- **Batch processing** of multiple templates
- **Template validation** and error checking
- **File export** capabilities

## 📖 Documentation

- **[Prompt Maker Manual](README_PromptMaker.md)** - Complete GUI documentation
- **[Workflow Guide](README_workflow.md)** - Command-line workflow instructions
- **[Template Documentation](utility/documentation-prompt-template.md)** - Template format and usage

## 🔧 Configuration

All tools save user preferences and templates locally in:
- `~/.prompt_maker/config.json` (user settings)
- `~/.prompt_maker/templates/` (custom templates)

## 🆘 Support

For issues or questions:
1. Check the troubleshooting sections in the documentation
2. Ensure Python 3.8+ and tkinter are installed
3. Verify virtual environment creation permissions