Port Probe
==========

Port Probe helps to monitor a specific service on the remote machine. It tries
to connect to the service port and if it fails, the service is definitely not
running. In this case, an event will be generated that is definitely an
indication of problems. It is very similar to Ping Probe with a key difference
that it does not check the IP stack availability but rather a specific TCP port.


.. image:: ../images/portprobe.png
   :width: 100%

* Port Probe*

Here is an example how to monitor :doc:`external devices via port probe <../shared/gettingstarted/monitoringexternaldevicesportprobe>`.

Further details can be found here: :doc:`port probe <../mwagentspecific/portprobe>`.
