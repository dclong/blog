Status: published
Author: Ben Chuanlong Du
Date: 2020-05-22 13:36:17
Title: Synchronize Files Using Dropbox
Slug: dropbox-tips
Category: Software
Tags: tips, Dropbox, Synchronizaion, backup, cloud

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 

1. Dropbox won't sync files that you don't have the right permissions.

2. You'd better not merge an old Dropbox folder while installing/configuring Dropbox.

3. You'd better not store symbolic links in the Dropbox folder,
    because the symbolic links will be replaced by the real files/folders 
    when synchronized to other computers.
    It might have problem if you push things to a repository 
    and give the symbolic link to public for downloading. 
    Strickly speaking, 
    this is a problem of using symbolic with GIT not with Dropbox.

4. It is not a good idea to put Git repository in Dropbox,
    especially these repositories than generate lots of small files after compiling.

## References

https://www.addictivetips.com/ubuntu-linux-tips/enable-dropbox-support-in-dolphin-file-manager/