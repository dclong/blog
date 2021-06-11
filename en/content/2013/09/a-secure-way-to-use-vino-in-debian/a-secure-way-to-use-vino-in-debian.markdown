UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: A Secure Way to Use Vino in Debian
Date: 2013-09-03 19:41:59
Slug: a-secure-way-to-use-vino-in-debian
Author: Ben Chuanlong Du
Category: OS
Tags: vino, Linux, vnc, network
Modified: 2015-02-03 19:41:59

VNC on Linux is not secure. 
Most implementations of VNC servers for Linux allows password only up to 8 characters. 
Such a VNC server is very vulnerable to brute-force attack. 
This article discuss a secure way to use VNC.
The VNC (vino) server is started only when needed,
thus reduce the chance of your server to be hacked.


First install the vino server in debian using the following command.

    wajig install vino

Whenever you want to use VNC on the server, 
follow the steps below.

1. ssh into the server with X11 forwarding enabled. 

        ssh -X username@servername

2. Edit vino server settings by typing the following command.

        vino-preference

It will prompt a window for you to edit vino settings. 
Close the window after you are done. 
This step only has to done once and can be skipped 
if you don't want to change the settings.

3. Start the vino server using the following commands.

        export DISPLAY=:0.0 && /usr/lib/vino/vino-server

4. Connect to your server using Remmina.

5. Lock the screen of you Debian/Linux server 
when you have finished using VNC on your server. 

6. Stop/kill the vino server by hot keys `CTRL + C`.


