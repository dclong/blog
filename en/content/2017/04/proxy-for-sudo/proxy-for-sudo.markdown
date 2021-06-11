Status: published
Date: 2017-04-07 23:42:48
Author: Ben Chuanlong Du
Slug: proxy-for-sudo
Title: Proxy for `sudo`
Category: Internet
Tags: Network, proxy, environment variable, sudo
Modified: 2019-03-07 23:42:48

You can setup proxy in a terminal by export environment variables `http_proxy` and `https_proxy'.
```bash
export http_proxy='proxy_server:port'
export https_proxy='proxy_server:port'
```
However,
you might find the exported environment variables are not visible to `sudo`.
This can be resovled by simplying adding the `-E` (preserve environment) option to `sudo`.
```bash
sudo -E command_to_run
```

## Question

Can a socks proxy be used as a HTTP/HTTPS proxy directly?
