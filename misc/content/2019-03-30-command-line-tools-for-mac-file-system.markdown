Status: published
Date: 2020-03-26 11:20:06
Author: Benjamin Du
Slug: command-line-tools-for-mac-file-system
Title: Command Line Tools for Mac File System
Category: OS
Tags: macOS, file system, filesystem, shell, terminal, command line

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


Please refer to
[Command Line Tools for Linux File System](http://www.legendu.net/misc/blog/command-line-tools-for-linux-file-system/)
for the Linux version.


1. Notice that disks in macOS are often named as `/dev/diskXsY`
    where `X` and `Y` are numbers.

2. It is suggested that you use the unified command `diskutil` 
    (instead of scattered commands such as `df`, `newfs_*`, etc.)
    to manage (list, format, partition, etc.) disks in macOS.

        :::bash
        diskutil partitionDisk /dev/diskX 2 MBR \
            ExFAT NewVolumeA 100M \
            ExFAT NewVolumeB R
        diskutil eraseVolume ExFat NewVolume /dev/diskXsY


3. List disk information.

        diskutil list

2. Management disk partition tables.

        fdisk.

3. Format disk partitions.

        newfs_ext4 /dev/sd3 /path_to_mount_in

        newfs_ntfs /dev/sd3 /path_to_mount_in

        newfs_exfat /dev/sd3 /path_to_mount_in

4. Report disk usage.

        du -lhd 1 .

5. dd

        dd

6. badblocks

## References

[How to format multiple exFAT partitions on USB drive?](https://apple.stackexchange.com/questions/218818/how-to-format-multiple-exfat-partitions-on-usb-drive)

[How to Erase a Disk from Command Line in Mac OS X](https://osxdaily.com/2016/08/30/erase-disk-command-line-mac/)

[How do you make filesystems in mac OSX](https://unix.stackexchange.com/questions/271826/how-do-you-make-filesystems-in-mac-osx)
