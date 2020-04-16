UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2016-07-13 22:09:04
Slug: desktop-environments-for-linux
Author: Ben Chuanlong Du
Category: OS
Title: Desktop Environments for Linux
Tags: DE, Linux, desktop environment, Xfce, GNOME, KDE, Unity, lightdm, gdm3, kdm, mdm

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 

1. desktop files in /usr/share/applications/
different DEs might have different format. 
At least I know that a desktop file created by Xfce cannot be used in GNOME,
not sure the opposite works or not.

The icon entry in the desktop file can be defined as a full path.

2. Do not remove Iceweasel in GNOME 
even if you have installed other web browsers like Firefox, Chrome, etc.
Some GNOME components depends on Iceweasel. 
Removing Iceweasel might have undesirable effect on your GNOME desktop environment.


## Desktop Environments

1. LXQt
1. Xfce
2. KDE
3. Gnome
4. Cinnamon

## Desktop Manager

1. lightdm
lightdm might have problems when multiple desktop enviroments are installed.

2. gdm3

3. kdm

### Tiling Windows Manager

1. Xmonad
2. i3
