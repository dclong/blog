Status: published
Date: 2020-05-22 15:37:47
Author: Ben Chuanlong Du
Title: Batch File Renaming Using "rename" 
Slug: rename-tips
Category: OS
Tags: Linux, rename, shell, tip

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

It is suggested that you use Python script to rename files in batch.

Change names of `.txt` files to lowercase.
```bash
rename 'y/A-Z/a-z/' *.txt
```

Get rid of `(1)` in file names.
```bash
rename 's/\(1\)//' * 
```

