:orphan:

.. _rest-output-getting-started:

How do I set up HTTP REST Output?
=================================

Question
--------

How do I forward events to a REST API or OpenSearch using the configuration
client?

Answer
------

Add an **HTTP REST Output** action to your ruleset, choose a profile (Custom or
OpenSearch bulk), configure the endpoint and request body, and save the
configuration.

Details
-------

The **HTTP REST Output** action (type **1032**, ``RestOutput``) is available on
WinSyslog, EventReporter, and MonitorWare Agent starting with **26.07**. It is
listed under **Forwarding** in the action list.

Action path
-----------

1. Open the configuration client and select the target ruleset and rule.
2. Add action → **HTTP REST Output**.
3. On the **General** tab, choose **Custom** or **OpenSearch bulk** and set the
   endpoint (server, path, port, TLS as needed).
4. On the **Request** tab, set the HTTP method, content type, headers, and
   request template or JSON property mappings.
5. On the **Advanced** tab, adjust timeout, user agent, and retry status codes
   if needed.
6. Save the configuration and restart the service.
7. Send a test event and verify delivery at the remote endpoint.

Related information
-------------------

- See **HTTP REST Output** and **HTTP Request** under **Actions → Forwarding**
  in the WinSyslog, EventReporter, or MonitorWare Agent manual when those
  actions are part of your product build.
- :doc:`../references/accessingproperties`
