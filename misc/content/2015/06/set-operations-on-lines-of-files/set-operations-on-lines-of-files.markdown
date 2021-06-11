UUID: 8c20e61c-fcaf-433c-890f-9973d9e423ab
Status: published
Date: 2015-06-14 02:12:06
Author: Ben Chuanlong Du
Slug: set-operations-on-lines-of-files
Title: Set Operations on Lines of Files
Category: Computer Science
Tags: programming, set operations, file, lines, sort, uniq, comm, shell
Modified: 2016-06-14 02:12:06

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. union of lines in 2 files
```bash
comm f1 f2
```
Or you can use
```bash
cat f1 f2 | sort -u
```

3. Show symmetric difference 
```bash
comm -3 file1 file2
```
Show difference of 1 and 2
```bash
comm -23 file1 file2
```
Or you can use if both files contain unique lines
```bash
cat f1 f2 f2 | sort | uniq -u
```
Note that lines in files must be sorted first if you use the command `comm`.
To sort lines in a file, 
you can use the following command.
```bash
sort file -o file
```

