:orphan:

.. _event-id-procedure-queue-diagnose-backlog-and-disk-queue:

.. meta::
   :description: Identify why queued work is not draining while preserving data.
   :procedure-id: queue.diagnose-backlog-and-disk-queue
   :procedure-reference: true

Diagnose an action backlog or disk queue
========================================

When to use this procedure
--------------------------

Use for action cache, queue manager, disk queue, retry, and saturation events.

Applies to
----------

This procedure applies to rsyslog Windows Agent.

Prerequisites
-------------

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Do not delete, rename, copy over, or manually edit active queue files.
- Collect evidence before any support-directed recovery.

Configuration path
------------------

Configuration Client > the service, rule, or action named on the Event ID page.

Procedure
---------

#. Record queue depth, oldest item time, target action, directory, and whether depth is increasing.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-ChildItem -LiteralPath '<QUEUE_DIRECTORY>' | Measure-Object -Property Length -Sum
      Get-PSDrive -Name '<DRIVE_LETTER>' | Format-List Used,Free

   **Expected result:** Queue files are readable, space remains, the downstream cause is corrected, and depth decreases.

   **If it fails:** Diagnose the first downstream error; never edit or delete live queue files.

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

- :ref:`rsyslog Windows Agent Event ID 11014 <rsyslog-event-id-11014>`
- :ref:`rsyslog Windows Agent Event ID 11019 <rsyslog-event-id-11019>`
- :ref:`rsyslog Windows Agent Event ID 11022 <rsyslog-event-id-11022>`
- :ref:`rsyslog Windows Agent Event ID 11023 <rsyslog-event-id-11023>`
- :ref:`rsyslog Windows Agent Event ID 11024 <rsyslog-event-id-11024>`
- :ref:`rsyslog Windows Agent Event ID 11025 <rsyslog-event-id-11025>`
- :ref:`rsyslog Windows Agent Event ID 11026 <rsyslog-event-id-11026>`
- :ref:`rsyslog Windows Agent Event ID 11027 <rsyslog-event-id-11027>`
- :ref:`rsyslog Windows Agent Event ID 11028 <rsyslog-event-id-11028>`
- :ref:`rsyslog Windows Agent Event ID 11033 <rsyslog-event-id-11033>`
- :ref:`rsyslog Windows Agent Event ID 11036 <rsyslog-event-id-11036>`
- :ref:`rsyslog Windows Agent Event ID 11037 <rsyslog-event-id-11037>`
- :ref:`rsyslog Windows Agent Event ID 11170 <rsyslog-event-id-11170>`
- :ref:`rsyslog Windows Agent Event ID 11171 <rsyslog-event-id-11171>`
- :ref:`rsyslog Windows Agent Event ID 11172 <rsyslog-event-id-11172>`
- :ref:`rsyslog Windows Agent Event ID 11173 <rsyslog-event-id-11173>`
- :ref:`rsyslog Windows Agent Event ID 11174 <rsyslog-event-id-11174>`
- :ref:`rsyslog Windows Agent Event ID 11176 <rsyslog-event-id-11176>`
- :ref:`rsyslog Windows Agent Event ID 11178 <rsyslog-event-id-11178>`
- :ref:`rsyslog Windows Agent Event ID 11179 <rsyslog-event-id-11179>`
- :ref:`rsyslog Windows Agent Event ID 11180 <rsyslog-event-id-11180>`
- :ref:`rsyslog Windows Agent Event ID 11181 <rsyslog-event-id-11181>`
- :ref:`rsyslog Windows Agent Event ID 11182 <rsyslog-event-id-11182>`


Related procedures
------------------

- :ref:`Verify sender, receiver, and queued-message recovery <event-id-procedure-transport-verify-sender-receiver-recovery>`
- :ref:`Verify file paths, permissions, and free space <event-id-procedure-file-verify-path-permissions-and-disk-space>`
