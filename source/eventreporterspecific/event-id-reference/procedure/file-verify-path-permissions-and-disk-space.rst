:orphan:

.. _event-id-procedure-file-verify-path-permissions-and-disk-space:

.. meta::
   :description: Check expansion, existence, ACLs, service-account context, and storage.
   :procedure-id: file.verify-path-permissions-and-disk-space
   :procedure-reference: true

Verify file paths, permissions, and free space
==============================================

When to use this procedure
--------------------------

Use for file actions, File Monitor, queue files, debug logs, and rotation.

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

#. Resolve the exact local or UNC directory used by the service.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Test-Path -LiteralPath '<DIRECTORY_PATH>'
      Get-Acl -LiteralPath '<DIRECTORY_PATH>' | Format-List Owner,AccessToString
      Get-PSDrive -Name '<DRIVE_LETTER>' | Format-List Used,Free

   **Expected result:** The path exists, the service account has minimum required rights, and sufficient free space remains.

   **If it fails:** Correct expansion, share/NTFS permissions, availability, or storage without granting broad rights.

#. Perform one uniquely identifiable product test through the same service, rule, or action.

   **Expected result:** The intended destination records the test exactly once.

   **If it fails:** Collect the first new product event and bounded debug output; do not change unrelated settings.

Rollback
--------

#. Restore the previous path or ACL backup if the change prevents operation.

Verify the result
-----------------

Repeat the affected operation, confirm its positive output, and verify that queues, collection positions, or remote delivery continue normally.

Evidence to collect
-------------------

- The complete Event Log entry and neighboring product events with timestamps.
- The command output, relevant configuration export, and bounded debug log from the same interval.

Related Event IDs
-----------------

- :ref:`EventReporter Event ID 11009 <eventreporter-event-id-11009>`
- :ref:`EventReporter Event ID 11026 <eventreporter-event-id-11026>`
- :ref:`EventReporter Event ID 11042 <eventreporter-event-id-11042>`
- :ref:`EventReporter Event ID 11071 <eventreporter-event-id-11071>`
- :ref:`EventReporter Event ID 11074 <eventreporter-event-id-11074>`
- :ref:`EventReporter Event ID 11075 <eventreporter-event-id-11075>`
- :ref:`EventReporter Event ID 11076 <eventreporter-event-id-11076>`
- :ref:`EventReporter Event ID 11077 <eventreporter-event-id-11077>`
- :ref:`EventReporter Event ID 11078 <eventreporter-event-id-11078>`
- :ref:`EventReporter Event ID 11079 <eventreporter-event-id-11079>`
- :ref:`EventReporter Event ID 11080 <eventreporter-event-id-11080>`
- :ref:`EventReporter Event ID 11081 <eventreporter-event-id-11081>`
- :ref:`EventReporter Event ID 11173 <eventreporter-event-id-11173>`
