Status: published
Date: 2018-09-15 15:07:31
Author: Ben Chuanlong Du
Slug: windows-emulation-on-linux
Title: Windows Emulation on Linux
Category: Software
Tags: software, VirtualBox, Wine, CrossOver, Windows Emulation
Modified: 2025-12-25 18:23:08

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Virtual machine is the recommend way to emulate Windows working environment on Linux.

## Windows Virtual Machine 

1. A Windows virtual machine (e.g., using Virtual Machine Manager)
    provides a full working Windows environment.
    The only downside is that
    a Windows virtual machine requires lots of resource to run. 
    You need a very powerful Linux/macOS host machine.
    
2. WinTPC is a relatively lightweight 32-bit Windows operating system.
    What's more important,
    Microsoft provides free registration for WinTPC.
    [Get a Windows 10 development environment](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)
    offers free Windows 10 virtual machines for developers.

## ReactOS Virtual Machine

[ReactOS](https://reactos.org/)
([@GitHub](https://github.com/reactos/reactos))
is a free Windows-compatible Operating System
.

## WinApps 

[WinApps](https://github.com/winapps-org/winapps)
allows you to run Windows applications 
(including Microsoft 365 and Adobe Creative Cloud) 
on GNU/Linux with KDE Plasma, GNOME or XFCE, 
integrated seamlessly as if they were native to the OS.

## WINE, CrossOver

WINE and CrossOver requires way less resource than a Windows virtual machine.
However, 
the Windows app you want to run might not be supported by WINE or CrossOver. 
And even if it works, 
it might be buggy. 
For more discussions on WINE and CrossOver,
please refer to
[Windows Emulation Using WINE](http://www.legendu.net/misc/blog/wine-tips)
.

## References 

- [x86 Virtualization in Browser](https://copy.sh/v86/)

- [Windows Emulation Using WINE](http://www.legendu.net/misc/blog/wine-tips)
