:orphan:

.. _mwagent-event-id-11037:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11037: Send to Communications Port action could not write a byte.
   :event-id: 11037
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Send to Communications Port action
   :event-reference: true

MonitorWare Agent Event ID 11037: Send to Communications Port action could not write a byte
===========================================================================================

Answer
------

The action opened the configured communications port but Windows reported an error while writing the message. The product closes the port after the failure.

Event details
-------------

- **Event ID:** ``11037``
- **Severity:** Error
- **Component:** Send to Communications Port action
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Error in SendMessage - GetLastError: {error_code}`

Possible causes
---------------

- The serial device was disconnected or stopped responding.
- The port, driver, flow-control, baud-rate, parity, or stop-bit settings do not match the device.
- Another process took control of the port or the device driver failed.

Immediate checks
----------------

#. Translate the Windows error code and confirm the configured port name.
#. Verify the device and driver state, then compare both endpoints' serial settings.
#. Close other applications using the port and send a controlled test message.

Detailed procedures
-------------------

- :ref:`Interpret a Windows or Winsock error code <event-id-procedure-windows-interpret-error-code>` — Translate a numeric code without losing its operation or subsystem context.
- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the complete controlled message reaches the serial device without Event ID 11037.

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

- :ref:`Event ID 11014 <mwagent-event-id-11014>`
- :ref:`Event ID 11019 <mwagent-event-id-11019>`
- :ref:`Event ID 11021 <mwagent-event-id-11021>`
