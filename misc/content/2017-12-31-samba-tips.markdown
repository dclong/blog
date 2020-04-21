Status: published
Date: 2020-02-29 17:14:25
Author: Ben Chuanlong Du
Slug: samba-tips
Title: Tips on Samba
Category: OS
Tags: Linux, SAMBA, remote file system, file sharing

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

SAMBA File System is a great way to share files among computers in local network (e.g., office or home).
You do NOT need a synchronization software.
However,
if you use SAMBA in office,
make sure that the file permissions are as you expected.
Some companies make SAMBA file system accessible to everyone!

## Docker Images

dclong/samba

## Mount Windows Samba Share on Ubuntu
```
sudo mount //WINSRV/SHARE -t cifs -o uid=1000,gid=1000,username=winuser /mnt/path
```

## Mount Samba in WSL

It is now possible to mount USB media (including formatted as FAT)
and network shares with `drvfs` on Windows 10.

You can use the following command to mount removable media (e.g. D:).
```
sudo mkdir /mnt/d
sudo mount -t drvfs D: /mnt/d
```
And use the following command to safely unmount it.
```
sudo umount /mnt/d
```
You can also mount network shares without `smbfs`.
```
sudo mount -t drvfs '\\server\share' /mnt/share
```

https://blogs.msdn.microsoft.com/wsl/2017/04/18/file-system-improvements-to-the-windows-subsystem-for-linux/

## Issues

I couldn't mount ubuntu SAMBA share on windows ...

## Misc

https://ubuntuforums.org/showthread.php?t=1865953

https://stackoverflow.com/questions/3323966/echo-smbpasswd-by-stdin-doesnt-work



https://help.ubuntu.com/community/How%20to%20Create%20a%20Network%20Share%20Via%20Samba%20Via%20CLI%20%28Command-line%20interface/Linux%20Terminal%29%20-%20Uncomplicated%2C%20Simple%20and%20Brief%20Way%21



https://superuser.com/questions/1109993/accessing-removable-media-in-bash-on-windows/1209701#1209701
