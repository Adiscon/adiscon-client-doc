:orphan:

.. only:: winsyslog or winsyslog_j or mwagent or eventreporter or rsyslog

   .. _err-2026-005-file-rotation-startup-pending:

   ERR-2026-005: File Action rotation can remain pending after service startup
   ===========================================================================

   **Status:** Scheduled

   **Publication:** Draft prepared for review

   **First published:** Pending publication

   Description
   -----------

   When licensed File Action rotation is enabled and a rotation occurs while
   the service is starting, the rotated file may remain in a pending file
   instead of completing its configured move or compression. The expected
   archive may therefore be missing even though the rotated log contents are
   still retained.

   Affected products
   -----------------

   The following released service builds are confirmed affected:

   - **WinSyslog:** ``26.07.0.768``, ``26.08.0.773``, and ``26.09.0.774``
   - **MonitorWare Agent:** ``26.07.0.683``, ``26.08.0.688``, and
     ``26.09.0.689``
   - **EventReporter:** ``26.07.0.603``, ``26.08.0.608``, and ``26.09.0.609``
   - **rsyslog Windows Agent:** ``26.07.0.347``, ``26.08.0.352``,
     ``26.09.0.353``, and ``26.10.0.354``

   These are the affected releases confirmed so far. The earliest affected
   release has not been established, and other versions are not confirmed as
   unaffected.

   Impact
   ------

   A rotated file may not reach its configured archive location or complete
   its configured compression. Its contents remain retained in the pending
   file. This condition does not by itself indicate that the log data was
   deleted.

   How to determine whether you are affected
   -----------------------------------------

   Check whether File Action rotation is enabled and whether the expected
   archive is missing after a service start. Look for the rotated contents in
   any retained pending files. If you cannot identify them, contact Adiscon
   Support before changing those files.

   Workarounds
   -----------

   Preserve the original and pending files. Do not delete or manually rename
   them. Contact Adiscon Support for recovery guidance, and provide the product
   name, service version, and the affected File Action configuration.

   Resolution status
   -----------------

   A correction is scheduled. No corrected service build has been publicly
   confirmed. The first fixed version is not yet known; this notice will be
   updated when a corrected release is published.

   Revision history
   ----------------

   - **October 8, 2026:** Draft prepared for review; not published.
