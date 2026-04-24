.. _log-rotation-short-delay-eventreporter:

Why does log rotation fail when using ZIP compression in EventReporter?
========================================================================

This article explains why log rotation preparation can time out before the service detaches a file for background compression or move processing.

Problem
-------

Log rotation preparation can fail when the "Maximum wait time for log rotation" setting is too short for the File Action to acquire the rotation mutex while the service is busy.

Symptoms
--------

* Log files are compressed into ZIP format but remain in the live logging directory
* Rotation is skipped or deferred because the rotation preparation mutex could not be acquired in time
* Incomplete log rotation leaves compressed files in active directories
* Current day logs may be archived prematurely when using time-based rotation triggers

Root Cause
----------

The "Maximum wait time for log rotation" setting in the EventReporter Configuration Client controls how long rotation preparation waits to acquire the File Action rotation mutex. Compression and move operations run afterward as detached background work. When this wait is too short, the file may not be detached for rotation under load.

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

* Set the rotation wait time to at least 60 seconds when the service is busy or storage is slow
* Consider increasing to 120 seconds for large log files or slow storage systems
* Use size-based rotation instead of time-based to prevent current-day log pre-archiving

Related Settings
----------------

* **Maximum wait time for log rotation**: Controls how long rotation preparation waits for the File Action rotation mutex (in milliseconds)
* **Rotation trigger**: Determines when rotation begins (time-based vs size-based)
* **Compression method**: Affects processing time (ZIP compression takes longer than other methods)

Verification
------------

* Monitor log directories after rotation triggers to ensure files are properly moved
* Check that compressed files are not remaining in live logging directories
* Verify rotation completes within expected timeframes
* Confirm no rotation failures in EventReporter logs during test periods
