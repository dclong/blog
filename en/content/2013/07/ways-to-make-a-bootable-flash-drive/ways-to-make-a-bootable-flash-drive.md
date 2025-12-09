Status: published
Title: Ways to Make a Bootable Flash Drive in Linux
Date: 2013-07-19 10:33:38
Slug: ways-to-make-a-bootable-flash-drive
Author: Ben Chuanlong Du
Category: OS
Tags: bootable, flash drive, hybird, USB, Hardware, Linux
Modified: 2025-12-09 03:45:56

## Fedora Media Writer

[Fedora Media Writer](https://fedoraproject.org/workstation/download)
is recommended for making bootable flash drives for Fedora Linux images.

## Use [Ventoy](https://github.com/ventoy/Ventoy)

[Ventoy](https://github.com/ventoy/Ventoy)
is the best graphical tool for making bootable flash drives currently.
However,
Ventoy doesn't always work.
For example,
Ventoy is not compatible with [Universal Blue](https://universal-blue.org/) Linux images.

## Use the Command `dd` or `cat`

You can use 

    dd if=path_to_linux_image of=path_to_device bs=4M; sync

or

    cat path_to_linux_image > path_to_device

to write a hybird Linux image into a flash drive.
Note that you 
<span style="color:red">
must use the whole device 
</span>
(e.g., `/dev/sdb`) 
not just a partition (e.g., `/dev/sdb1`)
on the device.
For a non-hybrid Linux image, 
you can make it hybid using the following command 
if it uses isolinux/syslinux technology.

    isohybird path_to_linux_image

<span style="color:red">
Be very careful when you run the above 2 commands
(`dd` and `cat`)
</span>
,
as they will erase the whole target device you specify.
Accidentally providing a wrong device will make you lose all data on it!

## Use the Command zcat

This is an even more manual way,
which is not recommended.

1. `zcat boot.img.gz > /dev/sdX
2. Mount the USB stick and copy a iso image to it.
3. Umount the USB stick.

## Use the GUI Tool [UNetbootin](http://unetbootin.sourceforge.net/)

1. [Ventoy](https://github.com/ventoy/Ventoy)
    is a much better tool than
    [UNetbootin](http://unetbootin.sourceforge.net/)
    now.
    Please use 
    [Ventoy](https://github.com/ventoy/Ventoy)
    instead.

2. If you create a boot flash drive for Ubuntu in Windows using UNetbootin or other softwares, 
    then you'd better format the flash drive as `FAT` instead of `FAT32`. 
    Otherwise, 
    you might get the error information: "BOOTMGR is missing".

## Use the Universal Online Booting Tool [netboot.me](http://www.netboot.me/)

Note that you must have an ethernet connection in order to use 
[netboot.me](http://www.netboot.me/).
netboot.me is a fantastic tool for general purposes,
but it has problems on some old computers.

## More Such Tools

- [rufus](https://github.com/pbatard/rufus)

- [etcher](https://github.com/balena-io/etcher)

