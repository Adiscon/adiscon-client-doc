Send to Communications Port
===========================

This action allows you to send a string to an attached communications device,
that is, it sends a message through a Serial Port.


.. image:: ../images/a-sendtocommunicationsport.png
   :width: 100%

* Action - Send to Communication Port*


Timeout Limit
^^^^^^^^^^^^^

**File Configuration field:**
  nTimeOutLimit

**Description:**
  The maximum time allowed for the device to accept the message. If the message
  could not be sent within that period, the action is aborted. Depending on the
  device, it may be left in an unstable state.



Send message to this communication port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**File Configuration field:**
  szPortName

**Description:**
  Specify the port to which your device is being attached. Typically, this
  should be one of the COMx: ports. The list box shows all ports that can be
  found on your local machine. You may need to adjust this to a different
  value, if you are configuring a remote machine.

  1.   MSFAX
  2.   COM1
  3.   COM2
  4.   COM3
  5.   COM4
  6.   FILE
  7.   LPT1
  8.   LPT2
  9.   LPT3
  10.  AVMISDN1
  11.  AVMISDN2
  12.  AVMISDN3
  13.  AVMISDN4
  14.  AVMISDN5
  15.  AVMISDN6
  16.  AVMISDN7
  17.  AVMISDN8
  18.  AVMISDN9



Port Settings
^^^^^^^^^^^^^

**File Configuration field:**
  szPortSettings

**Description:**
  Use those settings that your device expects. Please consult your device
  manual if in doubt.



Bits per Seconds
^^^^^^^^^^^^^^^^

**File Configuration field:**
  nBps

**Description:**
  Bits per second can be 110 and go up to 256000, by default 57600 is selected.



Databits
^^^^^^^^

**File Configuration field:**
  nDatabits

**Description:**
  Databits defines that how many bits you want to send and receive to the
  communication port.



Parity
^^^^^^

**File Configuration field:**
  nParity

**Description:**
  With Parity you can configure the Parity scheme to be used. This can be one
  of the following values:

  1.   Even
  2.   Mark
  3.   No parity
  4.   Odd
  5.   Space



Stop bits
^^^^^^^^^

**File Configuration field:**
  nStopbits

**Description:**
  You can configure the number of stop bits to be used. This can be one of the
  following values:

  1.   1 stop bit
  2.   1.5 stop bits
  3.   2 stop bits



DTR Control Flow
^^^^^^^^^^^^^^^^

**File Configuration field:**
  nDtsControl

**Description:**
  DTR (data-terminal-ready) flow control. This member can be one of the
  following values:

  1. DTR_CONTROL_DISABLE - Disables the DTR line when the device is opened and
     leaves it disabled.
  2. DTR_CONTROL_ENABLE - Enables the DTR line when the device is opened and
     leaves it on.
  3. DTR_CONTROL_HANDSHAKE - Enables DTR handshaking.



RTS Control Flow
^^^^^^^^^^^^^^^^

**File Configuration field:**
  nRtsControl

**Description:**
  RTS (request-to-send) flow control. This member can be one of the following
  values:

  1. RTS_CONTROL_DISABLE - Disables the RTS line when the device is opened and
     leaves it disabled.
  2. RTS_CONTROL_ENABLE - Enables the RTS line when the device is opened and
     leaves it on.
  3. RTS_CONTROL_HANDSHAKE - Enables RTS handshaking. The driver raises the RTS
     line when the "type-ahead" (input) buffer is less than one-half full and
     lowers the RTS line when the buffer is more than three-quarters full.
  4. RTS_CONTROL_TOGGLE - Specifies that the RTS line will be high if bytes are
     available for transmission. After all buffered bytes have been sent, the
     RTS line will be low.



Message to Send
^^^^^^^^^^^^^^^

**File Configuration field:**
  szMessage

**Description:**
  This is the message that is to be sent to the device. You can enter text
  plainly and you can also include all properties from the current event.
  For example, if you have a serial audit printer and you would just plainly
  like to log arrived messages to that printer, you could use the string
  "%msg%%$CRLF%" to write the actual message arrived plus a CRLF (line feed)
  sequence to the printer.

  Please note that the message content of the Message field can now be
  configured.
  :doc:`event properties <../shared/references/eventspecificproperties>` are described in the
  :doc:`property replacer section <../shared/references/eventproperties>`.
