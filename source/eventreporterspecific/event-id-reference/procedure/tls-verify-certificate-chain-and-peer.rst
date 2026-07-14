:orphan:

.. _event-id-procedure-tls-verify-certificate-chain-and-peer:

.. meta::
   :description: Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
   :procedure-id: tls.verify-certificate-chain-and-peer
   :procedure-reference: true

Verify TLS certificates, private keys, and permitted peers
==========================================================

When to use this procedure
--------------------------

Use when an Event ID reports a TLS certificate, private-key, trust-chain, fingerprint, or permitted-peer failure, or when TCP succeeds but the secure session does not.

Applies to
----------

This procedure applies to EventReporter.

Prerequisites
-------------

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.
- Record whether the affected object is a listener or a forwarding action and whether certificate-name or certificate-fingerprint authentication is configured.

Safety
------

- Run diagnostic checks before changing configuration.
- Never display, copy, upload, or include a private key or passphrase in troubleshooting evidence.
- Back up the affected configuration and certificate files before changing paths, files, or permissions.

Configuration path
------------------

Configuration Client > the service, rule, or action named on the Event ID page.

Procedure
---------

#. Record the configured CA PEM, certificate PEM, private-key PEM, permitted peers, and authentication mode. Do not record file contents.

   **Expected result:** The affected object and the exact configured paths and peer-authentication mode are identified.

   **If it fails:** Use the complete Event Log detail and a redacted configuration export to identify the affected object before changing settings.

#. Confirm that each configured file exists, is readable, and contains the expected PEM object type. The private-key check reports only classification booleans.

   .. code-block:: powershell

      Get-Item -LiteralPath '<CA_PEM_PATH>','<CERTIFICATE_PEM_PATH>','<PRIVATE_KEY_PEM_PATH>' | Format-Table FullName,Length,LastWriteTime
      certutil -dump '<CA_PEM_PATH>'
      certutil -dump '<CERTIFICATE_PEM_PATH>'
      $keyText = [IO.File]::ReadAllText('<PRIVATE_KEY_PEM_PATH>'); [pscustomobject]@{ HasPrivateKey = $keyText -match '-----BEGIN (?:RSA |EC |DSA )?PRIVATE KEY-----'; IsCertificateRequest = $keyText -match '-----BEGIN (?:NEW )?CERTIFICATE REQUEST-----'; IsEncrypted = $keyText -match '-----BEGIN ENCRYPTED PRIVATE KEY-----' }; Remove-Variable keyText
      icacls '<PRIVATE_KEY_PEM_PATH>'

   **Expected result:** The CA and certificate parse successfully. The key classification reports HasPrivateKey=True, IsCertificateRequest=False, and IsEncrypted=False. The product service account has read access.

   **If it fails:** Correct a wrong or missing path, replace a CSR with the actual matching private key, export an unencrypted service key, or grant the product service account the minimum required read access. Never weaken access for all users.

#. Verify the certificate chain and compare the peer identity with the configured authentication mode.

   .. code-block:: powershell

      certutil -verify '<CERTIFICATE_PEM_PATH>' '<CA_PEM_PATH>'

   **Expected result:** The chain verifies to the intended CA. In certificate-name mode, a configured permitted peer matches a certificate subject alternative name or common name. In fingerprint mode, a configured fingerprint matches the peer certificate using the configured format.

   **If it fails:** Correct the CA chain or permitted-peer value. Do not disable peer validation as a permanent repair.

#. After saving the correction and restarting or reloading the affected object as required, perform one uniquely identifiable TLS test through the same listener or forwarding action.

   **Expected result:** The secure session completes and the intended destination records the test exactly once.

   **If it fails:** Collect the first new product event and bounded debug output from the same test. A later 'no shared cipher' handshake error can be a consequence of a local certificate or key that did not load.

Repair
------

