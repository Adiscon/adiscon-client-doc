.. _winsyslog-two-date-stamps-faq:

Why Does a WinSyslog Message Show Two Timestamps?
=================================================

Question
--------

Why do some WinSyslog log entries show two timestamps?

Answer
------

Because the entry can contain both the sender-provided event time and the time
when WinSyslog received the message. These serve different purposes and both
can be useful.

Details
-------

A typical received syslog message may contain:

* the timestamp created by the sending device or application
* the timestamp added by WinSyslog when the message arrives

The sender timestamp tells you when the original event happened according to
that sender. The WinSyslog timestamp tells you when the message reached the
WinSyslog server.

These values are often close, but they can differ when:

* the sending device has an incorrect clock
* the sender buffers messages and sends them later
* network or forwarding delays exist
* an intermediate collector relays the message

Interpretation guidance
^^^^^^^^^^^^^^^^^^^^^^^

If you need to understand event chronology on the sender, the sender timestamp
is usually the more relevant value. If you need to understand transport delay,
collection timing, or queuing effects, the WinSyslog receive timestamp is the
more useful one.

If the sender does not include a timestamp at all, WinSyslog's receive time may
be the only reliable time reference available.

Related information
-------------------

* :doc:`defaulttime-explained`
* :doc:`../../shared/references/syslogmessageproperties`
