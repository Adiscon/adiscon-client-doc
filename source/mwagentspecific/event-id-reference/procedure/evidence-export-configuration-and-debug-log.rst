:orphan:

.. _event-id-procedure-evidence-export-configuration-and-debug-log:

.. meta::
   :description: Create a text configuration export and time-bounded debug capture, then disable debugging.
   :procedure-id: evidence.export-configuration-and-debug-log
   :procedure-reference: true

Export configuration and collect a bounded debug log
====================================================

When to use this procedure
--------------------------

Use this when configuration or runtime sequencing must be reviewed.

Applies to
----------

This procedure applies to MonitorWare Agent.

Prerequisites
-------------

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Disable debug logging immediately after the bounded capture.
- Remove credentials, private keys, license material, and unrelated customer data before sharing.

Configuration path
------------------

Configuration Client > Computer > Export Settings to Registry File; then General > Debug.

Procedure
---------

#. Export settings as a text registry file, then enable the minimum debug level that reproduces the problem.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-Item -LiteralPath '<CONFIG_EXPORT>' | Format-List FullName,Length,LastWriteTime
      Get-Item -LiteralPath '<DEBUG_LOG>' | Format-List FullName,Length,LastWriteTime

   **Expected result:** Both files exist, are readable, and cover the recorded reproduction interval.

   **If it fails:** Verify the service account can write the debug directory and restart only if the setting requires it.

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

- :ref:`MonitorWare Agent Event ID 100 <mwagent-event-id-100>`
- :ref:`MonitorWare Agent Event ID 101 <mwagent-event-id-101>`
- :ref:`MonitorWare Agent Event ID 102 <mwagent-event-id-102>`
- :ref:`MonitorWare Agent Event ID 103 <mwagent-event-id-103>`
- :ref:`MonitorWare Agent Event ID 104 <mwagent-event-id-104>`
- :ref:`MonitorWare Agent Event ID 105 <mwagent-event-id-105>`
- :ref:`MonitorWare Agent Event ID 106 <mwagent-event-id-106>`
- :ref:`MonitorWare Agent Event ID 108 <mwagent-event-id-108>`
- :ref:`MonitorWare Agent Event ID 118 <mwagent-event-id-118>`
- :ref:`MonitorWare Agent Event ID 11000 <mwagent-event-id-11000>`
- :ref:`MonitorWare Agent Event ID 11001 <mwagent-event-id-11001>`
- :ref:`MonitorWare Agent Event ID 11002 <mwagent-event-id-11002>`
- :ref:`MonitorWare Agent Event ID 11003 <mwagent-event-id-11003>`
- :ref:`MonitorWare Agent Event ID 11004 <mwagent-event-id-11004>`
- :ref:`MonitorWare Agent Event ID 11005 <mwagent-event-id-11005>`
- :ref:`MonitorWare Agent Event ID 11006 <mwagent-event-id-11006>`
- :ref:`MonitorWare Agent Event ID 11007 <mwagent-event-id-11007>`
- :ref:`MonitorWare Agent Event ID 11009 <mwagent-event-id-11009>`
- :ref:`MonitorWare Agent Event ID 11010 <mwagent-event-id-11010>`
- :ref:`MonitorWare Agent Event ID 11011 <mwagent-event-id-11011>`
- :ref:`MonitorWare Agent Event ID 11012 <mwagent-event-id-11012>`
- :ref:`MonitorWare Agent Event ID 11013 <mwagent-event-id-11013>`
- :ref:`MonitorWare Agent Event ID 11014 <mwagent-event-id-11014>`
- :ref:`MonitorWare Agent Event ID 11015 <mwagent-event-id-11015>`
- :ref:`MonitorWare Agent Event ID 11016 <mwagent-event-id-11016>`
- :ref:`MonitorWare Agent Event ID 11017 <mwagent-event-id-11017>`
- :ref:`MonitorWare Agent Event ID 11018 <mwagent-event-id-11018>`
- :ref:`MonitorWare Agent Event ID 11019 <mwagent-event-id-11019>`
- :ref:`MonitorWare Agent Event ID 11020 <mwagent-event-id-11020>`
- :ref:`MonitorWare Agent Event ID 11022 <mwagent-event-id-11022>`
- :ref:`MonitorWare Agent Event ID 11023 <mwagent-event-id-11023>`
- :ref:`MonitorWare Agent Event ID 11024 <mwagent-event-id-11024>`
- :ref:`MonitorWare Agent Event ID 11025 <mwagent-event-id-11025>`
- :ref:`MonitorWare Agent Event ID 11026 <mwagent-event-id-11026>`
- :ref:`MonitorWare Agent Event ID 11027 <mwagent-event-id-11027>`
- :ref:`MonitorWare Agent Event ID 11028 <mwagent-event-id-11028>`
- :ref:`MonitorWare Agent Event ID 11029 <mwagent-event-id-11029>`
- :ref:`MonitorWare Agent Event ID 11030 <mwagent-event-id-11030>`
- :ref:`MonitorWare Agent Event ID 11031 <mwagent-event-id-11031>`
- :ref:`MonitorWare Agent Event ID 11032 <mwagent-event-id-11032>`
- This procedure is used by 169 additional Event IDs; use the product Event ID index to locate them.
