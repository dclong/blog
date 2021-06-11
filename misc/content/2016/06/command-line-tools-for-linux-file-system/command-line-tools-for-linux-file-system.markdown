UUID: 7caebdd0-8af6-4a5a-a338-eeb121c1f023
Status: published
Date: 2016-06-24 18:50:50
Author: Ben Chuanlong Du
Slug: command-line-tools-for-linux-file-system
Title: Command Line Tools for Linux File System
Category: OS
Tags: Linux, file system, filesystem, shell, terminal, command line
Modified: 2020-03-24 18:50:50

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


Please refer to
[Command Line Tools for Mac File System](http://www.legendu.net/misc/blog/command-line-tools-for-mac-file-system/)
for the macOS version.


1. List disk information.

        df
        df /HOME

3. Format disk partitions.

        mkfs.ext4 /dev/sd3 /path_to_mount_in

        mkfs.ntfs /dev/sd3 /path_to_mount_in

        mkfs.exfat /dev/sd3 /path_to_mount_in

2. Management disk partition tables.

        fdisk

4. Report disk usage.

        du -lhd 1 .

5. dd

        dd

6. badblocks
