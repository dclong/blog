Status: published
Date: 2019-03-08 18:57:48
Author: Ben Chuanlong Du
Slug: socks-proxy-to-http-proxy
Title: Socks Proxy to HTTP Proxy
Category: Internet
Tags: network, socks proxy, http proxy, polipo
Modified: 2019-03-08 18:57:48

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Convert Socks Proxy to HTTP Proxy

Polipo is a tool that can convert a socks proxy to a HTTP proxy.
However this might not be needed
as many tools directly accepts a socks proxy as a HTTP/HTTPS proxy.
For example, 
if you have a socks5 proxy at `localhost:1080`,
you can pass `socks5://localhost:1080` to tools that require a HTTP/HTTPS proxy.

```Bash
# install polipo
wajig search polipo

# create a http proxy at 8123 using the socks proxy
polipo socksParentProxy=localhost:1080
```

## HTTP Proxy to Socks Proxy

https://www.npmjs.com/package/http-proxy-to-socks


## References

https://www.codevoila.com/post/16/convert-socks-proxy-to-http-proxy-using-polipo
