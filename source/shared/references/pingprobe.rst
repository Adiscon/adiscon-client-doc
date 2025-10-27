Ping Probe
==========

**echostatus**

Status returned for the echo request

The status value can be one of the following:

.. code-block:: text

  0 = IP_SUCCESS
  11002 = IP_DEST_NET_UNREACHABLE
  11003 = IP_DEST_HOST_UNREACHABLE
  11010 = IP_REQ_TIMED_OUT
  11013 = IP_TTL_EXPIRED_TRANSIT
  11016 = IP_SOURCE_QUENCH
  11018 = IP_BAD_DESTINATION

**roundtriptime**

Round trip time for the ping packet (if successful)
