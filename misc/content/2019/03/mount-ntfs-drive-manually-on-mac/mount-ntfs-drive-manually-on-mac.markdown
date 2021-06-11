Status: published
Date: 2019-03-10 10:25:07
Author: Benjamin Du
Slug: mount-external-hard-drive-manually-on-mac
Title: Mount NTFS Drive Manually on Mac
Category: OS
Tags: OS, macOS, mount, NTFS, external drive, ExFAT
Modified: 2021-01-10 10:25:07

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

First use `diskutil list` to list all avaiable disks and identifiy the external hard drive to mount.
For example,
running `diskutil list` on my Mac gives me the following output
and `/dev/disk2s1` is the partition (NTFS) to mount.

```
$ diskutil list
/dev/disk0 (internal):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                         500.3 GB   disk0
   1:                        EFI EFI                     314.6 MB   disk0s1
   2:                 Apple_APFS Container disk1         500.0 GB   disk0s2

/dev/disk1 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +500.0 GB   disk1
                                 Physical Store disk0s2
   1:                APFS Volume Macintosh HD            102.7 GB   disk1s1
   2:                APFS Volume Preboot                 45.2 MB    disk1s2
   3:                APFS Volume Recovery                517.0 MB   disk1s3
   4:                APFS Volume VM                      3.2 GB     disk1s4

/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *1.0 TB     disk2
   1:                      Linux                         1.0 TB     disk2s1
```

## NTFS 

```Bash
sudo mount_ntfs /dev/disk2s1 /path_to_mount_in
```

## ExFAT

```Bash
sudo mount_exfat /dev/disk2s1 /path_to_mount_in
```

## Unmount 

diskutil unmount