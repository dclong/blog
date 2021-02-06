Status: published
Date: 2019-10-11 01:11:28
Author: Ben Chuanlong Du
Slug: resolve-the-dns-contamination-issue-in-firefox
Title: Resolve the DNS Contamination Issue in Firefox
Category: Software
Tags: software, Firefox, proxy, DNS contamination, socks

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

The local DNS you use in China is probably contaminated
and popular sites like Google, Facebook, etc. are not interpreted correctly.
So if you are in China and use Firefox with Proxy,
make sure to set `network.proxy.socks_remote_dns` to be true (follow the steps below).

1. Open an empty tab in Firefox.

2. Go to about:config in the URL bar.

3. Search for `network.proxy.socks_remote_dns`.

4. Change the value to be `true`.
