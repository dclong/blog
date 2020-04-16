Status: published
Date: 2019-03-25 00:53:40
Author: Benjamin Du
Slug: best-filesystem-format-for-cross-platform-data-exchanging
Title: Best Filesystem Format for Cross-Platform Data Exchanging
Category: OS
Tags: OS, macOS, external drive, filesystem

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**
## FAT32

FAT32 is an outdated filesystem. 
The maximum size for a single file is 4G.
You should instead exFAT instead of FAT32 where possible.

## [exFAT](https://en.wikipedia.org/wiki/ExFAT)

exFAT is great cross-platform filesystem that is support out-of-box by Windows, Linux and macOS.
There is practically no limit (big enough for average users) on single file size.

## NTFS

NTFS is the current MS Windows Filesystem. 
It is superior to exFAT and is supported by Linux out-of-box, 
however, there is limited support on macOS. 
Reading a NTFS filesystem is supported in macOS 
but writing to a NTFS drive is experimental currently
and it is strongly suggest that you don't try it at this time.

NTFS is a POSIX-compatible filesystem, 
and it is POSSIBLE to use permissions (even though complicated) on NTFS (but not on FAT systems).
To enable permissions on NTFS, 
you need a "User Mapping File" or just give the permissions option when mounting (when no compatibility with Windows is needed). 
This maps linux users on your system with the user IDs like NTFS/Windows use them internally.
Please refer to the [ntfs-3g manual](http://manpages.ubuntu.com/manpages/bionic/en/man8/ntfs-3g.8.html) for more information.

## ext4

`ext4` is the current default filesystem for Linux operating systems.
It worth mentioning that the Windows Subsystem Linux (WSL) sees what the Windows system sees,
so it supports mounting Windows fileystems (FAT32, exFAT and NTFS) into WSL but not the ext4 filesystem at this time.
However, 
this might be changed in future. 
And if mouting ext4 is supported in WSL, 
ext4 will be even a better way for sharing data between Windows and Linux.

Reading ext4 on Mac can be supported by installing `ext4fuse`,
however, 
reading/writing ext4 on Mac is experimental and it is strongly suggested that you don't try it at this time.

## Mount External Hard Drive Via Virtual Machine 

Given the above said,
there is a heavy and hacking way to read all kinds of filesystem 
if your machine is powerful enough to run a Virtual Machine.
You can mount an external hard drive that is not supported by the current operating system 
via a virtual machine which can read/write it.
For example, 
if you have an external ext4 hard drive and want to read/write in Mac, 
you can run a Ubuntu virtual machine in Mac to read/write it.
In order for the guest virtual machine to read/write the external hard drive, 
it must be able to access the USB devices.
Below are details steps to access an external hard drive in a VirtualBox VM.

1. Download and install VirtualBox.

2. Download and install VirtualBox Extension pack. 
    You can install it by double clicking it.

3. Plug in your external hard drive to the host machine. 
    Notice that you must be umounted on the host machine 
    in order for it to be accsible on the guest virtual machine.

4. Enable the USB device on the guest virtual machine.
    You hve to do this by adding a corresponding USB filter.

5. The hard drive will auto mount on some Linux distributions (e.g., Ubuntu). 
    If not, just manually mount it.

## References

https://dzone.com/articles/how-to-mount-usb-drives-on-virtualbox

https://www.virtualbox.org/wiki/Downloads

https://askubuntu.com/questions/11840/how-do-i-use-chmod-on-an-ntfs-or-fat32-partition
