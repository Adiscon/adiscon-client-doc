:orphan:

Net Send
========

Send short alert messages to a recipient machine via the Windows
Messenger service (``net send``).

.. warning::

   **Removed from configuration client (26.07):** Net Send cannot be created
   in the **26.07** configuration client. See :doc:`../mwagentspecific/a-netsend`
   for legacy reference and alternatives.

   **Deprecated:** ``net send`` pop-up messages are not available by default on
   modern Windows versions.


.. image:: ../images/a-netsend.png
   :width: 100%

* Net Send*

This page is retained for historical reference. For current alerting, use
**Send Email**, :doc:`HTTP REST Output <../mwagentspecific/a-restoutput>`, or
syslog forwarding.

Further details: :doc:`net send <../mwagentspecific/a-netsend>`.
