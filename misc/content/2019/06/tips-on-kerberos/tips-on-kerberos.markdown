Status: published
Date: 2020-02-05 13:11:06
Author: Benjamin Du
Slug: tips-on-kerberos
Title: Tips on Kerberos
Category: OS
Tags: OS, Linux, CentOS, Ubuntu, kerberos, authentication

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Installation 

### Ubuntu

apt-get install krb5-user

### CentOS

yum install -y ntp
yum install krb5-workstation krb5-libs krb5-auth-dialog


## Issues 

### kinit: Permission denied while initializing Kerberos 5 library

It is likely due to the fact that /etc/krb5.conf is not readable. 
Run the following command can help fix the issue.

    :::bash
    sudo chmod +r /etc/krb5.conf


## References

https://gist.github.com/ashrithr/4767927948eca70845db
