.. _winsyslog-eventreporter-properties-via-setp:

Why can WinSyslog use EventReporter properties?
===============================================

Question
--------

Why can WinSyslog rules use EventReporter or Windows Event Log properties when
WinSyslog does not collect Windows Event Logs locally?

Answer
------

WinSyslog can use those properties when the event arrives through SETP. SETP
preserves structured Adiscon event properties, so a WinSyslog ruleset can
filter, format, and forward those properties after receiving the event.

Details
-------

This applies to events sent by another Adiscon product, such as EventReporter,
to a WinSyslog ``SETP Server`` service. WinSyslog receives the structured event
and processes it through the configured ruleset.

This does not mean that WinSyslog provides EventReporter's local Windows Event
Log Monitor service. EventReporter collects the Windows Event Log event;
WinSyslog can process the transported event properties after SETP delivery.

The ``SETP Server`` service is available in WinSyslog Enterprise and Trial.
Sending events through SETP is a separate sender-side action.

Related information
-------------------

- :doc:`setp-vs-syslog`
- :doc:`../tutorial-setp-server`
- :doc:`../../mwagentspecific/setpserver`
