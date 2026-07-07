:orphan:

How to enter the license information
====================================

Article created 2021-10-05 by adiscon team

This article describes how to enter the license information you received when
buying one of our products.

The Article is applicable to EventReporter, MonitorWare Agent, WinSyslog and
rsyslog WindowsAgent.


The license screen can be found on the left side of the client under the item
General. Applying the license is very straightforward with only a few steps.
For product versions 2026 and later, Adiscon provides a signed
``license.alic`` file. Older product versions use a legacy registration name
and license key.

Under General - on the left side of the Configuration Client - you will find
the menu entry: License.

.. image:: ../images/license-mw.png
   :width: 320px


If you click on it, you will find the license screen on the right. On product
versions 2026 and later, use the **License File** tab to deploy
``license.alic``.

Browse for the file, drag-and-drop it onto the client, or paste the file path.
Use **Verify License** to check the selected file.

For pre-2026 product versions, open the **Legacy License** tab.

Copy and paste the license name without quotation marks into the field
"Registration Name" because it is case sensitive and must be entered exactly as
given. Leading and trailing spaces are also part of the registration name. Be
careful not to enter any.

Copy the full license key and use the button "Import from Clipboard" to paste
it into the key fields. The client detects invalid registration numbers and
reports the corresponding error.

Save the configuration and restart the service.

This is all that will be required to apply the license.
