Tutorial: Forward Events via SETP
=================================

Goal
----

Forward events from MonitorWare Agent to a downstream SETP receiver.

Prerequisites
-------------

- A ruleset that receives events from a MonitorWare Agent service
- The destination SETP server host name or IP address
- The destination port and authentication details if required

Steps
-----

1. Create or choose the ruleset whose events should be forwarded.
2. Add a :doc:`Forward SETP <a-forwardsetpoptions>` action to that ruleset.
3. Configure the destination server and port.
4. Configure any required sender identity or security settings.
5. Save and apply the configuration.
6. Restart the service if required in your environment.

Verification
------------

Trigger a matching event and confirm that the destination SETP server receives
it.
