:orphan:

.. only:: mwagent or eventreporter or rsyslog

   .. _err-2026-004-eventlog-resume-first-event:

   ERR-2026-004: The first event after a subscription restart can be skipped
   ===========================================================================

   **Status:** Scheduled

   **Publication:** Draft prepared for review

   **First published:** Pending publication

   Description
   -----------

   When a supported Windows Event Log subscription restarts and resumes from a
   saved position, the first new event after that position can be skipped.
   Later events can continue to be processed, leaving a single-record gap near
   the time the subscription resumed.

   Affected products
   -----------------

   The following released service builds are confirmed affected:

   - **MonitorWare Agent:** ``26.7.0.683``, ``26.8.0.688``, and ``26.9.0.689``
   - **EventReporter:** ``26.7.0.603``, ``26.8.0.608``, and ``26.9.0.609``
   - **rsyslog Windows Agent:** ``26.7.0.347``, ``26.8.0.352``, and
     ``26.9.0.353``

   These are the affected releases confirmed so far. The earliest affected
   release has not been established, and other versions are not confirmed here.

   Impact
   ------

   The first event after a subscription resumes may be absent from downstream
   files, alerts, or forwarded messages. This can create a gap in monitoring
   or audit records even when later events are processed normally.

   How to determine whether you are affected
   -----------------------------------------

   Compare the Windows Event Log record IDs with the events processed or
   forwarded around a service restart. The condition is indicated when the
   first new record after the saved position is missing but a later record
   from the same channel is present.

   Workarounds
   -----------

   Keep the source Event Log channel available long enough to review records
   after a service restart. If the first resumed record is missing downstream,
   retrieve it from the Windows Event Log while it is still retained and
   reprocess it using your normal recovery procedure. Check for duplicates
   before replaying it. No configuration workaround is confirmed for
   bookmarked subscription resumption in the affected builds.

   Resolution status
   -----------------

   A correction is scheduled. No corrected service build has been publicly
   confirmed. This notice will be updated with the exact service builds when
   the correction is released.

   Revision history
   ----------------

   - **October 7, 2026:** Draft prepared for review; not published.
