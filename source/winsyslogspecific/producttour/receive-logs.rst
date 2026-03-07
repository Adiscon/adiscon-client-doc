.. _winsyslog-tour-receive-logs:

Receive Logs
============

WinSyslog receives logs from multiple sources and turns them into events that
can be processed by rules.

.. image:: ../../images/winsyslog-simple-routing.jpg
   :width: 100%
   :alt: Diagram showing log sources feeding WinSyslog through Syslog UDP/TCP, RELP, SETP, and SNMP traps, then being processed by services, rulesets, and actions before output to file, database, Windows Event Log, forwarded syslog, or email.

*WinSyslog can receive logs from multiple source types, process them through
services, rulesets, and actions, and then store or forward them to downstream
targets.*

What you can receive:

- Syslog over UDP/TCP and secure syslog over TLS
- RELP (reliable transport)
- Windows Event Log events
- SNMP traps

Where to configure it:

- :doc:`Services <../services>` provide the inputs.
- :doc:`Syslog server service <../../mwagentspecific/syslogserver>` receives syslog.
- :doc:`RELP listener <../../mwagentspecific/relplistener>` receives RELP.
- :doc:`SETP server <../../mwagentspecific/setpserver>` receives SETP.
- :doc:`SNMP trap receiver <../../mwagentspecific/snmptrapreceiver>` receives SNMP traps.

Quick verification:

- In the WinSyslog Configuration Client, open `Tools` and use `Send Syslog Test Message`
  (see :ref:`Send Syslog Test Message <winsyslog-send-test-message>`).
- Confirm messages arrive in the configured ruleset (for example, write to a file).
