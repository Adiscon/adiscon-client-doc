:orphan:

.. index:: Comparison of Properties

Comparison of properties
========================

**Available in MonitorWare Agent, EventReporter and WinSyslog**

The property replacer is a reference. The actual properties available for an
event depend on the product, the configured service, and in some cases the
edition. For WinSyslog, Windows Event Log properties are available when the
event is received through SETP from another Adiscon product.

.. code-block:: text

  Properties Available  MonitorWare Agent  WinSyslog  EventReporter

  Standard Property            Yes             Yes        Yes
  Windows Event Log            Yes             SETP       Yes
  Syslog Message               Yes             Yes
  Disk Space Monitor           Yes
  File Monitor                 Yes
  Windows Service Monitor      Yes                        Yes
  Ping Probe                   Yes
  Port Probe                   Yes
  Database Monitor             Yes
  Serial Port Monitor          Yes
  MonitorWare Echo Request     Yes
  System                       Yes             Yes        Yes
  Custom                       Yes             Yes        Yes
  NNTP Probe                   Yes
  HTTP Probe                   Yes
  FTP Probe                    Yes
  SMTP Probe                   Yes
  POP3 Probe                   Yes

``SETP`` means that WinSyslog can use those properties when they are
transported through SETP; it does not mean that WinSyslog collects Windows
Event Logs locally.
