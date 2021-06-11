Status: published
Date: 2012-06-29 22:25:13
Slug: ssh-copy-id
Author: Ben Chuanlong Du
Title: Copy SSH Public Key Using "ssh-copy-id"
Category: OS
Tags: Linux, SSH, server, remote, port, ssh-copy-id
Modified: 2020-02-29 22:25:13

You can use the following command to copy your SSH public key to a Linux server.

    :::bash
    ssh-copy-id -i ~/.ssh/id_rsa.pub host_machine

However, 
if a Linux server runs the SSH deamon on a non default port (default is 22), 
you have to specify the port with option `-p port`. 
In addition, 
the host machine and the port options must be in quotes 
(either single or double quotes), 
otherwise, 
you will get an error message.
Suppose sshd runs on port 323 on `host_machine`, 
the following command copies the ssh public key to it. 

    :::bash
    ssh-copy-id -i ~/.ssh/id_rsa.pub "host_machine -p 323"

You can of course SSH into the server 
and add your SSH public key(s) into the `~/.ssh/authorized_keys` file manually.
