Status: published
Date: 2020-06-26 23:23:44
Author: Ben Chuanlong Du
Slug: wsl-tips
Title: Tips on WSL
Category: OS
Tags: Linux, WSL, Windows, BashOnWindows, Bash on Windows, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Installation 

https://devtidbits.com/2017/06/08/run-ubuntu-16-04-on-windows-10-creators-update/

## Access Linux Filesystems from Windows 

https://blogs.msdn.microsoft.com/commandline/2016/11/17/do-not-change-linux-files-using-windows-apps-and-tools/

With the 1903 update, users can access Linux Filesystem from Windows directly.


## General Tips

1. [cmder](http://cmder.net/) is a good alternative UI for WSL (and also PowerShell and CMD).

2. All windows disks are mounted under `/mnt`. 
    You can visit all Windows files/directories that do not require admin privilige in WSL. 
    However, 
    if you want to visit files/directories that require admin privilige, 
    you have to run WSL with admin and visit these files/directories using sudo in WSL.

3. You'd better use files names that work both in Windows and Linux, 
  otherwise, weird behavior might happen. 

4. Shift + Right Click -> "Open CMD here ..."

5. Starting with Win 10 Creator Update, Ubuntu 16.04 is available. if you installed old Ubuntu bash,
    you need to first uninstall it and then reinstall again to get Ubuntu 16.04.
    Upgrade to Ubuntu 16.04
    https://www.howtogeek.com/278152/how-to-update-the-windows-bash-shell/



## Copy and Paste

Another solution would be to enable "QuickEdit Mode" and then you can paste by right-clicking in the terminal.

To enable QuickEdit Mode, right-click on the toolbar (or simply click on the icon in the upper left corner), select Properties, and in the the Options tab, click the checkbox next to QuickEdit Mode.

With this mode enabled, you can also copy text in the terminal by clicking and dragging. Once a selection is made, you can press Enter or right-click to copy.



## Daemon/Service

You cannot run daemon/services in WSL currently. However, it might be supported in future.

## Samba Remote File System

cannot mount samba in WSL currently.
samba requires kernelspace while WSL only implements a userspace.


## References

[简明的WSL教程](https://zhuanlan.zhihu.com/p/24537874)

https://towardsdatascience.com/dual-boot-is-dead-windows-and-linux-are-now-one-27555902a128