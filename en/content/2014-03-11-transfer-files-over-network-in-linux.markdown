Status: published
Author: Ben Chuanlong Du
Date: 2016-07-13 22:42:20
Slug: transfer-files-over-network-in-linux
Title: Transfer Files over Network in Linux
Category: internet
Tags: internet, Linux, network, web, transfer, file system, nfs, SSH

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
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

2. There are some other file-copying tools such as mbuffer, nc, etc. 
    if you want to squeeze the most out of network speed.

        tar zcf - bigfile.m4p | mbuffer -s 1K -m 512 | ssh otherhost "tar zxf -"

## References

https://linuxaria.com/article/tar-rsync-netcat-scp

http://moo.nac.uci.edu/~hjm/HOWTO_move_data.html

https://unix.stackexchange.com/questions/48399/fast-way-to-copy-a-large-file-on-a-lan