#. Copy corrected CA, certificate, and unencrypted matching private-key files to a service-readable protected directory, then update only the affected object's paths.
#. Restrict the private-key ACL to administrators and the product service account with read access; do not grant broad user access.
#. Correct permitted peers from the actual peer certificate identity: use a subject alternative name or common name for certificate-name mode, or the documented fingerprint format for certificate-fingerprint mode.

Rollback
--------

#. Restore the backed-up configuration paths and files if the corrected TLS test fails.
#. Restore the prior ACL from the recorded backup, then restart or reload only the affected object as required.

Verify the result
-----------------

Repeat the same uniquely identifiable secure transfer, confirm positive receipt, and verify that the applicable TLS Event ID does not recur during that test and that queued delivery or listener acceptance continues normally.

Evidence to collect
-------------------

- The complete Event Log entry and neighboring product events with timestamps.
- A redacted configuration export showing the affected TLS mode and paths, with hostnames and addresses replaced by example values.
- Certificate metadata, chain-verification output, private-key classification booleans, and the private-key ACL; never collect the private key or its contents.
- A bounded debug log covering one failed test after removing credentials, private material, customer names, addresses, and environment-specific object names.

Optional tools
--------------

- OpenSSL may be used offline to compare the public key derived from the certificate with the public key derived from the private key. Compare hashes only, never key contents, and never place a passphrase on a command line.
- Wireshark may be used for a bounded handshake capture when native evidence is insufficient; redact addresses before sharing it.

Related Event IDs
-----------------

- :ref:`EventReporter Event ID 11000 <eventreporter-event-id-11000>`
- :ref:`EventReporter Event ID 11001 <eventreporter-event-id-11001>`
- :ref:`EventReporter Event ID 11002 <eventreporter-event-id-11002>`
- :ref:`EventReporter Event ID 11003 <eventreporter-event-id-11003>`
- :ref:`EventReporter Event ID 11004 <eventreporter-event-id-11004>`
- :ref:`EventReporter Event ID 11034 <eventreporter-event-id-11034>`
- :ref:`EventReporter Event ID 11035 <eventreporter-event-id-11035>`
- :ref:`EventReporter Event ID 11048 <eventreporter-event-id-11048>`
- :ref:`EventReporter Event ID 11049 <eventreporter-event-id-11049>`
- :ref:`EventReporter Event ID 11050 <eventreporter-event-id-11050>`
- :ref:`EventReporter Event ID 11051 <eventreporter-event-id-11051>`
- :ref:`EventReporter Event ID 11052 <eventreporter-event-id-11052>`
- :ref:`EventReporter Event ID 11053 <eventreporter-event-id-11053>`
- :ref:`EventReporter Event ID 11054 <eventreporter-event-id-11054>`
- :ref:`EventReporter Event ID 11055 <eventreporter-event-id-11055>`
- :ref:`EventReporter Event ID 11056 <eventreporter-event-id-11056>`
- :ref:`EventReporter Event ID 11057 <eventreporter-event-id-11057>`
- :ref:`EventReporter Event ID 11072 <eventreporter-event-id-11072>`
- :ref:`EventReporter Event ID 11073 <eventreporter-event-id-11073>`
- :ref:`EventReporter Event ID 11090 <eventreporter-event-id-11090>`
- :ref:`EventReporter Event ID 11091 <eventreporter-event-id-11091>`
- :ref:`EventReporter Event ID 11092 <eventreporter-event-id-11092>`
- :ref:`EventReporter Event ID 11093 <eventreporter-event-id-11093>`
- :ref:`EventReporter Event ID 11094 <eventreporter-event-id-11094>`
- :ref:`EventReporter Event ID 11121 <eventreporter-event-id-11121>`
- :ref:`EventReporter Event ID 11122 <eventreporter-event-id-11122>`
- :ref:`EventReporter Event ID 11198 <eventreporter-event-id-11198>`
- :ref:`EventReporter Event ID 11199 <eventreporter-event-id-11199>`
- :ref:`EventReporter Event ID 11200 <eventreporter-event-id-11200>`
- :ref:`EventReporter Event ID 11201 <eventreporter-event-id-11201>`


Related procedures
------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>`
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>`
