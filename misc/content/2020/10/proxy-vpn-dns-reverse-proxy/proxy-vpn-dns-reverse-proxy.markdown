Status: published
Date: 2020-10-03 10:47:34
Author: Benjamin Du
Slug: proxy-vpn-dns-reverse-proxy
Title: Proxy, Reverse Proxy, Load Balancer, VPN and DNS
Category: Computer Science
Tags: Computer Science, proxy, reverse proxy, DNS, VPN, network, internet, web, load balancing
Modified: 2021-05-03 10:47:34

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**



3. socks proxy 

4. [nginx](https://github.com/nginx/nginx)
    and
    [caddy](https://github.com/caddyserver/caddy)
    are good choices for reverse proxy.

5. sshuttle is a poor man's VPN.

6. [TunnelTo](https://tunnelto.dev/) (written in Rust leveraging tokio)
    allows you to expose your local web server to the internet with a public URL.

## Proxy vs VPN

1. When you connect to a VPN,
    all traffic will be routed through the VPN.
    You don't have the option to route part of the traffic through the VPN. 
    On the other hand,
    a proxy server is more flexible.
    It is easy to route some specific traffic through a proxy server.
    As a matter of fact,
    there are many different types of proxy corresponding to different traffic type,
    e.g., http proxy, socks proxy, ftp proxy, etc.
    Generally speaking, 
    a specific type of traffic can only be visisted using the right type of proxy server.
    For example,
    a FTP server can only be visited with a FTP proxy.

2. A proxy server is not as secure as a VPN.
    However,
    a proxy server can be used to visit web sites anonymously.

## Proxy vs Reverse Proxy

1. When a client C visits a server S using proxy P,
    the server S knows the proxy P (but not the client C) who visists it.
    When a client C visits a server S which uses a reverse proxy R 
    that balancing traffic to servers S1 and S2 (load balancing),
    the client C know only knows the server S but does not know underlying servers S1 and S2. 

2. A proxy can be used for caching, anonymity, logging, blocking sites and microservices
    while a reverse proxy can be used for 
    caching, load balancing, ingress, canary deployment and miroservices.

3. Proxy and Reverse Proxy can be used together.

For more discussions,
please refer to 
[Proxy vs Reverse Proxy Server Explained](https://www.youtube.com/watch?v=SqqrOspasag)
.

## Load Balancer vs Reverse Proxy

Load Balancing is one application (special case) of reverse proxy.
For more discussions,
please refer to
[Load Balancer vs Reverse Proxy (Explained by Example)](https://www.youtube.com/watch?v=S8J2fkN2FeI)
.


## References

[Proxy vs Reverse Proxy Server Explained](https://www.youtube.com/watch?v=SqqrOspasag)
