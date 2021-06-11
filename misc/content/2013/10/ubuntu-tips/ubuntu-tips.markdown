Status: published
Author: Ben Chuanlong Du
Title: Misc Tips on Ubuntu
Date: 2013-10-19 12:20:43
Slug: ubuntu-tips
Category: OS
Tags: tips, Ubuntu, Linux, OS
Modified: 2017-02-19 12:20:43

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 
[How to solve boot problems with Ubuntu after kernel upgrade](http://www.dedoimedo.com/computers/ubuntu-initrd-bug.html)

[Ubuntu Sources List Generator](https://repogen.simplylinux.ch/)

1. use CTRL + D in a folder to add it as a bookmark

1. If a user never logged in before, the removal disk won't be mounted.
    But you can always mount the disk manually.

2. If a user never logged in before, the vino-server is not usable. 
    There is a solution if gdm is used, 
    but I don't know how to resolve this problem when lightdm is used. 
    One good way is to let ubuntu login automatically and then lock screen automatically.
    You can also think about whether the way you used in Debian is applicable to Ubuntu.

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

## Installation

1. Ubuntu image is Hybrid, 
    which means that you can dd/cat it into a flash drive directly to make a bootable flash drive.

2. Ubuntu have good hardware support. 
    You can probably also use a wireless network while installing Ubuntu.

## VPN

1. openvpn

## Check Whether a Ubuntu Server Has a Desktop Installed

Look at 
Check the directory `/usr/share/xsessions/` to see 
if there are any X sessions available on the Ubuntu server.

    :::bash
    ls /usr/share/xsessions/
