Status: published
Author: Ben Chuanlong Du
Title: Operate Remote Servers Using SSH
Date: 2013-10-22 11:03:15
Slug: ssh-tips
Category: Software
Tags: tips, SSH, software, remote, Linux, ControlMaster, ControlPersist, ProxyCommand, ControlPath
Modified: 2020-10-22 11:03:15


## General Tips and Traps

1. The permissions of the directory `~/.ssh` and its subcontents
    on **both the local machine and the remote server** must be properly set 
    in order for SSH login via public key to work.
    A good pratice is to set the permission of `~/.ssh` to `700` (on both the local machine and the rmeote server)
    and set permissions of files under `~/.ssh` to  `600`.
    
2. SSH automatically maintains and checks a database containing identification 
    for all hosts it has ever been used with. 
    Host keys are stored in `~/.ssh/known_hosts` in the user's home directory. 
    Additionally, 
    the file `/etc/ssh/ssh_known_hosts` is automatically checked for known hosts. 
    Any new hosts are automatically added to the user's file. 
    If a host's identification ever changes, 
    SSH warns about this and disables password authentication 
    to prevent server spoofing or man-in-the-middle attacks, 
    which could otherwise be used to circumvent the encryption. 
    The option `-o StrictHostKeyChecking=no` can be used to turn off strict host key checking
    (on both new host keys and changed host keys).

        :::bash
        ssh -o StrictHostKeyChecking=no your_server

    You can also turn of strickt host key checking permanently by adding the following line into `~/.ssh/config`.

        StrictHostKeyChecking no

    This is helpful for automation when you are in a safe environment (e.g., private VPN). 
    However, 
    be aware of the risk and avoid using it in public environment.
    For more details, 
    please refer to
    [ssh(1) - Linux man page](https://linux.die.net/man/1/ssh)
    and
    [SSH: Disable Host Checking for Scripts & Automation](http://bencane.com/2013/07/22/ssh-disable-host-checking-for-scripts-automation/).

2. You can use the option `-o ProxyCommand='ssh proxy_server -W %h:%p'` 
    to SSH into a machine via a proxy server.
    Below is an illustration.
    For more details,
    please refer to
    [SSH Proxies and Jump Hosts](https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Proxies_and_Jump_Hosts).

        :::bash
        ssh -o ProxyCommand='ssh proxy_server -W %h:%p' target_server

3. When using `sshfs` and `fuse`, 
    make sure to add your user account into the `fuse` group.

        :::bash
        gpasswd -a dclong fuse
        newgrp fuse

4. It is suggested that you do not set any password for your SSH keys. 
    First, setting passwords for SSH keys defeats the purpose of using SSH keys.
    Seconds, 
    settings passwords for SSH keys might causes problems to other applicatons 
    (e.g., keyring management, cron jobs, duplicity, etc.) rely on SSH.

5. You can use SSH to run commands on a remote server in non-interactive mode.
    For example, 
    the following command logs into a server named `vm1.example.com` using SSH 
    and then use `rsync` to synchronize the directory `/workdir/` on the server `vm2.example.com`
    to the directory `/workdir/` on the server `vm1.example.com` (which is the local machine of `rsync`).

        :::bash
        ssh vm1.example.com rsync -avh --info=progress2 --delete vm2.example.com:/workdir/ /workdir/ \
            > backup.log 2> backup.err

## Multiplexing / ControlMaster

1. The `ControlMaster auto` option can be used to allow SSH reuse an existing connection.
    The `ControlPersist yes` option goes one step further to persist a connection once it's established.
    This means that there will essentially be one long-term SSH connection to each host. 
    Those 2 options together is a very good way to avoid frequently SSH logins 
    especially when you have to rely on bastion servers to login (e.g., in an Enterprise environment).
    Notice that you must also specify a `ControlPath` 
    if you use `ControlMaster`.
    For more discussions, 
    please refer to
    [How To Reuse SSH Connection To Speed Up Remote Login Process Using Multiplexing](https://www.cyberciti.biz/faq/linux-unix-reuse-openssh-connection/)
    .

        :::text
        Host *
        # ControlMaster: persist connections for reuse
            ControlPath ~/.ssh/control/%r@%h:%p
            ControlMaster auto
            ControlPersist yes
        #
            SendEnv LANG LC_*
            HashKnownHosts yes
            GSSAPIAuthentication yes
            GSSAPIDelegateCredentials no
        # make connection alive
            ServerAliveInterval 10
            ServerAliveCountMax 3

2. There are some potential drawbacks with `ControlMaster` turned on though. 
    It is mainly due to limited bandwidth.
    This is, generally speaking, not really an issue 
    unless you transfer huge amount of data over SSH.
    For more discussions,
    please refer to
    [SSH ControlMaster: The Good, The Bad, The Ugly](https://www.anchor.com.au/blog/2010/02/ssh-controlmaster-the-good-the-bad-the-ugly/)
    .

## References

[How To Reuse SSH Connection To Speed Up Remote Login Process Using Multiplexing](https://www.cyberciti.biz/faq/linux-unix-reuse-openssh-connection/)

[SSH ControlMaster: The Good, The Bad, The Ugly](https://www.anchor.com.au/blog/2010/02/ssh-controlmaster-the-good-the-bad-the-ugly/)

https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Proxies_and_Jump_Hosts

https://www.cyberciti.biz/faq/linux-unix-ssh-proxycommand-passing-through-one-host-gateway-server/

https://stackoverflow.com/questions/22635613/what-is-the-difference-between-ssh-proxycommand-w-nc-exec-nc

