Status: published
Date: 2015-05-17 16:36:48
Author: Ben Chuanlong Du
Slug: run-unix-linux-commands-in-sas
Title: Run Unix/Linux Commands in SAS
Category: Computer Science
Tags: programming, SAS, Unix, Linux, command

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

SAS can run Unix/Linux commands everywhere using
```SAS
x command;
```
For exampel,
to create a directory named "abc" in your home directory.
```SAS
x mkdir ~/abc;
```

It can even run user-defined shell scripts, 
which is great. 
even though you can use unix/linux command in sas, 
it seems that it is not robust and it is often hard 
to test whether the command has run successfully.
It is suggested that you avoid using unix/linux commands in sas.
