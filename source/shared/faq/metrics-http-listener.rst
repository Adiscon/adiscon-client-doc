:orphan:

.. _metrics-http-listener:

How do I enable the Metrics HTTP listener for Message Ringbuffer access?
========================================================================

Question
--------

Message Ringbuffer remote reads require a secure Metrics HTTP listener. How do
I enable that listener?

Answer
------

Enable Metrics and its HTTP listener in the file-based
``general(name="Metrics")`` block. Both ``nMetricsEnable`` and
``nMetricsHttpEnable`` must be enabled. Current configuration clients preserve
that block but do not provide a Metrics editor. This path is required for
Message Ringbuffer remote reads starting with **26.08**.

Details
-------

Message Ringbuffer remote access is served by the Metrics HTTP listener, not by
a separate ringbuffer listener. If either ``nMetricsEnable`` or
``nMetricsHttpEnable`` is missing or disabled, the listener is treated as
disabled and remote buffer reads are unavailable.

Configure Metrics by editing CFG, YAML, or equivalent registry settings that
contain ``general(name="Metrics")``. After you change Metrics settings, reload
or restart the service so the listener picks them up.

Action path
-----------

1. Back up the current configuration.
2. In the configuration file, ensure a ``general(name="Metrics")`` block exists.
3. Set ``nMetricsEnable`` and ``nMetricsHttpEnable`` so both are enabled.
4. Save the file, then reload or restart the service.
5. Confirm the Message Ringbuffer action can be read through the Metrics HTTP
   endpoint for your deployment.

Related information
-------------------

- Message Ringbuffer action documentation in the product manual
- :ref:`unsupported-configuration-blocks`
