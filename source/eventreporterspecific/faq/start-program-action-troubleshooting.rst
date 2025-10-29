.. _start-program-action-troubleshooting-eventreporter:

Why doesn't my Start Program action work in EventReporter?
==========================================================

This article explains common issues with the Start Program action in EventReporter and provides solutions to resolve them.

Background
----------

The Start Program action allows EventReporter to execute external programs, batch files, or scripts when specific Windows event log conditions are met. However, there are several common issues that can prevent this action from working correctly.

Common Issues and Solutions
---------------------------

**Issue 1: Program not found or path problems**

**Symptoms:**
- The Start Program action appears to run but nothing happens
- No error messages in the Windows Event Log
- The external program works when run manually from command line

**Root Cause:**
EventReporter may not be able to locate the executable file due to path issues or missing dependencies.

**Solutions:**

1. **Use absolute paths for all executables**
   - Instead of: ``curl google.com > temp.txt``
   - Use: ``C:\curl\curl-win\bin\curl.exe google.com > C:\temp\temp.txt``

2. **Verify executable location**
   - Check if the program exists in the specified path
   - Ensure all required DLL files are present
   - Test the command manually from Windows Command Prompt

3. **Check Windows PATH environment variable**
   - EventReporter may not have access to the same PATH as your user session
   - Use full paths instead of relying on PATH resolution

**Issue 2: Permission problems**

**Symptoms:**
- No error messages in Event Log
- Program works when run manually but not through EventReporter

**Root Cause:**
EventReporter runs as a Windows service with different permissions than your user account.

**Solutions:**

1. **Store files in accessible locations**
   - Avoid system folders like ``C:\Windows\System32``
   - Use generic folders like ``C:\temp`` or ``C:\scripts``
   - Ensure EventReporter service has read/execute permissions

2. **Check file permissions**
   - Right-click on the executable file
   - Go to Properties > Security
   - Ensure "SYSTEM" and "SERVICE" accounts have execute permissions

**Issue 3: Working directory problems**

**Symptoms:**
- Program runs but cannot find input/output files
- Relative paths in scripts don't work

**Root Cause:**
The working directory when EventReporter executes the program may be different from expected.

**Solutions:**

1. **Use absolute paths for all file references**
   - Instead of: ``> temp.txt``
   - Use: ``> C:\temp\temp.txt``

2. **Set working directory in batch files**
   - Add ``cd /d C:\your\working\directory`` at the beginning of batch files

**Issue 4: Event-specific parameter passing**

**Symptoms:**
- Program runs but doesn't receive expected parameters
- Event data is not passed correctly to the external program

**Root Cause:**
EventReporter uses specific replacement characters to pass event data to external programs.

**Solutions:**

1. **Use correct replacement characters**
   - ``%d`` - Date and time in local time
   - ``%s`` - Source system IP address or name
   - ``%f`` - Numeric facility code
   - ``%p`` - Numeric priority code
   - ``%m`` - The event message itself
   - ``%%`` - Represents a single % sign

2. **Quote parameters properly**
   - Use quotes around parameters that contain spaces
   - Example: ``"Event occurred: %m"`` instead of ``Event occurred: %m``

Troubleshooting Steps
---------------------

1. **Check Windows Event Log**
   - Open Event Viewer (type "Event Viewer" in Windows search)
   - Navigate to Windows Logs > Application
   - Look for EventReporter-related error events

2. **Test with simple commands first**
   - Start with a basic batch file that creates a text file
   - Example: ``echo Test > C:\temp\test.txt``

3. **Verify the command works manually**
   - Open Command Prompt as Administrator
   - Run the exact same command that EventReporter should execute
   - Ensure it works from the command line first

4. **Check EventReporter service account**
   - Verify which account EventReporter is running under
   - Ensure that account has necessary permissions

5. **Test event triggering**
   - Create a test event that should trigger your Start Program action
   - Verify the event is being detected by EventReporter
   - Check if the action is configured correctly

Example Working Configuration
-----------------------------

Here's an example of a properly configured Start Program action for EventReporter:

**Command to execute:**
``C:\scripts\process-event.bat``

**Parameters:**
``"%d" "%s" "%m"``

**Batch file content (C:\scripts\process-event.bat):**
````batch
@echo off
echo Event occurred at %1 from %2 >> C:\temp\event-log.txt
echo Message: %3 >> C:\temp\event-log.txt
````

**Key points:**
- Full path to batch file
- Quoted parameters to handle spaces in event messages
- Absolute paths for output files
- Proper use of replacement characters

Additional Tips
---------------

- **Timeout settings:** Keep external programs under 5 seconds runtime for best performance
- **Error handling:** Consider adding error checking to your batch files
- **Logging:** Add logging to your scripts to help troubleshoot issues
- **Testing:** Always test Start Program actions with actual Windows events
- **Event filtering:** Ensure your event filters are correctly configured to trigger the action

If you continue to experience issues after following these steps, please contact Adiscon support with:
- EventReporter version
- Windows version
- Exact command being executed
- Any error messages from Event Log
- Results of manual command testing
- Sample event that should trigger the action