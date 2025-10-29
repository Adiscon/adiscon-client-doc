.. _start-program-action-troubleshooting-mwagent:

Why doesn't my Start Program action work in MonitorWare Agent?
==============================================================

This article explains common issues with the Start Program action in MonitorWare Agent and provides solutions to resolve them.

Background
----------

The Start Program action allows MonitorWare Agent to execute external programs, batch files, or scripts when specific monitoring conditions are met. However, there are several common issues that can prevent this action from working correctly.

Common Issues and Solutions
---------------------------

**Issue 1: Program not found or path problems**

**Symptoms:**
- The Start Program action appears to run but nothing happens
- No error messages in the Windows Event Log
- The external program works when run manually from command line

**Root Cause:**
MonitorWare Agent may not be able to locate the executable file due to path issues or missing dependencies.

**Solutions:**

1. **Use absolute paths for all executables**
   - Instead of: ``curl google.com > temp.txt``
   - Use: ``C:\curl\curl-win\bin\curl.exe google.com > C:\temp\temp.txt``

2. **Verify executable location**
   - Check if the program exists in the specified path
   - Ensure all required DLL files are present
   - Test the command manually from Windows Command Prompt

3. **Check Windows PATH environment variable**
   - MonitorWare Agent may not have access to the same PATH as your user session
   - Use full paths instead of relying on PATH resolution

**Issue 2: Permission problems**

**Symptoms:**
- No error messages in Event Log
- Program works when run manually but not through MonitorWare Agent

**Root Cause:**
MonitorWare Agent runs as a Windows service with different permissions than your user account.

**Solutions:**

1. **Store files in accessible locations**
   - Avoid system folders like ``C:\Windows\System32``
   - Use generic folders like ``C:\temp`` or ``C:\scripts``
   - Ensure MonitorWare Agent service has read/execute permissions

2. **Check file permissions**
   - Right-click on the executable file
   - Go to Properties > Security
   - Ensure "SYSTEM" and "SERVICE" accounts have execute permissions

**Issue 3: Working directory problems**

**Symptoms:**
- Program runs but cannot find input/output files
- Relative paths in scripts don't work

**Root Cause:**
The working directory when MonitorWare Agent executes the program may be different from expected.

**Solutions:**

1. **Use absolute paths for all file references**
   - Instead of: ``> temp.txt``
   - Use: ``> C:\temp\temp.txt``

2. **Set working directory in batch files**
   - Add ``cd /d C:\your\working\directory`` at the beginning of batch files

**Issue 4: Parameter processing problems**

**Symptoms:**
- Program runs but doesn't receive expected parameters
- Event data is not passed correctly to the external program

**Root Cause:**
MonitorWare Agent uses specific replacement characters to pass event data to external programs.

**Solutions:**

1. **Use correct replacement characters**
   - ``%d`` - Date and time in local time
   - ``%s`` - Source system IP address or name
   - ``%f`` - Numeric facility code
   - ``%p`` - Numeric priority code
   - ``%m`` - The message itself
   - ``%%`` - Represents a single % sign

2. **Quote parameters properly**
   - Use quotes around parameters that contain spaces
   - Example: ``"Alert: %m"`` instead of ``Alert: %m``

3. **Check legacy parameter processing setting**
   - Enable "Use legacy parameter processing" if you're using old-style parameters
   - This affects how replacement characters are processed

**Issue 5: Timeout and performance issues**

**Symptoms:**
- Program starts but gets terminated unexpectedly
- MonitorWare Agent becomes unresponsive
- Action is marked as unsuccessful

**Root Cause:**
External programs running too long can affect MonitorWare Agent performance.

**Solutions:**

1. **Set appropriate timeout values**
   - Default timeout is 10 seconds
   - Keep external programs under 5 seconds for best performance
   - Maximum recommended timeout is 30 seconds

2. **Optimize external programs**
   - Use efficient scripts and programs
   - Avoid long-running operations
   - Consider asynchronous execution for longer tasks

Troubleshooting Steps
---------------------

1. **Check Windows Event Log**
   - Open Event Viewer (type "Event Viewer" in Windows search)
   - Navigate to Windows Logs > Application
   - Look for MonitorWare Agent-related error events

2. **Test with simple commands first**
   - Start with a basic batch file that creates a text file
   - Example: ``echo Test > C:\temp\test.txt``

3. **Verify the command works manually**
   - Open Command Prompt as Administrator
   - Run the exact same command that MonitorWare Agent should execute
   - Ensure it works from the command line first

4. **Check MonitorWare Agent service account**
   - Verify which account MonitorWare Agent is running under
   - Ensure that account has necessary permissions

5. **Test rule triggering**
   - Create a test condition that should trigger your Start Program action
   - Verify the rule is being triggered correctly
   - Check if the action is configured properly

6. **Check sync timeout settings**
   - Ensure the sync timeout is appropriate for your external program
   - Consider using async execution for longer-running programs

Example Working Configuration
-----------------------------

Here's an example of a properly configured Start Program action for MonitorWare Agent:

**Command to execute:**
``C:\scripts\process-alert.bat``

**Parameters:**
``"%d" "%s" "Alert: %m"``

**Sync Timeout:**
``10`` (seconds)

**Batch file content (C:\scripts\process-alert.bat):**
````batch
@echo off
echo Alert at %1 from %2 >> C:\temp\alerts.log
echo Message: %3 >> C:\temp\alerts.log
````

**Key points:**
- Full path to batch file
- Quoted parameters to handle spaces in messages
- Absolute paths for output files
- Proper use of replacement characters
- Appropriate timeout setting

Additional Tips
---------------

- **Performance considerations:** Use Start Program actions only for rules that apply relatively seldom
- **Error handling:** Consider adding error checking to your batch files
- **Logging:** Add logging to your scripts to help troubleshoot issues
- **Testing:** Always test Start Program actions in a development environment first
- **Rule optimization:** Ensure your rules are efficient and don't trigger too frequently

If you continue to experience issues after following these steps, please contact Adiscon support with:
- MonitorWare Agent version
- Windows version
- Exact command being executed
- Any error messages from Event Log
- Results of manual command testing
- Rule configuration details