About EventReporter
===================

**EventReporter is a Windows event log collector and forwarding engine. It
collects Windows Event Log data, filters it through rules, and then stores,
forwards, or alerts on the events that matter.**

EventReporter is designed for administrators who need more than the native
Windows Event Viewer. It provides centralized forwarding, rule-based filtering,
and background service operation for environments that want to integrate Windows
Event Log data into syslog, SETP, email, files, databases, or other downstream
systems.

Typical use cases include:

- forwarding Windows Event Log events to a central syslog server or SIEM
- sending selected events by email for operational alerting
- storing events in files or databases for retention and analysis
- filtering noisy event streams before they leave the Windows host
- running Windows event collection as a background service with a separate
  configuration client

EventReporter is focused on Windows Event Log collection. It complements, but
is distinct from, products such as WinSyslog, which focus on syslog reception.

For a neutral summary of how EventReporter and the other Adiscon Windows
products can deliver data into ROSI-oriented deployments, see
:doc:`shared/how-to-integrate-adiscon-windows-products-into-rosi`.

This manual is organized around first-time setup, task-oriented tutorials,
configuration reference, FAQ content, and reference material.

Manual
======

.. toctree::
   :maxdepth: 1

   eventreporterspecific/index
   Tutorials <eventreporterspecific/stepbystepguides>
   Configuration <eventreporterspecific/eventreporter>
   eventreporterspecific/faq
   Licensing and purchasing <shared/sales/index>
   Reference <eventreporterspecific/references>
   copyrights


* :ref:`genindex`
