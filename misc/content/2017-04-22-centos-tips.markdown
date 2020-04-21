UUID: 818dd6af-953f-4eaf-a772-1f0667509cf7
Status: published
Date: 2017-04-22 13:24:33
Author: Ben Chuanlong Du
Slug: centos-tips
Title: CentOS Tips
Category: OS
Tags: Linux, CentOS, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. The `wheel` group is the `sudo` group.
So to grant a user the sudo previlege,
just add it to the `wheel` group.

```bash
gpasswd -a user_name wheel
```

## EPEL

```bash
sudo yum -y install epel
```

## IUS Release
```bash
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
```
