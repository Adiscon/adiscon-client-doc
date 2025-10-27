About WinSyslog
===============

**WinSyslog is a powerful and professional-grade syslog server for Microsoft Windows. It is designed for demanding enterprise environments and provides the same core functionality as a Unix syslog daemon, but with extended capabilities, modular
design, and seamless Windows integration.**

WinSyslog is actively maintained and continuously enhanced. With over two decades
of development, it is one of the most mature, robust, and feature-rich syslog
solutions available for the Windows platform today.

Network administrators rely on WinSyslog to monitor critical infrastructure in
real time and receive alerts the moment important events occur.

`Syslog <https://www.adiscon.com/syslog>`_ is a well-established protocol for centralized
logging of system events. While it originated in the UNIX world, today it is used
by nearly all networked devices—including routers, switches, firewalls, and printers—
to report events, status updates, and diagnostics.

Microsoft Windows does not include a native syslog server (known as "syslogd" on UNIX).
This is where Adiscon’s `WinSyslog <https://www.WinSyslog.com>`_ steps in. Developed
since 1996, it was the first syslog server for Windows and remains a trusted
solution for system and network administrators worldwide.

WinSyslog is developed by the same experienced team behind the industry-leading
`Rsyslog <https://www.Rsyslog.com>`_ project, the de facto syslog standard in Linux.
This shared expertise ensures deep protocol understanding and consistent
implementation across platforms.

The product has evolved significantly since its early days. Originally released
as "NTSLog", it became "WinSyslog" starting with version 3 to reflect its
expanded capabilities. Each release has introduced meaningful enhancements,
with version 4 adding rule-based processing and modular services that allow
for extremely flexible setups.

WinSyslog can operate as a standalone solution or be combined with other Adiscon
tools—such as `MonitorWare Agent <https://www.mwagent.com>`_ and
`EventReporter <https://www.EventReporter.com>`_—to form a comprehensive, centralized
event monitoring and alerting system for Windows-based infrastructures.

Typical use cases include:

- Logging events from syslog-capable devices such as routers, switches, and printers
- Long-term storage of logs in text files, ODBC databases, or the Windows Event Log
- Real-time display of messages and automatic notification (e.g., via email) on critical events
- Running multiple concurrent syslog listeners on different ports

WinSyslog runs as a stable, low-maintenance Windows service that starts
automatically with the system. Once configured, it operates reliably in the
background, requiring no manual intervention.

With decades of field-tested experience, WinSyslog delivers unmatched
reliability and versatility for professionals who demand robust, scalable,
and secure event logging on Windows systems.

To learn more about the full suite of MonitorWare products, visit:
`https://www.adiscon.com/products <https://www.adiscon.com/products>`_

Manual
======

.. toctree::
   :maxdepth: 1

   winsyslogspecific/introduction
   winsyslogspecific/producttour
   winsyslogspecific/index
   winsyslogspecific/stepbystepguides
   ../interactivesyslogviewer/index
   winsyslogspecific/winsyslog
   winsyslogspecific/gettinghelp
   winsyslogspecific/winsyslogconcepts
   winsyslogspecific/purchasingwinsyslog
   winsyslogspecific/articles
   winsyslogspecific/faq
   winsyslogspecific/references
   winsyslogspecific/glossaryofterms
   copyrights


* :ref:`genindex`
