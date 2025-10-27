#!/bin/bash

# =============================================================================
# Configuration file for Adiscon Documentation Build System
# =============================================================================

# -----------------------------------------------------------------------------
# Build Tool Paths
# -----------------------------------------------------------------------------

# Sphinx Build Executable
# Try to use the virtual environment sphinx-build first, then fallback to system
if [ -f "venv/Scripts/sphinx-build.exe" ]; then
    SPHINX_BUILD="venv/Scripts/sphinx-build.exe"
elif [ -f "venv/bin/sphinx-build" ]; then
    SPHINX_BUILD="venv/bin/sphinx-build"
elif command -v sphinx-build >/dev/null 2>&1; then
    SPHINX_BUILD="sphinx-build"
else
    echo "Error: sphinx-build not found. Please install Sphinx or activate the virtual environment."
    exit 1
fi

# HTML Help Compiler (for Windows HTMLHelp builds)
if [ -n "${HHC:-}" ]; then
    HHC="$HHC"
elif command -v hhc.exe >/dev/null 2>&1; then
    HHC="$(command -v hhc.exe)"
elif command -v hhc >/dev/null 2>&1; then
    HHC="$(command -v hhc)"
elif [ -f "/mnt/c/Program Files (x86)/HTML Help Workshop/hhc.exe" ]; then
    HHC="/mnt/c/Program Files (x86)/HTML Help Workshop/hhc.exe"
else
    echo "Warning: HTML Help Compiler (hhc.exe) not found. Install HTML Help Workshop and set the HHC environment variable if needed."
    HHC=""
fi

# -----------------------------------------------------------------------------
# Project Configuration
# -----------------------------------------------------------------------------

# All available projects
ALL_PROJECTS=("eventreporter" "mwagent" "rsyslog" "syslogviewer" "winsyslog" "winsyslog-j")

# Default projects to build (excluding syslogviewer if needed)
DEFAULT_PROJECTS=("eventreporter" "mwagent" "rsyslog" "winsyslog" "winsyslog-j")

# -----------------------------------------------------------------------------
# Build Directories
# -----------------------------------------------------------------------------

# Source directory for all documentation
SOURCE_DIR="source"

# Base build directory
BUILD_DIR="build"

# -----------------------------------------------------------------------------
# Theme Configuration
# -----------------------------------------------------------------------------

# Default HTML theme (now using Furo for all projects)
HTML_THEME="furo"

# -----------------------------------------------------------------------------
# Build Options
# -----------------------------------------------------------------------------

# Sphinx build options
SPHINX_OPTS="-W --keep-going"  # Treat warnings as errors but keep going

# Parallel build jobs (adjust based on your system)
SPHINX_JOBS="auto"

# -----------------------------------------------------------------------------
# Utility Functions
# -----------------------------------------------------------------------------

# Function to check if a project exists
check_project() {
    local project="$1"
    if [ ! -d "$project" ]; then
        echo "Error: Project directory '$project' not found."
        return 1
    fi
    if [ ! -f "$project/conf.py" ]; then
        echo "Error: Configuration file '$project/conf.py' not found."
        return 1
    fi
    return 0
}

# Function to create build directory if it doesn't exist
ensure_build_dir() {
    local build_path="$1"
    if [ ! -d "$build_path" ]; then
        mkdir -p "$build_path"
        if [ $? -ne 0 ]; then
            echo "Error: Failed to create build directory '$build_path'"
            return 1
        fi
    fi
    return 0
}

# Function to print build information
print_build_info() {
    echo "=============================================================================="
    echo "Adiscon Documentation Build Configuration"
    echo "=============================================================================="
    echo "Sphinx Build: $SPHINX_BUILD"
    echo "HTML Help Compiler: ${HHC:-"Not found"}"
    echo "Source Directory: $SOURCE_DIR"
    echo "Build Directory: $BUILD_DIR"
    echo "Default Theme: $HTML_THEME"
    echo "Available Projects: ${ALL_PROJECTS[*]}"
    echo "=============================================================================="
}

# -----------------------------------------------------------------------------
# Validation
# -----------------------------------------------------------------------------

# Validate sphinx-build executable
if [ ! -x "$(command -v $SPHINX_BUILD)" ]; then
    echo "Error: Sphinx build executable '$SPHINX_BUILD' is not executable or not found."
    exit 1
fi

# Validate source directory
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' not found."
    exit 1
fi

# Create base build directory if it doesn't exist
ensure_build_dir "$BUILD_DIR"

# -----------------------------------------------------------------------------
# Export Variables
# -----------------------------------------------------------------------------

export SPHINX_BUILD
export HHC
export SOURCE_DIR
export BUILD_DIR
export HTML_THEME
export SPHINX_OPTS
export SPHINX_JOBS

# Export project arrays (for scripts that need them)
export ALL_PROJECTS
export DEFAULT_PROJECTS

# -----------------------------------------------------------------------------
# Success Message
# -----------------------------------------------------------------------------

if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
    # Script is being run directly, not sourced
    print_build_info
    echo "✓ Configuration loaded successfully"
else
    # Script is being sourced
    echo "✓ Configuration loaded: $SPHINX_BUILD"
fi 