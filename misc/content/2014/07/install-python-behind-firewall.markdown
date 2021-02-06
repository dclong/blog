Status: published
Date: 2019-03-09 02:23:14
Author: Ben Chuanlong Du
Slug: install-python-behind-firewall
Title: Install Python Packages Behind Firewall
Category: Computer Science
Tags: Python, programming, Windows, proxy, install package

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**



It is recommended that you use `pip` to install Python packages.

1. If you don't already know the proxy in use (in your company),
    read the post [Find out Proxy in Use](http://www.legendu.net/en/blog/find-out-proxy-in-use/)
    to figure it out.

2. Set proxy environment variables.

        set http_proxy=http://user:password@proxy_ip:port
        set https_proxy=https://user:password@proxy_ip:port

3. Install Python packages.

        pip install package_name

As an alternative to steps 2 and 3, 
you can also pass the proxy to pip directly without setting environment variables for it.

    pip install --proxy="user:password@proxy_ip:port" package_name

Notice that if you have the pysocks package installed,
you can use a socks proxy with pip as well.
For example, 
if you have a socks5 proxy at `localhost:1080` you can use it with pipe as illustrated below.

    pip install --proxy socks5:localhost:1080 package_name


