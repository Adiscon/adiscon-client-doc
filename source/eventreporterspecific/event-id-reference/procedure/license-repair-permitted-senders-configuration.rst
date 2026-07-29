:orphan:

.. _event-id-procedure-license-repair-permitted-senders-configuration:

.. meta::
   :description: Authorize an intended sender without weakening the sender restriction.
   :procedure-id: license.repair-permitted-senders-configuration
   :procedure-reference: true

Repair the permitted-senders configuration
==========================================

When to use this procedure
--------------------------

Use for Event ID 11043 when a sender should be permitted but is absent from, or outside the active range of, the permitted-senders configuration.

Applies to
----------

This procedure applies to EventReporter.

Prerequisites
-------------

- Use an account that can read and update the affected product configuration.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Do not disable permitted-senders protection solely to accept a sender.
- Do not publish sender addresses or a full configuration export.

Configuration path
------------------

Configuration Client > General > permitted-senders settings.

Procedure
---------

#. Record whether permitted senders is enabled, the configured sender count, and the position of each intended sender without recording sender addresses.

   **Expected result:** The intended sender and the active permitted-sender positions are known.

   **If it fails:** Collect a redacted configuration summary and the complete Event ID 11043 detail before changing the sender list.

#. Compare the intended sender inventory with the configured count and active entry order.

   **Expected result:** Each required sender is present within the active permitted-sender range.

   **If it fails:** Remove or replace an entry only when it is confirmed obsolete; do not disable permitted-senders protection.

#. If the rejected sender is intended and capacity is available, add it to, or move it into, the active permitted-sender range. If the required inventory exceeds the configured or licensed allowance, obtain the authorized capacity before retrying.

   **Expected result:** The intended sender is authorized without admitting unapproved senders.

   **If it fails:** Do not broaden network access as a workaround. Record the non-secret configured count and license allowance, then follow the approved capacity process.

#. Apply the configuration as required by the product, then send one uniquely identifiable test from the intended sender.

   **Expected result:** The product accepts the test exactly once and Event ID 11043 does not recur.

   **If it fails:** Restore the previous sender order if the change was unintended, then collect the new Event ID 11043 detail and a redacted configuration summary.

Verify the result
-----------------

Confirm that every required sender remains authorized, unapproved senders remain refused, and the intended sender completes one test without Event ID 11043.

Evidence to collect
-------------------

- The complete Event ID 11043 entry and neighboring product events with timestamps.
- A redacted list of sender positions, configured count, and intended-sender status; do not collect sender addresses.
- The product version and non-secret license allowance when the intended inventory exceeds the configured count.

Related Event IDs
-----------------

- :ref:`EventReporter Event ID 11043 <eventreporter-event-id-11043>`


Related procedures
------------------

- :ref:`Verify product license and feature entitlement state <event-id-procedure-license-verify-license-state>`
