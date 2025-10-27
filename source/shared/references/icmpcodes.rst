.. index:: ICMP Codes

ICMP Codes
==========

ICMP codes are often used when doing firewall and/or router diagnostics. For
convenience, find an excerpt from RFC1700 below. The full RFC can be obtained
from several places, for example at http://www.ietf.org/rfc/rfc1700.txt

ICMP Type Numbers - The Internet Control Message Protocol (ICMP) has many
messages that are identified by a "type" field. Many of these ICMP types have
a "code" field. Here we list the types with their assigned code fields.


.. code-block:: text

  Type Name                       Reference

  0    Echo Reply                 [RFC792]
       Codes:
       0 No Code

  1    Unassigned                 [JBP]

  2    Unassigned                 [JBP]

  3    Destination Unreachable    [RFC792]
       Codes:
       0 Net Unreachable
       1 Host Unreachable
       2 Protocol Unreachable
       3 Port Unreachable
       4 Fragmentation Needed and Don't Fragment was Set
       5 Source Route Failed
       6 Destination Network Unknown
       7 Destination Host Unknown
       8 Source Host Isolated
       9 Communication with Destination Network is
         Administratively Prohibited
      10 Communication with Destination Host is
         Administratively Prohibited
      11 Destination Network Unreachable for Type of Service
      12 Destination Host Unreachable for Type of Service

  4   Source Quench               [RFC792]
      Codes:
      0 No Code

  5   Redirect                    [RFC792]
      Codes:
      0 Redirect Datagram for the Network (or subnet)
      1 Redirect Datagram for the Host
      2 Redirect Datagram for the Type of Service and Network
      3 Redirect Datagram for the Type of Service and Host

  6   Alternate Host Address      [JBP]
      Codes:
      0 Alternate Address for Host

  7   Unassigned                  [JBP]

  8   Echo                        [RFC792]
      Codes:
      0 No Code

  9   Router Advertisement        [RFC1256]
      Codes:
      0 No Code

  10  Router Selection            [RFC1256]
      Codes:
      0 No Code

  11  Time Exceeded               [RFC792]
      Codes:
      0 Time to Live exceeded in Transit
      1 Fragment Reassembly Time Exceeded

  12  Parameter Problem           [RFC792]
      Codes:
      0 Pointer indicates the error
      1 Missing a Required Option
      2 Bad Length

  13  Timestamp                   [RFC792]
      Codes:
      0 No Code

  14  Timestamp Reply             [RFC792]
      Codes:
      0 No Code

  15  Information Request         [RFC792]
      Codes:
      0 No Code

  16  Information Reply           [RFC792]
      Codes:
      0 No Code

  17  Address Mask Request        [RFC950]
      Codes:
      0 No Code

  18  Address Mask Reply          [RFC950]
      Codes:
      0 No Code

  19  Reserved (for Security)     [Solo]

  20-29 Reserved                  [ZSu]
      (for Robustness Experiment)

  30  Traceroute                  [RFC1393]

  31  Datagram Conversion Error   [RFC1475]

  32  Mobile Host Redirect        [David Johnson]

  33  IPv6 Where-Are-You          [Bill Simpson]

  34  IPv6 I-Am-Here              [Bill Simpson]

  35  Mobile Registration Request [Bill Simpson]

  36  Mobile Registration Reply   [Bill Simpson]

  37-255 Reserved                 [JBP]
