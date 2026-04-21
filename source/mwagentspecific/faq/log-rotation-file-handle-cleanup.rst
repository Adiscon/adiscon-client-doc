.. _log-rotation-file-handle-cleanup-mwagent:

Why were dynamic log files sometimes not rotated in older MonitorWare Agent versions?
======================================================================================

Older MonitorWare Agent versions could miss some scheduled rotations when
dynamic filenames were combined with file-handle cleanup. That historical
behavior affected older releases and was improved in later versions of the
shared log rotation subsystem.

For the guarantees of the current subsystem, including graceful shutdown,
restart recovery, reload behavior, and dynamic filename support, see
:doc:`../../shared/faq/log-rotation-guarantees`.

Summary
-------

In affected older versions, unused dynamic log file handles could already be
closed when a scheduled rotation time arrived. In that case, the product could
skip the rotation for that inactive file.

If you are still running one of those older builds, increasing the file handle
cleanup timeout can reduce the chance of missing a scheduled rotation, but the
recommended long-term solution is to upgrade to a current release.
