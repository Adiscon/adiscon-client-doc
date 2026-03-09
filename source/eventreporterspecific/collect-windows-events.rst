.. _eventreporter-tour-collect-events:

Collect Windows Events
======================

EventReporter collects Windows Event Log data and turns it into internal events
that can be filtered, stored, and forwarded.

What EventReporter receives
---------------------------

EventReporter is centered on Windows Event Log collection. In practice, this
means:

- classic Windows Event Log sources
- modern Windows event channels exposed through the operating system
- custom event logs that Windows and the originating application register

Where to configure it
---------------------

- :doc:`Services <services>` is the entry point for event collection.
- :doc:`Event Log Monitor V1 <../mwagentspecific/eventlogmonitorv1>` and
  :doc:`Event Log Monitor V2 <../mwagentspecific/eventlogmonitorv2>` are the
  key EventReporter collection services.

Choosing a monitor version
--------------------------

Use the newer Event Log Monitor where it matches the target system and event
channel requirements. Keep the older monitor only when you have a defined
reason to use it for compatibility or legacy behavior.

Quick verification
------------------

- Configure one Event Log Monitor service.
- Bind it to a ruleset with a visible action such as
  :doc:`Write to File <../mwagentspecific/a-fileoptions>`.
- Apply the configuration and confirm that new Windows events reach the target.
