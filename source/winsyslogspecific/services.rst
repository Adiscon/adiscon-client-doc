Services
========

Services are the configured WinSyslog inputs and generators. They receive or
generate events and pass those events into a ruleset for further processing.

You need at least one active input service. Without a service, WinSyslog does
not collect any data.

A few points matter in practice:

- **Actual services** process events.
- **Service defaults** are only templates for creating new service instances.
- Multiple service instances are possible when their ports and settings do not
  conflict.

In this manual, **input** is the clearest plain-language concept, while
**service** remains the main operational term for the configured WinSyslog
object. Some GUI pages use specific labels such as ``Syslog server``,
``RELP Listener``, and ``SETP Server``. Those are exact current service names.
Use
:doc:`faq/services-listeners-and-servers` if you need the terminology mapping.

Use the service pages below when you need to choose the right input type or
understand what a specific input service receives.

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
