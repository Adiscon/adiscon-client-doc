:orphan:

.. only:: (winsyslog or winsyslog_j or mwagent or eventreporter or rsyslog) and errata_preview

   .. _err-2026-003-tls-forwarding-stall:

   ERR-2026-003: TLS forwarding can stall when a receiver stops reading
   =====================================================================

   **Status:** Scheduled

   **Publication:** Draft prepared for review

   **First published:** Pending publication

   Description
   -----------

   When Forward Syslog uses TLS over TCP, a receiver that stops reading
   messages can leave a send operation blocked instead of promptly entering
   the normal failure and disk-queue handling. The service can remain running
   while forwarding through that action stops making progress. Because the
   send has not returned as a failure, the action may not yet place the message
   in its disk queue.

   If a Windows Event Log subscription calls the action synchronously, the
   blocked send can also delay that subscription from processing later events.
   This condition requires the remote receiver or network path to stop
   accepting application data; an idle TLS connection by itself is not the
   issue described here.

   Affected products
   -----------------

   The following released service builds are confirmed affected:

   - **WinSyslog:** ``26.07.0.768``, ``26.08.0.773``, and ``26.09.0.774``
   - **MonitorWare Agent:** ``26.07.0.683``, ``26.08.0.688``, and
     ``26.09.0.689``
   - **EventReporter:** ``26.07.0.603``, ``26.08.0.608``, and ``26.09.0.609``
   - **rsyslog Windows Agent:** ``26.07.0.347``, ``26.08.0.352``,
     ``26.09.0.353``, and ``26.10.0.354``

   These are the affected releases confirmed so far. They do not establish the
   earliest affected release, and other versions may also be affected.

   Impact
   ------

   Messages may stop reaching the remote Syslog receiver while the service
   process remains active. The action's disk queue can remain empty while the
   send is still blocked, so an empty queue does not confirm that forwarding is
   healthy. A source that waits synchronously for the action can also stop
   advancing until the send returns.

   How to determine whether you are affected
   -----------------------------------------

   Check whether the affected action forwards over TLS-enabled TCP. The list
   above identifies confirmed affected builds; other versions are not confirmed
   as unaffected. Then check whether the receiver is accepting
   the TLS connection but no longer reading incoming messages. Compare the
   receiver's records with the source records and inspect the action queue
   during the same period. An idle persistent connection with no message to
   send does not indicate this condition.

   Workarounds
   -----------

   Restore the receiver or network path so it can read the forwarded messages.
   If a controlled restart is needed, first check the source's retention and
   the action queue, then verify that forwarding resumes and reconcile any
   source events not present at the destination.

   The Session Timeout setting (``nTimeoutValue``) controls an idle persistent
   connection; it does not bound a send that is already waiting. The affected
   builds do not provide a configuration setting that reliably limits this
   blocked TLS send. On affected builds, service stop or reload can also be
   delayed while a send remains blocked. Confirm that Windows reports the
   service as stopped before starting it again. If stop remains pending,
   preserve the source log records and follow your normal service recovery
   procedure. After recovery, compare source and receiver records and
   reconcile any gap.

   Resolution status
   -----------------

   The correction is scheduled for version 26.11. Exact service build numbers
   will be added when the release is published.

   Revision history
   ----------------

   - **October 7, 2026:** Draft prepared for review; not published.
