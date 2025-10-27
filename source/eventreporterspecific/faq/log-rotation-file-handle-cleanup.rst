.. _log-rotation-file-handle-cleanup-eventreporter:


Why are Logfiles sometimes not rotated in EventReporter 18.5 to 19.1?
=====================================================================

This article explains why log files may sometimes not be rotated as expected in EventReporter versions 18.5 to 19.1, and provides solutions for this issue.

Background
----------

In EventReporter versions 18.5 to 19.1, there are several factors that can interfere with log file rotation under certain circumstances. These issues were addressed in later versions with improved rotation handling.

The Problem
-----------

Users may experience inconsistent log file rotation behavior where:

* Some log files rotate successfully every day as scheduled
* Some log files rotate only partially (not every day)
* Some log files never rotate at all

This typically occurs when log rotation is scheduled at specific times (e.g., at 0:00 every day) or when using dynamic filenames with property replacer.

Root Cause
----------

The issue can be related to several factors:

* **File Handle Management:** When dynamic filenames are used, file handles are cached internally to avoid excessive file open/close operations. If files become inactive for extended periods, the cached handles may not be properly managed during rotation.

* **Timing Issues:** The rotation process may conflict with file access patterns, especially when multiple processes are accessing log files simultaneously.

* **Resource Constraints:** In high-volume logging environments, system resources may become constrained, affecting the rotation process.

Affected Versions
-----------------

This issue affects EventReporter versions 18.5 to 19.1. Later versions include improvements to the log rotation logic that handle these scenarios more reliably.

Solutions
---------

**Recommended Solution: Upgrade EventReporter**

The most effective solution is to upgrade to EventReporter version 19.1 or later, where the log rotation logic has been improved to handle these scenarios more reliably.

**Alternative Solutions**

If upgrading is not immediately possible, try these workarounds:

1. **Adjust File Handle Management:**
   * Review your file logging configuration
   * Ensure property replacer settings in filenames are optimized
   * Consider simplifying dynamic filename patterns if possible

2. **Modify Rotation Timing:**
   * Schedule rotations during periods of lower activity
   * Avoid scheduling rotations at exactly 00:00 when possible
   * Consider using size-based rotation instead of time-based rotation

3. **Resource Optimization:**
   * Monitor system resources during peak logging periods
   * Ensure adequate disk space is available
   * Consider load balancing if multiple instances are logging simultaneously

**Important:** Monitor your logging environment closely when implementing these workarounds, as they may affect overall system performance.
