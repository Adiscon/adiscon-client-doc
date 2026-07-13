:orphan:

.. _event-id-procedure-transport-verify-sender-receiver-recovery:

.. meta::
   :description: Prove end-to-end recovery and backlog drainage.
   :procedure-id: transport.verify-sender-receiver-recovery
   :procedure-reference: true

Verify sender, receiver, and queued-message recovery
====================================================

When to use this procedure
--------------------------

Use after correcting connectivity or protocol failures.

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

Configuration Client > the service, rule, or action named on the Event ID page.

Procedure
---------

#. Record sender connection and queue state before retrying.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-Date -Format o

   **Expected result:** A uniquely identifiable new test arrives and delayed work begins draining without repeated failure events.

   **If it fails:** Return to connectivity, TLS, receiver, filter, or queue diagnostics using the first recurring error.

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

- :ref:`EventReporter Event ID 11000 <eventreporter-event-id-11000>`
- :ref:`EventReporter Event ID 11001 <eventreporter-event-id-11001>`
- :ref:`EventReporter Event ID 11002 <eventreporter-event-id-11002>`
- :ref:`EventReporter Event ID 11003 <eventreporter-event-id-11003>`
- :ref:`EventReporter Event ID 11004 <eventreporter-event-id-11004>`
- :ref:`EventReporter Event ID 11017 <eventreporter-event-id-11017>`
- :ref:`EventReporter Event ID 11018 <eventreporter-event-id-11018>`
- :ref:`EventReporter Event ID 11034 <eventreporter-event-id-11034>`
- :ref:`EventReporter Event ID 11035 <eventreporter-event-id-11035>`
- :ref:`EventReporter Event ID 11039 <eventreporter-event-id-11039>`
- :ref:`EventReporter Event ID 11040 <eventreporter-event-id-11040>`
- :ref:`EventReporter Event ID 11060 <eventreporter-event-id-11060>`
- :ref:`EventReporter Event ID 11061 <eventreporter-event-id-11061>`
- :ref:`EventReporter Event ID 11062 <eventreporter-event-id-11062>`
- :ref:`EventReporter Event ID 11063 <eventreporter-event-id-11063>`
- :ref:`EventReporter Event ID 11084 <eventreporter-event-id-11084>`
- :ref:`EventReporter Event ID 11085 <eventreporter-event-id-11085>`


Related procedures
------------------

- :ref:`Diagnose an action backlog or disk queue <event-id-procedure-queue-diagnose-backlog-and-disk-queue>`
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>`
