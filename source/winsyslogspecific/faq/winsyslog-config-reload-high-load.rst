.. _winsyslog-config-reload-high-load:


WinSyslog Configuration Reload Not Completing Under High Load
==============================================================

.. meta::
   :author: Andre Lorbach
   :created: 2026-01-13
   :updated: 2026-01-29
   :products: WinSyslog

Overview
--------

This FAQ explains how to troubleshoot and resolve issues where WinSyslog configuration reloads fail to complete during periods of high message volume. The service detects configuration changes but does not finish the reload process, leaving the system in an inconsistent state.

Problem
-------

During periods of high message volume, WinSyslog configuration reloads may fail to complete. The service detects configuration changes but does not finish the reload process, leaving the system in an inconsistent state. This can also cause service stop operations to timeout.

Symptoms
--------

* Configuration changes are detected, but Event ID 126 ("Configuration reload successfully done") is not logged in WinSyslog debug logs
* WinSyslog service stop operations timeout with "Could not stop the service within 20 seconds" errors
* Configuration reloads complete successfully during low-load periods but fail during high-load periods
* Significant time gaps between when configuration changes are detected and when reloads complete (or fail to complete)

Root Cause
----------

During a WinSyslog configuration reload, the service must:

1. Pause message processing
2. Drain in-flight messages from worker threads
3. Re-read the configuration from the Windows registry
4. Reinitialize all rules, filters, and actions
5. Resume message processing
6. Log Event ID 126 to confirm completion

Under high message volume with insufficient worker threads, step 2 (draining in-flight work) takes significantly longer. If WinSyslog is processing many messages simultaneously, the drain phase can extend significantly. In extreme cases, the reload process may appear to stall or never complete, resulting in missing Event ID 126 entries.

**Contributing factors:**

* Insufficient worker threads relative to message volume and CPU cores
* Single syslog input service with single ruleset requiring all messages to be evaluated against all rules sequentially
* High concurrent load relative to available processing capacity

Solution
--------

Option 1: Increase Worker Threads (Immediate Action)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Location in WinSyslog Config Client:** General Options > Queue Manager > Worker Threads

**Recommendation:** Set the "Number of worker threads" to at least half your CPU core count

* If you have 8 cores, use 4 threads
* If you have 16 cores, use 8 threads

**Impact:** Allows more parallel processing in WinSyslog, faster queue drainage during reloads, shorter reload windows

**Steps:**

1. Open WinSyslog Config Client
2. Navigate to **General Options > Queue Manager** section
3. Set **Number of worker threads** to at least **half the CPU core count**
4. Save the configuration

   * If automatic configuration reload is enabled in WinSyslog, the service will reload automatically
   * If automatic configuration reload is disabled, manually restart the WinSyslog service

Option 2: Upgrade to Latest WinSyslog Build.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upgrade to the latest WinSyslog build which includes fixes for configuration-reload issues related to log rotation. This may resolve incomplete reloads observed in logs.

Option 3: Reduce Main Queue Limit (if Action Queue enabled)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Location in WinSyslog Config Client:** General Options > Queue Manager > Main Queue Limit

**Recommendation:** Consider reducing Main Queue Limit to 100,000-200,000 if configured higher

**Impact:** Reduces memory consumption and CPU overhead from WinSyslog queue management. The Action Queue will handle database write buffering separately.

Option 4: Disable Auto-Reload for Production WinSyslog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Location in WinSyslog Config Client:** General Options > Configuration > Auto-Reload settings

**Recommendation:** If WinSyslog configuration changes are infrequent, consider disabling automatic configuration reload

**Procedure:** Perform all WinSyslog configuration changes via manual service restart during maintenance windows

**Impact:** Eliminates the risk of incomplete reloads during high-load periods

Option 5: Split WinSyslog Configuration into Multiple Receivers and RuleSets (Advanced Optimization)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Problem:** A single syslog input service in WinSyslog with a single ruleset requires every message to be evaluated against all rules sequentially, creating significant overhead under high load.

**Solution:** Split WinSyslog configuration by network range into multiple syslog input services and rulesets.

**Performance Impact:**

* Before: 1 syslog input, 1 ruleset, multiple rules, all rules evaluated per message
* After: Multiple syslog inputs, multiple rulesets, fewer rules per ruleset, significantly fewer rules evaluated per message
* Expected results: 75% reduction in rule evaluation, 4-8x throughput improvement

**Benefits:**

* Each WinSyslog syslog input only accepts designated network ranges via permitted senders
* Significant reduction in rule evaluation per message
* Parallel processing: Multiple syslog inputs process simultaneously (4-8x throughput improvement)

**Implementation Steps for WinSyslog:**

1. In WinSyslog Config Client, create new syslog input services with different UDP/TCP ports and permitted senders for each network range
2. Create corresponding new rulesets in WinSyslog and move rules to appropriate rulesets
3. Update network device syslog destinations to send to the new WinSyslog ports
4. Update firewall rules to allow the new WinSyslog ports
5. Test each WinSyslog input/ruleset combination
6. Migrate one network segment at a time (start with smallest segment)
7. Keep original WinSyslog configuration as backup

This is the most effective long-term solution for high-load WinSyslog environments, addressing the root cause by reducing rule evaluation overhead and enabling true parallel processing.

Best Practices for WinSyslog
-----------------------------

* **Worker Threads:** Set to at least half your CPU core count for optimal parallel processing in WinSyslog
* **Action Queue:** Use WinSyslog Action Queue feature at Database Action level instead of increasing main queue limit excessively
* **Configuration Splitting:** For high-load WinSyslog environments, split configuration into multiple syslog input services and rulesets by network range or message type
* **Maintenance Windows:** For production WinSyslog systems with infrequent configuration changes, consider disabling auto-reload and performing manual restarts during maintenance windows
* **Monitoring:** Monitor Event ID 126 entries in WinSyslog debug logs to verify configuration reloads complete successfully
* **Gradual Migration:** When splitting WinSyslog configurations, migrate one network segment at a time and test thoroughly before proceeding

Verification
------------

To verify WinSyslog configuration reloads are completing successfully:

1. Check WinSyslog debug logs for Event ID 126 entries after configuration changes
2. Monitor WinSyslog service stop times - should complete within timeout period
3. Verify WinSyslog configuration changes are applied correctly after reload
4. Monitor worker thread utilization and queue depths during high-load periods in WinSyslog
5. Check that reload completion times are consistent and reasonable (typically 1-2 seconds under normal load)

If Event ID 126 is missing from WinSyslog debug logs after configuration changes, this indicates an incomplete reload and the system may be operating with inconsistent configuration.

