.. _eventreporter-custom-event-logs-faq:

Can EventReporter Work with Custom Event Logs?
==============================================

Question
--------

Can EventReporter monitor custom Windows event logs and application-defined
logs?

Answer
------

Yes. EventReporter can monitor custom Windows event logs as long as the target
system exposes them through the Windows Event Log infrastructure.

Details
-------

Many Windows applications and server roles register their own event sources or
custom logs. If Windows exposes those logs or channels, EventReporter can read
them through the Event Log Monitor service.

The practical limitation is usually not EventReporter itself, but whether the
log exists on the system and whether the account context used by the service
can read it.

Action path
-----------

1. Identify the custom log or channel in Windows Event Viewer.
2. Configure an Event Log Monitor service to read that log or channel.
3. Bind the service to a ruleset with a visible action such as
   :doc:`Write to File <../../mwagentspecific/a-fileoptions>`.
4. Apply the configuration.
5. Trigger a test event in the custom log and confirm that EventReporter
   captures it.
