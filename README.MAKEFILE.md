# Adiscon Documentation Build System - Makefile Guide

## Overview

This Makefile replaces all individual build shell scripts with a unified, cross-platform build system for the Adiscon documentation repository. It supports building multiple documentation projects in various formats (HTML, single-page HTML, HTMLHelp/CHM, PDF).

## Prerequisites

- **Python 3.x**: Required for Sphinx and documentation build tools
- **Git**: For cloning the repository
- **Sphinx toolchain**: Install via `pip install -r requirements.txt`
  (using a virtual environment is recommended; see below)
  
- **HTML Help Compiler** (optional, for CHM builds on Windows):
  - Windows: Install HTML Help Workshop
  - Linux/WSL: The Makefile will automatically detect `hhc.exe` if available

## Virtual Environment Setup

Using a virtual environment is recommended to avoid conflicts with system Python packages.

### Setup Scripts

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

### What the Setup Scripts Do

1. **Check Python Installation**: Verify that Python 3.x is installed and accessible
2. **Create Virtual Environment**: Create a new Python virtual environment in the `venv` directory
3. **Activate Environment**: Activate the virtual environment
4. **Upgrade pip**: Update pip to the latest version
5. **Install Dependencies**: Install the pinned toolchain from `requirements.txt`

### Manual Virtual Environment Setup

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

### Activating the Virtual Environment

Before building documentation, activate the virtual environment:

**Windows:**
```cmd
venv\Scripts\activate.bat
```

**Linux/macOS/Unix:**
```bash
source venv/bin/activate
```

### Deactivating the Virtual Environment

When done:
```bash
deactivate
```

## Quick Start

```bash
# Show all available targets
make help

# Build HTML documentation for a specific project
make html-rsyslog

# Build only the shared content library
make shared-html

# Build all HTML documentation
make all-html

# Build single-page HTML documentation for a specific project
make singlehtml-rsyslog

# Build single-page HTML documentation for every project
make all-singlehtml

# Build everything (all formats for all projects)
make all

# Clean all build artifacts
make clean
```

### Single-Page HTML Builds at a Glance

Single-page HTML combines an entire manual into one file—ideal for full-text
browser searches, printing, or sharing an offline copy. Use it when you need a
portable reference without the multi-page navigation scaffolding.

- `make singlehtml-<project>` builds one product's single-page manual.
- `make all-singlehtml` runs the single-page build for every project in the
  repository.
- Output is written to `build/singlehtml/<project>/index.html`.

## Available Projects

The documentation is organized into several projects:

- **eventreporter** - EventReporter documentation
- **mwagent** - MonitorWare Agent documentation
- **rsyslog** - Rsyslog documentation
- **syslogviewer** - SyslogViewer documentation
- **winsyslog** - Windows Syslog documentation
- **winsyslog-j** - Windows Syslog Java edition documentation

Each project has its own configuration and can be built independently.

## Target Reference

### General Targets

| Target | Description |
|--------|-------------|
| `help` | Show help message with all available targets |
| `all` | Build all formats for all projects |
| `clean` | Remove all build artifacts |
| `list-projects` | List all available projects |
| `shared-html` | Build HTML output for the shared content library |
| `test-build` | Quick test build (builds winsyslog HTML) |
| `migration-guide` | Show migration guide from old shell scripts |

### Shared Content Workflow

- Use `make shared-html` to validate changes made under `source/shared/` without
  rebuilding every product manual. This runs `sphinx-build -b html` directly on
  the shared content tree with a lightweight configuration so you can spot
  syntax or include issues quickly.
- `make html-<project>` and `make singlehtml-<project>` automatically rebuild
  the shared library first. This guarantees that any shared topic edits are
  incorporated before the product-specific build begins—no extra steps are
  required once you're ready to test a single manual end-to-end.
- `make all-html` (or `make all`) remains the best choice for pre-release
  validation when you need to confirm every deliverable, but it's no longer
  required for quick checks on shared material.

### Format-Specific Targets

| Target Pattern | Description | Example |
|----------------|-------------|---------|
| `html-<project>` | Build HTML for specific project | `make html-rsyslog` |
| `singlehtml-<project>` | Build single-page HTML for specific project | `make singlehtml-rsyslog` |
| `htmlhelp-<project>` | Build HTMLHelp (CHM) for specific project | `make htmlhelp-winsyslog` |
| `pdf-<project>` | Build PDF for specific project | `make pdf-mwagent` |

### Batch Build Targets

| Target | Description |
|--------|-------------|
| `all-html` | Build HTML for all projects |
| `all-singlehtml` | Build single-page HTML for all projects |
| `all-htmlhelp` | Build HTMLHelp for all projects |
| `all-pdf` | Build PDF for all projects |

### Quality Assurance Targets

| Target | Description |
|--------|-------------|
| `linkcheck` | Check external links for all projects |
| `linkcheck-<project>` | Check links for specific project |
| `spelling` | Run spell check (requires sphinxcontrib-spelling) |
| `validate` | Run all validation checks |
| `preview` | Start local HTTP server to preview HTML builds |

## Features

### Cross-Platform Support

