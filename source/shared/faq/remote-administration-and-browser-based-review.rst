:orphan:

.. _shared-remote-administration-and-browser-based-review:

How Do Remote Administration and Browser-Based Log Review Fit Together?
=======================================================================

Question
--------

How do remote administration and browser-based log review work in the current
Adiscon Windows products?

Answer
------

Treat them as two separate functions.

- Administrative changes are made with the Configuration Client, either on the
  local system or through the remote-connect workflow when that product
  supports it.
- The current product family does not use a built-in browser administration
  interface for service configuration.
- Browser-based review is handled by Adiscon LogAnalyzer, which is a separate
  and optional component for stored data. It is not the service administration
  interface.

Details
-------

Remote administration
^^^^^^^^^^^^^^^^^^^^^

The current product family uses the Windows Configuration Client for
administration. Depending on the product and deployment style, you typically
work in one of these ways:

- connect to another machine from the client
- export and import configuration
- use a rollout process for repeated deployments

This means remote administration is a client-and-deployment workflow, not a
built-in browser administration console.

When the client connects to another machine directly, the target system must be
reachable over the network and the current user must have the required access
rights on that remote machine.

Browser-based log review
^^^^^^^^^^^^^^^^^^^^^^^^

Adiscon LogAnalyzer is the browser-based component in this ecosystem. It is
used to review data that has already been written to a file or database.
It is deployed separately from the logging service and requires its own web
server and PHP runtime.

That split is important:

- LogAnalyzer is for stored data review.
- The logging service still receives, processes, and stores or forwards data.
- The Configuration Client is still the place where you change service
  settings.

What this means operationally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want both remote administration and browser-based visibility, plan them
as separate pieces:

1. Decide how the product configuration will be administered remotely.
2. Decide where retained data will be stored.
3. Deploy LogAnalyzer separately if browser-based review of stored data is
   needed.

Action path
-----------

1. Use the Configuration Client for administrative changes.
2. If the target system is remote, use the product's remote-connect or
   deployment workflow.
3. Configure file or database storage for the data you want to review later.
4. Deploy Adiscon LogAnalyzer separately on a web server if browser-based
   review is required.
5. Point LogAnalyzer at the same stored data source and verify end-to-end that
   new rows appear there.

Related information
-------------------

- :doc:`../tutorials/loganalyzer-setup-and-use`
- Use the product-specific remote-connect page when the Configuration Client
  can connect to another machine directly.
- Use the product-specific rollout or configuration-copy guidance when you need
  repeatable deployment across multiple systems.
