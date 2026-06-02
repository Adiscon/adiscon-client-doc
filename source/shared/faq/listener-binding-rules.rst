:orphan:

.. _shared-listener-binding-rules:

How Do Port, Address, and Transport Conflicts Work for Input Services?
======================================================================

Question
--------

When I create multiple input services, which combinations can run at the same
time and which ones conflict?

Answer
------

Treat each receive-side service as an input service. When a GUI field or older
page says **listener**, it refers to the network side of that input service.
In practice, the relevant settings are the transport protocol, the local IP
address, and the local port.

Two input services can run side by side only when those settings do not
conflict. Changing the transport, IP address, or port avoids the conflict. If
two input services need the same combination, only one of them can use it.

TLS does not change that rule. A TLS-enabled input service still binds a TCP
port, so plain TCP and TCP+TLS cannot both listen on the same IP address and
port.

Details
-------

Use this rule of thumb:

- Different transport protocols can coexist on the same port, for example
  UDP/514 and TCP/514.
- TCP and TCP+TLS cannot both use the same IP address and port, because both
  bind TCP at the socket level.
- Different ports can coexist, for example TCP/514 and TCP+TLS/1514.
- Different local IP addresses can also coexist, as long as the input type
  exposes that setting.

For most administrators, the simplest practical rule is this:

- Reusing the same port number is usually safe only when the transport differs,
  for example UDP versus TCP.
- Do not expect reuse to work when both services ultimately use TCP on the same
  local address, even if the higher-level protocol is different.
- TLS does not create a separate transport; it still runs on top of TCP.
- DTLS is a notable exception because it runs over UDP.

Short IP primer
^^^^^^^^^^^^^^^

The special address ``0.0.0.0`` means "all local IPv4 addresses" and ``::``
means "all local IPv6 addresses". If one input service already uses
``0.0.0.0`` on a given transport and port, another input service with the same
transport usually cannot reuse that port on one specific IPv4 address because
the wildcard address already covers it.

GUI-specific differences
^^^^^^^^^^^^^^^^^^^^^^^^

The exact UI fields depend on the input type:

- Some input services expose transport, IP address, and port directly.
- Some input services expose only part of that combination.
- Some input services support only one transport mode and therefore do not
  offer a
  transport choice at all.
- Some input services separate IPv4 and IPv6 into different services or
  settings.

The conflict rule still stays the same: one active input service per effective
address, port, and transport combination.

In WinSyslog-oriented wording, that usually means one active network input
service per effective address, port, and transport combination.

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

1. Identify the transport, local IP address, and local port required by each
   input service.
2. Check whether any active input service already uses the same effective
   address, port, and transport combination.
3. If there is a conflict, change the port or bind to a different local IP
   address when that input type allows it.
4. If TLS is required in parallel with plain TCP, plan separate ports or
   addresses before configuring the senders.
5. After changing the input settings, update the senders so they use the new
   destination port or IP address.

Related information
-------------------

- :doc:`tls-listener-certificate-files`
- Use the product-specific service reference page for the exact UI fields of
  the input type you are configuring.
