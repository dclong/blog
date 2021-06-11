Status: published
Date: 2019-05-02 02:41:04
Author: Benjamin Du
Slug: alternative-to-the-rm-command-in-linux
Title: Alternative to the rm Command in Linux
Category: OS
Tags: Linux, Shell, rm, Trash, mv
Modified: 2019-05-02 02:41:04

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

As is know to all,
it can be dangerous to use the `rm` command directly in Linux/Unix. 
A simple idea is to define other commands/alias/script to replace it.
For example, 
I have a shell script named `trash` which moves files (as input arguments) to the system's Trash directory.

    trash files_to_remove

Another even simplier way is to directly move files to the directory `/tmp`.

    mv files_to_remove /tmp
