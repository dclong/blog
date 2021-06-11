UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Title: Comparision of Linux Emulation Solutions on Windows
Author: Ben Chuanlong Du
Date: 2016-07-13 22:21:09
Slug: comparision-of-linux-emulation-solutions-on-windows
Category: Software
Tags: Virtual Machine, Cygwin, MobaXterm, VirtualBox, Linux Emulation
Modified: 2016-07-13 22:21:09

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 
1. Virtual Machine is generally speaking a overkill. 
    It has complete functionalities 
    but also needs more CPU and memory resources.

2. Cygwin is a very good one 
   espcially the portable one with ConEmu console.

3. MobaXterm has the best integration with Windows system 
    (multi-tab, window split, case-insensitive completion, case conversion rename, etc.),
    but since it is based on BusyBox, 
    it has limited functionalities. 
    Many commands have only a subset functionalities of popular Linux commands.

4. The 2 most used programs are vim and git. 
    Vim in MobaXterm has a problem to use UltraSnip, SAS_Syntax, SQLUtil, etc.
    because it is not compiled with Python support.
    Git in MobaXterm also has limited functionalities. 
    If these 2 problems are solved, then MobaXterm is a good solutions for daily use.

5. Cygwin/MobaXterm can run Windows program directly,
    e.g., to open a file/directory in Windows.
    There is no simple way to do this in a Linux guest machine 
    to the extent of my knowledge.

6. MobaXterm has a better GUI than Cygwin.
    If MobaXterm is based on Cygwin not BusyBox then it is perfect for me.
