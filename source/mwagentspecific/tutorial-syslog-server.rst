Tutorial: Configure a Syslog Server Service
===========================================

Goal
----

Configure MonitorWare Agent to receive incoming syslog messages.

Prerequisites
-------------

- The MonitorWare Agent Configuration Client is available.
- You know which protocol and port should be used.

Steps
-----

1. Under **Running Services**, add a :doc:`Syslog Server <syslogserver>`
   service.
2. Select the protocol and port.
3. Assign the service to the ruleset that should process received messages.
4. Save and apply the configuration.
5. Restart the service if required in your environment.

Verification
------------

Send a test syslog message to the configured port and confirm that the
assigned ruleset processes it.
