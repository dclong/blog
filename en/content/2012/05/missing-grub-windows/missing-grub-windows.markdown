UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Missing Grub Menu of Windows Operating System
Date: 2015-02-03 19:10:47
Slug: missing-grub-windows
Author: Ben Chuanlong Du
Category: OS
Tags: Windows, Linux, OS, Debian

I came across this problem after I installed both Debian and Windows 7 system on my laptop.
After searching online, I found a solution to this problem. 
1. Open /etc/default/grub as root user and make sure the following line is somewhere in the file and uncommented:

        GRUB_DISABLE_OS_PROBER=false

2. Run command `update-grub2` and then reboot your computer.

This solution is not just for Windows and Linux dual boot. 
It is also for dual/multiple Linux operating systems boot. 
