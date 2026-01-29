.. _rsyslogwa-config-reload-high-load:


Rsyslog Windows Agent Configuration Reload Not Completing Under High Load
==========================================================================

.. meta::
   :author: Andre Lorbach
   :created: 2026-01-13
   :updated: 2026-01-29
   :products: Rsyslog Windows Agent

Overview
--------

This FAQ explains how to troubleshoot and resolve issues where Rsyslog Windows Agent configuration reloads fail to complete during periods of high message volume. The service detects configuration changes but does not finish the reload process, leaving the system in an inconsistent state.

Problem
-------

During periods of high message volume, Rsyslog Windows Agent configuration reloads may fail to complete. The service detects configuration changes but does not finish the reload process, leaving the system in an inconsistent state. This can also cause service stop operations to timeout.

Symptoms
--------

* Configuration changes are detected, but Event ID 126 ("Configuration reload successfully done") is not logged in Rsyslog Windows Agent debug logs
* Rsyslog Windows Agent service stop operations timeout with "Could not stop the service within 20 seconds" errors
* Configuration reloads complete successfully during low-load periods but fail during high-load periods
* Significant time gaps between when configuration changes are detected and when reloads complete (or fail to complete)

Root Cause
----------

During a Rsyslog Windows Agent configuration reload, the service must:

1. Pause message processing
2. Drain in-flight messages from worker threads
3. Re-read the configuration file
4. Reinitialize all rules, filters, and actions
5. Resume message processing
6. Log Event ID 126 to confirm completion

Under high message volume with insufficient worker threads, step 2 (draining in-flight work) takes significantly longer. If Rsyslog Windows Agent is processing many messages simultaneously, the drain phase can extend significantly. In extreme cases, the reload process may appear to stall or never complete, resulting in missing Event ID 126 entries.

**Contributing factors:**

* Insufficient worker threads relative to message volume and CPU cores
* Single input service with single ruleset requiring all messages to be evaluated against all rules sequentially
* High concurrent load relative to available processing capacity

Solution
--------

Option 1: Increase Worker Threads (Immediate Action)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Location in Rsyslog Windows Agent:** Queue Manager > Worker Threads

**Recommendation:** Set the "Number of worker threads" to at least half your CPU core count

* If you have 8 cores, use 4 threads
* If you have 16 cores, use 8 threads

**Impact:** Allows more parallel processing in Rsyslog Windows Agent, faster queue drainage during reloads, shorter reload windows

**Steps:**

1. Open the Rsyslog Windows Agent configuration interface
2. Navigate to the **Queue Manager** section
3. Set **Number of worker threads** to at least **half the CPU core count**
4. Save the configuration

   * If automatic configuration reload is enabled in Rsyslog Windows Agent, the service will reload automatically
   * If automatic configuration reload is disabled, manually restart the Rsyslog Windows Agent service

Option 2: Upgrade to Latest Rsyslog Windows Agent Build.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upgrade to the latest Rsyslog Windows Agent build which includes fixes for configuration-reload issues related to log rotation. This may resolve incomplete reloads observed in logs.

Option 3: Reduce Main Queue Limit (if Action Queue enabled)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Location in Rsyslog Windows Agent:** Queue Manager > Main Queue Limit

**Recommendation:** Consider reducing Main Queue Limit to 100,000-200,000 if configured higher

**Impact:** Reduces memory consumption and CPU overhead from Rsyslog Windows Agent queue management. The Action Queue will handle database write buffering separately.

Option 4: Disable Auto-Reload for Production Rsyslog Windows Agent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Location in Rsyslog Windows Agent:** Configuration > Auto-Reload settings

**Recommendation:** If Rsyslog Windows Agent configuration changes are infrequent, consider disabling automatic configuration reload

**Procedure:** Perform all Rsyslog Windows Agent configuration changes via manual service restart during maintenance windows

**Impact:** Eliminates the risk of incomplete reloads during high-load periods

Option 5: Split Rsyslog Windows Agent Configuration into Multiple Inputs and RuleSets (Advanced Optimization)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Problem:** A single input service in Rsyslog Windows Agent with a single ruleset requires every message to be evaluated against all rules sequentially, creating significant overhead under high load.

**Solution:** Split Rsyslog Windows Agent configuration by network range or message type into multiple input services and rulesets.

**Performance Impact:**

* Before: 1 input, 1 ruleset, multiple rules, all rules evaluated per message
* After: Multiple inputs, multiple rulesets, fewer rules per ruleset, significantly fewer rules evaluated per message
* Expected results: 75% reduction in rule evaluation, 4-8x throughput improvement

**Benefits:**

* Each Rsyslog Windows Agent input only accepts designated network ranges or message types
* Significant reduction in rule evaluation per message
* Parallel processing: Multiple inputs process simultaneously (4-8x throughput improvement)

**Implementation Steps for Rsyslog Windows Agent:**

1. In Rsyslog Windows Agent configuration, create new input services with different ports for each network range or message type
2. Create corresponding new rulesets in Rsyslog Windows Agent and move rules to appropriate rulesets
3. Update network device syslog destinations to send to the new Rsyslog Windows Agent ports
4. Update firewall rules to allow the new Rsyslog Windows Agent ports
5. Test each Rsyslog Windows Agent input/ruleset combination
6. Migrate one network segment or message type at a time (start with smallest)
7. Keep original Rsyslog Windows Agent configuration as backup

This is the most effective long-term solution for high-load Rsyslog Windows Agent environments, addressing the root cause by reducing rule evaluation overhead and enabling true parallel processing.

Best Practices for Rsyslog Windows Agent
-----------------------------------------

* **Worker Threads:** Set to at least half your CPU core count for optimal parallel processing in Rsyslog Windows Agent
* **Action Queue:** Use Rsyslog Windows Agent Action Queue feature at Database Action level instead of increasing main queue limit excessively
* **Configuration Splitting:** For high-load Rsyslog Windows Agent environments, split configuration into multiple input services and rulesets by network range or message type
* **Maintenance Windows:** For production Rsyslog Windows Agent systems with infrequent configuration changes, consider disabling auto-reload and performing manual restarts during maintenance windows
* **Monitoring:** Monitor Event ID 126 entries in Rsyslog Windows Agent debug logs to verify configuration reloads complete successfully
* **Gradual Migration:** When splitting Rsyslog Windows Agent configurations, migrate one network segment or message type at a time and test thoroughly before proceeding

Verification
------------

To verify Rsyslog Windows Agent configuration reloads are completing successfully:

1. Check Rsyslog Windows Agent debug logs for Event ID 126 entries after configuration changes
2. Monitor Rsyslog Windows Agent service stop times - should complete within timeout period
3. Verify Rsyslog Windows Agent configuration changes are applied correctly after reload
4. Monitor worker thread utilization and queue depths during high-load periods in Rsyslog Windows Agent
5. Check that reload completion times are consistent and reasonable (typically 1-2 seconds under normal load)

If Event ID 126 is missing from Rsyslog Windows Agent debug logs after configuration changes, this indicates an incomplete reload and the system may be operating with inconsistent configuration.

