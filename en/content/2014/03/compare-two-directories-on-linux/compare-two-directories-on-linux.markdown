Status: published
Author: Ben Chuanlong Du
Date: 2014-03-10 19:13:40
Slug: compare-two-directories-on-linux
Title: Compare Two Directories on Linux
Category: OS
Tags: difference, directory, folder, Linux, md5sum, md5deep, diff, ssh
Modified: 2019-05-10 19:13:40


## On the Same Machine

If the two directories are on the same machine, 
you can use either `colordiff` (preferred over `diff`) or `git diff`
to find the differences between them. 
```sh
colordiff -qr dir_1 dir_2
```
```sh
git diff --no-index dir_1 dir_2
```

## On Different Machines

It is a little bit tricky when the two directories are on different machines. 
You have to first calculate md5sums of files in the two directories recursively,
and then compare the md5sums.
To calculate the md5sums of files in a directory recursively 
and output the results into a file `md5.txt`, 
you can use the following command.
```sh
md5deep -r path_to_directory > md5.txt
```
Once you have the md5sums for the 2 directories calculated 
and outputed into files (e.g., `j.txt`) on the 2 machines,
you can then compare the contents of the 2 files on the 2 machines.
One way to achieve this is to run the following command on one of the machines.
```sh
ssh -p port user_name@the_other_server cat md5.txt | git diff --no-index md5.txt -
```
You can also copy (using `rsync` or `scp`) the output file on one machine to the other machine 
and then compare them locally using `git diff`.
