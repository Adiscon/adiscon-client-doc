.. _mwagent-repeatable-update-deployment:

How Do I Perform a Repeatable Update Deployment?
================================================

Answer
------

Use repeatable update deployment when MonitorWare Agent is already deployed and
you need to distribute an updated configuration or package revision to multiple
systems.

Details
-------

Repeatable update deployment differs from initial repeatable deployment because
the target systems already exist in production and may already process data.

Action path
-----------

1. Validate the updated package or configuration on a non-production system.
2. Plan restart timing and rollback expectations.
3. Deploy the update in stages.
4. Confirm that services restart cleanly and continue to process data.

Related information
-------------------

* :doc:`repeatable-deployment`
* :doc:`repeatable-deployment-vs-repeatable-update-deployment`
