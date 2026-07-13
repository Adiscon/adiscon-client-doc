:orphan:

.. _event-id-procedure-eventlog-verify-channel-access-and-bookmark:

.. meta::
   :description: Confirm channel existence, enablement, account access, and collection position.
   :procedure-id: eventlog.verify-channel-access-and-bookmark
   :procedure-reference: true

Verify Event Log channel access and bookmark state
==================================================

When to use this procedure
--------------------------

Use for Event Log Monitor and Event Log Monitor V2.

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

Configuration Client > Services > Event Log Monitor or Event Log Monitor V2 > affected service.

Procedure
---------

#. Record exact channel name, collection mode, service account, and intended start position.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-WinEvent -ListLog '<CHANNEL_NAME>' | Format-List LogName,IsEnabled,RecordCount,LogMode
      Get-WinEvent -LogName '<CHANNEL_NAME>' -MaxEvents 5 | Format-List TimeCreated,Id,ProviderName,Message

   **Expected result:** The channel is enabled and readable in the service-account context; a test event is collected once.

   **If it fails:** Correct the channel name or least-privilege access; reset position only after recording replay impact.

#. Perform one uniquely identifiable product test through the same service, rule, or action.

   **Expected result:** The intended destination records the test exactly once.

   **If it fails:** Collect the first new product event and bounded debug output; do not change unrelated settings.

Verify the result
-----------------

Repeat the affected operation, confirm its positive output, and verify that queues, collection positions, or remote delivery continue normally.

Evidence to collect
-------------------

- The complete Event Log entry and neighboring product events with timestamps.
- The command output, relevant configuration export, and bounded debug log from the same interval.

Related Event IDs
-----------------

- :ref:`WinSyslog Event ID 11097 <winsyslog-event-id-11097>`
- :ref:`WinSyslog Event ID 11098 <winsyslog-event-id-11098>`
- :ref:`WinSyslog Event ID 11099 <winsyslog-event-id-11099>`
- :ref:`WinSyslog Event ID 11100 <winsyslog-event-id-11100>`
- :ref:`WinSyslog Event ID 11101 <winsyslog-event-id-11101>`
- :ref:`WinSyslog Event ID 11102 <winsyslog-event-id-11102>`
- :ref:`WinSyslog Event ID 11103 <winsyslog-event-id-11103>`
- :ref:`WinSyslog Event ID 11104 <winsyslog-event-id-11104>`
- :ref:`WinSyslog Event ID 11105 <winsyslog-event-id-11105>`
- :ref:`WinSyslog Event ID 11106 <winsyslog-event-id-11106>`
- :ref:`WinSyslog Event ID 11107 <winsyslog-event-id-11107>`
- :ref:`WinSyslog Event ID 11108 <winsyslog-event-id-11108>`
- :ref:`WinSyslog Event ID 11109 <winsyslog-event-id-11109>`
- :ref:`WinSyslog Event ID 11110 <winsyslog-event-id-11110>`
- :ref:`WinSyslog Event ID 11147 <winsyslog-event-id-11147>`
- :ref:`WinSyslog Event ID 11148 <winsyslog-event-id-11148>`
- :ref:`WinSyslog Event ID 11149 <winsyslog-event-id-11149>`
- :ref:`WinSyslog Event ID 11150 <winsyslog-event-id-11150>`
- :ref:`WinSyslog Event ID 11151 <winsyslog-event-id-11151>`
