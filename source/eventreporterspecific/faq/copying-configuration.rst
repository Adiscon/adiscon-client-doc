.. _copying-configuration-eventreporter:

How to Copy the EventReporter Configuration to Other Servers
============================================================

Question
--------

How can I copy an EventReporter configuration to other servers?

Answer
------

Export the configuration from one EventReporter system as a text-based registry
file and import it on the target systems.

Details
-------

This is useful when several servers should use the same rulesets, actions, and
service structure. It avoids rebuilding the same configuration manually on each
system.

Action path
-----------

1. Open the EventReporter Configuration Client on the source system.
2. Go to **Computer -> Export Settings to Registry File**.
3. Save the export as a text-based ``.reg`` file.
4. Copy the file to the target systems.
5. Import the file on each target system.
6. Open the EventReporter Configuration Client and review any system-specific
   values such as local file paths, credentials, or target hosts.
7. Apply the configuration and restart the EventReporter service if required.

Related information
-------------------

* :doc:`mass-rollout-deployment`
* :doc:`export-settings-support-call`
