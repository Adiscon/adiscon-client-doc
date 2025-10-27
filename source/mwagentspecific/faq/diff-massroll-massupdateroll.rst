.. _mass_rollout_vs_update_rollout:

Differences Between Mass Rollout and Mass Update Rollout
========================================================

While "Mass Rollout" and "Mass Update Rollout" are often perceived
as similar, there are crucial distinctions, especially in the context
of deploying and maintaining Adiscon products. Understanding these
differences is vital for successful large-scale deployments.

1.  Mass Rollout (Initial Deployment)
-------------------------------------

A **Mass Rollout**, also known as an initial deployment, refers to the
**first-time, widespread installation** of software on numerous target systems where the application **does not currently exist**.

* **Primary Goal:** To establish the software and its baseline
  configuration on new machines.

* **Target System State:** The software is **not installed** yet.
* **Key Steps:**
    #.  Perform an initial, full installation on a master system.
    #.  Create and thoroughly test the **baseline configuration**.
    #.  Export this baseline configuration to a :doc:`registry file <../../glossaryofterms/registry-file>`.
    #.  Package the product's executable files (e.g., ``winsyslg.exe``, ``mwagent.exe``) and associated DLLs along with the
        exported :doc:`registry file <../../glossaryofterms/registry-file>`.
    #.  Distribute and execute a script that will:

        * Copy the product files to the target machine's desired installation directory.
        * **Install** the product as a Windows service (e.g., using ``winsyslg -i`` or ``mwagent -i``).
        * Import the baseline configuration from the `.reg` file.
        * **Start** the newly installed service.

* **Focus:** Establishing a functional, standardized installation from a clean slate.

2.  Mass Update Rollout
-----------------------

A **Mass Update Rollout** involves the **widespread upgrade or patching**
of an application that is **already installed** on the target systems
to a newer version.

* **Primary Goal:** To update the software and potentially its
    configuration to a newer version, while ensuring minimal
    downtime and maintaining operational continuity.

* **Target System State:** The software is **already installed** and
    likely running.

* **Key Steps:**
    #.  Perform an **in-place upgrade** of the software on a master system to the new version.
    #.  Adjust and refine the configuration for the new version, if
        necessary, and thoroughly test it.
    #.  Export the **updated configuration** to a :doc:`registry file <../../glossaryofterms/registry-file>`.
    #.  Package the **new product files** (executables, DLLs) and the
        updated :doc:`registry file <../../glossaryofterms/registry-file>`.
    #.  Distribute and execute a script that will:

        * **Stop** the existing, running service on the target machine.
        * Copy the new files to the existing installation directory,
          **overwriting** the old executables.
        * Import the updated configuration from the `.reg` file,
          applying changes to the existing registry entries.
        * **Restart** the service.

* **Focus:** Updating existing installations with minimal disruption.

3.  Key Differences at a Glance
-------------------------------

.. rubric:: Comparison of Rollout Types

**Mass Rollout (Initial):**

* **Target State:** Software **not installed**.
* **Core Action:** First-time installation, provisioning.
* **Service Handling:** Service is **installed and started**.
* **File Copying:** Copying **new** files for initial setup.
* **Configuration:** Import of a **baseline configuration**.
* **Complexity:** Generally simpler, no running service to manage.

**Mass Update Rollout:**

* **Target State:** Software **already installed**.
* **Core Action:** Upgrade, patch, version migration.
* **Service Handling:** Existing service is **stopped, then restarted**.
* **File Copying:** Copying **new** files to **overwrite old ones**.
* **Configuration:** Import of an **updated configuration**
    (changes applied to existing).
* **Complexity:** Slightly more complex, requires service
    management and compatibility checks.
