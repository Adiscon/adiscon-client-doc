Configuration Reload Not Completing Under High Load
====================================================

This article explains what to do when configuration reloads fail to complete during periods of high message volume, leaving the service in an inconsistent state or causing service stop operations to timeout.

Problem
-------

During periods of high message volume, configuration reloads may fail to complete. The service detects configuration changes but does not finish the reload process, leaving the system in an inconsistent state. This can also cause service stop operations to timeout.

Symptoms
--------

* Configuration changes are detected, but Event ID 126 ("Configuration reload successfully done") is not logged
* Service stop operations timeout with "Could not stop the service within 20 seconds" errors
* Configuration reloads complete successfully during low-load periods but fail during high-load periods
* Significant time gaps between when configuration changes are detected and when reloads complete (or fail to complete)

Root Cause
----------

During a configuration reload, MonitorWare Agent must:

1. Pause message processing
2. Drain in-flight messages from worker threads
3. Re-read the configuration from its storage location
4. Reinitialize all rules, filters, and actions
5. Resume message processing
6. Log Event 126 to confirm completion

Under high message volume with insufficient worker threads, step 2 (draining in-flight work) takes significantly longer. If the system is processing many messages simultaneously, the drain phase can extend significantly. In extreme cases, the reload process may appear to stall or never complete, resulting in missing Event 126 entries.

**Contributing factors:**

* Insufficient worker threads relative to message volume and CPU cores
* Single input service with single ruleset requiring all messages to be evaluated against all rules sequentially
* High concurrent load relative to available processing capacity

Solution
--------

Option 1: Increase Worker Threads (Immediate Action)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Location:** General > QueueManager > Worker Threads

**Recommendation:** Set to at least half your CPU core count

* If you have 8 cores, use 4 threads
* If you have 16 cores, use 8 threads

**Impact:** Allows more parallel processing, faster queue drainage during reloads, shorter reload windows

Option 2: Upgrade to Latest Build
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upgrade to the latest build which includes fixes for configuration-reload issues related to log rotation. This may resolve incomplete reloads observed in logs.

Option 3: Reduce Main Queue Limit (if Action Queue enabled)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Location:** General > QueueManager > Main Queue Limit

**Recommendation:** Consider reducing Main Queue Limit to 100,000-200,000 if configured higher!

**Impact:** Reduces memory consumption and CPU overhead from queue management. The Action Queue will handle database write buffering separately.

Option 4: Disable Auto-Reload for Production
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Location:** General > Configuration > Auto-Reload settings

**Recommendation:** If configuration changes are infrequent, consider disabling automatic configuration reload

**Procedure:** Perform all changes via manual service restart during maintenance windows

**Impact:** Eliminates the risk of incomplete reloads during high-load periods

Option 5: Split Configuration into Multiple Receivers and RuleSets (Advanced Optimization)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Problem:** A single input service with a single ruleset requires every message to be evaluated against all rules sequentially, creating significant overhead under high load.

**Solution:** Split configuration by network range into multiple input services and rulesets.

**Performance Impact:**

* Before: 1 input, 1 ruleset, multiple rules, all rules evaluated per message
* After: Multiple inputs, multiple rulesets, fewer rules per ruleset, significantly fewer rules evaluated per message
* Expected: 75% reduction in rule evaluation, 4-8x throughput improvement

**Benefits:**

* Each input only accepts designated network ranges via permitted senders
* Significant reduction in rule evaluation per message
* Parallel processing: Multiple inputs process simultaneously (4-8x throughput improvement)

**Implementation Steps:**

1. Create new input services with different ports and permitted senders for each network range
2. Create corresponding new rulesets and move rules to appropriate rulesets
3. Update network device syslog destinations to use new ports
4. Update firewall rules for new ports
5. Test each input/ruleset combination
6. Migrate one network segment at a time (start with smallest segment)
7. Keep original configuration as backup

This is the most effective long-term solution for high-load environments, addressing the root cause by reducing rule evaluation overhead and enabling true parallel processing.

Best Practices
--------------

* **Worker Threads:** Set to at least half your CPU core count for optimal parallel processing
* **Action Queue:** Use Action Queue feature at Database Action level instead of increasing main queue limit excessively
* **Configuration Splitting:** For high-load environments, split configuration into multiple input services and rulesets by network range or message type
* **Maintenance Windows:** For production systems with infrequent configuration changes, consider disabling auto-reload and performing manual restarts during maintenance windows
* **Monitoring:** Monitor Event ID 126 entries in logs to verify configuration reloads complete successfully
* **Gradual Migration:** When splitting configurations, migrate one network segment at a time and test thoroughly before proceeding

Verification
------------

To verify configuration reloads are completing successfully:

1. Check debug logs for Event ID 126 entries after configuration changes
2. Monitor service stop times - should complete within timeout period
3. Verify configuration changes are applied correctly after reload
4. Monitor worker thread utilization and queue depths during high-load periods
5. Check that reload completion times are consistent and reasonable (typically 1-2 seconds under normal load)

If Event ID 126 is missing after configuration changes, this indicates an incomplete reload and the system may be operating with inconsistent configuration.
