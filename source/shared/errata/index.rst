:orphan:

.. _known-issues-and-errata:

.. only:: winsyslog or winsyslog_j or mwagent or eventreporter or rsyslog

   Known issues and errata
   =======================

   This section documents confirmed product behavior that can affect operation
   or the interpretation of collected data. Each notice identifies the
   affected products and service versions, the practical impact, available
   workarounds, and the planned or released correction.

   Current errata
   --------------

.. only:: eventreporter

   * `ERR-2026-002: EventReporter update reports success but program files are
     not upgraded correctly
     <err-2026-002-cross-generation-installer-upgrade.html>`__

.. only:: winsyslog or winsyslog_j or mwagent

   * `ERR-2026-001: Incorrect source address for received SNMP traps
     <err-2026-001-snmp-trap-source-address.html>`_

.. only:: winsyslog or winsyslog_j

   * `ERR-2026-002: WinSyslog update reports success but program files are not
     upgraded correctly
     <err-2026-002-winsyslog-cross-generation-installer-upgrade.html>`__

.. only:: mwagent

   * `ERR-2026-002: MonitorWare Agent update reports success but program files
     are not upgraded correctly
     <err-2026-002-mwagent-cross-generation-installer-upgrade.html>`__

.. only:: rsyslog

   * `ERR-2026-002: rsyslog Windows Agent update reports success but program
     files are not upgraded correctly
     <err-2026-002-rsyslogwa-cross-generation-installer-upgrade.html>`__

.. only:: winsyslog or winsyslog_j or mwagent or eventreporter or rsyslog

   * `ERR-2026-003: TLS forwarding can stall when a receiver stops reading
     <err-2026-003-tls-forwarding-stall.html>`__

.. only:: mwagent or eventreporter or rsyslog

   * `ERR-2026-004: The first event after a subscription restart can be skipped
     <err-2026-004-eventlog-resume-first-event.html>`__

.. only:: winsyslog or winsyslog_j or mwagent or eventreporter or rsyslog

   * `ERR-2026-005: File Action rotation can remain pending after service startup
     <err-2026-005-file-rotation-startup-pending.html>`__
