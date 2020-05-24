Status: published
Date: 2020-05-24 10:37:18
Author: Benjamin Du
Slug: tips-on-systemd
Title: Tips on Systemd
Category: OS
Tags: OS, Linux, systemd, service

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## systemctl

systemctl may be used to introspect and control the state of the `systemd` system and service manager. 

1. List services managed by systemd.

        :::bash
        systemctl 

2. Check whether systemd is running as PID 1.

        :::bash
        ps --no-headers -o comm 1

## References

https://superuser.com/questions/1017959/how-to-know-if-i-am-using-systemd-on-linux

https://unix.stackexchange.com/questions/121654/convenient-way-to-check-if-system-is-using-systemd-or-sysvinit-in-bash

[How To Use Systemctl to Manage Systemd Services and Units](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)