Status: published
Date: 2020-01-28 10:27:55
Author: Benjamin Du
Slug: tips-on-systemd
Title: Tips on Systemd
Category: OS
Tags: OS, Linux, systemd, service

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. run systemctl to list services managed by systemd.

2. Use the command `ps aux | less` to check whether systemd is running as PID 1.

3. `ps --no-headers -o comm 1`

## References

https://superuser.com/questions/1017959/how-to-know-if-i-am-using-systemd-on-linux

https://unix.stackexchange.com/questions/121654/convenient-way-to-check-if-system-is-using-systemd-or-sysvinit-in-bash