The Makefile automatically detects the operating system and adjusts commands accordingly:
- **Windows**: Uses appropriate path separators and commands
- **Linux/macOS**: Uses Unix-style commands
- **WSL**: Automatically detects Windows tools like `hhc.exe`

### Virtual Environment Support

The Makefile automatically detects and uses Sphinx from:
1. Virtual environment (`venv/bin/sphinx-build` or `venv/Scripts/sphinx-build.exe`)
2. System installation

### Parallel Builds

All builds use `-j auto` for automatic parallelization, significantly speeding up the build process.

### Strict Error Checking

Builds use `-W --keep-going` options to treat warnings as errors while continuing to show all issues.

### Colorized Output

On supported terminals, the output includes color-coded messages:
- 🔵 Blue: Information and build starts
- 🟢 Green: Success messages
- 🟡 Yellow: Warnings
- 🔴 Red: Errors

## Migration from Shell Scripts

### Script Replacement Map

| Old Script | New Command |
|------------|-------------|
| `build-all-html.sh` | `make all-html` |
| `build-all-htmlhelp.sh` | `make all-htmlhelp` |
| `build-all-pdf.sh` | `make all-pdf` |
| `build-cleanup.sh` | `make clean` |
| `build-<project>-html.sh` | `make html-<project>` |
| `build-<project>-htmlhelp.sh` | `make htmlhelp-<project>` |
| `build-<project>-pdf.sh` | `make pdf-<project>` |

### Removing Old Scripts

After verifying the new Makefile works correctly:

```bash
git rm build-*.sh
git commit -m "Remove old build scripts, replaced by Makefile"
```

## Build Directory Structure

```
build/
├── html/           # HTML output
│   ├── eventreporter/
│   ├── mwagent/
│   ├── rsyslog/
│   ├── shared/     # Shared content preview build
│   └── ...
├── chm/            # HTMLHelp working directories
│   └── <project>/
├── pdf/            # PDF output
│   └── <project>/
├── linkcheck/      # Link check results
│   └── <project>/
├── spelling/       # Spell check results
│   └── <project>/
└── *.chm          # Compiled CHM files (copied from chm/)
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
If the virtual environment already exists, the setup script will inform you and exit. You can:
- Use the existing environment (recommended)
- Delete the `venv` directory and run the setup script again

### Make Warnings about .PHONY

The Makefile properly handles phony targets by:
- Not using `.PHONY` with pattern rules (e.g., `html-%`)
- Instead, explicitly declaring each generated target as phony using `foreach`
- This avoids GNU Make warnings while ensuring targets always rebuild

### "sphinx-build not found"

This usually means the virtual environment is not activated or Sphinx is not installed:

1. **Activate the virtual environment:**
   ```bash
   # Windows:
   venv\Scripts\activate.bat
   # Linux/macOS:
   source venv/bin/activate
   ```

2. **Install Sphinx:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   which sphinx-build  # Linux/macOS
   where sphinx-build  # Windows
   ```

### "HTML Help Compiler not found"

- **Windows**: Install HTML Help Workshop and ensure `hhc.exe` is on your `PATH`
  or set the `HHC` environment variable to the full path.
- **Linux**: HTMLHelp builds will skip CHM compilation (HTML files are still
  generated) unless you provide an `HHC` path via Wine.
- **WSL**: Set `HHC=/mnt/c/Program\ Files\ (x86)/HTML\ Help\ Workshop/hhc.exe`
  before invoking `make htmlhelp-<project>`.
  The repository no longer ships `htmlhelp.exe` directly.

### Build Warnings/Errors

The build system treats warnings as errors. To see all issues:
- The `-W --keep-going` options ensure all problems are shown
- Check the build output for specific error messages
- Run `make linkcheck-<project>` to check for broken links

## Advanced Usage

### Building Specific Formats

```bash
# Build only HTML for rsyslog
make html-rsyslog

# Build PDF for all projects
make all-pdf

# Build everything for eventreporter
make html-eventreporter htmlhelp-eventreporter pdf-eventreporter
```

### Continuous Integration

The Makefile is integrated with GitHub Actions for automated builds on pull requests. The workflow:

1. Sets up Python environment
2. Installs dependencies
3. Builds all HTML documentation with strict error checking (`make all-html SPHINXOPTS="-W"`)

See `.github/workflows/pr-build-docs.yml` for the complete workflow configuration.

Example usage in CI/CD pipelines:

```yaml
# Build all HTML documentation with warnings as errors
- name: Build Documentation
  run: make all-html SPHINXOPTS="-W"

# Run quality checks
- name: Check Links
  run: make linkcheck

# Build specific format
- name: Build PDFs
  run: make all-pdf
```

### Preview Server

After building HTML documentation:

```bash
make preview
# Opens http://localhost:8000 in your browser
```

## Contributing

When adding new projects:

1. Create the project directory with `conf.py`
2. Add the project name to the `PROJECTS` variable in the Makefile
3. Test with `make html-<newproject>`

## Support

For issues or questions:
- Check the build output for specific error messages
- Run `make help` for available options
- Run `make migration-guide` for migration assistance