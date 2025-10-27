# Documentation Article Creation Prompt Template

## Variables Section
Fill in these variables at the top - they will be used throughout the prompt:

**ARTICLE_TYPE** = [FAQ Article | Step-by-Step Guide | Technical Article | Troubleshooting Guide | Best Practices Guide | Configuration Guide | Reference Documentation]

**SUPPORT_REQUEST** = [Original support request or question if applicable - leave empty if not relevant]

**SUPPORT_ANSWER** = [Original support answer or solution if applicable - leave empty if not relevant]

**ARTICLE_TITLE** = [Clear, descriptive title following Adiscon documentation conventions]

**AUTHOR_NAME** = [Your name or "adiscon team"]

**CREATED_DATE** = [Creation date in YYYY-MM-DD format]

**UPDATED_DATE** = [Last update date in YYYY-MM-DD format]

**APPLICABLE_PRODUCTS** = [List of relevant products: EventReporter, MonitorWare Agent, WinSyslog, Rsyslog Windows Agent, etc.]

**ARTICLE_DESCRIPTION** = [Brief description of what the article covers]

**CONTENT_OUTLINE** = [Specific content structure for your article type]

**FILE_PATH** = [Target file path in the documentation structure]

**REFERENCE_LABEL** = [RST reference label for cross-references, e.g., descriptive-label]

## Article Type Selection
Choose the type of documentation article you want to create:

1. **FAQ Article** - Addresses specific questions, problems, or common issues
2. **Step-by-Step Guide** - Provides detailed procedural instructions
3. **Technical Article** - Explains concepts, features, or how things work
4. **Troubleshooting Guide** - Helps diagnose and resolve specific problems
5. **Best Practices Guide** - Recommends optimal approaches and methodologies
6. **Configuration Guide** - Explains how to set up and configure features
7. **Reference Documentation** - Detailed technical specifications and parameters

## Prompt Template

```
Create a **{{ARTICLE_TYPE}}** for the Adiscon product documentation.

**Context Information:**
**{{SUPPORT_REQUEST}}** - Insert the original support request or question here if applicable
**{{SUPPORT_ANSWER}}** - Insert the original support answer or solution here if applicable

**Article Requirements:**

1. **Title:** {{ARTICLE_TITLE}}
   - Use title case
   - Include relevant product names (EventReporter, MonitorWare Agent, WinSyslog, Rsyslog Windows Agent)
   - Be specific about the topic or problem being addressed

2. **Metadata:**
   - Author: {{AUTHOR_NAME}}
   - Created/Updated dates: {{CREATED_DATE}} / {{UPDATED_DATE}}
   - Applicable products: {{APPLICABLE_PRODUCTS}}

3. **Content Structure:**
   {{CONTENT_OUTLINE}}

   For FAQ Articles:
   - Start with the question or problem statement
   - Provide clear, direct answer
   - Include step-by-step resolution if applicable
   - Add notes, warnings, or additional context as needed

   For Step-by-Step Guides:
   - Include numbered steps with clear actions
   - Add screenshots or code examples where helpful
   - Include prerequisites and requirements
   - Add verification steps and troubleshooting tips

   For Technical Articles:
   - Explain the concept or feature clearly
   - Provide examples and use cases
   - Include technical details and parameters
   - Reference related documentation

   For Troubleshooting Guides:
   - Describe the problem/symptom
   - List possible causes
   - Provide systematic diagnosis steps
   - Offer solutions for each cause

4. **Documentation Standards:**
   - Use proper RST (reStructuredText) formatting
   - Include cross-references using `:doc:` directive
   - Add images with proper paths (../images/filename.png)
   - Use appropriate admonitions (note, warning, important, tip)
   - Follow existing documentation patterns and terminology

5. **SEO and Navigation:**
   - Include reference label (`.. _{{REFERENCE_LABEL}}:`)
   - Use descriptive section headers
   - Include relevant keywords for search

**Additional Instructions:**
- Ensure technical accuracy and consistency with existing documentation
- Use clear, professional language appropriate for technical users
- Include practical examples when possible
- Consider edge cases and error conditions
- Reference related articles and documentation sections

**File Placement:**
- FAQ articles: `/source/shared/faq/`
- Step-by-step guides: `/source/step-by-step/` or `/source/eventreporterspecific/stepbystepguides.rst`
- Technical articles: `/source/articles/`
- Product-specific guides: Appropriate product subdirectory
- Specific path: {{FILE_PATH}}
```

