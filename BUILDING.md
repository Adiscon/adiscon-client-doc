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
1. Clone the repository
   ```bash
   git clone [repository-url]
   ```
2. Change into the project folder
   ```bash
   cd [repository-folder]
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

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
