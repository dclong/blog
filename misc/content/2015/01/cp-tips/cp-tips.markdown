Status: published
Date: 2020-05-02 14:57:03
Author: Ben Chuanlong Du
Slug: cp-tips
Title: Copying Files in Linux
Category: OS
Tags: linux, cp, command-line, rsync, scp
Modified: 2020-05-02 14:57:03

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Generally speaking, 
    you do not want to follow symbolic links when copying files 
    unless you are copying from one machine to another.
    If you do not want follow symbolic links,
    use `cp -av` and `rsync -avh`.
    If you do want to follow symbolic links,
    use `cp -rL` and `rsync -rLvh`.
    It is suggested that you use `rsync` instead of `cp` and `scp`.

## cp

By default, 
cp does not copy directories. 
However, 
the `-R`, `-a`, and `-r` options cause cp to copy recursively 
by descending into source directories 
and copying files to corresponding destination directories.

When copying from a symbolic link, 
cp normally follows the link only when not copying recursively 
or when `--link` (`-l`) is used. 
This default can be overridden 
with the `--archive` (`-a`), `-d`, `--dereference` (`-L`), `--no-dereference` (`-P`), 
and `-H` options. 
If more than one of these options is specified, the last one silently overrides the others.

When copying to a symbolic link, 
cp follows the link only when it refers to an existing regular file. 
However, 
when copying to a dangling symbolic link, 
cp refuses by default, 
and fails with a diagnostic, 
since the operation is inherently dangerous. 
This behavior is contrary to historical practice and to POSIX. 
Set POSIXLY_CORRECT to make cp attempt to create the target of a dangling destination symlink, in spite of the possible risk. Also, when an option like --backup or --link acts to rename or remove the destination before copying, cp renames or removes the symbolic link rather than the file it points to.

By default, cp copies the contents of special files only when not copying recursively. This default can be overridden with the --copy-contents option.

cp generally refuses to copy a file onto itself, with the following exception: if --force --backup is specified with source and dest identical, and referring to a regular file, cp will make a backup file, either regular or numbered, as specified in the usual ways (see Backup options). This is useful when you simply want to make a backup of an existing file before changing it.

The program accepts the following options. Also see Common options. 
