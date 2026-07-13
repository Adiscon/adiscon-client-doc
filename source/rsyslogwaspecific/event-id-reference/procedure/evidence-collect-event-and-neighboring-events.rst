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

This procedure applies to rsyslog Windows Agent.

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

- :ref:`rsyslog Windows Agent Event ID 100 <rsyslog-event-id-100>`
- :ref:`rsyslog Windows Agent Event ID 101 <rsyslog-event-id-101>`
- :ref:`rsyslog Windows Agent Event ID 102 <rsyslog-event-id-102>`
- :ref:`rsyslog Windows Agent Event ID 103 <rsyslog-event-id-103>`
- :ref:`rsyslog Windows Agent Event ID 104 <rsyslog-event-id-104>`
- :ref:`rsyslog Windows Agent Event ID 105 <rsyslog-event-id-105>`
- :ref:`rsyslog Windows Agent Event ID 106 <rsyslog-event-id-106>`
- :ref:`rsyslog Windows Agent Event ID 108 <rsyslog-event-id-108>`
- :ref:`rsyslog Windows Agent Event ID 118 <rsyslog-event-id-118>`
- :ref:`rsyslog Windows Agent Event ID 11000 <rsyslog-event-id-11000>`
- :ref:`rsyslog Windows Agent Event ID 11001 <rsyslog-event-id-11001>`
- :ref:`rsyslog Windows Agent Event ID 11002 <rsyslog-event-id-11002>`
- :ref:`rsyslog Windows Agent Event ID 11003 <rsyslog-event-id-11003>`
- :ref:`rsyslog Windows Agent Event ID 11004 <rsyslog-event-id-11004>`
- :ref:`rsyslog Windows Agent Event ID 11005 <rsyslog-event-id-11005>`
- :ref:`rsyslog Windows Agent Event ID 11006 <rsyslog-event-id-11006>`
- :ref:`rsyslog Windows Agent Event ID 11007 <rsyslog-event-id-11007>`
- :ref:`rsyslog Windows Agent Event ID 11009 <rsyslog-event-id-11009>`
- :ref:`rsyslog Windows Agent Event ID 11010 <rsyslog-event-id-11010>`
- :ref:`rsyslog Windows Agent Event ID 11011 <rsyslog-event-id-11011>`
- :ref:`rsyslog Windows Agent Event ID 11012 <rsyslog-event-id-11012>`
- :ref:`rsyslog Windows Agent Event ID 11013 <rsyslog-event-id-11013>`
- :ref:`rsyslog Windows Agent Event ID 11014 <rsyslog-event-id-11014>`
- :ref:`rsyslog Windows Agent Event ID 11015 <rsyslog-event-id-11015>`
- :ref:`rsyslog Windows Agent Event ID 11016 <rsyslog-event-id-11016>`
- :ref:`rsyslog Windows Agent Event ID 11017 <rsyslog-event-id-11017>`
- :ref:`rsyslog Windows Agent Event ID 11018 <rsyslog-event-id-11018>`
- :ref:`rsyslog Windows Agent Event ID 11019 <rsyslog-event-id-11019>`
- :ref:`rsyslog Windows Agent Event ID 11020 <rsyslog-event-id-11020>`
- :ref:`rsyslog Windows Agent Event ID 11022 <rsyslog-event-id-11022>`
- :ref:`rsyslog Windows Agent Event ID 11023 <rsyslog-event-id-11023>`
- :ref:`rsyslog Windows Agent Event ID 11024 <rsyslog-event-id-11024>`
- :ref:`rsyslog Windows Agent Event ID 11025 <rsyslog-event-id-11025>`
- :ref:`rsyslog Windows Agent Event ID 11026 <rsyslog-event-id-11026>`
- :ref:`rsyslog Windows Agent Event ID 11027 <rsyslog-event-id-11027>`
- :ref:`rsyslog Windows Agent Event ID 11028 <rsyslog-event-id-11028>`
- :ref:`rsyslog Windows Agent Event ID 11029 <rsyslog-event-id-11029>`
- :ref:`rsyslog Windows Agent Event ID 11030 <rsyslog-event-id-11030>`
- :ref:`rsyslog Windows Agent Event ID 11031 <rsyslog-event-id-11031>`
- :ref:`rsyslog Windows Agent Event ID 11032 <rsyslog-event-id-11032>`
- This procedure is used by 171 additional Event IDs; use the product Event ID index to locate them.
