Status: published
Date: 2020-05-22 15:00:33
Author: Ben Chuanlong Du
Title: Java PPA for Ubuntu
Slug: java-ppa
Category: Computer Science
Tags: programming, Java, Ubuntu, PPA
Modified: 2020-05-22 15:00:33

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

```bash
sudo add-apt-repository ppa:webupd8team/java
```
If you are behind a firewall and has to communicate to the internal via a proxy,
you can first export the environment vairables `http_proxy` and `https_proxy`.
```bash
export http_proxy='proxy_server:port'
export https_proxy='proxy_server:port'
```
If a user name and password is needed, 
export them using the following command.
```bash
export http_proxy=http://username:password@proxy_server:port
export https_proxy=https://username:password@proxy_server:port
```
However, make sure to run `sudo` with the `-E` (preserve environment) option.
```bash
sudo -E add-apt-repository ppa:webupd8team/java
```
