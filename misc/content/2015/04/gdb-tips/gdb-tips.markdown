Status: published
Date: 2020-05-22 13:58:39
Author: Ben Chuanlong Du
Title: Debug C/C++ Code Using GDB
Slug: gdb-tips
Category: Computer Science
Tags: programming, C++, C, debug, GDB, cpp
Modified: 2020-05-22 13:58:39

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. lines use : while functions use ::

2. use relative path from the executable to implementation files!!!

        :::gdb
        b ../../tree.cpp:31 if knot->name()=="GO:0006139"

3. it seems that there is a bug in GDB? 
    Sometimes the results of running an executable directly and within GDB are different!

## References

<http://www.unknownroad.com/rtfm/gdbtut/gdbtoc.html>