.. _log-rotation-file-handle-cleanup-winsyslog:


Why were dynamic log files sometimes not rotated in older WinSyslog versions?
=============================================================================

Older WinSyslog versions could miss some scheduled rotations when dynamic
filenames were combined with file-handle cleanup. That historical behavior was
improved in later versions of the shared log rotation subsystem.

For the guarantees of the current subsystem, including graceful shutdown,
restart recovery, reload behavior, and dynamic filename support, see
:doc:`../../shared/faq/log-rotation-guarantees`.

Background
----------

In older WinSyslog versions, the automatic file handle cleanup logic could
close an inactive dynamic log file before the scheduled rotation time arrived.
Later versions improved the shared log rotation subsystem to handle this more
reliably.

The Problem
-----------

Users may experience inconsistent log file rotation behavior where:

* Some log files rotate successfully every day as scheduled
* Some log files rotate only partially (not every day)
* Some log files never rotate at all

This typically occurs when log rotation is scheduled at specific times (e.g., at 0:00 every day).

Root Cause
----------

The issue is related to WinSyslog's Automatic File Handle Cleanup feature, which by default:

* Closes inactive log files after 2 hours of no activity
* Frees up memory and system resources
* Prevents resource exhaustion when many log files are being monitored

At the time of scheduled rotation, if a log file has been inactive for more than 2 hours, WinSyslog may have already closed its file handle. When the rotation process runs, it cannot rotate a file that is no longer actively opened by WinSyslog.

**Note:** This behavior is similar to how your computer closes unused programs to maintain system stability.

Affected Versions
-----------------

This issue affects WinSyslog versions 17.5 and earlier. The log rotation logic was redesigned starting with WinSyslog version 18.1, which resolves these limitations.

Solutions
---------

**Recommended Solution: Upgrade WinSyslog**

The most effective solution is to upgrade to WinSyslog version 18.1 or later, where the log rotation logic has been redesigned to handle these scenarios properly.

**Alternative Solution: Adjust File Handle Cleanup Interval**

If upgrading is not immediately possible:

1. Open the WinSyslog configuration
2. Navigate to the service settings
3. Increase the "Automatic File Handle Cleanup" interval from the default 2 hours to 24 hours (or longer, depending on your environment)
4. This adjustment will reduce the likelihood of missing log rotations

**Important:** The longer cleanup interval may increase memory usage, so monitor your system's resource utilization accordingly.
.. _log-rotation-file-handle-cleanup-winsyslog:

Why were dynamic log files sometimes not rotated in older WinSyslog versions?
=============================================================================

Older WinSyslog versions could miss some scheduled rotations when dynamic
filenames were combined with file-handle cleanup. That historical behavior was
improved in later versions of the shared log rotation subsystem.

For the guarantees of the current subsystem, including graceful shutdown,
restart recovery, reload behavior, and dynamic filename support, see
:doc:`../../shared/faq/log-rotation-guarantees`.

If you are still running one of the older affected builds, increasing the file
handle cleanup timeout can reduce the chance of a missed scheduled rotation,
but the recommended long-term solution is to upgrade to a current release.
