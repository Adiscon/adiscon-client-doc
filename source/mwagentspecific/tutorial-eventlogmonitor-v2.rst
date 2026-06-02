Tutorial: Configure Event Log Monitor V2
========================================

Goal
----

Configure Event Log Monitor V2 to collect Windows Event Log channels and feed
them into a ruleset.

Prerequisites
-------------

- The MonitorWare Agent Configuration Client is available.
- You know which event channels should be monitored.

Steps
-----

1. Under **Running Services**, add an
   :doc:`Event Log Monitor V2 <eventlogmonitorv2>` service.
2. Select the required Windows Event Log channels.
3. Assign the service to the ruleset that should process those events.
4. Save and apply the configuration.
5. Restart the service if required in your environment.

Verification
------------

Trigger a test event in one of the selected channels and confirm that the
assigned ruleset processes it.
