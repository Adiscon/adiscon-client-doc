MonitorWare Echo Request
========================

**responsestatus**

The status of the echo request. Possible values:

.. code-block:: text

  0 - request failed (probed system not alive)
  1 - request succeeded

If the request failed, additional information can be found in the
* msg* :doc:`standard property <../references/standardproperties>`.
