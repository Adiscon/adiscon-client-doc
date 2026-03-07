.. _winsyslog-non-standard-syslog-format-faq:

How Do I Handle Non-Standard Syslog Messages from Unix or Linux Systems?
========================================================================

Question
--------

How should I handle syslog messages from Unix or Linux systems when the sender
uses a non-standard format that WinSyslog does not parse correctly?

Answer
------

If the sender does not produce RFC-compliant syslog, disable strict parsing for
that stream and treat the payload more defensively. The cleanest fix is still
on the sender side: make it emit standards-compliant syslog if possible.

Details
-------

Some Unix or Linux senders emit messages that do not fully match RFC 3164 or
RFC 5424 expectations. A common example is a message that omits the hostname in
positions where the parser expects it. In those cases, WinSyslog may interpret
parts of the message incorrectly.

Best-practice approach
^^^^^^^^^^^^^^^^^^^^^^

1. Fix the sender format if you control the source system.
2. If that is not possible, reduce dependence on strict header parsing.
3. Apply parsing, filtering, or normalization later in the processing chain.

Operational guidance
^^^^^^^^^^^^^^^^^^^^

When you see incorrectly parsed hostnames, empty tags, or broken field
extraction:

* inspect a raw sample message
* verify whether the sender actually follows RFC 3164 or RFC 5424
* adjust the WinSyslog service configuration so it does not rely on a header
  format the sender does not provide
* use downstream filtering or custom property extraction where necessary

Related information
-------------------

* :doc:`../../mwagentspecific/syslogserver`
* :doc:`../producttour/receive-logs`
* :doc:`../../shared/references/syslogmessageproperties`
