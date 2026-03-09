.. _rsyslogwa-mass-rollout-deployment:

How Do I Prepare rsyslog Windows Agent for Mass Rollout?
========================================================

Answer
------

Use a reference system to build and test the configuration, export that
configuration, and then deploy the service and settings consistently to the
target systems.

Details
-------

Mass rollout is a deployment task, not a first-time setup task. The goal is to
prepare one known-good configuration and reuse it safely across many Windows
systems.

A typical rollout uses:

- one reference installation for testing
- exported configuration data for reuse
- installer options or deployment tooling that match your environment
- a validation step on a small pilot group before broader rollout

Action path
-----------

1. Install and configure rsyslog Windows Agent on a reference system.
2. Verify that event collection and forwarding work as expected.
3. Export the configuration from the reference system.
4. Decide whether the rollout needs the full product or only the service on the
   target systems.
5. Deploy the software and import the validated configuration on a pilot group.
6. Confirm that pilot systems forward the expected events.
7. Roll out to the remaining systems.

Related information
-------------------

* :doc:`copying-configuration`
* :doc:`../installation`
