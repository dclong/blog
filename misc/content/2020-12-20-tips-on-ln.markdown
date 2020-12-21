Status: published
Date: 2020-12-20 20:32:29
Author: Benjamin Du
Slug: tips-on-ln
Title: Tips on the Linux Command ln
Category: Computer Science
Tags: Computer Science, ln, symbolic, link, rsync

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

It is suggest that you avoid using the trailing slash 
when you use `ln` to create symbolic link for a directory. 
This is different from the command `rsync` 
which a trailing slash is recommended when synchronize a directory.

ln -s /path/to/dir /target/dir

ln -s /path/to/file /target/dir 