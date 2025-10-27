#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Adiscon Documentation Build Environment${NC}"
echo -e "${BLUE}========================================${NC}"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}ERROR: Python 3 is not installed or not in PATH${NC}"
    echo "Please install Python 3.x from https://python.org"
    exit 1
fi

echo -e "${GREEN}Python found:${NC}"
python3 --version
echo

# Check if virtual environment already exists
if [ -f "venv/bin/activate" ]; then
    echo -e "${YELLOW}Virtual environment already exists.${NC}"
    echo
    echo "To activate it, run:"
    echo "  source venv/bin/activate"
    echo
    echo "To deactivate it, run:"
    echo "  deactivate"
    echo
    exit 0
fi

# Create virtual environment
echo -e "${BLUE}Creating virtual environment...${NC}"
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo -e "${RED}ERROR: Failed to create virtual environment${NC}"
    exit 1
fi

# Activate virtual environment
echo -e "${BLUE}Activating virtual environment...${NC}"
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo -e "${RED}ERROR: Failed to activate virtual environment${NC}"
    exit 1
fi

# Upgrade pip
echo -e "${BLUE}Upgrading pip...${NC}"
python -m pip install --upgrade pip
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}WARNING: Failed to upgrade pip, continuing anyway...${NC}"
fi

# Install pinned documentation toolchain
if [ -f "requirements.txt" ]; then
    echo -e "${BLUE}Installing documentation requirements...${NC}"
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo -e "${RED}ERROR: Failed to install requirements from requirements.txt${NC}"
        exit 1
    fi
else
    echo -e "${YELLOW}WARNING: requirements.txt not found. Skipping dependency installation.${NC}"
fi

echo
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Setup completed successfully!${NC}"
echo -e "${GREEN}========================================${NC}"
echo
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo
echo "To build documentation, run:"
echo "  make html-winsyslog"
echo "  make html-rsyslog"
echo "  make html-mwagent"
echo "  make html-eventreporter"
echo "  make html-syslogviewer"
echo
echo "To deactivate the virtual environment, run:"
echo "  deactivate"
echo 