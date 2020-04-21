Status: published
Date: 2020-04-20 08:17:02
Author: Ben Chuanlong Du
Slug: rsync-tips
Title: Tips on rsync
Category: OS
Tags: Linux, copy, synchronization, file system, filesystem, rsync

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Tips and Traps

The command `rsync -avh src_dir des_dir` (`src_dir` has no trailing slash) 
synchronizes the whole directory `src_dir` into the destination directory `des_dir`
while `rsync -avh src_dir/ des_dir` (`src_dir/` has trailing slash) 
synchronizes the contents (sub-files and sub-directories) of `src_dir` into the destination directory `des_dir`.
However, 
one thing tricky is that `rsync -avh . des_dir` synchronizes the content 
(sub-files and sub-directories) of the current directory into the destination directory `des_dir`.
This is especially tricky if you programmally get the source directory that you want to synchronize.
Here are a few good practices to follow.

1. Convert programmally generated path (for use in `rsync`) into its absolute form.

2. Always use the form `rsync -avh src_dir/ des_dir/` instead of the form `rsync -avh src_dir des_dir`.

## Examples

1. Disable strickt host key checking. 

        :::bash
        rsync -e "ssh -o StrictHostKeyChecking=no" ...

2. Use a different port (rather than 22).

        :::bash
        rsync -e "ssh -p 323" ...

3. Copy specified patterns (e.g., JupyterLab notebooks) only.

        :::bash
        rsync -avh --include='*.ipynb' --include='*/' --exclude='*' --delete src_dir/ des_dir/

4. Sync one directory to another one. 

        :::bash
        rsync -avh --info=progress2 --exclude=‘*.pyc’ --exclude=‘.Trash-*’ --exclude=‘lost+found’ --delete $tiger:/workdir/ /workdir/

5. An example script for synchronizing a Java project directory.

        :::bash
        #!/usr/bin/env bash

        dir=$(dirname $(dirname "$0"))

        rsync -avh \
            --info=progress2 \
            --delete \
            --exclude=.git/ \
            --exclude=target/ \
            --exclude=build/ \
            --exclude=analysis/ \
            --exclude=classes/ \
            --exclude=maven-archiver/ \
            --exclude=surefire-reports/ \
            --exclude=test-classes/ \
            --exclude=generated-sources/ \
            --exclude=generated-test-sources/ \
            --exclude=java.io.tmpdir/ \
            --exclude=out \
            $dir/ \
            $tiger:/workdir/users/

## Squeeze the Performance out of `rsync` over `ssh`

### Some Options of `rsync`

- a: archive mode - rescursive, preserves owner, preserves permissions, preserves modification times, preserves group, copies symlinks as symlinks, preserves device files.
- H: preserves hard-links
- A: preserves ACLs
- X: preserves extended attributes
- x: don't cross file-system boundaries
- v: increase verbosity
- --numeric-ds: don't map uid/gid values by user/group name
- --delete: delete extraneous files from dest dirs (differential clean-up during sync)
- --info=progress2: show progress during transfer

## Some Options of `ssh`

- T: turn off pseudo-tty to decrease cpu load on destination.
- c arcfour: use the weakest but fastest SSH encryption. Must specify "Ciphers arcfour" in sshd_config on destination.
- o Compression=no: Turn off SSH compression.
- x: turn off X forwarding if it is on by default.

Example of copying files from local to a remote server using rsync and ssh with optimal speed.

    :::bash
    rsync -aHAXxv --numeric-ids --delete --info=progress2 -e "ssh -T -c arcfour -o Compression=no -x" user@remote_host:source_dir dest_dir

Example of copying files from a remote server to local using rsync and ssh with optimal speed.

    :::bash
    rsync -aHAXxv --numeric-ids --delete --info=progress2 -e "ssh -T -c arcfour -o Compression=no -x" source_dir user@remote_host:dest_dir]




## Errors & Solutions

### error in protocol data stream (code 12)
It is probably because the remote diretory does not exist.

### References

[14 Practical examples of the rsync command](http://www.librebyte.net/en/gnulinux/14-practical-examples-of-the-rsync-command/)

https://askubuntu.com/questions/625085/rsync-over-ssh-error-in-protocol-data-stream-code-12-ssh-works

https://gist.github.com/KartikTalwar/4393116
