:orphan:

.. _err-2026-001-snmp-trap-source-address:

.. only:: winsyslog or winsyslog_j or mwagent

   ERR-2026-001: Incorrect source address for received SNMP traps
   ================================================================

   **Status:** Resolved

   **First published:** August 6, 2026

   Description
   -----------

   The SNMP Trap Receiver can record the name or address of the local system as
   the event source instead of the address of the device that sent the trap.
   The incorrect value can appear both in the event source property and in the
   formatted message text.

   The trap is still received and processed. The problem is limited to sender
   attribution for events received by the SNMP Trap Receiver. Source detection
   for the Syslog service and other input services is not affected.

   Affected products
   -----------------

   - **WinSyslog:** service versions ``18.3.0.657``, ``18.4.0.661``,
     ``26.07.0.768``, and ``26.08.0.773``
   - **MonitorWare** `Agent <https://www.mwagent.com/>`_: service versions
     ``15.3.0.572``, ``15.4.0.576``, ``26.07.0.683``, and ``26.08.0.688``

   Impact
   ------

   Rules, files, database records, alerts, or forwarded messages that rely on
   the event source can identify the receiving Windows system instead of the
   device that sent the SNMP trap. This can affect device-specific filtering,
   correlation, and incident analysis.

   How to determine whether you are affected
   -----------------------------------------

   You are affected when all of the following conditions apply:

   - You use an affected service version listed above.
   - You receive events through the SNMP Trap Receiver.
   - The recorded source is the local product host instead of the sending
     device.

   Send a test trap from a device with a known address and compare that address
   with the event source property and any ``source=`` value in the formatted
   message.

   Workarounds
   -----------

   There is no configuration change that restores the correct sender address
   in the affected versions.

   If correct source attribution is operationally critical, contact Adiscon
   Support to review a controlled rollback. The last known unaffected service
   versions are WinSyslog ``18.2.0.656`` and MonitorWare
   `Agent <https://www.mwagent.com/>`_ ``15.2.0.571``. Before a rollback, back
   up the configuration and verify compatibility because a configuration saved
   by a later release can contain settings that an earlier release does not
   support.

   When a rollback is not suitable, use an independent network capture or the
   sending device's own records to confirm the sender. Do not rely on the
   affected source field alone for device-specific processing or incident
   decisions.

   Resolution
   ----------

   The correction is included in the ``26.09`` releases: WinSyslog service
   version ``26.9.0.774`` and MonitorWare `Agent <https://www.mwagent.com/>`_
   service version ``26.9.0.689``.

   After updating, send a test trap from a device with a known address and
   confirm that the event source property and formatted message identify that
   device.

   Related release notes
   ---------------------

   - `WinSyslog 26.09 Technical Release Notes <https://www.winsyslog.com/version-history/winsyslog-26-09-technical-release-notes/>`_
   - `MonitorWare Agent 26.09 Technical Release Notes <https://www.mwagent.com/version-history/monitorware-agent-26-09-technical-release-notes/>`_

   Revision history
   ----------------

   - **September 1, 2026:** Resolved in the ``26.09`` releases; added links to
     the Technical Release Notes.
   - **August 6, 2026:** Initial publication.
