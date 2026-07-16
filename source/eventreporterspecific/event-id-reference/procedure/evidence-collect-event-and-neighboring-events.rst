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

Event Viewer > Windows Logs > Application > Filter Current Log.

Procedure
---------

#. Record the Event Log source, Event ID, level, timestamp, and complete General and Details data.

   **Expected result:** The record includes the provider, Event ID, timestamp with time zone, message text, and all dynamic detail.

   **If it fails:** Export the original event as an EVTX file before copying text or changing filters.

#. Record the host clock state, then collect only the product events in a bounded window around the event.

   .. code-block:: powershell

      Get-Date -Format o
      w32tm /query /status
      $start=(Get-Date '<EVENT_TIME>').AddMinutes(-5)
      $end=(Get-Date '<EVENT_TIME>').AddMinutes(5)
      Get-WinEvent -FilterHashtable @{LogName='Application';StartTime=$start;EndTime=$end} | Where-Object ProviderName -eq '<EVENT_SOURCE>' | Format-List TimeCreated,Id,LevelDisplayName,Message

   **Expected result:** The clock output is recorded and the event sequence contains the first failure plus any later state or recovery event.

   **If it fails:** Verify the provider shown on the Event ID page. Expand the window only enough to include the first related event.

#. After diagnosis, perform one uniquely identifiable product test through the same input, rule, and action, and record its sender and destination timestamps.

   **Expected result:** The intended destination records the test exactly once.

   **If it fails:** Collect the first new product event and bounded debug output from that exact test; do not change unrelated settings.

Verify the result
-----------------

Repeat the affected operation, confirm its positive output, and verify that queues, collection positions, or remote delivery continue normally.

Evidence to collect
-------------------

- The original EVTX record plus the complete rendered event and neighboring product events with timestamps.
- Clock-status output from every involved host and the sender and destination timestamps for the identifiable test.
- The relevant configuration export and bounded debug log from the same interval, with credentials, license data, private keys, addresses, hostnames, and environment-specific object names removed.

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
- :ref:`EventReporter Event ID 118 <eventreporter-event-id-118>`
- :ref:`EventReporter Event ID 901 <eventreporter-event-id-901>`
- :ref:`EventReporter Event ID 11000 <eventreporter-event-id-11000>`
- :ref:`EventReporter Event ID 11001 <eventreporter-event-id-11001>`
- :ref:`EventReporter Event ID 11002 <eventreporter-event-id-11002>`
- :ref:`EventReporter Event ID 11003 <eventreporter-event-id-11003>`
- :ref:`EventReporter Event ID 11004 <eventreporter-event-id-11004>`
- :ref:`EventReporter Event ID 11005 <eventreporter-event-id-11005>`
- :ref:`EventReporter Event ID 11006 <eventreporter-event-id-11006>`
- :ref:`EventReporter Event ID 11007 <eventreporter-event-id-11007>`
- :ref:`EventReporter Event ID 11009 <eventreporter-event-id-11009>`
- :ref:`EventReporter Event ID 11010 <eventreporter-event-id-11010>`
- :ref:`EventReporter Event ID 11011 <eventreporter-event-id-11011>`
- :ref:`EventReporter Event ID 11012 <eventreporter-event-id-11012>`
- :ref:`EventReporter Event ID 11013 <eventreporter-event-id-11013>`
- :ref:`EventReporter Event ID 11014 <eventreporter-event-id-11014>`
- :ref:`EventReporter Event ID 11015 <eventreporter-event-id-11015>`
- :ref:`EventReporter Event ID 11016 <eventreporter-event-id-11016>`
- :ref:`EventReporter Event ID 11017 <eventreporter-event-id-11017>`
- :ref:`EventReporter Event ID 11018 <eventreporter-event-id-11018>`
- :ref:`EventReporter Event ID 11019 <eventreporter-event-id-11019>`
- :ref:`EventReporter Event ID 11020 <eventreporter-event-id-11020>`
- :ref:`EventReporter Event ID 11022 <eventreporter-event-id-11022>`
- :ref:`EventReporter Event ID 11023 <eventreporter-event-id-11023>`
- :ref:`EventReporter Event ID 11024 <eventreporter-event-id-11024>`
- :ref:`EventReporter Event ID 11025 <eventreporter-event-id-11025>`
- :ref:`EventReporter Event ID 11026 <eventreporter-event-id-11026>`
- :ref:`EventReporter Event ID 11027 <eventreporter-event-id-11027>`
- :ref:`EventReporter Event ID 11028 <eventreporter-event-id-11028>`
- :ref:`EventReporter Event ID 11029 <eventreporter-event-id-11029>`
- :ref:`EventReporter Event ID 11030 <eventreporter-event-id-11030>`
- :ref:`EventReporter Event ID 11031 <eventreporter-event-id-11031>`
- This procedure is used by 177 additional Event IDs; use the product Event ID index to locate them.
