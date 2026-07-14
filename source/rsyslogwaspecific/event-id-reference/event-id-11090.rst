:orphan:

.. _rsyslog-event-id-11090:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11090: SETP listener stopped after a protocol server error.
   :event-id: 11090
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: SETP listener
   :event-reference: true

rsyslog Windows Agent Event ID 11090: SETP listener stopped after a protocol server error
=========================================================================================

Answer
------

The SETP listener encountered a protocol-server error while setting up or running the listener. The listener stops rather than continuing after this error.

Event details
-------------

- **Event ID:** ``11090``
- **Severity:** Error
- **Component:** SETP listener
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`SETP listener error: {error_detail}`

Possible causes
---------------

- The configured SETP listener settings are invalid or unavailable.
- A socket, TLS, or SETP protocol operation failed.
- A required listener resource could not be initialized.

Immediate checks
----------------

#. Record the complete embedded error and the affected SETP listener configuration.
#. Verify listener binding, port availability, firewall rules, and any TLS certificate or peer settings.
#. Correct the reported cause and restart or reload the listener once.

Detailed procedures
-------------------

- :ref:`Verify listener binding and Windows Firewall rules <event-id-procedure-network-verify-listener-binding-and-firewall>` — Confirm effective address, port, transport, owning process, and inbound policy.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the SETP listener remains running and accepts a controlled connection without another Event ID 11090.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11091 <rsyslog-event-id-11091>`
- :ref:`Event ID 11092 <rsyslog-event-id-11092>`
- :ref:`Event ID 11093 <rsyslog-event-id-11093>`
