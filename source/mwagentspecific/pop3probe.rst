POP3 Probe
==========

POP3 probe does a connection to POP3 server. It receives the response from POP3
server and sends the QUIT command to terminate the connection.

The connection status is saved in the property **pop3status** and the response in the property **pop3respmsg**.


.. image:: ../images/pop3probe.png
   :width: 100%

* Service - POP3 Probe*

Probe Interval
^^^^^^^^^^^^^^

**File Configuration field:**
  nSleepTime

**Description:**
  This is the interval of the probe. After each probe, the Service will sleep
  for the configured probe interval. This period is specified in milliseconds.



Timeout Limit
^^^^^^^^^^^^^

**File Configuration field:**
  nTimeOutLimit

**Description:**
  The amount of time (in :doc:`milliseconds <../glossaryofterms/millisecond>`)
  the remote system is expected to answer in. If no response is received within
  this period, the probe fails and an event is generated. The default value of
  1000 milliseconds is a proper value for most well connected networks. If the
  probe runs against a heavily loaded system and/or slow network link, the
  amount must be adjusted accordingly.



Generate an event if POP3 Probe was successful
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**File Configuration field:**
  nGenerateOnSuccess

**Description:**
  When checked, an event is generated every time. If unchecked, it is generated
  only when the POP3 probe fails. The most common option is to leave it
  unchecked to catch events upon a failed POP3 probe.



POP3 Server
^^^^^^^^^^^

**File Configuration field:**
  szPOP3Server

**Description:**
  Either the IP address or resolvable host name of the POP3 server, the POP3
  probe is to be run against. You can either use an IPv4, an IPv6 Address, or a
  Hostname that resolves to an IPv4 or IPv6 Address. This system has been
  called "remote host" in the description above. Please note that specifying a
  host name can cause the POP3 probe to fail if DNS name resolution fails (for
  example due to a failing DNS server). To avoid this, specify an IP address.



POP3 Port
^^^^^^^^^

**File Configuration field:**
  nPOP3Port

**Description:**
  This port is to be probed. Please see your server's reference for the actual
  value to use. For example, mail servers typically listen to port 110.



General Values (Common settings for most services)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Syslog Facility
^^^^^^^^^^^^^^^

**File Configuration field:**
  nSyslogFacility

**Description:**
  The :doc:`syslog facility <../glossaryofterms/syslogfacility>` to be assigned to events created by this service. Most
  useful if the message is to forward to a Syslog server.



Syslog Priority
^^^^^^^^^^^^^^^

**File Configuration field:**
  nSyslogPriority

**Description:**
  The Syslog priority to be assigned to events created by this service. Most
  useful if the message is to forward to a Syslog server.



Syslog Tag Value
^^^^^^^^^^^^^^^^

**File Configuration field:**
  szSyslogTagValue

**Description:**
  The Syslog tag value to be assigned to events created by this service. Most
  useful if the message is to forward to a Syslog server.



Resource ID
^^^^^^^^^^^

**File Configuration field:**
  szResource

**Description:**
  The :doc:`resource id <../glossaryofterms/resourceid>` to be assigned to events created by this service. Most useful
  if the message is to forward to a Syslog server.



RuleSet to Use
^^^^^^^^^^^^^^

**File Configuration field:**
  szRuleSetName

**Description:**
  Name of the ruleset to be used for this service. The RuleSet name must be a
  valid RuleSet.
