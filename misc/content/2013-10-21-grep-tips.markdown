Status: published
Author: Ben Chuanlong Du
Date: 2020-05-22 14:53:28
Title: Search for Files in Command-line Using grep
Slug: grep-tips
Category: OS
Tags: tips, grep, egrep

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**

Following are some good articles about `grep`.
- [14 Practical examples of the grep command](http://www.librebyte.net/en/gnulinux/14-practical-examples-of-the-grep-command/)

1. The Perl style (option `-P`) regular expression is more powerful 
    than the basic (default) and extended (option `-E`) regular expression. 
    It is suggested that you use the perl style as much as possible.
    However, 
    be careful about unimplemented features. 

2. Options `-n` and `-o` of `grep` are useful.

3. Search in current directory recursively for files containing the text "video".
    Symbolic links are followed.

        :::bash
        grep -iR 'video' .

4. Search in current directory recursively for files containing the text "video".
    Symbolic links are NOT followed.

        :::bash
        grep -ir 'video' .