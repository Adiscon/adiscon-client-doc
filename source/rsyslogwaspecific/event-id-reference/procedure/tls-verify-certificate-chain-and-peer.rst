:orphan:

.. _event-id-procedure-tls-verify-certificate-chain-and-peer:

.. meta::
   :description: Check validity, trust chain, key pairing, protocol mode, and peer authorization.
   :procedure-id: tls.verify-certificate-chain-and-peer
   :procedure-reference: true

Verify TLS certificates, private keys, and permitted peers
==========================================================

When to use this procedure
--------------------------

Use after TCP succeeds but TLS, DTLS, SETP, RELP, or secure syslog fails.

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

Configuration Client > the service, rule, or action named on the Event ID page.

Procedure
---------

#. Record CA PEM, certificate PEM, key PEM, peer identity, and authentication mode.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      certutil -dump '<CERTIFICATE_PATH>'
      certutil -verify '<CERTIFICATE_PATH>'

   **Expected result:** The certificate is valid for its purpose, chains to the intended trust anchor, and matches the configured peer policy.

   **If it fails:** Replace invalid files, provide the matching unencrypted PEM key, or correct trust and peer settings; do not disable validation permanently.

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

- :ref:`rsyslog Windows Agent Event ID 11000 <rsyslog-event-id-11000>`
- :ref:`rsyslog Windows Agent Event ID 11001 <rsyslog-event-id-11001>`
- :ref:`rsyslog Windows Agent Event ID 11002 <rsyslog-event-id-11002>`
- :ref:`rsyslog Windows Agent Event ID 11003 <rsyslog-event-id-11003>`
- :ref:`rsyslog Windows Agent Event ID 11004 <rsyslog-event-id-11004>`
- :ref:`rsyslog Windows Agent Event ID 11034 <rsyslog-event-id-11034>`
- :ref:`rsyslog Windows Agent Event ID 11035 <rsyslog-event-id-11035>`
- :ref:`rsyslog Windows Agent Event ID 11048 <rsyslog-event-id-11048>`
- :ref:`rsyslog Windows Agent Event ID 11049 <rsyslog-event-id-11049>`
- :ref:`rsyslog Windows Agent Event ID 11050 <rsyslog-event-id-11050>`
- :ref:`rsyslog Windows Agent Event ID 11051 <rsyslog-event-id-11051>`
- :ref:`rsyslog Windows Agent Event ID 11052 <rsyslog-event-id-11052>`
- :ref:`rsyslog Windows Agent Event ID 11053 <rsyslog-event-id-11053>`
- :ref:`rsyslog Windows Agent Event ID 11054 <rsyslog-event-id-11054>`
- :ref:`rsyslog Windows Agent Event ID 11055 <rsyslog-event-id-11055>`
- :ref:`rsyslog Windows Agent Event ID 11056 <rsyslog-event-id-11056>`
- :ref:`rsyslog Windows Agent Event ID 11057 <rsyslog-event-id-11057>`
- :ref:`rsyslog Windows Agent Event ID 11072 <rsyslog-event-id-11072>`
- :ref:`rsyslog Windows Agent Event ID 11073 <rsyslog-event-id-11073>`
- :ref:`rsyslog Windows Agent Event ID 11090 <rsyslog-event-id-11090>`
- :ref:`rsyslog Windows Agent Event ID 11091 <rsyslog-event-id-11091>`
- :ref:`rsyslog Windows Agent Event ID 11092 <rsyslog-event-id-11092>`
- :ref:`rsyslog Windows Agent Event ID 11093 <rsyslog-event-id-11093>`
- :ref:`rsyslog Windows Agent Event ID 11094 <rsyslog-event-id-11094>`
- :ref:`rsyslog Windows Agent Event ID 11121 <rsyslog-event-id-11121>`
- :ref:`rsyslog Windows Agent Event ID 11122 <rsyslog-event-id-11122>`
- :ref:`rsyslog Windows Agent Event ID 11198 <rsyslog-event-id-11198>`
- :ref:`rsyslog Windows Agent Event ID 11199 <rsyslog-event-id-11199>`
- :ref:`rsyslog Windows Agent Event ID 11200 <rsyslog-event-id-11200>`
- :ref:`rsyslog Windows Agent Event ID 11201 <rsyslog-event-id-11201>`
- :ref:`rsyslog Windows Agent Event ID 11202 <rsyslog-event-id-11202>`


Related procedures
------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>`
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>`
