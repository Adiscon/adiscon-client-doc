# Documentation Build Environment Setup

This directory contains scripts to set up a Python virtual environment for building the Adiscon documentation.

## Prerequisites

- Python 3.x installed on your system
- Git (for cloning the repository)

## Setup Scripts

### Windows
Run the Windows batch script:
```cmd
setup_venv.bat
```

### Linux/macOS/Unix
Run the shell script:
```bash
./setup_venv.sh
```

## What the Scripts Do

1. **Check Python Installation**: Verify that Python 3.x is installed and accessible
2. **Create Virtual Environment**: Create a new Python virtual environment in the `venv` directory
3. **Activate Environment**: Activate the virtual environment
4. **Upgrade pip**: Update pip to the latest version
5. **Install Dependencies**: Install required packages:
   - `sphinx` - Documentation generator
   - `furo` - Sphinx theme
   - Additional packages from `requirements.txt` (if present)

## After Setup

### Activating the Virtual Environment

**Windows:**
```cmd
venv\Scripts\activate.bat
```

**Linux/macOS/Unix:**
```bash
source venv/bin/activate
```

### Building Documentation

For detailed information on building documentation using the Makefile, see [README.MAKEFILE.md](README.MAKEFILE.md).

### Deactivating the Virtual Environment

```bash
deactivate
```

## Troubleshooting

### Python Not Found
If you get an error that Python is not found:
1. Make sure Python 3.x is installed
2. Ensure Python is in your system PATH
3. On Windows, you may need to restart your command prompt after installing Python

### Permission Errors (Linux/macOS)
If you get permission errors when running the shell script:
```bash
chmod +x setup_venv.sh
```

### Virtual Environment Already Exists
If the virtual environment already exists, the script will inform you and exit. You can:
- Use the existing environment (recommended)
- Delete the `venv` directory and run the setup script again 