UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-02-15 23:45:23
Author: Ben Chuanlong Du
Slug: change-file-permission-on-linux
Title: Change File Permission on Linux
Category: OS
Tags: Linux, file permission, file system, filesystem
Modified: 2016-08-15 23:45:23

R: 4
W: 2
X: 1

Make a directory readable to other people.
```sh
chmod 755 dir  
```
Make a file readable to other people.
```sh
chmod 644 file 
```
Make a directory and all its subcontents readable to other people.
```sh
# make the dir and its subcontents readable and executable
chmod 755 -R dir
# remove executable permission from files
find dir -type f | xargs chmod -x
```
