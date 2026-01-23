.. _log-rotation-short-delay-eventreporter:

Why does log rotation fail when using ZIP compression in EventReporter?
========================================================================

This article explains why log rotation operations fail when the rotation action delay setting is configured too short, causing ZIP compression to be interrupted by the move operation before completion.

Problem
-------

Log rotation operations fail when the rotation action delay setting is configured too short, causing ZIP compression to be interrupted by the move operation before completion.

Symptoms
--------

* Log files are compressed into ZIP format but remain in the live logging directory
* Move operations fail after the configured delay period
* Incomplete log rotation leaves compressed files in active directories
* Current day logs may be archived prematurely when using time-based rotation triggers

Root Cause
----------

The "Maximum wait time for log rotation" setting in the EventReporter Configuration Client controls the waiting period between when log rotation is triggered and when move operations begin. When this delay is too short (such as the default 15 seconds), ZIP compression processes that take longer than the delay period get interrupted by the move operation, causing the rotation to fail.

Solution
--------

Option 1: Increase Maximum Wait Time for Log Rotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open the EventReporter Configuration Client
2. Navigate to the rotation settings section
3. Locate the "Maximum wait time for log rotation" setting
4. Change the value from 15000 (15 seconds) to 60000 (60 seconds) or 120000 (120 seconds)
5. Save the configuration and restart the EventReporter service
6. Test log rotation during the next scheduled rotation period

Option 2: Switch to Size-Based Rotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Change rotation trigger from time-based to size-based
2. Configure appropriate file size thresholds for rotation
3. Adjust rotation timing to avoid current-day log pre-archiving
4. Test rotation behavior with smaller log files first

Best Practices
--------------

* Set rotation action delay to at least 60 seconds when using ZIP compression
* Consider increasing to 120 seconds for large log files or slow storage systems
* Use size-based rotation instead of time-based to prevent current-day log pre-archiving

Related Settings
----------------

* **Maximum wait time for log rotation**: Controls the delay between rotation trigger and move operations (in milliseconds)
* **Rotation trigger**: Determines when rotation begins (time-based vs size-based)
* **Compression method**: Affects processing time (ZIP compression takes longer than other methods)

Verification
------------

* Monitor log directories after rotation triggers to ensure files are properly moved
* Check that compressed files are not remaining in live logging directories
* Verify rotation completes within expected timeframes
* Confirm no rotation failures in EventReporter logs during test periods
