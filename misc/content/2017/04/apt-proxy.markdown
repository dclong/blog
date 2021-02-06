Status: published
Date: 2019-03-07 23:42:48
Author: Ben Chuanlong Du
Slug: apt-proxy
Title: Configure Proxy for Apt
Category: OS
Tags: Linux, apt, source list, proxy

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Add the following lines into the file `/etc/apt/apt.conf`,
where `proxy_server` is the address/ip of the server
and `port` is the port of the proxy service.
```bash
Acquire::http::Proxy "proxy_server:port";
Acquire::https::Proxy "proxy_server:port";
```

A HTTP proxy can be used as both HTTP and HTTPS proxy.

## Question

1. Does apt support socks proxy? If not, can a socks proxy be used as HTTP/HTTPS proxy for apt?