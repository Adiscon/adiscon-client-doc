File Monitor
============

**genericfilename**

The configured generic name of the file being reported.

**generatedbasefilename**

Contains the generated file name without the full path.

Special IIS LogFile Properties
------------------------------

The Logfile Fields in IIS Logfiles are customizable, so there is no hardcoded
command for their use.

The property-name depends on its name in the logfile. For example we take this
Logfile:

.. code-block:: text

  #Software: Microsoft Internet Information Services 5.0
  #Version: 1.0
  #Date: 2005-10-27 14:15:25
  #Fields: date time c-ip cs-username s-ip s-port cs-method cs-uri-stem
  cs-uri-query sc-status cs(User-Agent)
  2005-10-27 14:15:16 127.0.0.1 - 192.168.0.1 443 POST /eCommerce/asdf.php
  2005-10-27 14:15:16 127.0.0.1 - 192.168.0.1 443 POST /eCommerce/asdf.php
  2005-10-27 14:15:16 127.0.0.2 - 192.168.0.1 443 POST /eCommerce/asdf.php
  2005-10-27 14:15:16 127.0.0.2 - 192.168.0.1 443 POST /eCommerce/asdf.php

As you can see, in our sample the fields are named: date, time, c-ip,
cs-username, s-ip, and so on.

To use them as a Property inside our MonitorWareProducts, just use the names
from your Logfile and add a "p-" before it:


**p-date**

The Date on which the Event occurs

**p-time**

The Time on which the Event occurs

**p-c-ip**

The IP address of the User which accessed

**p-cs-username**

The Username of the User which accessed

**p-s-ip**

The Server IP

**p-s-port**

The Server Port

**p-cs-method**

The Client-Server Method (POST,GET)

**p-cs-uri-stem**

The accessed File including its path
