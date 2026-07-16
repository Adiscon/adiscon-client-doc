:orphan:

.. _event-id-procedure-service-verify-state-and-account:

.. meta::
   :description: Confirm service state, start mode, dependencies, account, and SCM errors.
   :procedure-id: service.verify-state-and-account
   :procedure-reference: true

Verify service state, dependencies, and service account
=======================================================

When to use this procedure
--------------------------

Use for service startup, shutdown, permission, and monitoring events.

Applies to
----------

This procedure applies to WinSyslog.

Prerequisites
-------------

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Run diagnostic checks before changing configuration.
- Remove passwords, private keys, license data, and other secrets from evidence.

Configuration path
------------------

Configuration Client > Service; then Windows Services > the product service.

Procedure
---------

#. Identify the internal Windows service name and intended service account.

   **Expected result:** The internal service name and intended account are known before any start, stop, or account change.

   **If it fails:** Use the service Properties dialog or the command output below; do not guess the internal name.

#. Capture current service configuration, state, required dependencies, and bounded Service Control Manager events.

   .. code-block:: powershell

      Get-CimInstance Win32_Service -Filter "Name='<SERVICE_NAME>'" | Format-List Name,DisplayName,State,StartMode,StartName,PathName,ExitCode
      Get-Service -Name '<SERVICE_NAME>' -RequiredServices | Format-Table Name,Status,StartType
      $start=(Get-Date '<EVENT_TIME>').AddMinutes(-5)
      $end=(Get-Date '<EVENT_TIME>').AddMinutes(5)
      Get-WinEvent -FilterHashtable @{LogName='System';ProviderName='Service Control Manager';StartTime=$start;EndTime=$end} | Format-List TimeCreated,Id,LevelDisplayName,Message

   **Expected result:** The executable path, start mode, service account, dependencies, and first Windows service error agree with the intended installation.

   **If it fails:** Use the first Service Control Manager error to distinguish a dependency, account-logon, path, timeout, or process-termination failure.

#. After correcting the specific startup condition, start the service once and perform one identifiable product test.

   **Expected result:** The service remains Running, at least one configured input is active, and the intended destination records the test exactly once.

   **If it fails:** Stop retrying and collect the first new product and Service Control Manager errors from that start attempt.

Verify the result
-----------------

Confirm that the service remains Running and that one configured input processes an identifiable event through its intended destination.

Evidence to collect
-------------------

- The complete Event Log entry and neighboring product events with timestamps.
- The command output, relevant configuration export, and bounded debug log from the same interval.

Related Event IDs
-----------------

- :ref:`WinSyslog Event ID 100 <winsyslog-event-id-100>`
- :ref:`WinSyslog Event ID 101 <winsyslog-event-id-101>`
- :ref:`WinSyslog Event ID 102 <winsyslog-event-id-102>`
- :ref:`WinSyslog Event ID 103 <winsyslog-event-id-103>`
- :ref:`WinSyslog Event ID 104 <winsyslog-event-id-104>`
- :ref:`WinSyslog Event ID 105 <winsyslog-event-id-105>`
- :ref:`WinSyslog Event ID 106 <winsyslog-event-id-106>`
- :ref:`WinSyslog Event ID 108 <winsyslog-event-id-108>`
- :ref:`WinSyslog Event ID 11059 <winsyslog-event-id-11059>`
- :ref:`WinSyslog Event ID 11111 <winsyslog-event-id-11111>`
- :ref:`WinSyslog Event ID 11167 <winsyslog-event-id-11167>`
- :ref:`WinSyslog Event ID 11168 <winsyslog-event-id-11168>`
- :ref:`WinSyslog Event ID 11194 <winsyslog-event-id-11194>`
- :ref:`WinSyslog Event ID 11210 <winsyslog-event-id-11210>`
