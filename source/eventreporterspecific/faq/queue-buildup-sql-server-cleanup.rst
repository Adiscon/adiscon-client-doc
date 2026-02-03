.. _queue-buildup-sql-server-cleanup-eventreporter:

Queue Buildup During SQL Server Table Cleanup Operations in EventReporter
==========================================================================

This article explains queue buildup issues in EventReporter when performing regular cleanup operations on Microsoft SQL Server SystemEvents tables.

Question
--------

Why does EventReporter's message queue build up when deleting old rows from the SQL Server SystemEvents table, even though the table is not explicitly locked?

Answer
------

When using Microsoft SQL Server as storage via OLEDB or ODBC Actions in EventReporter, performing regular cleanup operations (deleting old rows) on the SystemEvents table may cause EventReporter's message queue to build up even though the table is not explicitly locked. This can occur even with optimized batch delete processes that use primary key-based deletes.

**Note:** This issue applies specifically to EventReporter using Microsoft SQL Server as storage through OLEDB or ODBC Actions. The queue buildup occurs when cleanup operations (DELETE statements) run concurrently with EventReporter's INSERT operations to the same SQL Server database.

Symptoms
--------

- Queue saturation incidents that correlate with cleanup schedule times
- Queue buildup during delete operations, even with batch delete processes
- Brief blocking or slowdowns during cleanup operations
- High memory consumption when queue holds large numbers of messages
- Processing rate barely keeping up with ingestion rate during cleanup

Root Cause
----------

Even with optimized delete processes, several subtle mechanisms can cause contention between INSERT and DELETE operations:

1. **Page-Level Locks**: SQL Server may use page-level locks during deletes. If EventReporter's INSERT operations target the same pages being deleted, brief blocking can occur. With high-frequency inserts (200-400 messages per second or higher), even brief page-level contention can cause queue buildup.

2. **Index Maintenance Overhead**: The primary key index must be maintained during each delete batch. Even with efficient primary key-based deletes, index pages need to be updated, which can cause brief contention that slows INSERT operations.

3. **Transaction Log Activity**: Regular delete operations generate significant transaction log activity. If the transaction log is on the same disk as data files, I/O contention can occur during delete operations, temporarily slowing all database operations including inserts.

4. **Ghost Record Cleanup**: SQL Server marks deleted rows as "ghost records" initially, then cleans them up asynchronously. If ghost record cleanup coincides with high INSERT activity, page-level contention can occur.

These issues are more subtle than traditional locking problems and may not show up as explicit table locks, but can still cause queue buildup during delete operations.

Solution
--------

Option 1: Enhance Delete Process with ROWLOCK Hint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ROWLOCK hint forces SQL Server to keep locks at the row level instead of escalating to page-level locks, which means INSERT operations can proceed on other rows within the same pages even while deletes are running. Adding OPTION (MAXDOP 1) prevents parallel execution that could escalate locks.

**Implementation:**

.. code-block:: sql

   DELETE TOP (5000) FROM SystemEvents WITH (ROWLOCK)
   WHERE [Date] < DATEADD(day, -1, GETDATE())
   OPTION (MAXDOP 1);

**Benefits:**

- Simple change that can reduce blocking
- No SQL Server edition changes required
- Works with Standard Edition
- Reduces lock escalation to page level

**Considerations:**

- Provides partial improvement, not complete elimination of contention
- Still requires index maintenance during deletes

Option 2: Separate Transaction Log Disk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Place the transaction log on a separate physical disk, separate from data files. This is a SQL Server best practice and eliminates I/O contention between log writes and data file operations.

**Benefits:**

- Eliminates I/O contention between log and data operations
- Works with any SQL Server edition
- Best practice for SQL Server configuration

**Considerations:**

- Requires separate physical disk or storage volume
- Addresses I/O contention only, not locking issues

