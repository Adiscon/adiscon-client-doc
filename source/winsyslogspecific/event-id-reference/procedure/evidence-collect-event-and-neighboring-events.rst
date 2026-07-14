:orphan:

.. _event-id-procedure-evidence-collect-event-and-neighboring-events:

.. meta::
   :description: Preserve the complete event and the product events immediately before and after it.
   :procedure-id: evidence.collect-event-and-neighboring-events
   :procedure-reference: true

Collect an Event ID and neighboring product events
==================================================

When to use this procedure
--------------------------

Use this first when an event contains dynamic detail or several failures occur together.

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

Event Viewer > Windows Logs > Application > Filter Current Log.

Procedure
---------

#. Record the Event Log source, Event ID, level, timestamp, and complete General and Details data.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      $start=(Get-Date '<EVENT_TIME>').AddMinutes(-5)
      $end=(Get-Date '<EVENT_TIME>').AddMinutes(5)
      Get-WinEvent -FilterHashtable @{LogName='Application';StartTime=$start;EndTime=$end} | Where-Object ProviderName -eq '<EVENT_SOURCE>' | Format-List TimeCreated,Id,LevelDisplayName,Message

   **Expected result:** The output contains the first product failure and later state or recovery events.

   **If it fails:** Increase the bounded time window and verify the Event Log source shown on the Event ID page.

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

- :ref:`WinSyslog Event ID 100 <winsyslog-event-id-100>`
- :ref:`WinSyslog Event ID 101 <winsyslog-event-id-101>`
- :ref:`WinSyslog Event ID 102 <winsyslog-event-id-102>`
- :ref:`WinSyslog Event ID 103 <winsyslog-event-id-103>`
- :ref:`WinSyslog Event ID 104 <winsyslog-event-id-104>`
- :ref:`WinSyslog Event ID 105 <winsyslog-event-id-105>`
- :ref:`WinSyslog Event ID 106 <winsyslog-event-id-106>`
- :ref:`WinSyslog Event ID 108 <winsyslog-event-id-108>`
- :ref:`WinSyslog Event ID 118 <winsyslog-event-id-118>`
- :ref:`WinSyslog Event ID 125 <winsyslog-event-id-125>`
- :ref:`WinSyslog Event ID 900 <winsyslog-event-id-900>`
- :ref:`WinSyslog Event ID 901 <winsyslog-event-id-901>`
- :ref:`WinSyslog Event ID 11000 <winsyslog-event-id-11000>`
- :ref:`WinSyslog Event ID 11001 <winsyslog-event-id-11001>`
- :ref:`WinSyslog Event ID 11002 <winsyslog-event-id-11002>`
- :ref:`WinSyslog Event ID 11003 <winsyslog-event-id-11003>`
- :ref:`WinSyslog Event ID 11004 <winsyslog-event-id-11004>`
- :ref:`WinSyslog Event ID 11005 <winsyslog-event-id-11005>`
- :ref:`WinSyslog Event ID 11006 <winsyslog-event-id-11006>`
- :ref:`WinSyslog Event ID 11007 <winsyslog-event-id-11007>`
- :ref:`WinSyslog Event ID 11009 <winsyslog-event-id-11009>`
- :ref:`WinSyslog Event ID 11010 <winsyslog-event-id-11010>`
- :ref:`WinSyslog Event ID 11011 <winsyslog-event-id-11011>`
- :ref:`WinSyslog Event ID 11012 <winsyslog-event-id-11012>`
- :ref:`WinSyslog Event ID 11013 <winsyslog-event-id-11013>`
- :ref:`WinSyslog Event ID 11014 <winsyslog-event-id-11014>`
- :ref:`WinSyslog Event ID 11015 <winsyslog-event-id-11015>`
- :ref:`WinSyslog Event ID 11016 <winsyslog-event-id-11016>`
- :ref:`WinSyslog Event ID 11017 <winsyslog-event-id-11017>`
- :ref:`WinSyslog Event ID 11018 <winsyslog-event-id-11018>`
- :ref:`WinSyslog Event ID 11019 <winsyslog-event-id-11019>`
- :ref:`WinSyslog Event ID 11020 <winsyslog-event-id-11020>`
- :ref:`WinSyslog Event ID 11022 <winsyslog-event-id-11022>`
- :ref:`WinSyslog Event ID 11023 <winsyslog-event-id-11023>`
- :ref:`WinSyslog Event ID 11024 <winsyslog-event-id-11024>`
- :ref:`WinSyslog Event ID 11025 <winsyslog-event-id-11025>`
- :ref:`WinSyslog Event ID 11026 <winsyslog-event-id-11026>`
- :ref:`WinSyslog Event ID 11027 <winsyslog-event-id-11027>`
- :ref:`WinSyslog Event ID 11028 <winsyslog-event-id-11028>`
- :ref:`WinSyslog Event ID 11029 <winsyslog-event-id-11029>`
- This procedure is used by 173 additional Event IDs; use the product Event ID index to locate them.
