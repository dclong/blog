Status: published
Date: 2020-05-22 14:25:22
Author: Ben Chuanlong Du
Title: Backup Files Using "rsnapshot" 
Slug: rsnapshot-tips
Category: Software
Tags: software, rsnapshot, backup, synchronization, rsync

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

To truncate the relative path while backing up using Rsnapshot:

1. Uncomment the line started with `rsync_long_args`.

2. Remove the `--relative` option and add the `--no-relative` option.

