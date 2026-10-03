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
``nMetricsHttpEnable`` must be enabled. If your Adiscon User Interface does not provide a Metrics editor, edit this
block directly. This path is required for
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

Target-host provisioning for remote configuration
-------------------------------------------------

In service builds whose command help lists ``-metrics``, an administrator can
provision the supported local HTTPS endpoint directly on the service machine.
This also applies when the configuration was saved through Remote Registry
from the Adiscon User Interface on another machine. The Adiscon User Interface
does not need to be installed on the service machine.

Save the requested Metrics settings, then run an elevated console on the
service machine. For MonitorWare Agent, use::

    mwagent.exe -metrics provision
    mwagent.exe -metrics repair
    mwagent.exe -metrics validate

Use ``winsyslg.exe``, ``evntslog.exe`` or ``rsyslogcl.exe`` for the corresponding
product. Add the installed service name after the operation when selecting a
custom service instance.

The supported command profile is exactly
``https://127.0.0.1:<port>/metrics/``, including the default port 9109, with
Windows Integrated Authentication. The command creates missing owned local
URL reservations and certificate bindings, enables the requested endpoint,
restarts the selected service, and requires an authenticated health check.
Repair can restore a drifted prefix to the service's manifest-owned endpoint.
Foreign reservations or bindings are rejected rather than adopted or removed.

``validate`` is a dry run: it checks configuration, ownership and authenticated
health without changing configuration, certificates, HTTP.sys or service state.
Successful provision, repair and validation return codes 0, 10 and 20
respectively. A stopped endpoint, failed authentication or unsupported response
returns a failure code. A restart or health failure can occur after the
configuration was committed; review the JSON result before retrying repair.

HTTPS and Windows authentication remain required. NTLM fallback is disabled
when no policy is saved; an explicitly saved compatibility policy is preserved.
The command never enables fallback to make a check pass. Some Windows/domain
configurations require deliberate authentication configuration before an
IP-loopback endpoint can pass health with NTLM disabled.

The first command profile supports ordinary local UTF-8 CFG/YAML documents and
registry configuration. It rejects includes, automatic URL reload, network
configuration files, custom/remote endpoints, external certificates and mTLS.
Use manual HTTPS provisioning for those advanced profiles. Remote execution
and credential delegation are separate administrator tasks.