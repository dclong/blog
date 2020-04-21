Status: published
Date: 2017-08-26 20:18:18
Author: Ben Chuanlong Du
Slug: mount-samba-on-mac
Title: Mount Samba on Mac
Category: OS
Tags: macOS, mount, SAMBA

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## GUI

Go -> Connect to Server

smb://path_to_dir

## Command Line

    mount -t smbfs //user@server/sharename share

    mount_smbfs //user@SERVER/folder ./mntpoint
