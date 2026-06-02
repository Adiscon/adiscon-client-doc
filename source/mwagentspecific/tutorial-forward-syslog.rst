Tutorial: Forward Events via Syslog
===================================

Goal
----

Forward events collected by MonitorWare Agent to a downstream syslog receiver.

Prerequisites
-------------

- A ruleset that receives events from a MonitorWare Agent service
- The target syslog server host name or IP address
- The target port and framing mode

Steps
-----

1. Create or choose the ruleset whose events should be forwarded.
2. Add a :doc:`Forward Syslog <a-forwardsyslogoptions>` action to that ruleset.
3. Configure the target host and port.
4. Choose the TCP or UDP transport mode required by the receiver.
5. Save and apply the configuration.
6. Restart the service if required in your environment.

Verification
------------

Trigger a matching event and confirm that the downstream syslog receiver gets
it.

Next step
---------

If encryption is required, continue with
:doc:`tutorial-forward-tls-to-rsyslog`.
