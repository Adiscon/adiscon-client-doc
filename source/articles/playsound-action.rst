How can I use a second sound card with the Play Sound Action?
=============================================================

I have got a second sound card on my machine, how can I use it with the Play
Sound Action?

PlaySounds action plays a sound on the local machine. It is possible to play
wave files and some other "system" supported sound files. This does "NOT"
include mp3 files. As MonitorWare Agent is usually running "as a" System
service, there are some things which needed to be noted!

On machines with more then ONE sound card, the MonitorWare Agent Service will
take the "first active installed soundcard as output device regardless what is
configured".

If there is a need to play the sound on another sound card instead of the first
active installed one, then there are two workarounds:

1. Specify a "User Account" for the Service which has a local profile where the
   sound card you want to use configured as primary playback device.
2. Run the MonitorWare Agent Service in console mode using the "-r" switch under
   a user account which has the sound card you want to use configured as primary
   playback device.

By following the above mentioned work around, you would be able to use second
sound card (even x sound cards where x is user configurable) with the Play
Sound Action.

**The following things are user configurable in the Play Sound Action**

Filename of the Soundfile - A full path and filename to the wave file which
will be played. If the sound file specified here cannot be found or is not a
valid wave file, a simple system beep will be played.

Playcount: Default is 1 - can be configured up to 100 times.

Delay between the sound plays - Only useful if the sound is played more then
once. Between each play, MonitorWare Agent will wait for this time until it
plays the sound again.

**Note:** A prior running sound will be aborted when this action is executed.
