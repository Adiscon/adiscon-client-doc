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

Use for service startup, shutdown, removal, permission, and monitoring events.

Applies to
----------

This procedure applies to EventReporter.

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

#. After correcting the condition, repeat the requested lifecycle operation once. For startup events, start the service and perform one identifiable product test; for removal events, retry the intended removal and do not restart the service.

   **Expected result:** For startup events, the service remains Running, at least one configured input is active, and the intended destination records the test exactly once. For removal events, the service registration is absent after the authorized removal. For other lifecycle events, only the requested state changes.

   **If it fails:** Stop retrying and collect the first new product and Service Control Manager errors from the attempted operation.

Verify the result
-----------------

Confirm the requested lifecycle state: Running after startup, Stopped after shutdown, and registration absent after removal. Perform an identifiable product test only when the service is expected to run.

Evidence to collect
-------------------

- The complete Event Log entry and neighboring product events with timestamps.
- The command output, relevant configuration export, and bounded debug log from the same interval.

Related Event IDs
-----------------

- :ref:`EventReporter Event ID 100 <eventreporter-event-id-100>`
- :ref:`EventReporter Event ID 101 <eventreporter-event-id-101>`
- :ref:`EventReporter Event ID 102 <eventreporter-event-id-102>`
- :ref:`EventReporter Event ID 103 <eventreporter-event-id-103>`
- :ref:`EventReporter Event ID 104 <eventreporter-event-id-104>`
- :ref:`EventReporter Event ID 105 <eventreporter-event-id-105>`
- :ref:`EventReporter Event ID 106 <eventreporter-event-id-106>`
- :ref:`EventReporter Event ID 108 <eventreporter-event-id-108>`
- :ref:`EventReporter Event ID 11059 <eventreporter-event-id-11059>`
- :ref:`EventReporter Event ID 11111 <eventreporter-event-id-11111>`
- :ref:`EventReporter Event ID 11167 <eventreporter-event-id-11167>`
- :ref:`EventReporter Event ID 11168 <eventreporter-event-id-11168>`
- :ref:`EventReporter Event ID 11194 <eventreporter-event-id-11194>`
- :ref:`EventReporter Event ID 11203 <eventreporter-event-id-11203>`
- :ref:`EventReporter Event ID 11204 <eventreporter-event-id-11204>`
- :ref:`EventReporter Event ID 11205 <eventreporter-event-id-11205>`
- :ref:`EventReporter Event ID 11206 <eventreporter-event-id-11206>`
- :ref:`EventReporter Event ID 11207 <eventreporter-event-id-11207>`
- :ref:`EventReporter Event ID 11208 <eventreporter-event-id-11208>`
- :ref:`EventReporter Event ID 11209 <eventreporter-event-id-11209>`
