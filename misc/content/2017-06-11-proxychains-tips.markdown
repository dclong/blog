Status: published
Date: 2019-11-12 09:12:45
Author: Ben Chuanlong Du
Slug: proxychains-tips
Title: ProxyChains Tips
Category: Software
Tags: Software, ProxyChains, network, web, proxy

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Installation

### Ubuntu

```
wajig install proxychains4
```

### Mac

```
brew install proxychains-ng
```
Notice that the proxychains-ng installed using Homebrew on Mac does not work well right now (as of 2019-03-07).
An alternative way is to use proxychains via Docker on Mac.
The Docker image
[dclong/jupyterhub-ds](https://cloud.docker.com/repository/docker/dclong/jupyterhub-ds)
has proxychains (NOT proxychains-ng) installed.

## Use Case of ProxyChains

There are multiple typical use cases of ProxyChains.
First,
ProxyChains can be used to circumstance a firewall through a single proxy. 
In this case, 
there can only be 1 proxy defined for ProxyChains
and it is best to specify the `strict_chain` option for ProxyChains.
```text
strict_chain
quiet_mode
tcp_read_time_out 15000
tcp_connect_time_out 8000
localnet 127.0.0.1/255.0.0.0

[ProxyList]
socks5     127.0.0.1 1080
```
Second,
ProxyChains can be used to cirumstance a firewall through a chain of proxies (in a certain order).
In this situation, 
a single proxy is not enough but you must redict your connection 
through multiple proxies in a certain order (a chain of proxies).
You have to list the proxies to use in the order you want to connect 
and specify the `strict_chain` option. 
Different types of proxies can be used.
```text
strict_chain
quiet_mode
tcp_read_time_out 15000
tcp_connect_time_out 8000
localnet 127.0.0.1/255.0.0.0

[ProxyList]
socks5     proxy_ip_1 1080
http     proxy_ip_2 1080
socks5     proxy_ip_3 1080
```
Last,
ProxyChains can be used to hide your identity similar to what tor can do for you. 
In order to do this, 
you have to define multiple proxies 
and redirect your connection through a chain of those proxies (in random order).
You have to specify the `dynamic_chain` or `random_chain` option.
```text
dynamic_chain
quiet_mode
tcp_read_time_out 15000
tcp_connect_time_out 8000
localnet 127.0.0.1/255.0.0.0

[ProxyList]
socks5     proxy_ip_1 1080
http     proxy_ip_2 1080
socks5     proxy_ip_3 1080
```

## Tricks and Traps 

1. It is suggested that you use IP addresses instead of URL names when configuring ProxyChains. 
  The reason is that IP addresses always work while URL names might not work if all the following situations are met.
    - The proxy is for internal use in an enterprise, which is often the case.
    - You use ProxyChains in a Docker container and forget to configure DNS for your Docker container.

2. no special requirement on `$HOME/.ssh/config`

3. socks5 is recommended

4. `proxychains ssh -i /path_to_key user@server_ip`


## Example of ProxyChains Configuration

```text
strict_chain
quiet_mode
tcp_read_time_out 15000
tcp_connect_time_out 8000
localnet 127.0.0.1/255.0.0.0

[ProxyList]
socks5     127.0.0.1 1080
```

## Error Message

1. SSH Configuration

        muxserver_listen bind(): No such file or directory

    This is probably due to configuration of SSH.
    For example,
    if you have the following line in the config file for SSH,
    you have to make sure that the directory `~/.ssh/control` exists.

        :::Bash
        ControlPath ~/.ssh/control/ssh_%h


2. Shell Alias

    > [proxychains] config file found: /home/chdu/.proxychains/proxychains.conf
    > [proxychains] preloading /usr/local/lib/libproxychains4.so
    > proxychains can't load process....: No such file or directory

    It is possibly due to alias used with ProxyChains.
    For example,
    I have the alias defined.

        :::sh
        alias ssh.analytics='ssh analytics_server_ip'

    `proxychains4 ssh.analytics` throws the above error message
    while `proxychains4 ssh analytics_server_ip` works well.


3. There seems to be an issue if ProxyChains is directly in a VM,
    but it works well if used in a Docker on the VM ...

## References

https://linuxhint.com/proxychains-tutorial/

https://www.milesweb.com/blog/technology-hub/concatenate-multiple-proxies-proxychains/
