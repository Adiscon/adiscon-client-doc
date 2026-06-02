:orphan:

.. _tls-listener-certificate-files-shared:

What do CA PEM, Certificate PEM, and Key PEM mean for TLS input services?
=========================================================================

Question
--------

What do the ``CA PEM``, ``Certificate PEM``, and ``Key PEM`` fields mean for
TLS-enabled input services such as ``RELP Listener`` or ``SETP Server``?

Answer
------

For TLS-enabled input services:

- ``CA PEM`` is the CA bundle used to validate peer certificates.
- ``Certificate PEM`` is the certificate presented by the receiving service.
- ``Key PEM`` is the private key that matches that certificate.

The private key must be in PEM format and must not be protected by a
passphrase.

Details
-------

The ``CA PEM`` field is used when certificate validation is enabled for
incoming TLS connections. The receiving service uses the certificates in this
file to validate certificates presented by connecting clients.

The ``Certificate PEM`` field should contain the certificate that the product
presents to connecting clients. If intermediate CA certificates are required so
that clients can build the chain, include the service certificate first and then
append the intermediate CA certificates in order toward the root CA.

The ``Key PEM`` field must contain the private key that belongs to that
certificate. Use an unencrypted PEM key file. Passphrase-protected private keys
are not supported in these fields.

If client certificates are issued through a CA chain, the ``CA PEM`` file can
contain multiple CA certificates. Include the intermediate CA certificates
first, followed by the root CA certificate.

Action path
-----------

1. Decide whether the input service should validate client certificates.
2. Prepare a PEM CA bundle for ``CA PEM`` if certificate validation is used.
3. Prepare a PEM certificate file for ``Certificate PEM``. Include the
   intermediate chain if clients need it to validate the certificate.
4. Prepare the matching PEM private key for ``Key PEM`` and remove any
   passphrase protection before using it.
5. Load the files into the TLS configuration fields and test the connection.

Related information
-------------------

See the product-specific TLS service reference page for the exact
UI location of these fields.
