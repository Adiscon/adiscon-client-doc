NT Service Monitor
==================

The NT Services Monitor is used to monitor if vital operating services are
running. The monitor continuously checks all services set to "automatic"
startup. If such a service does not run, an event is generated and passed to
the rule engine.

.. image:: ../images/ntservicemonitor.png
   :width: 100%

* Service - NT Service Monitor*


Probe Interval
^^^^^^^^^^^^^^

**File Configuration field:**
  nSleepTime

**Description:**
  This is the interval in which the service status is checked. This period is
  specified in :doc:`milliseconds <../glossaryofterms/millisecond>`. The default is 60,000 ms, which is one minute.
  We recommend to lower this interval only if the server is performing very
  critical operations and service stops need to be detected in close real-time.

  For performance reasons, we do not recommend using an interval of less than
  2000 ms.




Delay on Startup in Milliseconds (1000 ms -> 1 second)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**File Configuration field:**
  nDelayOnStartup

**Description:**
  During system boot, the monitoring service eventually starts before all other
  services have been started. As such, the service monitor probably finds some
  services not running – simply because they are to be started very soon.
  Nevertheless, the service monitor still generates a "service not running"
  event.

  To avoid this situation, use the startup delay setting. It specifies an
  amount of time (in :doc:`milliseconds <../glossaryofterms/millisecond>`) that
  the service monitor is to hold right after startup. So during system boot,
  the operating system has a chance to start all other services before the
  service monitor comes into action.

  The actual delay is very much depending on the number of services and
  hardware sizing of a particular server. Typically, a value 60,000 ms (one
  minute) should be a good value. But a busy server with many services might
  require a much higher value.




Generate an event if a Service is in the running state
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**File Configuration field:**
  nGenerateOnSuccess

**Description:**
  When checked, an event is generated every time. If unchecked, it is generated
  only when the Service probe fails. The most common option is to leave it
  unchecked to catch events upon a failed Service startup.



General Values (Common settings for most services)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Syslog Facility
^^^^^^^^^^^^^^^

**File Configuration field:**
  nSyslogFacility

**Description:**
  The :doc:`syslog facility <../glossaryofterms/syslogfacility>` to be
  assigned to events created by this service. Most useful if the message is to
  forward to a Syslog server.



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
  The :doc:`resource id <../glossaryofterms/resourceid>` to be assigned to
  events created by this service. Most useful if the message is to forward to a
  Syslog server.



RuleSet to Use
^^^^^^^^^^^^^^

**File Configuration field:**
  szRuleSetName

**Description:**
  Name of the ruleset to be used for this service. The RuleSet name must be a
  valid RuleSet.
