Shutdown protection timeout
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This capability is available starting with **26.08**.

**File Configuration field:**
  nShutdownProtectionTimeout

**Description**
   This setting applies only when **Protect Service against shutdown** is
   enabled. Enter the maximum time in milliseconds for the complete protected
   shutdown. Set it to ``0`` to wait without a deadline for cooperative queue
   processing to finish.

   A positive timeout bounds shutdown time, but messages that are still in
   memory or have not been stored durably can be lost when that deadline is
   reached.

.. image:: /images/generaloptions-shutdown-protection-timeout.png
   :width: 100%
   :alt: Shutdown protection timeout

*Shutdown protection enabled with the timeout set to 0 (unlimited).*
