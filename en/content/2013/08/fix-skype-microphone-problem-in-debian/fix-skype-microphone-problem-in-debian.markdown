UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Fix Microphone Problem of Skype in Debian
Date: 2013-08-21 00:00:00
Tags: audio, Software, Linux
Category: Software
Slug: fix-skype-microphone-problem-in-debian
Author: Ben Chuanlong Du
Modified: 2013-08-21 00:00:00

Install Pulseaudio if you only have ALSA. 
ALSA alone does NOT work with skype whatever people 
on the #Debian channel might think and tell you.

    sudo apt-get install pulseaudio

Install pulseaudio volume control

    sudo apt-get install pavucontrol

Run Skype.

Go to the Sound devices sections. 
Click on the Open PulseAudio Volume Control button. 
pavucontrol will open.

In every tab maximize ALL the volume sliders.
Go to the configuration tab. Mine has two sections. 
One is called RV710/730. 
Turn this off in the dropdown menu below it.
The other one is called "Internal Audio". 
Choose "Analog Stereo Duplex" in the dropdown menu.
When you go back to the "Input Devices" tab now, 
you will see that there is an setting for "Internal Audio Analog Stereo". 
Crank this to 100%.
In the "Output Devices" tab, 
choose the "Analog Output" port from the dropdown menu. 
Crank the front left as well as front right channel to the max 100%.
