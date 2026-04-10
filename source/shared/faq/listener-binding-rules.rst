:orphan:

.. _shared-listener-binding-rules:

How Do Listener IP, Port, and Protocol Conflicts Work?
======================================================

Question
--------

When I create multiple listeners or server services, which combinations can
run at the same time and which ones conflict?

Answer
------

Treat each listener as binding to a local network endpoint. In practice, that
endpoint is defined by the transport protocol, the local IP address, and the
local port.

Two listeners can run side by side only when their bindings do not conflict.
Changing the protocol, IP address, or port avoids the conflict. If two
listeners need the same binding, only one of them can own it.

TLS does not change that rule. A TLS-enabled listener still binds a TCP port,
so plain TCP and TCP+TLS cannot both listen on the same IP address and port.

Details
-------

Use this rule of thumb:

- Different transport protocols can coexist on the same port, for example
  UDP/514 and TCP/514.
- TCP and TCP+TLS cannot both use the same IP address and port, because both
  bind TCP at the socket level.
- Different ports can coexist, for example TCP/514 and TCP+TLS/1514.
- Different local IP addresses can also coexist, as long as the listener type
  exposes that setting.

Short IP primer
^^^^^^^^^^^^^^^

The special address ``0.0.0.0`` means "all local IPv4 addresses" and ``::``
means "all local IPv6 addresses". If a listener already binds ``0.0.0.0`` on a
given protocol and port, another listener of the same protocol usually cannot
reuse that port on one specific IPv4 address because the wildcard listener
already covers it.

Listener-specific differences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The exact UI fields depend on the listener type:

- Some listeners expose protocol, IP address, and port directly.
- Some listeners expose only part of that combination.
- Some listeners support only one transport mode and therefore do not offer a
  protocol choice at all.
- Some listeners separate IPv4 and IPv6 into different services or settings.

The conflict rule still stays the same: one active listener per effective
binding.

Concrete examples
^^^^^^^^^^^^^^^^^

These combinations are valid:

- UDP / ``0.0.0.0`` / ``514``
- TCP / ``0.0.0.0`` / ``514``
- TCP+TLS / ``0.0.0.0`` / ``1514``

This combination conflicts:

- TCP / ``0.0.0.0`` / ``514``
- TCP+TLS / ``0.0.0.0`` / ``514``

Action path
-----------

1. Identify the protocol, local IP address, and local port required by each
   listener.
2. Check whether any active listener already uses the same effective binding.
3. If there is a conflict, change the port or bind to a different local IP
   address when that listener type allows it.
4. If TLS is required in parallel with plain TCP, plan separate bindings before
   configuring the senders.
5. After changing the listener side, update the senders so they use the new
   destination port or IP address.

Related information
-------------------

- :doc:`tls-listener-certificate-files`
- Use the product-specific listener reference page for the exact UI fields of
  the listener type you are configuring.
