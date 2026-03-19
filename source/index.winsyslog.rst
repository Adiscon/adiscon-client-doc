About WinSyslog
===============

**WinSyslog is a Windows syslog server for collecting, processing, storing, and
forwarding log messages across Windows-centric and mixed environments. It helps
IT operations, security, and compliance teams centralize syslog data from
network devices, appliances, servers, and applications on a native Windows
platform.**

Developed since 1996, WinSyslog was the first syslog server for Windows. It is
built by the same team behind `rsyslog <https://www.rsyslog.com>`_ and combines
long-standing syslog expertise with a Windows-focused deployment and management
model. Adiscon has published additional background on this shared engineering
lineage in `The rsyslog Evolution: Bridging BSD Heritage with Adiscon Innovation <https://www.rsyslog.com/the-rsyslog-evolution-bridging-bsd-heritage-with-adiscon-innovation/>`_.

`Syslog <https://www.adiscon.com/syslog>`_ remains one of the standard protocols
for centralized event logging. Routers, switches, firewalls, printers,
hypervisors, Linux systems, and many security appliances can all send syslog
messages. WinSyslog provides the Windows-side collection point for these events
and lets you route them to the destinations and workflows your environment
requires.

WinSyslog is centered on syslog data. It is not the product for collecting and
forwarding Windows Event Log data. When the source is Windows Event Log, use
`EventReporter <https://www.eventreporter.com/>`_,
`MonitorWare Agent <https://www.mwagent.com/>`_, or
`rsyslog Windows Agent <https://www.rsyslog.com/windows-agent/>`_ instead,
depending on the required scope.

WinSyslog is designed for environments that need more than a basic message
receiver. It can receive syslog over UDP and TCP, support secure syslog
transport with TLS, and integrate with RELP-based forwarding for reliable log
delivery. It also runs as a native Windows service and fits naturally into
Windows administration and monitoring practices.

.. figure:: /images/winsyslog-edge-collector-architecture.jpg
   :alt: WinSyslog as a Windows edge collector that receives noisy log streams, filters and normalizes them, and forwards cleaner events to downstream systems
   :align: center

   WinSyslog can act as a Windows edge collector that reduces noise and forwards
   cleaner event streams to SIEMs, databases, files, and other downstream
   systems.

Typical use cases include:

- Centralized logging for routers, switches, firewalls, wireless controllers,
  printers, and other syslog-capable devices
- Real-time alerting and event-driven automation for critical infrastructure and
  security incidents
- Long-term log storage in text files, ODBC databases, and the Windows Event
  Log
- Secure forwarding and relay scenarios that require TCP, TLS, or reliable log
  transport
- Edge or node-level collection in Windows environments, where WinSyslog can
  remove noise, normalize messages, and forward cleaner event streams upstream
- Windows-based syslog collection for SIEM pre-filtering, compliance retention,
  and operational troubleshooting

WinSyslog uses a flexible rule engine to filter, enrich, store, display, and
forward events. You can use it as a standalone Windows syslog server or as part
of a larger logging architecture with other Adiscon components and downstream
analysis systems. In distributed logging pipelines, this also helps reduce
unnecessary upstream traffic, storage volume, and processing load by dropping
low-value events early and forwarding only the data that needs further
retention or analysis.

For a neutral summary of how WinSyslog and the other Adiscon Windows products
can deliver data into ROSI-oriented deployments, see
:doc:`shared/how-to-integrate-adiscon-windows-products-into-rosi`.

This manual covers installation, features, configuration, operations, FAQ
content, and reference material for WinSyslog. Use the sections below to get
started or go directly to the area you need.

Manual
======

.. toctree::
   :maxdepth: 1

   winsyslogspecific/index
   Tutorials <winsyslogspecific/stepbystepguides>
   Interactive Syslog Viewer <../interactivesyslogviewer/index>
   Configuration <winsyslogspecific/winsyslog>
   winsyslogspecific/faq
   Licensing and purchasing <shared/sales/index>
   Reference <winsyslogspecific/references>
   copyrights


* :ref:`genindex`
