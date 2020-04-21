UUID: 45fb68b1-9fb8-4732-a197-99d8a452f785
Status: published
Date: 2017-06-25 10:37:51
Author: Ben Chuanlong Du
Slug: install-sbt-on-centos
Title: Install sbt on CentOS
Category: OS
Tags: Linux, CentOS, RedHat, sbt, install

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

```sh
wget http://dl.bintray.com/sbt/rpm/sbt-0.13.5.rpm
sudo yum install sbt-0.13.5.rpm
```

```sh
curl https://bintray.com/sbt/rpm/rpm | sudo tee /etc/yum.repos.d/bintray-sbt-rpm.repo
sudo yum install sbt
```
