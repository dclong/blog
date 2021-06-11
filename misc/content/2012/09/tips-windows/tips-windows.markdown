Status: published
Date: 2012-09-30 19:30:05
Author: Ben Chuanlong Du
Title: Windows Operating System
Slug: tips-windows
Category: OS
Tags: tips, anti-virus, Windows, Dropbox, OS
Modified: 2020-05-30 19:30:05

<img src="http://dclong.github.io/media/windows/windows.png" height="200" width="240" align="right"/>

[winget](https://github.com/microsoft/winget-cli)
is the official Windows Package Manager CLI.

[Chocolatey](https://chocolatey.org/) 
is a cool community-driven software management tool for Windows.

## Tricky Problem

1. When Dropbox is synchronizing a file, 
    it might be unaccessible temporarily. 
    If this happens, 
    you can simplify retry 
    or you can quit Dropbox and try again.

## Tips

To add an entry into the right-click menu in Windows, 
edit the registry following the steps below.

1. Navigate to the key `HKEY_CLASSES_ROOT\Directory\Background\shell` in the registry.

2. Create another key with any name (e.g., rstudio) under `HKEY_CLASSES_ROOT\Directory\Background\shell`. 

3. Set a value (e.g., Rstudio) for the newly created key (rstudio)
    in the right-side pane of the registry.
    This value (Rstudio) shows up in the right-click menu whenever you right click.

4. Create another key named `command` under the newly created key (rstudio).

5. Set the value of the newly created key `command` 
    to be the full path of the application
    (e.g., `C:\Program Files\RStudio\bin\rstudio.exe`)
    that you want to launch.


2. Though you can also use `/` as the delimiter for paths in Windows system sometimes, 
    you can only use `\` as the delimiter for paths when you use DOS command, 
    because `/` has been already used for other meanings in DOS command.

3. `?` stand for a single character in DOS command, 
    and `??` stand for one or two characters.

4. By default Windows 7 updates automatically unless you turn the auto update off. 
    This can be annoying if you do some long time computing in Windows, 
    because the auto-updating might force the computer to reboot 
    when the computing is still running. 
    A way to solve this problem is to turn off the auto-updating 
    before you do computing in Windows. 
    However it is a convenient way, 
    because you have to turn on the auto-updating after the computing is done. 
    A better way is to lock your computer, 
    in this way the auto-updating will be halt and won't screw up your running program. 
    What's more, this can also prevent your privacy from other people. 
    (Actually I have to check whether it is because of lock or it is just because of the computer is too busy.)


## VBScript

1. An VBScript is accesible anywhere if it is placed into a searchable path 
    (a path included in the path environment). 