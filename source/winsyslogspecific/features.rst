Features
========

This page summarizes what WinSyslog can do so you can decide which parts of
this manual matter for your environment. For setup guidance, continue with
:doc:`installation` and :doc:`creatinganinitialconfiguration`.

Core capabilities
-----------------

WinSyslog is designed to collect, process, store, and forward syslog data on
Windows systems. Its main capabilities include:

- centralized syslog collection from network devices, appliances, servers, and
  applications
- rule-based processing with filters and ordered actions
- local storage in text files, databases, and the Windows Event Log
- forwarding to downstream systems by syslog, RELP, SETP, email, and other
  action types
- live message display through the Interactive Syslog Viewer
- background operation as a native Windows service

When WinSyslog is a good fit
----------------------------

WinSyslog is a strong fit when you need one or more of the following:

- a native Windows syslog server for mixed network environments
- an edge collector that reduces noise before forwarding data upstream
- local retention on Windows hosts in files or ODBC-connected databases
- alerting or automated follow-up actions based on selected events
- a flexible ruleset model instead of a fixed receive-and-store workflow

Processing and routing
----------------------

WinSyslog uses services, rulesets, filter conditions, and actions to control
how messages move through the product. This allows you to:

- receive different inputs on different ports or protocols
- route different event classes to different outputs
- store, forward, or alert on only the events that matter
- run multiple listener instances when ports and settings do not conflict

For the underlying model, see :doc:`winsyslogconcepts` and
:doc:`multiple-rulesets-rules-actions`.

Storage, forwarding, and visibility
-----------------------------------

WinSyslog can keep data locally and pass it on to other tools and systems.
Common options include:

- writing to text files for simple retention and troubleshooting
- writing to databases for structured querying and downstream analysis
- writing to the Windows Event Log for Windows-focused workflows
- forwarding to remote log collectors or SIEM platforms
- displaying live traffic in the Interactive Syslog Viewer

See also:

- :doc:`Actions <actions>`
- :doc:`producttour/store-and-forward`
- :doc:`tutorial-write-to-file`
- :doc:`tutorial-forward-syslog`

Operations and platform support
-------------------------------

WinSyslog runs as a Windows service and is intended for unattended background
operation after configuration. It supports current Windows releases including
Windows 10, Windows 11, Windows Server 2016, Windows Server 2019, Windows
Server 2022, Windows Server 2025, and newer versions.

For deployment constraints and platform questions, see:

- :doc:`systemrequirements`
- :doc:`faq/winsyslog-iot2025-support`
- :doc:`faq/mass-rollout-deployment`

Feature notes
-------------

A few product features are useful but should be understood in context:

.. _winsyslog-send-test-message:

- **Send Syslog Test Message** is a quick validation tool in the Configuration
  Client. It sends a simple UDP syslog test message.
- **Freeware mode** is available for limited use cases. See
  :doc:`faq/what-is-freeware-mode`.
- **Interactive viewing** is available, but it requires WinSyslog to forward
  events to the Interactive Syslog Viewer.
- **IPv6** is supported in network-related facilities, but some service types
  require separate listener instances depending on protocol behavior.
