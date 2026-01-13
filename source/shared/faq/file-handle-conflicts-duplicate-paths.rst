:orphan:

.. _file-handle-conflicts-duplicate-paths:

Why do log files remain locked when multiple rules write to the same file?
===========================================================================

This article explains why WinSyslog, EventReporter, and MonitorWare Agent may continue to hold file handles to log files even after the configured timeout period, preventing external processes from accessing or archiving those files.

Applies To
----------

* WinSyslog
* EventReporter
* MonitorWare Agent

Problem
-------

The service continues to hold file handles to log files even after the configured timeout period has elapsed. This prevents external processes such as batch scripts or archiving tools from accessing, moving, or archiving the log files.

Symptoms
--------

* Log files remain locked after the expected release time (e.g., after 2:00 AM daily when "Create unique filenames" is enabled)
* External batch scripts fail to archive log files because files are still in use by the service
* Files are not released even hours after the timeout period has passed
* CleanFileHandlesTimeout setting appears to be ignored or ineffective
* Error messages indicating files are in use when attempting to access them

Root Cause
----------

The issue occurs when multiple file actions use identical filename templates that can reference the same physical file. This creates a conflict in file handle management:

1. Each rule's file action creates its own independent file handle tracking mechanism
2. Multiple actions hold references to the same physical file simultaneously
3. The file cannot be released until ALL actions release their handles
4. Even though CleanFileHandlesTimeout is set correctly (e.g., 7200 seconds / 2 hours), the file remains locked because different actions have different timer states and may not all reach the timeout simultaneously

Problematic Configuration Pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multiple rules using identical filename templates:

* File Path: ``log-directory\%timegenerated%``
* File Base Name: ``%source%-%timegenerated%.log``

When multiple rules match messages from the same source device, they all write to the same physical file (e.g., ``device-ip-20251012.log``). This causes handle conflicts where each action maintains its own handle to the same file.

Example of the Issue
^^^^^^^^^^^^^^^^^^^^^

* Rule 1: Filter matches source "device-hostname" OR source "192.168.1.100" - File Action writes to ``device-ip-20251012.log``
* Rule 2: Filter matches source "device-hostname" OR source "192.168.1.100" - File Action writes to ``device-ip-20251012.log`` (SAME FILE!)
* Rule 3-N: Same pattern with different filters but identical file action configuration

Solution
--------

Option 1: Consolidate Rules with Identical File Actions (Recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instead of having multiple separate rules with identical file action configurations, consolidate them into ONE rule with all filter conditions combined. This ensures only one file action object manages each file.

Steps:

1. Create a new rule (e.g., "All Devices Combined")
2. Use Copy & Paste functions in the configuration client to combine filters from all existing rules:

   * For each existing rule:

     * Navigate to the rule
     * Go to Filters tab
     * Find the filter group for that rule
     * RIGHT-CLICK on the filter block (usually an AND or OR block)
     * Select "Copy"

   * Navigate to your new "All Devices Combined" rule
   * Go to Filters tab
   * RIGHT-CLICK on the top-level OR filter
   * Select "Paste" (or "Paste as child")
   * The entire filter block is now copied into your new rule
   * Repeat this process for all existing rules

3. Configure the file action once in the new combined rule
4. Delete the other rules so that only a single File Action remains

**Result:** Only ONE file action object manages each file, eliminating handle conflicts completely.

Option 2: Use Unique File Paths for Each Rule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you need to keep separate rules for organizational purposes, ensure each rule writes to a unique file location:

* Organize logs into separate subdirectories by device type, rule name, or other categorization
* Use different filename patterns for each rule
* Ensure no two rules can write to the same physical file under any circumstances

Example Configuration:

* Rule 1: File Path: ``log-directory\devices\type1\%timegenerated%``
* Rule 2: File Path: ``log-directory\devices\type2\%timegenerated%``
* Rule 3: File Path: ``log-directory\devices\type3\%timegenerated%``

Each rule writes to a completely separate directory structure, preventing any possibility of file handle conflicts.

Best Practices
--------------

* Each rule should write to a unique file location to avoid handle conflicts
* Consolidate rules with identical file action configurations into a single rule when possible
* Use the Copy & Paste functions in the configuration client to efficiently combine filter conditions from multiple rules
* When using "Create unique filenames" for daily rotation, ensure file paths are unique per rule
* Test file release behavior after configuration changes to verify files are released as expected
* Monitor file handles using Windows Resource Monitor or Process Explorer to verify proper release
* Verify that external batch scripts or archiving processes can access files after the timeout period

Verification
------------

After implementing the solution:

1. Monitor file handles using Windows Resource Monitor or Process Explorer to confirm files are released after the CleanFileHandlesTimeout period
2. Verify configuration using the configuration client's verification feature - it should report 0 errors related to duplicate filenames

If files are still not released after the timeout period, check for:

* Other file actions or rules that may be holding references to the same files
* Additional processes that may be accessing the files
* Configuration errors that may have been missed during the consolidation process
