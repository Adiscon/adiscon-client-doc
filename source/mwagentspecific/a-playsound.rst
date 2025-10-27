Play Sound
==========

This action allows you to play a sound file. Since Windows VISTA/2008/7,
Microsoft has disabled any interaction between a system service and the user
desktop. This includes playing sounds as well. So if you want to use the Play
Sound Action on any of this Windows Version, you will need to run the service
in console mode (From command prompt with the -r option).

.. image:: ../images/a-playsound.png
   :width: 100%

* Action - Play Sound*

**Please note: if your machine has multiple sound cards installed, the "Play Sound" action will always use the card, that was installed first into the system.**

There is a work around if you want to use :doc:`play sound action <../articles/playsound-action>`
for a second sound card!


Filename of the Soundfile
^^^^^^^^^^^^^^^^^^^^^^^^^

**File Configuration field:**
  szFilename

**Description:**
  Please enter the name of the sound file to play. **This must be a .WAV** file, other formats (like MP3) are not supported. While in theory it is possible
  that the sound file resides on a different machine, we highly recommend using
  files on the local machine only. Using remote files is officially not
  supported (but currently doable if you are prepared for some extra effort in
  getting this going).

  If the file can either not be found or is not in a valid format, a system
  beep is emitted instead (this should - by API definition - be possible on any
  system).



Playcount
^^^^^^^^^

**File Configuration field:**
  nCount

**Description:**
  This specifies how many times the file is played. It can be re-played up to
  a hundred times.



Delay between Plays
^^^^^^^^^^^^^^^^^^^

**File Configuration field:**
  nDelay

**Description:**
  If multiple repeats are specified, this is the amount of time that is to be
  waited for between each individual play.
