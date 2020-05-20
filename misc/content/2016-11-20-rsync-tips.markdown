Status: published
Date: 2020-05-20 14:04:56
Author: Ben Chuanlong Du
Slug: rsync-tips
Title: Tips on rsync
Category: OS
Tags: Linux, copy, synchronization, file system, filesystem, rsync

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Tips and Traps

1. The command `rsync -avh src_dir des_dir` (`src_dir` has no trailing slash) 
    synchronizes the whole directory `src_dir` into the destination directory `des_dir`
    while `rsync -avh src_dir/ des_dir` (`src_dir/` has trailing slash) 
    synchronizes the contents (sub-files and sub-directories) of `src_dir` into the destination directory `des_dir`.
    However, 
    one thing tricky is that `rsync -avh . des_dir` synchronizes the content 
    (sub-files and sub-directories) of the current directory into the destination directory `des_dir`.
    This is especially tricky if you programmally get the source directory that you want to synchronize.
    Here are a few **good practices to follow**.

    - Convert programmally generated path (for use in `rsync`) into its absolute form.

    - Always use the form `rsync -avh src_dir/ des_dir/` instead of the form `rsync -avh src_dir des_dir`.

2. Use the option `--partial` to keep partially transfered files 
    so that you can resume from break-point if rsync is interrupted.
    This is **really useful** 
    if you use rsync to transfer large files over unstable network.

3. You can specify the option `--relative` to ask `rsync` to create missing directories
    in order to keep the same directory structure.
    For example,
    suppose you want to copy the content of the directory `/new/x/y/z/` (of a machine) 
    to `/pre_existing/dir/` (on another machine)
    and you want keep the directory structure 
    (that is you want the content to be copied to `/pre_existing/dir/new/x/y/z/` instead of `/pre_existing/dir/`),
    you can use the following comamnd.

        :::bash
        rsync -a --relative /new/x/y/z/ user@remote:/pre_existing/dir/

    And if you want to have `y/z/` created but not inside `new/x/`
    (i.e., copy the content to `/pre_existing/dir/y/z/`), 
    you can add `./` where you want `--relative` to begin.

        :::bash
        rsync -a --relative /new/x/./y/z/ user@remote:/pre_existing/dir/

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

[rsync: how can I configure it to create target directory on server?](https://stackoverflow.com/questions/1636889/rsync-how-can-i-configure-it-to-create-target-directory-on-server)