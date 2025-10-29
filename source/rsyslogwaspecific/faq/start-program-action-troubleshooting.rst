.. _start-program-action-troubleshooting-rsyslog:

Why doesn't my Start Program action work in Rsyslog?
====================================================

This article explains common issues with the Start Program action in Rsyslog and provides solutions to resolve them.

Background
----------

The Start Program action allows Rsyslog to execute external programs or scripts when specific syslog message conditions are met. However, there are several common issues that can prevent this action from working correctly on Linux/Unix systems.

Common Issues and Solutions
---------------------------

**Issue 1: Program not found or path problems**

**Symptoms:**
- The Start Program action appears to run but nothing happens
- No error messages in the system log
- The external program works when run manually from command line

**Root Cause:**
Rsyslog may not be able to locate the executable file due to path issues or missing dependencies.

**Solutions:**

1. **Use absolute paths for all executables**
   - Instead of: ``curl google.com > temp.txt``
   - Use: ``/usr/bin/curl google.com > /tmp/temp.txt``

2. **Verify executable location**
   - Check if the program exists in the specified path: ``which curl``
   - Ensure the program has execute permissions: ``ls -la /usr/bin/curl``
   - Test the command manually from terminal

3. **Check PATH environment variable**
   - Rsyslog may not have access to the same PATH as your user session
   - Use full paths instead of relying on PATH resolution

**Issue 2: Permission problems**

**Symptoms:**
- No error messages in system log
- Program works when run manually but not through Rsyslog

**Root Cause:**
Rsyslog runs as a system service with different permissions than your user account.

**Solutions:**

1. **Check file permissions**
   - Ensure the executable has execute permissions: ``chmod +x /path/to/script``
   - Check if Rsyslog user can access the file: ``sudo -u rsyslog /path/to/script``

2. **Check directory permissions**
   - Ensure Rsyslog can access the directory containing the script
   - Check parent directory permissions: ``ls -la /path/to/``

3. **Use appropriate file locations**
   - Store scripts in system directories like ``/usr/local/bin/``
   - Avoid user home directories unless properly configured

**Issue 3: Working directory problems**

**Symptoms:**
- Program runs but cannot find input/output files
- Relative paths in scripts don't work

**Root Cause:**
The working directory when Rsyslog executes the program may be different from expected.

**Solutions:**

1. **Use absolute paths for all file references**
   - Instead of: ``> temp.txt``
   - Use: ``> /tmp/temp.txt``

2. **Set working directory in scripts**
   - Add ``cd /your/working/directory`` at the beginning of scripts
   - Use ``pushd`` and ``popd`` for temporary directory changes

**Issue 4: Environment variable problems**

**Symptoms:**
- Program runs but cannot access required environment variables
- Scripts fail due to missing environment settings

**Root Cause:**
Rsyslog service may not have access to the same environment variables as your user session.

**Solutions:**

1. **Set environment variables in scripts**
   - Add ``export VAR=value`` at the beginning of scripts
   - Use absolute paths instead of relying on environment variables

2. **Use system-wide environment files**
   - Configure environment variables in ``/etc/environment``
   - Use ``/etc/profile.d/`` for custom environment settings

**Issue 5: Shell and interpreter problems**

**Symptoms:**
- Scripts fail to execute
- Wrong interpreter is used for scripts

**Root Cause:**
Rsyslog may not use the same shell or interpreter as your user session.

**Solutions:**

1. **Use proper shebang lines**
   - Add ``#!/bin/bash`` for bash scripts
   - Add ``#!/usr/bin/python3`` for Python scripts
   - Ensure the interpreter path is correct

2. **Test with explicit interpreter**
   - Use ``/bin/bash /path/to/script`` instead of just ``/path/to/script``
   - Verify the interpreter exists and is executable

Troubleshooting Steps
---------------------

1. **Check system logs**
   - View Rsyslog logs: ``journalctl -u rsyslog``
   - Check system log: ``tail -f /var/log/syslog``
   - Look for error messages related to your script

2. **Test with simple commands first**
   - Start with a basic script that creates a file
   - Example: ``echo "Test" > /tmp/test.txt``

3. **Verify the command works manually**
   - Run the exact same command that Rsyslog should execute
   - Test as the rsyslog user: ``sudo -u rsyslog /path/to/script``

4. **Check Rsyslog configuration**
   - Verify the action is properly configured in ``/etc/rsyslog.conf``
   - Ensure the rule is being triggered correctly

5. **Test script execution**
   - Make script executable: ``chmod +x /path/to/script``
   - Test with different users: ``sudo -u rsyslog /path/to/script``

Example Working Configuration
-------------------------------

Here's an example of a properly configured Start Program action for Rsyslog:

**Rsyslog configuration:**

.. code-block:: text

   # Log all messages to file and execute script
   *.* /var/log/messages
   *.* ^/usr/local/bin/process-syslog.sh

**Script content (/usr/local/bin/process-syslog.sh):**

.. code-block:: bash

   #!/bin/bash
   # Process syslog message
   echo "$(date): $@" >> /var/log/processed-messages.log

**Key points:**
- Full path to script
- Proper shebang line
- Absolute paths for output files
- Script is executable and accessible by rsyslog user

Additional Tips
---------------

- **Security considerations:** Be careful with scripts that process syslog data
- **Performance:** Keep external programs lightweight to avoid impacting Rsyslog performance
- **Error handling:** Add proper error handling to your scripts
- **Logging:** Add logging to your scripts to help troubleshoot issues
- **Testing:** Always test scripts thoroughly before deploying in production

If you continue to experience issues after following these steps, please contact Adiscon support with:
- Rsyslog version
- Linux distribution and version
- Exact command being executed
- Any error messages from system logs
- Results of manual command testing
- Script permissions and ownership