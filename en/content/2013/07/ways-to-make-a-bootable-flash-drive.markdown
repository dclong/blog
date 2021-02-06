UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Ways to Make a Bootable Flash Drive in Linux
Date: 2017-03-19 10:33:38
Slug: ways-to-make-a-bootable-flash-drive
Author: Ben Chuanlong Du
Category: OS
Tags: bootable, flash drive, hybird, USB, Hardware, Linux

1. Use command

        dd if=path_to_linux_image of=path_to_device bs=4M; sync

    or

        cat path_to_linux_image > path_to_device

    to write a hybird Linux image into a flash drive.
    Note that you must use the whole device (e.g., `/dev/sdb`) 
    not just a partition (e.g., `/dev/sdb1`)
    on the device.
    For a non-hybrid Linux image, 
    you can make it hybid using the following command 
    if it uses isolinux/syslinux technology.

        isohybird path_to_linux_image

2. Manually copying files to the USB stick.
    1. `zcat boot.img.gz > /dev/sdX
    2. Mount the USB stick and copy a iso image to it.
    3. Umount the USB stick.

3. Use the GUI tool [UNetbootin](http://unetbootin.sourceforge.net/).

4. Use the universal online booting tool [netboot.me](http://www.netboot.me/).
Note that you must have ethernet connection in order to use netboot.me. 
netboot.me is a fantastic tool for general purposes, 
but it has problems on some old computers.
