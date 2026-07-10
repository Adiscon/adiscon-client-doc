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

Prerequisites
-------------

.. only:: eventreporter

   This procedure applies to EventReporter.

.. only:: winsyslog or winsyslog_j

   This procedure applies to WinSyslog.

.. only:: mwagent

   This procedure applies to MonitorWare Agent.

.. only:: rsyslog

   This procedure applies to rsyslog Windows Agent.

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Run diagnostic checks before changing configuration.
- Remove passwords, private keys, license data, and other secrets from evidence.

Configuration paths
-------------------

.. only:: eventreporter

   **EventReporter:** Configuration Client > the service, rule, or action named on the Event ID page.

.. only:: winsyslog or winsyslog_j

   **WinSyslog:** Configuration Client > the service, rule, or action named on the Event ID page.

.. only:: mwagent

   **MonitorWare Agent:** Configuration Client > the service, rule, or action named on the Event ID page.

.. only:: rsyslog

   **rsyslog Windows Agent:** Configuration Client > the service, rule, or action named on the Event ID page.

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

.. only:: winsyslog or winsyslog_j

   - WinSyslog Event ID 11000
   - WinSyslog Event ID 11001
   - WinSyslog Event ID 11002
   - WinSyslog Event ID 11003
   - WinSyslog Event ID 11004
   - WinSyslog Event ID 11034
   - WinSyslog Event ID 11035
   - WinSyslog Event ID 11048
   - WinSyslog Event ID 11049
   - WinSyslog Event ID 11050
   - WinSyslog Event ID 11051
   - WinSyslog Event ID 11052
   - WinSyslog Event ID 11053
   - WinSyslog Event ID 11054
   - WinSyslog Event ID 11055
   - WinSyslog Event ID 11056
   - WinSyslog Event ID 11057
   - WinSyslog Event ID 11072
   - WinSyslog Event ID 11073
   - WinSyslog Event ID 11090
   - WinSyslog Event ID 11091
   - WinSyslog Event ID 11092
   - WinSyslog Event ID 11093
   - WinSyslog Event ID 11094
   - WinSyslog Event ID 11121
   - WinSyslog Event ID 11122
   - WinSyslog Event ID 11198
   - WinSyslog Event ID 11199
   - WinSyslog Event ID 11200
   - WinSyslog Event ID 11201
   - WinSyslog Event ID 11202

.. only:: eventreporter

   - EventReporter Event ID 11000
   - EventReporter Event ID 11001
   - EventReporter Event ID 11002
   - EventReporter Event ID 11003
   - EventReporter Event ID 11004
   - EventReporter Event ID 11034
   - EventReporter Event ID 11035
   - EventReporter Event ID 11048
   - EventReporter Event ID 11049
   - EventReporter Event ID 11050
   - EventReporter Event ID 11051
   - EventReporter Event ID 11052
   - EventReporter Event ID 11053
   - EventReporter Event ID 11054
   - EventReporter Event ID 11055
   - EventReporter Event ID 11056
   - EventReporter Event ID 11057
   - EventReporter Event ID 11072
   - EventReporter Event ID 11073
   - EventReporter Event ID 11090
   - EventReporter Event ID 11091
   - EventReporter Event ID 11092
   - EventReporter Event ID 11093
   - EventReporter Event ID 11094
   - EventReporter Event ID 11121
   - EventReporter Event ID 11122
   - EventReporter Event ID 11198
   - EventReporter Event ID 11199
   - EventReporter Event ID 11200
   - EventReporter Event ID 11201
   - EventReporter Event ID 11202

.. only:: mwagent

   - MonitorWare Agent Event ID 11000
   - MonitorWare Agent Event ID 11001
   - MonitorWare Agent Event ID 11002
   - MonitorWare Agent Event ID 11003
   - MonitorWare Agent Event ID 11004
   - MonitorWare Agent Event ID 11034
   - MonitorWare Agent Event ID 11035
   - MonitorWare Agent Event ID 11048
   - MonitorWare Agent Event ID 11049
   - MonitorWare Agent Event ID 11050
   - MonitorWare Agent Event ID 11051
   - MonitorWare Agent Event ID 11052
   - MonitorWare Agent Event ID 11053
   - MonitorWare Agent Event ID 11054
   - MonitorWare Agent Event ID 11055
   - MonitorWare Agent Event ID 11056
   - MonitorWare Agent Event ID 11057
   - MonitorWare Agent Event ID 11072
   - MonitorWare Agent Event ID 11073
   - MonitorWare Agent Event ID 11090
   - MonitorWare Agent Event ID 11091
   - MonitorWare Agent Event ID 11092
   - MonitorWare Agent Event ID 11093
   - MonitorWare Agent Event ID 11094
   - MonitorWare Agent Event ID 11121
   - MonitorWare Agent Event ID 11122
   - MonitorWare Agent Event ID 11198
   - MonitorWare Agent Event ID 11199
   - MonitorWare Agent Event ID 11200
   - MonitorWare Agent Event ID 11201
   - MonitorWare Agent Event ID 11202

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 11000
   - rsyslog Windows Agent Event ID 11001
   - rsyslog Windows Agent Event ID 11002
   - rsyslog Windows Agent Event ID 11003
   - rsyslog Windows Agent Event ID 11004
   - rsyslog Windows Agent Event ID 11034
   - rsyslog Windows Agent Event ID 11035
   - rsyslog Windows Agent Event ID 11048
   - rsyslog Windows Agent Event ID 11049
   - rsyslog Windows Agent Event ID 11050
   - rsyslog Windows Agent Event ID 11051
   - rsyslog Windows Agent Event ID 11052
   - rsyslog Windows Agent Event ID 11053
   - rsyslog Windows Agent Event ID 11054
   - rsyslog Windows Agent Event ID 11055
   - rsyslog Windows Agent Event ID 11056
   - rsyslog Windows Agent Event ID 11057
   - rsyslog Windows Agent Event ID 11072
   - rsyslog Windows Agent Event ID 11073
   - rsyslog Windows Agent Event ID 11090
   - rsyslog Windows Agent Event ID 11091
   - rsyslog Windows Agent Event ID 11092
   - rsyslog Windows Agent Event ID 11093
   - rsyslog Windows Agent Event ID 11094
   - rsyslog Windows Agent Event ID 11121
   - rsyslog Windows Agent Event ID 11122
   - rsyslog Windows Agent Event ID 11198
   - rsyslog Windows Agent Event ID 11199
   - rsyslog Windows Agent Event ID 11200
   - rsyslog Windows Agent Event ID 11201
   - rsyslog Windows Agent Event ID 11202


Related procedures
------------------

- :doc:`Resolve a destination and test its TCP port <network-resolve-host-and-test-tcp-port>`
- :doc:`Export configuration and collect a bounded debug log <evidence-export-configuration-and-debug-log>`
