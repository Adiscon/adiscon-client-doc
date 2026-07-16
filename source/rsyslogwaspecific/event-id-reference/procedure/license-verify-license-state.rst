:orphan:

.. _event-id-procedure-license-verify-license-state:

.. meta::
   :description: Confirm product, version, validity, edition, and required feature without exposing license data.
   :procedure-id: license.verify-license-state
   :procedure-reference: true

Verify product license and feature entitlement state
====================================================

When to use this procedure
--------------------------

Use for trial, license validation, edition, and feature-denied events.

Applies to
----------

This procedure applies to rsyslog Windows Agent.

Prerequisites
-------------

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Never publish license files, signed payloads, keys, customer identifiers, or activation material.
- Do not edit a signed license file.

Configuration path
------------------

Configuration Client > General > License.

Procedure
---------

#. Record product version, displayed license status, edition, and feature named in the event without copying the license payload.

   **Expected result:** The running product, version, edition, license mode, and required feature or client allowance are known without exposing license material.

   **If it fails:** Do not copy the license file or key; record only the product UI's status and non-secret version information.

#. Verify the running executable's product and version, then compare the displayed entitlement with the module or client allowance named by the event.

   .. code-block:: powershell

      Get-Item -LiteralPath '<PRODUCT_EXECUTABLE>' | Select-Object -ExpandProperty VersionInfo | Format-List ProductName,ProductVersion,FileVersion

   **Expected result:** The authorized license targets the running product and version and includes the required feature or sufficient client capacity.

   **If it fails:** Install authorized replacement license material or disable the unsupported configuration; never edit signed data.

#. Restart or reload only as required by the license installation, then test the previously denied module or intended sender once.

   **Expected result:** The service remains Running and the intended module or sender processes the test exactly once without a license-denial event.

   **If it fails:** Record the new license-status and denial events without sharing license data; do not repeatedly reinstall or alter the license.

Verify the result
-----------------

Confirm the intended license mode in the product UI and prove the previously denied module or sender works once without exposing license material.

Evidence to collect
-------------------

- The complete Event Log entry and neighboring product events with timestamps.
- Product name, executable version, displayed edition or license mode, and the non-secret feature or client allowance involved.
- A redacted configuration export showing only the affected object; never collect license files, keys, signed payloads, activation data, or customer identifiers.

Related Event IDs
-----------------

- :ref:`rsyslog Windows Agent Event ID 118 <rsyslog-event-id-118>`
- :ref:`rsyslog Windows Agent Event ID 11005 <rsyslog-event-id-11005>`
- :ref:`rsyslog Windows Agent Event ID 11043 <rsyslog-event-id-11043>`
- :ref:`rsyslog Windows Agent Event ID 11044 <rsyslog-event-id-11044>`
- :ref:`rsyslog Windows Agent Event ID 11186 <rsyslog-event-id-11186>`
