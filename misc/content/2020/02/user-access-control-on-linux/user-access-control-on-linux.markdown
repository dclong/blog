Status: published
Date: 2020-02-29 17:47:12
Author: Benjamin Du
Slug: user-access-control-on-linux
Title: User Access Control on Linux
Category: OS
Tags: OS, Linux, sudoer, sudo, access, user, group, login, control
Modified: 2020-02-29 17:47:12

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Login Access Control

The `/etc/security/access.conf` file specifies (user/group, host), 
(user/group, network/netmask) or (user/group, tty) combinations 
for which a login will be either accepted or refused.

https://www.poftut.com/access-conf-security-configuration-linux-unix/

https://linux.die.net/man/5/access.conf


## Sudo Access Control

The `/etc/sudoers` file controls 
who can run what commands as what users on what machines 
and can also control special things 
such as whether you need a password for particular commands. 
The file is composed of aliases (basically variables) and user specifications (which control who can run what).
However, 
it is suggested you never touch the file `/etc/sudoers` directly 
(even not via the comamnd `visudo`).
You might screw up all sudo users if you damage the format of the file.
The right way to grant a user sudo access is to add the user to the `sudo` group.
Please refer to 
[Add Users to a Group in Linux](http://www.legendu.net/en/blog/add-a-user-to-the-sudo-group-on-linux/)
for more details on how to add user to a group.

https://medium.com/@viraj.khatavkar/understanding-the-sudoers-file-8d71961b28ac

https://help.ubuntu.com/community/Sudoers
