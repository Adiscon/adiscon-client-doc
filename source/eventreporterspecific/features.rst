.. index:: Features

Features
========

Centralized Logging
-------------------

This is the key feature. EventReporter allows consolidation of multiple Windows
event logs and forward them automatically to either a system process or an
administrator.

Ease of Use
-----------

Using the new EventReporter client interface, the product is very easy to setup
and customize. We also support full documentation and support for large-scale
unattended installations.

Syslog Support
--------------

Windows Event Messages can be forwarded using standard Syslog protocol. Windows
severity classes are mapped to the corresponding Syslog classes.
:doc:`syslog facility <../glossaryofterms/syslogfacility>` codes are fully supported.

SETP Support
------------

:doc:`setp <../glossaryofterms/setp>` was originally developed for MonitorWare but now it is a key feature added
in EventReporter 6.2 Professional Edition. Windows Event Messages can be
forwarded using SETP protocol. `Click here <https://www.adiscon.com/faq/difference-setp-and-syslog/>`_ for more information on SETP.

Email Support
-------------

Windows Event Log information can also be delivered via standard Internet
email. This option is an enabler for smaller organizations or service providers
unattended monitoring their client's servers.

Local Filtering
---------------

EventReporter can locally filter events based on the Windows Event Log type
(e.g. "System" or "Application") as well as severity.

IPv6
----

Support for IPv6 is available in all network related facilities of the engine.
All network related actions will automatically detect IPv6 and IPv4 target
addresses if configured. You can also use DNS resolution to resolve valid IPv6
addresses. Network related Services can either use IPv4 or IPv6 as internet
protocol. In order to support both protocols, you will need to create two
services. The only exception is the RELP Listener, which uses IPv4 and IPv6
automatically if available.

Runs on a large Variety of Windows Systems
------------------------------------------

Windows 2019/2016/2012/10/8/2008(R2)/7/Vista/2008/2003/2003(R2)/XP/2000
Workstation or Server – MonitorWare Agent runs on all of them.

Support for End-of-Life operating systems is only partially
available. Only a minimal service installation may be possible. More details:
:doc:`information for a mass rollout <../shared/gettingstarted/informationforamassrollout>`

Robustness
----------

EventReporter is running in a large number of installations. It is written to
perform robustly even under unusual circumstances. Its reliability has been
proven at customers' side since 1997.

Remote Administration
---------------------

The client interface can be used to remotely manage EventReporter instances.

Minimal Resource Usage
----------------------

EventReporter has no noticeable impact on system resources. It was specifically
written with minimal resource usage in mind. In typical scenarios, its
footprint is barely traceable. This ensures it can also be installed on heavily
loaded servers.

Full Windows Event Log Decoding
-------------------------------

EventReporter can fully decode all types of Windows Event Log entries. It has
the same capabilities like event viewer.

Windows Service
---------------

The EventReporter Service is implemented as a native multithreaded Windows
service. It can be controlled via the control panel services applet or the
computer management MMC.

Double Byte Character Set Support (e. g. Japanese)
--------------------------------------------------

EventReporter supports characters encoded in double byte character sets (DBCS).
This is mostly used with Asian languages like Japanese or Chinese. All DBCS
strings are forwarded correctly to the syslog daemon or email recipient.
However, the receiving side must also be able to process DBCS correctly.
Adiscon's syslog daemon for Windows, `WinSyslog <https://www.WinSyslog.com>`_, does so. The output character
encoding is selectable and supports Shift-JIS, JIS, and EUC-JP for Japanese users.

Multi-Language Client
---------------------

The EventReporter client comes with multiple languages ready to go. Out of the
box English, German, and Japanese are supported. Languages can be switched
instantly. Language settings are specific to a user.

Additional languages can be easily integrated using Adiscon's brand new XML
based localization technology. We ask customers interested in an additional
language for a little help with the translation work (roughly 1 hour of work).
Adiscon will then happily create a new version. This service is free!

Friendly User Interface
-----------------------

New Cloning feature has been also added to the EventReporter Client. In short
you can now clone a Ruleset, a Rule, an Action, or a Service with one mouse
click. Move up and Move down function has been added for Actions in the
EventReporter Client. The EventReporter Client Wizards has been enhanced for
creating Actions, Services, and RuleSets. And other minute changes!

Multiple RuleSets - Rules - Actions
-----------------------------------

With EventReporter as many "RuleSets", "Rules" and "Actions" as necessary can
be defined.

:doc:`multiple rulesets - rules - actions <../eventreporterspecific/multiple-rulesets-rules-actions>`

Handling for low-memory cases
-----------------------------

MWAgent allocates some emergency memory on startup. If the system memory limit
is reached, it releases the emergency memory and locks the queue. That means
not more items can be queued, this prevents a crash of the Agent and the queue
is still being processed. Many other positions in the code have been hardened
against out-of-memory scenarios.
