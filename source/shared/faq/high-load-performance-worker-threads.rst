:orphan:

.. _high-load-performance-worker-threads:

How to resolve performance issues on high-load systems?
========================================================

This article explains how to resolve performance issues such as slow configuration reloads, extended service start/stop times, queue buildup, and potential timeouts during service operations on systems with high message volume.

Applies To
----------

* WinSyslog
* MonitorWare Agent
* Rsyslog Windows Agent

Problem
-------

On systems with high message volume, these products may experience performance issues such as slow configuration reloads, extended service start/stop times, queue buildup, and potential timeouts during service operations. These issues are more likely to occur when the system is processing many messages with insufficient worker threads.

Symptoms
--------

* Configuration reloads take longer than expected or appear to hang
* Service restart operations timeout with "Could not stop the service within 20 seconds" error
* Extended service start and stop times, especially when debug logging is enabled
* Queue buildup during high message volume periods
* Slow filter and action processing during peak load
* System appears unresponsive during configuration changes

Root Cause
----------

Under high message load, these products need sufficient parallel processing capacity to handle incoming messages efficiently. When worker threads are too few relative to the CPU cores and message volume:

* Filters and actions cannot run in parallel effectively
* Queues drain slowly, causing message buildup
* Configuration reload windows stretch because in-flight work drains slowly
* Service start/stop operations take longer because the service must wait for in-flight work to complete

The default worker thread count may be insufficient for high-load systems with multiple CPU cores.

Solution
--------

Primary Recommendation: Increase Worker Threads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The most important setting for high-load systems is the Worker Threads configuration:

**For WinSyslog:**

1. Open WinSyslog Config Client
2. Navigate to **QueueManager** section
3. Set **Worker Threads** to at least **half the CPU core count**

   * Example: For an 8-core system, set to at least 4 worker threads
   * Example: For a 16-core system, set to at least 8 worker threads

4. Save the configuration

   * If automatic configuration reload is enabled, the service will reload automatically
   * If automatic configuration reload is disabled, manually restart the service

**For MonitorWare Agent and Rsyslog Windows Agent:**

1. Open the product configuration interface
2. Navigate to the **QueueManager** or equivalent section (location may vary by product)
3. Set **Worker Threads** to at least **half the CPU core count**

   * Example: For an 8-core system, set to at least 4 worker threads
   * Example: For a 16-core system, set to at least 8 worker threads

4. Save the configuration

   * If automatic configuration reload is enabled, the service will reload automatically
   * If automatic configuration reload is disabled, manually restart the service

**Why this helps:**

* Allows filters and actions to run in parallel
* Drains queues faster during high message volume
* Reduces configuration reload window duration under load
* Improves overall system responsiveness during peak periods

Additional Recommendations for High-Load Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Test Configuration Changes on Test System First**

For busy production systems, avoid making large configuration changes directly:

1. Perform larger configuration changes on a test system first
2. Verify the changes work correctly on the test system
3. Import the verified configuration into the production system
4. If automatic configuration reload is enabled, the service will reload automatically after saving
5. If automatic configuration reload is disabled, manually restart the service (from Config Client or Windows Services Management Console)
6. Monitor system performance after the change

**Use Windows Services Management Console for Service Operations**

If automatic configuration reload is disabled and you need to restart the service, or if the configuration client service restart fails or times out:

1. Open Windows Services Management Console (services.msc)
2. Locate the product service (WinSyslog, MonitorWare Agent, or Rsyslog Windows Agent service)
3. Right-click and select **Restart** (or **Stop** then **Start**)
4. The Services Console provides more reliable service control under high load

**Note:** If automatic configuration reload is enabled, manual service restart is typically not needed after configuration changes.

**Allow Sufficient Time for Operations**

On high-load systems, allow adequate time for:

* Configuration reloads to complete
* Service restarts to finish
* Queue processing to catch up after changes

Avoid making multiple rapid configuration changes in succession.

Best Practices
--------------

* **Set Worker Threads to at least half the CPU core count** - This is the most critical setting for high-load systems
* **Test configuration changes on a test system first** - Reduces risk of issues on production systems
* **Monitor system performance** - Watch for queue buildup, slow processing, or extended operation times
* **Avoid debug logging on production systems** - Debug logging significantly increases processing overhead and extends operation times
* **Plan configuration changes during lower-traffic periods** - When possible, schedule major changes during maintenance windows
* **Monitor Event ID 126 (WinSyslog)** - Verify that configuration reloads complete successfully ("Configuration reload successfully done")

Related Settings
----------------

* **Worker Threads** (QueueManager section or equivalent): Number of parallel worker threads for processing filters and actions. **Critical setting for high-load systems** - should be set to at least half the CPU core count for optimal performance. Default values may be too low for systems with many CPU cores. Location may vary by product (QueueManager section in WinSyslog, equivalent section in MonitorWare Agent and Rsyslog Windows Agent).
* **Main Queue Limit** (General section or equivalent): Maximum number of messages that can be queued. On high-load systems, ensure this is set appropriately to handle peak message volumes.
* **Event ID 126 (WinSyslog)**: Windows Event Log entry that indicates "Configuration reload successfully done". Monitor this to verify that configuration reloads complete successfully in WinSyslog.
* **Debug Logging**: Should be disabled on production high-load systems as it significantly increases processing overhead and extends operation times.

Verification
------------

To verify that worker thread settings are appropriate:

1. Check the current Worker Threads setting in QueueManager section
2. Determine your system's CPU core count
3. Verify that Worker Threads is set to at least half the CPU core count
4. Monitor system performance during peak message volume:

   * Check for queue buildup
   * Monitor service responsiveness
   * Verify configuration reloads complete in reasonable time
   * Check for timeout errors during service operations

If performance issues persist after adjusting worker threads, consider:

* Further increasing worker threads (up to the CPU core count)
* Reviewing filter and action complexity
* Checking for database or output bottlenecks
* Collecting debug logs during peak load for analysis (on test systems only)
