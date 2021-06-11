UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2012-09-20 10:30:22
Slug: rescue-linux-from-gui-freezing
Author: Ben Chuanlong Du
Title: Rescue Linux from GUI Freezing
Category: OS
Tags: GUI, DE, Dropbox, X, Linux, SSH, desktop environment
Modified: 2015-02-20 10:30:22

<img src="http://dclong.github.io/media/computer/computer.gif" height="200" width="240" align="right"/>

The kernel of Linux is usually very stable, 
but the existing free desktop environments are craps. 
Amongs these desktop environments I tried 
(Gnome, Xfce, LXDE and so on), none is even close to the desktop environments in Windows and Mac.
I do not require desktop environments in Linux to be as fancy as desktop environments in Windows and Mac,
but they have to be usable and stable. 
These two basic requirements, unfortunately, seems unreachable from these desktop environment developers.
Tought their desktop environments are full of all kinds of flaws, 
they never fell shame to brag about their products. 
My experience with Linux desktops is that they crash very often. 
The most annoying case is that the X windows freezes and does not react to the keyboard and touchpad. 
It is not recommended to shutdown the machine by pressing the power button. 
To solve this problem, you can ssh into the machine from another one and kill the Xorg process. 
There arises several problems:

1. How do you ssh into your machine in any network? 

2. What if you do not have another machine on hand?

The first problem often comes to how do you find the IP of the freezing machine?
If the machine is connected to your home network, 
you can just scan the network for connected machines. 
If the machine is connected to your work network, 
you often have a host name for your machine on the network. 
Scanning the network for ips is not a good idea in this case, 
because there are often many machines connected to your work network.
If the machine is connected to some network (e.g., public network),
it can be even harder to find the ip of your freezing machine.
My way to solve this problem is let the machine write its ip address 
into a file in Dropbox. 
So I can always know the ip of my machine no matter which network it is connected to. 
The second problem is not a problem if you have a (smart) phone with you. 
With a smartphone, you can install an application (e.g., connectBot) to login into 
Linux machine. 
If you only have a phone which cannot connect to internet, 
you can call someone who know Linux and you can trust and let him/her
login into your machine and kill the X window. 
If you hesitate to do that, well, just press the power button on your machine, 
hold it unitl your machine shut down. 
