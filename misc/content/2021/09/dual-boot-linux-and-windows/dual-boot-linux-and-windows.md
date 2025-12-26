Status: published
Date: 2021-09-16 09:22:59
Modified: 2025-12-25 18:23:08
Author: Benjamin Du
Slug: dual-boot-linux-and-windows
Title: Dual Boot Linux and Windows
Category: Computer Science
Tags: Computer Science, programming, Linux, Windows, dual boot, grub, device

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

I personally don't see much value in dual booting Linux and Windows.
Please refer to
[Windows Emulation on Linux](https://misc.legendu.net/blog/windows-emulation-on-linux/)
if you need to run Windows apps on Linux.

## Mount the Windows File System

When you dual boot your machine with Linux (e.g., Ubuntu) and Windows,
the Windows disk/partition might not be mounted automatically. 
In that case,
you can find out which device correspond to the Windows filesystem
and mount it manually.

```
ls /dev/sd*
```

```
ls /dev/vd*
```

```
ls /dev/nvme*
```

In Ubuntu,
you can open the "Disks" app,
which list all disks plugged into the machine.

## References

[Missing Grub Menu of Windows Operating System](http://www.legendu.net/en/blog/missing-grub-windows)
