Status: published
Author: Ben Chuanlong Du
Date: 2014-03-02 17:16:03
Slug: transfer-files-over-network-in-linux
Title: Transfer Files over Network in Linux
Category: Internet
Tags: internet, Linux, network, web, transfer, file system, nfs, SSH
Modified: 2020-05-02 17:16:03


## Comparison of Network Drives (Remote File System)

1. NFS is very fast but not secure and it is for Unix/Linux only. 
    It is a good choice for local network sharing.

2. Samba is fast, secure and cross-platform. 
    it is good for general purpose sharing and popular in companies.

3. SSHFS is slow but very secure and it is for Unix/Linux only. 
    It is good for situations where security is critical but performance is not.

To sum up,
**Samba is the one you want to use generally speaking**.
However,
if you are on a local network and performance is crtical, 
go with NFS.

## Comparison of File-copying Tools

1. Generally speaking, 
    `rsync` is the tool you want to use in most situations. 
    It is definitely preferred over `scp` 
    unless in situations when `rsync` is not available (e.g., on Andrioid).

2. There are some other file-copying tools such as `mbuffer` and `netcat`/`nc`
    to help you squeeze the most out of network speed.
    However,
    unless you want to transfer huge files over high speed LAN
    and security is not a concern,
    you still want to stick with `rsync`.
    The example below is how you can copy files suing `mbuffer`.

        :::bash
        tar zcf - bigfile.m4p | mbuffer -s 1K -m 512 | ssh otherhost "tar zxf -"

    The example below uses `tar` and `netcat` to copy files.

        :::bash
        # run this command on the machine with the source files
        tar --numeric-owner -cvf - ./ | netcat -l -p 2020
        # run this command on the machine to copy files to
        netcat source_machine_ip 2020 | tar -zxf -

## References

[The best way to move data](https://linuxaria.com/article/tar-rsync-netcat-scp)

[tar + netcat = very fast copy](http://blog.alanporter.com/2015-04-13/fast-copy/)

https://linuxaria.com/article/tar-rsync-netcat-scp

http://moo.nac.uci.edu/~hjm/HOWTO_move_data.html

https://unix.stackexchange.com/questions/48399/fast-way-to-copy-a-large-file-on-a-lan
