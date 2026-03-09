.. _rsyslogwa-copying-configuration:

How Can I Copy an rsyslog Windows Agent Configuration to Another System?
========================================================================

Answer
------

Export the configuration from the source system, import it on the target
system, then review host-specific settings before applying it.

Details
-------

The safest method is to export the configuration as a text-based registry file
from the Configuration Client and import it on the destination system.

Before applying the imported configuration, review:

- target host names or IP addresses
- TLS certificate paths
- service account or path differences
- local file paths used by debug logs or queues

Action path
-----------

1. Export the configuration from the source system.
2. Transfer the exported file to the destination system.
3. Open the rsyslog Windows Agent Configuration Client on the destination
   system.
4. Import the configuration file.
5. Review environment-specific settings.
6. Save and apply the configuration.
7. Restart the service if required.

Related information
-------------------

* :doc:`export-settings-support-call`
* :doc:`../tutorial-export-config-and-debug-log`
