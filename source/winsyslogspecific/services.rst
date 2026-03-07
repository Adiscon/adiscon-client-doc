Services
========

Services are the WinSyslog inputs. They receive or generate events and pass
those events into a ruleset for further processing.

You need at least one active service. Without a service, WinSyslog does not
collect any data.

A few points matter in practice:

- **Actual services** process events.
- **Service defaults** are only templates for creating new service instances.
- Multiple service instances are possible when their ports and settings do not
  conflict.

Use the service pages below when you need to choose the right input type or
understand what a specific listener does.

Basic services
--------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/heartbeat
   ../mwagentspecific/monitorwareechoreply

Network services
----------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/relplistener
   ../mwagentspecific/setpserver
   ../mwagentspecific/snmptrapreceiver
   ../mwagentspecific/syslogserver
