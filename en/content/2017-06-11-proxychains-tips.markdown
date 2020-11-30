Status: published
Date: 2020-11-30 14:34:01
Author: Ben Chuanlong Du
Slug: proxychains-tips
Title: Make Traffic Follow Through Proxies Using ProxyChains
Category: Software
Tags: Software, ProxyChains, network, web, proxy

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
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

## Syntax 

    proxychains4 [--help] [-q] [-f config_file] program_name [arguments]
    --help: show the help doc.
    -q makes proxychains quiet - this overrides the config setting
    -f allows one to manually specify a configfile to use

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

1. ProxyChains supports only `IP PORT` but not `DNS_NAME PORT` now.
    Notably, 
    `127.0.0.1` is OK but not `localhost`.
    For more details, 
    please refer to the issue 
    [How to specify server by DOMAIN PORT not IP PORT?](https://github.com/rofl0r/proxychains-ng/issues/246)
    .

2. There is no special requirement on the SSH configuration file (`$HOME/.ssh/config`).

3. `socks5` is prefer to `socks4` when you use a socks proxy (SSH tunnel).

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

    > [proxychains] config file found: /home/dclong/.proxychains/proxychains.conf
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

## Advanced Discussions

[How to specify server by DOMAIN PORT not IP PORT?](https://github.com/rofl0r/proxychains-ng/issues/246)

### Use Different Proxies for Different Servers

ProxyChains does not support configuring different proxies for different servers directly, 
however,
tinyproxy can be configured to use different upstream proxies for different destinations, 
and you can run tinyproxy on localhost and put its address into your proxychains configuration.



## References

https://linuxhint.com/proxychains-tutorial/

https://www.milesweb.com/blog/technology-hub/concatenate-multiple-proxies-proxychains/
