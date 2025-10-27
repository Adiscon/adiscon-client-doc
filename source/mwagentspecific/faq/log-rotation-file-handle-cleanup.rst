.. _log-rotation-file-handle-cleanup-mwagent:

Why are Logfiles sometimes not rotated in MonitorWare Agent 14.5 to 15.1?
==========================================================================

This article explains why log files may sometimes not be rotated as expected in MonitorWare Agent versions 14.5 to 15.1, and provides solutions for this issue.

Background
----------

In MonitorWare Agent versions 14.5 to 15.1, there is a feature called "Timeout until unused filehandles are closed" that can interfere with log file rotation under certain circumstances. This feature was improved in later versions to handle rotation more reliably.

The Problem
-----------

Users may experience inconsistent log file rotation behavior where:

* Some log files rotate successfully every day as scheduled
* Some log files rotate only partially (not every day)
* Some log files never rotate at all

This typically occurs when log rotation is scheduled at specific times (e.g., at 0:00 every day) or when using dynamic filenames with property replacer.

Root Cause
----------

The issue is related to MonitorWare Agent's file handle management feature, which by default:

* Caches file handles internally when dynamic filenames are used to avoid excessive file open/close operations
* Closes unused file handles after a timeout period if not used anymore
* Each write to a file resets the timeout counter for that file handle

At the time of scheduled rotation, if a log file has been inactive for an extended period, the cached file handle may be closed. When the rotation process runs, it cannot rotate a file that is no longer actively opened by MonitorWare Agent.

**Note:** This behavior is similar to how your computer closes unused programs to maintain system stability.

Affected Versions
-----------------

This issue affects MonitorWare Agent versions 14.5 to 15.1. Later versions include improvements to the file handle management and rotation logic that resolve these limitations.

Solutions
---------

**Recommended Solution: Upgrade MonitorWare Agent**

The most effective solution is to upgrade to MonitorWare Agent version 15.1 or later, where the file handle management and rotation logic have been improved to handle these scenarios properly.

**Alternative Solution: Adjust File Handle Timeout**

If upgrading is not immediately possible:

1. Open the MonitorWare Agent configuration
2. Navigate to the File Logging action settings
3. Increase the "Timeout until unused filehandles are closed" setting from the default value
4. A longer timeout (e.g., 24 hours instead of the default) will reduce the likelihood of missing log rotations

**Important:** The longer timeout interval may increase memory usage, so monitor your system's resource utilization accordingly.

**Additional Recommendations:**

* Review your dynamic filename patterns and property replacer usage
* Consider the timing of your log rotation schedules
* Monitor system resources during peak logging periods
