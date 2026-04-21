.. include:: ../faq-supporting-labels.rst

.. _log-rotation-guarantees:

What does the current log rotation subsystem guarantee?
=======================================================

This article summarizes the operational guarantees for the current log rotation
subsystem used by Adiscon products that write log files through the shared
Himalaya engine.

Normal operation
----------------

When log rotation is enabled, the service first detaches the current live log
file and then continues writing to the normal live file name. The follow-up
rotation work such as retention renaming, compression, and move-after-rotate is
handled asynchronously in the background.

This design means that new logging can continue even when post-processing takes
longer than expected.

Graceful shutdown
-----------------

Graceful shutdown is still bounded by the existing engine setting
``nLogRotateWorkerStopWaitTimeout``.

During shutdown the service:

* stops accepting new background rotation work immediately
* lets existing background workers continue for up to the configured wait time
* exits when that wait time is reached instead of waiting forever

If a background rotation finishes inside that wait time, it completes normally.
If it does not finish in time, the unfinished detached work is saved and
resumed on the next startup.

Restart recovery
----------------

The service now persists both:

* queued detached rotations that have not started yet
* detached rotations that were already active in the background worker

On the next startup, that saved work is loaded and resumed before normal new
runtime traffic begins. This prevents detached rotated files from being lost
just because service shutdown happened during compression or move-after-rotate.

Configuration reload
--------------------

Configuration reload does not intentionally tear down the asynchronous log
rotation subsystem. It keeps ownership of detached rotation work while runtime
settings are reapplied.

If the current background workers cannot be drained safely inside the bounded
wait timeout, the service keeps the existing log rotation worker pool instead
of dropping ownership of detached files during reload.

Dynamic filenames and segments
------------------------------

Rotation is supported together with dynamic filenames and segmented files. Each
concrete discovered file is rotated independently, and any unfinished detached
rotation for that file is recovered on restart in the same way as for
non-dynamic file names.

Time-of-day rotation after restart
----------------------------------

This hardening work does not change time-of-day catch-up behavior.

If the service restarts after the configured rotation time for the day, it does
not automatically create an additional catch-up rotation just because that time
was missed while the service was stopped.

What this does not mean
-----------------------

The current guarantee is about bounded graceful shutdown and restart recovery.
It should not be read as a promise that every single filesystem operation is
transactional across arbitrary machine crashes or power loss.

Related configuration
---------------------

The main setting that affects shutdown behavior is:

* ``nLogRotateWorkerStopWaitTimeout``: the maximum time the service waits for
  background rotation work during graceful shutdown

No additional log rotation shutdown setting is required for the current
recovery behavior.