## Usage Instructions

1. **Fill in Variables:** Fill in all the variables in the "Variables Section" at the top of this template
2. **Select Article Type:** Choose the most appropriate type from the options above (this will be used for the ARTICLE_TYPE variable)
3. **Customize Content Outline:** Based on your chosen article type, customize the CONTENT_OUTLINE variable with specific structure details
4. **Set File Path:** Determine the appropriate FILE_PATH for your article type and target location
5. **Review Variables:** Double-check all variables are filled in correctly - the prompt will use these values throughout
6. **Generate Documentation:** Use the completed prompt template with all variables filled in

## Example Filled Template

**Variables Section Example:**

**ARTICLE_TYPE** = Step-by-Step Guide

**SUPPORT_REQUEST** = How do I configure MonitorWare Agent to forward logs to a remote syslog server?

**SUPPORT_ANSWER** = You need to create a Send Syslog action in MonitorWare Agent and configure the destination server details.

**ARTICLE_TITLE** = How to Configure MonitorWare Agent to Forward Logs to a Remote Syslog Server

**AUTHOR_NAME** = adiscon team

**CREATED_DATE** = 2024-01-15

**UPDATED_DATE** = 2024-01-15

**APPLICABLE_PRODUCTS** = MonitorWare Agent

**ARTICLE_DESCRIPTION** = This step-by-step guide explains how to configure MonitorWare Agent to forward logs to a remote syslog server.

**CONTENT_OUTLINE** = **Prerequisites:** MonitorWare Agent installed and running, Network connectivity to target syslog server, Appropriate firewall rules configured. **Step 1:** Access the Configuration Client. **Step 2:** Create a New Rule. **Step 3:** Add Send Syslog Action. **Step 4:** Configure Additional Settings. **Step 5:** Save and Apply. **Verification:** Check logs on target syslog server.

**FILE_PATH** = /source/mwagentspecific/

**REFERENCE_LABEL** = configure-remote-syslog

```
Create a **Step-by-Step Guide** for the Adiscon product documentation.

**Context Information:**
**How do I configure MonitorWare Agent to forward logs to a remote syslog server?** - Insert the original support request or question here if applicable
**You need to create a Send Syslog action in MonitorWare Agent and configure the destination server details.** - Insert the original support answer or solution here if applicable

**Article Requirements:**

1. **Title:** How to Configure MonitorWare Agent to Forward Logs to a Remote Syslog Server
   - Use title case
   - Include relevant product names (EventReporter, MonitorWare Agent, WinSyslog, Rsyslog Windows Agent)
   - Be specific about the topic or problem being addressed

2. **Metadata:**
   - Author: adiscon team
   - Created/Updated dates: 2024-01-15 / 2024-01-15
   - Applicable products: MonitorWare Agent

3. **Content Structure:**
   **Prerequisites:** MonitorWare Agent installed and running, Network connectivity to target syslog server, Appropriate firewall rules configured. **Step 1:** Access the Configuration Client. **Step 2:** Create a New Rule. **Step 3:** Add Send Syslog Action. **Step 4:** Configure Additional Settings. **Step 5:** Save and Apply. **Verification:** Check logs on target syslog server.

   For FAQ Articles:
   - Start with the question or problem statement
   - Provide clear, direct answer
   - Include step-by-step resolution if applicable
   - Add notes, warnings, or additional context as needed

   For Step-by-Step Guides:
   - Include numbered steps with clear actions
   - Add screenshots or code examples where helpful
   - Include prerequisites and requirements
   - Add verification steps and troubleshooting tips

4. **Documentation Standards:**
   - Use proper RST (reStructuredText) formatting
   - Include cross-references using `:doc:` directive
   - Add images with proper paths (../images/filename.png)
   - Use appropriate admonitions (note, warning, important, tip)
   - Follow existing documentation patterns and terminology

5. **SEO and Navigation:**
   - Include reference label (`.. _configure-remote-syslog:`)
   - Use descriptive section headers
   - Include relevant keywords for search

**File Placement:**
- FAQ articles: `/source/shared/faq/`
- Step-by-step guides: `/source/step-by-step/` or `/source/eventreporterspecific/stepbystepguides.rst`
- Technical articles: `/source/articles/`
- Product-specific guides: Appropriate product subdirectory
- Specific path: /source/mwagentspecific/
```