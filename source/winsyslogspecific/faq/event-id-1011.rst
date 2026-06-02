.. _winsyslog-event-id-1011-faq:

What Does WinSyslog Event ID 1011 Mean?
=======================================

Question
--------

What does Event ID 1011 mean when it appears in the Windows Application Event
Log for WinSyslog?

Answer
------

Event ID 1011 indicates that WinSyslog could no longer find the last Windows
Event Log record it had processed before. This usually means the monitored
Windows Event Log was cleared or truncated.

Details
-------

This matters only when WinSyslog monitors Windows Event Log sources.

To continue processing, WinSyslog resets its internal read position and starts
again from the beginning of the available log data. That allows monitoring to
continue, but it can also lead to duplicate messages because WinSyslog must
resume from a safe point.

Typical causes
^^^^^^^^^^^^^^

* the monitored Windows Event Log was cleared manually
* the log was truncated because of retention settings or size limits
* the underlying record that WinSyslog expected no longer exists

Operational effect
^^^^^^^^^^^^^^^^^^

The condition is usually informational rather than catastrophic. It tells you
that continuity was interrupted and that re-reading may occur.

If you see this repeatedly, review the retention policy of the monitored event
log and the polling behavior of the event-monitoring service.

Related information
-------------------

Review the WinSyslog service configuration that reads Windows Event Log data
and the retention policy of the monitored Windows log sources.
