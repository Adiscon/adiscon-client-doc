# Analysis of the Adiscon Documentation Structure

## 1. High-Level Overview

This document outlines the current structure of the Adiscon documentation project. The content is organized into a mix of general categories and product-specific folders. A significant portion of the documentation, especially concerning core concepts, is shared across multiple products. The primary products covered are **WinSyslog**, **EventReporter**, **MonitorWare Agent**, **Rsyslog Windows Agent**, and **SyslogViewer**.

## 2. Core Technical Concepts

The documentation is built around a set of core technical concepts that are fundamental to how most of the products operate. These are:
* **Services:** These are the data inputs or listeners (e.g., Syslog Server, File Monitor). They collect information.
* **Rule Engine & Filter Conditions:** This is the processing core. It allows users to create rules to match specific events or data patterns.
* **Actions:** These are the outputs or event handlers (e.g., Write to File, Forward via Syslog). They define what happens when a rule is matched.
* **Property Engine:** A system that makes message properties (like source IP, message text, severity) available for use in filters and actions.

## 3. Documentation Categories

The following is a breakdown of the main content categories found in the `source/` directory and an analysis of their scope.

| Category Directory | Purpose | Scope | File Count |
| --- | --- | --- | --- |
| `introduction/` | General introductions, features, and system requirements. | **Shared** (with product-specific files) | 5 .rst files |
| `gettingstarted/` | Hands-on tutorials and step-by-step guides for common tasks. | **Shared** | 23 .rst files |
| `step-by-step/` | Additional step-by-step guides for specific procedures. | **Shared** | 1 .rst file |
| `monitorwareconcepts.rst` | High-level explanation of the core MonitorWare architecture. | **Shared** | Root-level file |
| `references/` | Technical references, property lists, error codes, etc. | **Shared** | 40 .rst files |
| `faq/` | Frequently Asked Questions. | **Shared** | 4 .rst files |
| `articles/` | In-depth articles on specific use cases or features. | **Shared** | 5 .rst files |
| `glossaryofterms/` | Definitions of technical terms. | **Shared** | 35 .rst files |
| `producttour/` | Product feature demonstrations and walkthroughs. | **Shared** | 38 .rst files |
| `winsyslogspecific/` | Content unique to the WinSyslog product. | **Product-Specific** (WinSyslog) | 40 .rst files |
| `eventreporterspecific/` | Content unique to the EventReporter product. | **Product-Specific** (EventReporter) | 28 .rst files |
| `rsyslogwaspecific/` | Content unique to the Rsyslog Windows Agent. | **Product-Specific** (Rsyslog WA) | 27 .rst files |
| `interactivesyslogviewer/` | Manual for the Interactive SyslogViewer tool. | **Product-Specific** (SyslogViewer) | 15 .rst files |
| `mwagentspecific/` | MonitorWare Agent-specific configuration and features. | **Product-Specific** (MonitorWare Agent) | 94 .rst files |

## 4. Notable Observations

### 4.1 MonitorWare Agent Structure
MonitorWare Agent now uses the `mwagentspecific/` directory, aligning with the naming convention already in place for other products. This folder contains the largest collection of documentation files (94 .rst files) and serves as the central hub for MonitorWare Agent-specific configuration details.

### 4.2 Content Distribution
- **Shared Content:** ~60 .rst files across shared directories (introduction, gettingstarted, step-by-step, references, faq, articles, glossaryofterms, producttour)
- **Product-Specific Content:** ~204 .rst files across product-specific directories
  - MonitorWare Agent: 94 .rst files (`mwagentspecific/`)
  - WinSyslog: 40 .rst files (`winsyslogspecific/`)
  - EventReporter: 28 .rst files (`eventreporterspecific/`)
  - Rsyslog WA: 27 .rst files (`rsyslogwaspecific/`)
  - SyslogViewer: 15 .rst files (`interactivesyslogviewer/`)
- **Total:** 367 .rst files across the entire documentation

### 4.3 Architectural Foundation
The documentation structure reflects the MonitorWare architecture with its core concepts of Services, Filter Conditions, Actions, and Rules. This architecture is shared across most products in the Adiscon portfolio, explaining why so much content can be reused.

## 5. Summary

The current structure relies on a combination of shared folders and product-specific folders. This leads to a scattered content architecture where related configurations and guides are not logically grouped. The `mwagentspecific/` directory serves as a de facto shared configuration reference, containing detailed documentation for services, actions, and filters that are applicable across multiple products. The upcoming refactoring in Issue #4 aims to address this by creating a centralized shared content repository that each product's documentation can reference, thereby eliminating redundancy and improving maintainability.

## 6. Shared Content Migration Notes

To keep cross-manual references stable while migrating shared topics, a
dedicated helper file now lives at ``source/shared/supporting-labels.rst``.
It adds the canonical label sources to a hidden toctree so every build parses
their targets. **Every shared page that references those labels must begin
with** ``.. include:: ../shared/supporting-labels.rst`` (pages stored at the
root of ``source/`` can use ``.. include:: /shared/supporting-labels.rst``).

Whenever a new reusable label is introduced, add the document to the hidden
toctree in ``supporting-labels.rst``. Keeping that helper list current prevents
undefined-reference warnings when content moves between manuals.
