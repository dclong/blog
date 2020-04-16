UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Title: Questions About Ubuntu
Date: 2016-07-13 23:04:35
Slug: ubuntu-questions
Category: OS
Tags: questions, Ubuntu, Linux, OS

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 


Ubuntu:

3. The openvpn is good choice for ubuntu. The vpnc does not work in my case. 

4. how to set hosts restriction for vpn?

6. How to change icon of files?

1. After upgrade to a new kernel, 
Ubuntu fails to boot both normally and in the recovery mode,
how do I remove the new kernel?


1. It seems that evince is not working properly in Ubuntu. 
The marks made in Adobe cannot be seen on evince in Ubuntu. 
However, there's no problem in debian.

1. If a user never logged in before, the removal disk is not accessible. 
I think one can probably mount the disk manually. 

2. If a user never logged in before, the vino-server is not usable. 
There is a solution if gdm is used, but I don't know how to resolve this problem when lightdm is used. 

3. It seems that account services override the lightdm configuration file. 

4. Unity in Ubuntu crashes frequently. 
This might due to Firefox not unity itself. 
You might want to check the log information. 
And if it's indeed the problem of firefox, 
it might due to plugins installed in firefox. 

5. lightdm fails to start on Y450. 
This is probably due to xfce environment installed. 
You can remove it and check whether it works OK then. 

6. For some reason I don't know, lightdm fails to restart after running "sudo service lightdm restart".
However, it starts if I login into tty and start it manually by "sudo service lightdm start".
I think this probably means that something is wrong stopping the lightdm service. 

7. How do I add a entry into the menu, e.g. MATLAB starting menu?

8. how to add a folder as bookmark in 13.04?
