.. _rsyslogwa-tour-collect-and-forward:

Collect and Forward Windows Events
==================================

rsyslog Windows Agent is primarily used to collect Windows-originated events
and forward them to rsyslog or another downstream receiver.

What the product collects
-------------------------

The most common sources are:

- Windows Event Log channels
- text-based application log files
- incoming syslog messages when the agent is used as a relay

What the product usually does next
----------------------------------

After collection, rsyslog Windows Agent processes the events through a ruleset
and then forwards the matching data to another system, most often a central
rsyslog server.

Where to configure it
---------------------

- :doc:`Services <services>` is the entry point for event collection.
- :doc:`Event Log Monitor V2 <../mwagentspecific/eventlogmonitorv2>` is the
  preferred service for modern Windows Event Log channels.
- :doc:`File Monitor <../mwagentspecific/filemonitor>` is available when you
  need to watch text-based log files.
- :doc:`Syslog server <../mwagentspecific/syslogserver>` is available when the
  agent should relay incoming syslog.

Quick verification
------------------

- Configure one collection service.
- Bind it to a ruleset with a visible forwarding action.
- Apply the configuration and confirm that new events reach the receiver.
