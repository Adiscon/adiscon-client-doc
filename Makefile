# =============================================================================
# Adiscon Documentation Build System Makefile
# =============================================================================
# This Makefile replaces all individual build-*.sh scripts with a unified
# build system that supports multiple projects and output formats.
#
# Usage:
#   make help                    - Show available targets
#   make all                     - Build all formats for all projects
#   make html-rsyslog           - Build HTML for rsyslog
#   make all-html               - Build HTML for all projects
#   make clean                  - Remove all build artifacts
#
# =============================================================================

# -----------------------------------------------------------------------------
# Platform Detection
# -----------------------------------------------------------------------------
ifeq ($(OS),Windows_NT)
    DETECTED_OS := Windows
    PATH_SEP := :
    NULL_DEVICE := /dev/null
    MKDIR := mkdir -p
    RM := rm -f
    RMDIR := rm -rf
    CP := cp
    # Use bash shell on Windows for compatibility with existing commands
    SHELL := C:/Program Files/Git/usr/bin/sh.exe
else
    DETECTED_OS := $(shell uname -s)
    PATH_SEP := :
    NULL_DEVICE := /dev/null
    MKDIR := mkdir -p
    RM := rm -f
    RMDIR := rm -rf
    CP := cp
endif

# -----------------------------------------------------------------------------
# Build Tool Configuration
# -----------------------------------------------------------------------------

# Try to use virtual environment sphinx-build first
ifeq ($(DETECTED_OS),Windows)
    ifneq ($(wildcard venv/Scripts/sphinx-build.exe),)
        SPHINXBUILD := venv/Scripts/sphinx-build.exe
    else ifneq ($(wildcard venv/Scripts/sphinx-build),)
        SPHINXBUILD := venv/Scripts/sphinx-build
    else ifneq ($(wildcard ./sphinx-build),)
        SPHINXBUILD := ./sphinx-build
    else
        SPHINXBUILD := sphinx-build
    endif
else
    ifneq ($(wildcard venv/bin/sphinx-build),)
        SPHINXBUILD := venv/bin/sphinx-build
    else ifneq ($(wildcard ./sphinx-build),)
        SPHINXBUILD := ./sphinx-build
    else
        SPHINXBUILD := sphinx-build
    endif
endif

# HTML Help Compiler configuration
# Respect a user-provided HHC path first
ifdef HHC
    override HHC := $(HHC)
else ifeq ($(DETECTED_OS),Windows)
    HHC := hhc.exe
else
    HHC := $(shell command -v hhc.exe 2>/dev/null)
    ifeq ($(HHC),)
        HHC := $(shell command -v hhc 2>/dev/null)
    endif
    ifeq ($(HHC),)
        # Try common Wine/WSL installation path
        ifneq ($(wildcard /mnt/c/Program Files (x86)/HTML Help Workshop/hhc.exe),)
            HHC := "/mnt/c/Program Files (x86)/HTML Help Workshop/hhc.exe"
        endif
    endif
endif

# -----------------------------------------------------------------------------
# Project Configuration
# -----------------------------------------------------------------------------
PROJECTS := eventreporter mwagent rsyslog syslogviewer winsyslog winsyslog-j
DEFAULT_PROJECTS := eventreporter mwagent rsyslog winsyslog winsyslog-j

# Directories
SOURCEDIR := source
SHAREDDIR := $(SOURCEDIR)/shared
BUILDDIR := build

# Sphinx options
# Use ?= to allow overriding from command line
SPHINXOPTS ?= -W --keep-going

# Python warning filters
PYTHONWARNINGS_IGNORE := ignore:The alias 'sphinx.util.progress_message' is deprecated
ifeq ($(strip $(PYTHONWARNINGS)),)
    export PYTHONWARNINGS := $(PYTHONWARNINGS_IGNORE)
else
    export PYTHONWARNINGS := $(PYTHONWARNINGS),$(PYTHONWARNINGS_IGNORE)
endif
# Parallel jobs only for PDF builds
# Note: rst2pdf extension may not be safe for parallel execution in HTML/HTMLHelp builds
SPHINXJOBS := -j auto

