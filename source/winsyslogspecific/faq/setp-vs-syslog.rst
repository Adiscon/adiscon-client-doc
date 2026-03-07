.. _winsyslog-setp-vs-syslog-faq:

What Is the Difference Between SETP and Syslog?
===============================================

Question
--------

What is the difference between SETP and syslog, and when should I use each one
with WinSyslog?

Answer
------

Use syslog when you need broad interoperability with network devices and
standard log senders. Use SETP when both sides are Adiscon products and you
need reliable transfer of richer event data.

Details
-------

**Syslog** is the standard protocol family for log transport. It is widely
supported by routers, switches, firewalls, Linux systems, appliances, and many
applications. It is the default choice whenever compatibility matters most.

**SETP** is an Adiscon-specific protocol for transferring events between
compatible Adiscon products. It is designed to preserve more event properties
than traditional syslog and is better suited for Windows-to-Windows Adiscon
scenarios.

Comparison
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 35 35 30

   * - Topic
     - Syslog
     - SETP
   * - Compatibility
     - Broad industry support
     - Adiscon-product specific
   * - Typical transport
     - UDP, TCP, TLS depending on sender and receiver
     - Adiscon protocol stack
   * - Reliability
     - Depends on transport and sender implementation
     - Intended for reliable Adiscon-to-Adiscon transfer
   * - Event detail preservation
     - Varies by sender format and parsing
     - Better preservation of original event properties
   * - Best fit
     - Devices and mixed environments
     - Internal Adiscon product chains

Action path
-----------

Choose **syslog** when:

* logs come from network devices or non-Adiscon systems
* interoperability is the main requirement
* the receiver is not an Adiscon product

Choose **SETP** when:

* both sender and receiver are Adiscon products
* you want better preservation of Windows event details
* you control both ends of the connection

Related information
-------------------

* :doc:`../../mwagentspecific/setpserver`
* :doc:`../tutorial-setp-server`
* :doc:`../producttour/receive-logs`
