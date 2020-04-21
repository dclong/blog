UUID: a09984bf-507d-4e0d-a039-4aa95a96fc22
Status: published
Date: 2015-09-12 01:39:06
Author: Ben Chuanlong Du
Slug: undelete-files-in-linux
Title: Undelete Files in Linux
Category: OS
Tags: Linux, undelete, recover, files, filesystem, restore, trash

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

```bash
sudo mount -o remount,ro /dev/sdb1
sudo extundelete --restore-all /dev/sdb1 
```
