.. _config-reload-high-load-mwagent:

Configuration reload issues under high load in MonitorWare Agent
===============================================================

This article explains why MonitorWare Agent configuration reloads can stall under heavy load and how to stabilize reload behavior.

Applies To
----------

* MonitorWare Agent

Problem
-------

During periods of high message volume, MonitorWare Agent detects configuration changes but may not complete the reload process. The service can appear to hang during reloads and stop requests can time out.

Symptoms
--------

* Configuration changes are detected, but Event ID 126 ("Configuration reload successfully done") is not logged
* Service stop operations timeout with "Could not stop the service within 20 seconds" errors
* Reloads complete successfully during low-load periods but fail during high-load periods
* Noticeable time gaps between detection of a configuration change and reload completion

Root Cause
----------

A configuration reload requires the service to pause message processing, drain in-flight work, reload configuration data, reinitialize rules and actions, and then resume processing. Under high message volume, draining in-flight work takes much longer when worker threads are insufficient, which stretches the reload window and can prevent completion.

Solution
--------

Option 1: Increase worker threads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open the MonitorWare Agent Configuration Client.
2. Navigate to **General Options > Queue Manager**.
3. Set **Number of worker threads** to at least half the CPU core count.

   * Example: For an 8-core system, set at least 4 worker threads.
   * Example: For a 16-core system, set at least 8 worker threads.

4. Save the configuration and allow MonitorWare Agent to reload.

Option 2: Upgrade to the latest build
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upgrade to the latest MonitorWare Agent build to pick up fixes that address configuration reload and log rotation behavior under load.

Option 3: Reduce the Queue Limit when Action Queue is enabled
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you use Action Queue on database actions, review **General Options > General > Queue Limit** and keep it around 100,000 to 200,000 when configured higher. This reduces queue management overhead while Action Queue continues to buffer output.

Option 4: Disable automatic reload in production
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If configuration changes are infrequent, clear **Automatically reload service on configuration changes** in **General Options > General** and perform manual service restarts during maintenance windows.

Option 5: Split configuration into multiple services and rulesets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A single high-volume service with a single ruleset forces every message to be evaluated against all rules. Split the configuration so each service uses a smaller ruleset.

Implementation steps:

1. Create additional services for the highest-volume inputs.
2. Create matching rulesets and move rules to the appropriate ruleset.
3. Update data sources to use the new services.
4. Test each service and ruleset combination.
5. Migrate one source at a time.
6. Keep the original configuration as a backup until migration is complete.

Best Practices
--------------

* Set worker threads to at least half the CPU core count.
* Use Action Queue for database actions instead of oversizing the main queue.
* Plan reloads during low-traffic periods or scheduled maintenance windows.
* Monitor for "Configuration reload successfully done" entries to confirm reload completion.

Verification
------------

1. Check the Windows Application Event Log for the reload completion message after configuration changes.
2. Confirm MonitorWare Agent service stop operations complete within the timeout period.
3. Monitor worker thread utilization and queue depth during peak load.
4. Verify reload completion times are consistent under normal conditions.