Option 3: Table Partitioning (Enterprise Edition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Partition the SystemEvents table by date (e.g., daily partitions). Inserts always go to today's partition while deletes target old partitions that no longer receive inserts, completely eliminating contention. When cleaning up, use partition switching to instantly move an entire partition to a staging table and drop it - this is a metadata-only operation that takes milliseconds instead of minutes.

**Benefits:**

- Completely eliminates contention between inserts and deletes
- Partition switching is a metadata-only operation (milliseconds)
- Inserts and deletes operate on different partitions

**Considerations:**

- Requires SQL Server Enterprise Edition
- Requires initial setup and ongoing partition management
- More complex implementation

Option 4: Delayed Durability (If Acceptable Risk)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This can improve insert performance by 20-40% by deferring transaction log writes. However, there's a risk of losing the last few seconds of inserts if the server crashes before the log is flushed.

**Implementation:**

.. code-block:: sql

   ALTER DATABASE [DatabaseName] SET DELAYED_DURABILITY = ALLOWED;

**Benefits:**

- Significant performance improvement (20-40%)
- Works with Standard Edition
- Simple configuration change

**Considerations:**

- Risk of data loss if server crashes before log flush
- Addresses I/O performance only, not locking issues
- May not be acceptable for all environments

Best Practices
--------------

1. **Monitor Queue Saturation Correlation**: Check whether queue saturation incidents correlate with cleanup schedule times. If deletes run on a regular schedule and queue buildup occurs at predictable intervals, this strongly suggests the cleanup process is a contributing factor.

2. **Monitor SQL Server Blocking**: Use the following query to check for blocking during delete operations:

.. code-block:: sql

   SELECT
   r.session_id,
   r.blocking_session_id,
   r.wait_type,
   r.wait_time,
   SUBSTRING(t.text, 1, 200) AS QueryText
   FROM sys.dm_exec_requests r
   CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) t
   WHERE r.blocking_session_id > 0;

3. **Optimize Batch Delete Process**: Use primary key-based deletes with appropriate batch sizes (e.g., 5000 rows) to balance performance and lock duration. Using the primary key ensures efficient index seeks.

4. **Isolate Parsing Workload**: If using separate processes for parsing, use (NOLOCK) hints to completely isolate the parsing workload from EventReporter's insert operations.

5. **Verify Transaction Log Location**: Ensure transaction log is on separate physical disk from data files to eliminate I/O contention.

6. **Consider Action Queue Feature**: Use Action Queue feature at Database Action level (OLEDB or ODBC Actions) instead of increasing main queue limit excessively. This can help manage queue buildup during temporary database slowdowns.

Related Settings
----------------

- **Main Queue Limit**: The maximum number of messages that can be queued in EventReporter. Large limits (e.g., 2-4 million) can cause increased CPU overhead and memory consumption when queue is full.

- **Worker Threads**: Number of worker threads for parallel processing in EventReporter. Increasing worker threads (e.g., from 2 to 4) can improve parallel processing during normal operations.

- **Action Queue**: Feature at Database Action level (OLEDB or ODBC Actions) in EventReporter that provides additional buffering during temporary database slowdowns. Recommended over excessive main queue limits.

- **Database Connection Settings**: Connection timeout and retry settings for SQL Server connections via OLEDB or ODBC Actions in EventReporter.

Verification
------------

To verify if cleanup process is contributing to queue issues in EventReporter:

1. **Check Timing Correlation**: Monitor whether queue saturation incidents occur at predictable intervals matching cleanup schedule.

2. **Monitor Blocking**: Run the blocking query during cleanup operations to identify any blocking sessions.

3. **Review SQL Server Wait Statistics**: Check for PAGEIOLATCH, LCK_M_* wait types during cleanup operations.

4. **Monitor Transaction Log Activity**: Check transaction log file growth and I/O during cleanup operations.

5. **Review Queue Metrics**: Monitor queue depth over time in EventReporter and correlate with cleanup schedule to identify patterns.

If queue buildup incidents correlate with cleanup schedule times, the recommendations described above can help address the contention issues.
