rsyslog Windows Agent Services
==============================

Services are the input objects that collect or receive events and pass them to
rulesets.

Key idea
--------

Each active service instance is bound to a ruleset. That binding decides which
processing logic sees the collected event.

Common service types
--------------------

- **Heartbeat** generates status events that show the agent is still alive.
- **MonitorWare Echo Reply** responds to echo requests in monitored
  environments.
- **Syslog Server** receives syslog messages on the configured port.
- **Event Log Monitor** reads Windows Event Log channels and creates internal
  events from them.
- **File Monitor** watches text-based logs and turns new lines into events.

Important distinction
---------------------

Service defaults are templates. They are not active services and do not collect
anything until you create a concrete service instance.
