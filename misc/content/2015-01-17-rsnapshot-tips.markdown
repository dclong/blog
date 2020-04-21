UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2016-07-13 22:49:24
Author: Ben Chuanlong Du
Slug: rsnapshot-tips
Title: Tips About "rsnapshot" 
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

