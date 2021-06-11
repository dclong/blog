UUID: c2334373-2554-4d65-9911-5836efc6bd9d
Status: published
Date: 2017-02-06 14:36:40
Author: Ben Chuanlong Du
Slug: print-rows-from-a-text-file
Title: Print Rows from a Text File
Category: OS
Tags: Linux, shell, command line, head, tail, sed, awk, rows, lines, text manipulation
Modified: 2020-04-06 14:36:40

It is suggested that you **use Python instead of Shell** to manipulate text files!

Please refer to 
[Advanced Use of "head" and "tail"](http://www.legendu.net/en/blog/advanced-use-head-tail/)
on how to use `head` and `tail` for printing rows from a text file.
These 2 commands are convenient when you want to take head/tail rows. 
If you want to take middle rows of a file,
better ways exists using `sed` and `awk`. 
```bash
# print lines 10 to 20 using sed
sed -n '10,20p' filename
# print lines 10 to 20 using awk
awk 'NR >= 10 && NR <= 20' file_name
```
If you work with a very large file, 
you make the `sed` command a little bit more efficient by quitting ealier. 
For example, 
the following command efficiently prints lines 10000000 to 10000020 of the file.
```bash
sed -n '10000000,10000020p; 10000021q' file_name 
```
Thi way is faster than `awk` (but slower without the quitting early trick) on large files.
