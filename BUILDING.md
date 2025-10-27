# Building the Adiscon Documentation

This guide explains how to build the documentation locally for browsing or verification.

## Prerequisites
- git
- python3
- pip
- make
- texlive (for PDF builds)
- Optional: HTML Help Workshop (`hhc.exe`) if you need CHM output on Windows

## Setup

### Virtual Environment Setup (Recommended)

Using a virtual environment is recommended to avoid conflicts with system Python packages.

#### Windows
Run the Windows batch script:
```cmd
setup_venv.bat
```

#### Linux/macOS/Unix
Run the shell script:
```bash
./setup_venv.sh
```

#### What the Setup Scripts Do
1. **Check Python Installation**: Verify that Python 3.x is installed and accessible
2. **Create Virtual Environment**: Create a new Python virtual environment in the `venv` directory
3. **Activate Environment**: Activate the virtual environment
4. **Upgrade pip**: Update pip to the latest version
5. **Install Dependencies**: Install required packages from `requirements.txt`

#### Manual Setup (Alternative)
If you prefer to set up the virtual environment manually:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate.bat
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

#### Activating the Virtual Environment

Before building documentation, activate the virtual environment:

**Windows:**
```cmd
venv\Scripts\activate.bat
```

**Linux/macOS/Unix:**
```bash
source venv/bin/activate
```

#### Deactivating the Virtual Environment

When done:
```bash
deactivate
```

### Troubleshooting Setup

**Python Not Found:**
- Make sure Python 3.x is installed
- Ensure Python is in your system PATH
- On Windows, you may need to restart your command prompt after installing Python

**Permission Errors (Linux/macOS):**
```bash
chmod +x setup_venv.sh
```

**Virtual Environment Already Exists:**
- Use the existing environment (recommended)
- Delete the `venv` directory and run the setup script again

## Building the Docs
- Build all HTML documentation
  ```bash
  make all-html
  ```

- Build all PDF versions
  ```bash
  make all-pdf
  ```

Output is written to the `build/` directory:
- HTML: `build/html/<product>/index.html`
- PDF: `build/pdf/<product>/*.pdf`

You can also build a single product:
```bash
make html-winsyslog
make pdf-rsyslog
```

### Per-Product Build Commands

- eventreporter
  ```bash
  make html-eventreporter
  make pdf-eventreporter
  ```

- mwagent
  ```bash
  make html-mwagent
  make pdf-mwagent
  ```

- rsyslog
  ```bash
  make html-rsyslog
  make pdf-rsyslog
  ```

- syslogviewer
  ```bash
  make html-syslogviewer
  make pdf-syslogviewer
  ```

- winsyslog
  ```bash
  make html-winsyslog
  make pdf-winsyslog
  ```

- winsyslog-j
  ```bash
  make html-winsyslog-j
  make pdf-winsyslog-j
  ```

For more targets (including CHM/HTMLHelp), run:
```bash
make help
```

### Installing the HTML Help Compiler

The Microsoft HTML Help Workshop provides the `hhc.exe` compiler required for
CHM output. The executable is no longer bundled with this repository.

1. Download the latest HTML Help Workshop installer from the
   [Microsoft Download Center](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/htmlhelp/microsoft-html-help-downloads).
2. Install it on a Windows machine (or on the Windows side of a WSL
   environment).
3. Add the installation directory (typically
   `C:\Program Files (x86)\HTML Help Workshop`) to your `PATH`, **or** set the
   `HHC` environment variable to the full path of `hhc.exe` before invoking the
   Makefile.
4. On WSL, you can access the Windows installation via the path
   `/mnt/c/Program Files (x86)/HTML Help Workshop/hhc.exe`.

When `HHC` is not available, the Makefile will still build HTML output but skip
the final CHM compilation step.