# Colors for output (if supported)
ifneq ($(DETECTED_OS),Windows)
    COLOR_RESET := \033[0m
    COLOR_GREEN := \033[32m
    COLOR_YELLOW := \033[33m
    COLOR_RED := \033[31m
    COLOR_BLUE := \033[34m
else
    COLOR_RESET :=
    COLOR_GREEN :=
    COLOR_YELLOW :=
    COLOR_RED :=
    COLOR_BLUE :=
endif

# -----------------------------------------------------------------------------
# Default Target
# -----------------------------------------------------------------------------
.DEFAULT_GOAL := help

# -----------------------------------------------------------------------------
# Help Target
# -----------------------------------------------------------------------------
.PHONY: help
help:
	@echo "$(COLOR_BLUE)=============================================================================$(COLOR_RESET)"
	@echo "$(COLOR_BLUE)Adiscon Documentation Build System$(COLOR_RESET)"
	@echo "$(COLOR_BLUE)=============================================================================$(COLOR_RESET)"
	@echo ""
	@echo "$(COLOR_GREEN)Available targets:$(COLOR_RESET)"
	@echo ""
	@echo "  $(COLOR_YELLOW)General Targets:$(COLOR_RESET)"
	@echo "    help                 - Show this help message"
	@echo "    all                  - Build all formats for all projects"
	@echo "    clean                - Remove all build artifacts"
	@echo "    list-projects        - List all available projects"
	@echo "    shared-html          - Build HTML for shared content library"
	@echo "    test-build           - Build winsyslog HTML for testing"
	@echo "    validate             - Run validation checks on documentation"
	@echo ""
	@echo "  $(COLOR_YELLOW)HTML Targets:$(COLOR_RESET)"
	@echo "    html-<project>       - Build HTML for specific project"
	@echo "    singlehtml-<project> - Build single-page HTML for specific project"
	@echo "    all-html             - Build HTML for all projects"
	@echo "    all-singlehtml       - Build single-page HTML for all projects"
	@echo ""
	@echo "  $(COLOR_YELLOW)HTMLHelp Targets:$(COLOR_RESET)"
	@echo "    htmlhelp-<project>   - Build HTMLHelp (CHM) for specific project"
	@echo "    all-htmlhelp         - Build HTMLHelp for all projects"
	@echo ""
	@echo "  $(COLOR_YELLOW)PDF Targets:$(COLOR_RESET)"
	@echo "    pdf-<project>        - Build PDF for specific project"
	@echo "    all-pdf              - Build PDF for all projects"
	@echo ""
	@echo "  $(COLOR_YELLOW)Quality Assurance:$(COLOR_RESET)"
	@echo "    linkcheck            - Check all external links"
	@echo "    linkcheck-<project>  - Check links for specific project"
	@echo "    spelling             - Run spell checking (requires sphinxcontrib-spelling)"
	@echo "    validate-rst         - Run reStructuredText linters (doc8 & rstcheck)"
	@echo "    preview              - Start local server to preview HTML builds"
	@echo ""
	@echo "$(COLOR_GREEN)Available projects:$(COLOR_RESET) $(PROJECTS)"
	@echo ""
	@echo "$(COLOR_GREEN)Examples:$(COLOR_RESET)"
	@echo "    make html-rsyslog    - Build HTML docs for rsyslog"
	@echo "    make singlehtml-rsyslog - Build single-page HTML docs for rsyslog"
	@echo "    make all-html        - Build HTML docs for all projects"
	@echo "    make clean           - Clean all build artifacts"
	@echo "    make all             - Build everything"
	@echo ""
	@echo "$(COLOR_BLUE)=============================================================================$(COLOR_RESET)"

# -----------------------------------------------------------------------------
# Utility Functions
# -----------------------------------------------------------------------------

# Function to check if project exists
define check_project
	@if [ ! -d "$(1)" ]; then \
		echo "$(COLOR_RED)Error: Project directory '$(1)' not found.$(COLOR_RESET)"; \
		exit 1; \
	fi
	@if [ ! -f "$(1)/conf.py" ]; then \
		echo "$(COLOR_RED)Error: Configuration file '$(1)/conf.py' not found.$(COLOR_RESET)"; \
		exit 1; \
	fi
endef

# Function to print build start message
define print_build_start
	@echo "$(COLOR_BLUE)Building $(2) for $(1)...$(COLOR_RESET)"
endef

# Function to print build success message
define print_build_success
	@echo "$(COLOR_GREEN)✓ $(2) build completed successfully for $(1)$(COLOR_RESET)"
endef

# -----------------------------------------------------------------------------
# Shared Content Target - HTML
# -----------------------------------------------------------------------------

.PHONY: shared-html
shared-html: FORCE
	$(call print_build_start,shared content,HTML)
	@$(MKDIR) $(BUILDDIR)/html/shared
	@$(SPHINXBUILD) -b html $(SPHINXOPTS) $(SHAREDDIR) $(BUILDDIR)/html/shared
	$(call print_build_success,shared content,HTML)

# -----------------------------------------------------------------------------
# Individual Product Targets - HTML
# -----------------------------------------------------------------------------

html-%: shared-html FORCE
	$(call check_project,$*)
	$(call print_build_start,$*,HTML)
	@$(MKDIR) $(BUILDDIR)/html/$*
	@$(SPHINXBUILD) -b html -c $* $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html/$*
	@$(CP) $(SOURCEDIR)/.htaccess.$* $(BUILDDIR)/html/$*/.htaccess
	$(call print_build_success,$*,HTML)

# -----------------------------------------------------------------------------
# Individual Product Targets - HTMLHelp
# -----------------------------------------------------------------------------

htmlhelp-%: FORCE
	$(call check_project,$*)
	$(call print_build_start,$*,HTMLHelp)
	@$(MKDIR) $(BUILDDIR)/chm/$*
	@$(SPHINXBUILD) -b htmlhelp -c $* $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/chm/$*
	@if [ -n "$(HHC)" ]; then \
		echo "$(COLOR_YELLOW)Compiling CHM file for $*...$(COLOR_RESET)"; \
		$(HHC) $(BUILDDIR)/chm/$*/*.hhp || true; \
		if [ -f $(BUILDDIR)/chm/$*/*.chm ]; then \
			$(CP) $(BUILDDIR)/chm/$*/*.chm $(BUILDDIR)/ 2>$(NULL_DEVICE) || true; \
			echo "$(COLOR_GREEN)✓ CHM file created for $*$(COLOR_RESET)"; \
		else \
			echo "$(COLOR_YELLOW)Warning: CHM file not created for $*$(COLOR_RESET)"; \
		fi \
	else \
		echo "$(COLOR_YELLOW)Warning: HTML Help Compiler not found, skipping CHM compilation$(COLOR_RESET)"; \
	fi
	$(call print_build_success,$*,HTMLHelp)

# -----------------------------------------------------------------------------
# Individual Product Targets - Single-Page HTML
# -----------------------------------------------------------------------------

singlehtml-%: shared-html FORCE
	$(call check_project,$*)
	$(call print_build_start,$*,Single-page HTML)
	@$(MKDIR) $(BUILDDIR)/singlehtml/$*
	@$(SPHINXBUILD) -b singlehtml -c $* $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/singlehtml/$*
	$(call print_build_success,$*,Single-page HTML)

# -----------------------------------------------------------------------------
# Individual Product Targets - PDF
# -----------------------------------------------------------------------------

pdf-%: FORCE
	$(call check_project,$*)
	$(call print_build_start,$*,PDF)
	@$(MKDIR) $(BUILDDIR)/pdf/$*
	@$(SPHINXBUILD) -b pdf -c $* $(SPHINXOPTS) $(SPHINXJOBS) $(SOURCEDIR) $(BUILDDIR)/pdf/$*
	$(call print_build_success,$*,PDF)

# -----------------------------------------------------------------------------
# Aggregate Targets
# -----------------------------------------------------------------------------
.PHONY: all-html all-singlehtml all-htmlhelp all-pdf all

all-html: $(addprefix html-,$(PROJECTS))
	@echo "$(COLOR_GREEN)✓ All HTML builds completed successfully$(COLOR_RESET)"

all-singlehtml: $(addprefix singlehtml-,$(PROJECTS))
	@echo "$(COLOR_GREEN)✓ All single-page HTML builds completed successfully$(COLOR_RESET)"

all-htmlhelp: $(addprefix htmlhelp-,$(PROJECTS))
	@echo "$(COLOR_GREEN)✓ All HTMLHelp builds completed successfully$(COLOR_RESET)"

all-pdf: $(addprefix pdf-,$(PROJECTS))
	@echo "$(COLOR_GREEN)✓ All PDF builds completed successfully$(COLOR_RESET)"

all: all-html all-singlehtml all-htmlhelp all-pdf
	@echo "$(COLOR_GREEN)✓ All documentation builds completed successfully$(COLOR_RESET)"

# -----------------------------------------------------------------------------
# Clean Target
# -----------------------------------------------------------------------------
.PHONY: clean
clean:
	@echo "$(COLOR_YELLOW)Cleaning build artifacts...$(COLOR_RESET)"
	@$(RMDIR) $(BUILDDIR) 2>$(NULL_DEVICE) || true
	@echo "$(COLOR_GREEN)✓ Build artifacts cleaned$(COLOR_RESET)"

# -----------------------------------------------------------------------------
# Utility Targets
# -----------------------------------------------------------------------------
.PHONY: list-projects
list-projects:
	@echo "$(COLOR_BLUE)Available projects:$(COLOR_RESET)"
	@for project in $(PROJECTS); do \
		echo "  - $$project"; \
	done

.PHONY: test-build
test-build: html-winsyslog
	@echo "$(COLOR_GREEN)✓ Test build completed$(COLOR_RESET)"

# -----------------------------------------------------------------------------
# Quality Assurance Targets
# -----------------------------------------------------------------------------
.PHONY: linkcheck spelling validate validate-rst

# Check links for all projects
linkcheck: $(addprefix linkcheck-,$(PROJECTS))
	@echo "$(COLOR_GREEN)✓ All link checks completed$(COLOR_RESET)"

# Check links for specific project
linkcheck-%: FORCE
	$(call check_project,$*)
	@echo "$(COLOR_BLUE)Checking links for $*...$(COLOR_RESET)"
	@$(MKDIR) $(BUILDDIR)/linkcheck/$*
	@$(SPHINXBUILD) -b linkcheck -c $* $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/linkcheck/$*
	@echo "$(COLOR_GREEN)✓ Link check completed for $*$(COLOR_RESET)"

# Spell checking (requires sphinxcontrib-spelling)
spelling:
	@echo "$(COLOR_BLUE)Running spell check...$(COLOR_RESET)"
	@set -e; \
	for project in $(PROJECTS); do \
		echo "$(COLOR_YELLOW)Checking $$project...$(COLOR_RESET)"; \
		$(MKDIR) $(BUILDDIR)/spelling/$$project; \
		$(SPHINXBUILD) -b spelling -c $$project $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/spelling/$$project; \
	done
	@echo "$(COLOR_GREEN)✓ Spell check completed$(COLOR_RESET)"

# Run all validation checks
validate: linkcheck spelling validate-rst
	@echo "$(COLOR_GREEN)✓ All validation checks completed$(COLOR_RESET)"

# Combined reStructuredText linting
RST_LINT_PATHS := $(SOURCEDIR) $(PROJECTS)
DOC8_MAX_LINE_LENGTH ?= 1000
RSTCHECK_IGNORE_DIRECTIVES ?= toctree,index,only,highlight
RSTCHECK_IGNORE_ROLES ?= doc,ref
RSTCHECK_IGNORE_LANGUAGES ?= none

.PHONY: validate-rst
validate-rst:
	@echo "$(COLOR_BLUE)Running doc8...$(COLOR_RESET)"
	@doc8 --max-line-length $(DOC8_MAX_LINE_LENGTH) $(RST_LINT_PATHS)
	@echo "$(COLOR_BLUE)Running rstcheck...$(COLOR_RESET)"
	@rstcheck --recursive --report-level WARNING \
	        --ignore-directives $(RSTCHECK_IGNORE_DIRECTIVES) \
	        --ignore-roles $(RSTCHECK_IGNORE_ROLES) \
	        --ignore-languages $(RSTCHECK_IGNORE_LANGUAGES) \
	        $(RST_LINT_PATHS)
	@echo "$(COLOR_GREEN)✓ reStructuredText linting completed$(COLOR_RESET)"

# -----------------------------------------------------------------------------
# Preview Target
# -----------------------------------------------------------------------------
.PHONY: preview
preview:
	@if [ -d "$(BUILDDIR)/html" ]; then \
		echo "$(COLOR_BLUE)Starting preview server...$(COLOR_RESET)"; \
		echo "$(COLOR_YELLOW)Preview available at: http://localhost:8000$(COLOR_RESET)"; \
		echo "$(COLOR_YELLOW)Press Ctrl+C to stop the server$(COLOR_RESET)"; \
		cd $(BUILDDIR)/html && python -m http.server 8000; \
	else \
		echo "$(COLOR_RED)Error: No HTML builds found. Run 'make all-html' first.$(COLOR_RESET)"; \
		exit 1; \
	fi

# -----------------------------------------------------------------------------
# Migration Guide
# -----------------------------------------------------------------------------
.PHONY: migration-guide
migration-guide:
	@echo "$(COLOR_BLUE)=============================================================================$(COLOR_RESET)"
	@echo "$(COLOR_BLUE)Migration Guide from Shell Scripts to Makefile$(COLOR_RESET)"
	@echo "$(COLOR_BLUE)=============================================================================$(COLOR_RESET)"
	@echo ""
	@echo "$(COLOR_GREEN)Script Replacements:$(COLOR_RESET)"
	@echo "  build-<project>-html.sh      → make html-<project>"
	@echo "  build-<project>-htmlhelp.sh  → make htmlhelp-<project>"
	@echo "  build-<project>-pdf.sh       → make pdf-<project>"
	@echo "  build-all-html.sh            → make all-html"
	@echo "  build-all-htmlhelp.sh        → make all-htmlhelp"
	@echo "  build-all-pdf.sh             → make all-pdf"
	@echo "  build-cleanup.sh             → make clean"
	@echo ""
	@echo "$(COLOR_GREEN)New Features:$(COLOR_RESET)"
	@echo "  - Parallel builds with -j auto"
	@echo "  - Cross-platform support (Windows/Linux/macOS)"
	@echo "  - Link checking and spell checking"
	@echo "  - Built-in preview server"
	@echo "  - Colorized output (on supported terminals)"
	@echo ""
	@echo "$(COLOR_GREEN)To remove old scripts:$(COLOR_RESET)"
	@echo "  git rm build-*.sh"
	@echo ""
	@echo "$(COLOR_BLUE)=============================================================================$(COLOR_RESET)"

# -----------------------------------------------------------------------------
# Special Targets
# -----------------------------------------------------------------------------

# Ensure SOURCEDIR exists
$(SOURCEDIR):
	@echo "$(COLOR_RED)Error: Source directory '$(SOURCEDIR)' not found$(COLOR_RESET)"
	@exit 1

# Prevent make from treating project names as files
.PHONY: $(PROJECTS)

# Mark all generated targets as phony to ensure they always rebuild
# Note: Using FORCE prerequisite instead of .PHONY for pattern rules
# .PHONY: $(foreach proj,$(PROJECTS),html-$(proj))
# .PHONY: $(foreach proj,$(PROJECTS),htmlhelp-$(proj))
# .PHONY: $(foreach proj,$(PROJECTS),pdf-$(proj))
# .PHONY: $(foreach proj,$(PROJECTS),linkcheck-$(proj))

# Force target to ensure pattern rules always execute
.PHONY: FORCE
FORCE:



# -----------------------------------------------------------------------------
# End of Makefile
# -----------------------------------------------------------------------------
