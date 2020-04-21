Status: published
Date: 2020-02-29 21:37:59
Author: Ben Chuanlong Du
Slug: ssh-tunnel
Title: SSH Tunnel
Category: Software
Tags: software, SSH tunnel, socks proxy, reverse

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## SSH Tunnel

You can create a SSH tunnel from your local machine to a server using the command below.

    :::bash
    ssh -i /path_to_key -fND 1080 user@server_ip

The created SSH tunnel is essentially a socks5 proxy 
and can be accessed as `localhost:1080`.
If you want the tunnel (socks5 proxy) to be accessible by other machines as well
rathe than the localhost only, 
you can bind it to all IPs.

    :::bash
    ssh -i /path_to_key -fND "*:1080" user@server_ip

You can verify that tunnel (socks5 proxy) is working using the following command.

    :::bash
    netstat -tlnp

Or you can try to visit a website using curl through the socks5 proxy.

    :::bash
    curl --socks5 localhost:1080 www.google.com

## Reverse SSH Tunnel

    :::bash
    ssh -o ProxyCommand='ssh bastion_server -W %h:%p' -R 20000:localhost:22 target_server

https://www.howtoforge.com/reverse-ssh-tunneling

https://unix.stackexchange.com/questions/46235/how-does-reverse-ssh-tunneling-work

https://blog.devolutions.net/2017/3/what-is-reverse-ssh-port-forwarding

## Advanced Usage 1: SSH into a Server Using Proxy

    :::bash
    ssh -o ProxyCommand='ssh bastion_server -W %h:%p' target_server

## Advanced Usage 2: SSH Tunnel to Avoid 2FA

Suppose you have 2 machines A and B. 
Machine B is only accssible from machine A using SSH through 2FA.
You can create and persist a SSH tunnel from machine A to machine B 
(2FA is still required when creating the SSH tunnel).
Then you can avoid 2FA when connecting from machine A to machine B 
by using the created SSH tunnel as socks5 proxy through tools such as proxychains. 

## Advanced Usage 3: SSH Reverse Tunnel Using Proxy

    :::bash
    ssh -o ProxyCommand='ssh bastion_server -W %h:%p' -R 20000:localhost:22 target_server

## Advanced Usage 4: SSH Reverse Tunnel + SSH Tunnel

Suppose you have 2 machines A and B. 
Machine B cannot visit the public network nor machine A.
However, machine B is accssible (directly or via a bastion server) from machine A using SSH
and machine A can visit the public network. 
You can follow the steps below to access the public network from machine B.

1. Create a Reversed SSH tunnel from machine A to machine B.

    :::bash
    ssh -i /path_to_key -o ProxyCommand='ssh bastion_server -W %h:%p' -R 20000:localhost:22 ip_b

2. Create a SSH Tunnel on machine B.

    :::bash
    ssh -i /path_to_key -fND 1080 localhost

3. Use the created SSH Tunnel as a socks5 proxy to visit the public network via proxychains.

    :::bash
    proxychains pip3 install pytorch

## References

[Proxy Using SSH Tunnel](https://www.systutorials.com/944/proxy-using-ssh-tunnel/)

[Quick-Tip: SSH Tunneling Made Easy](http://www.revsys.com/writings/quicktips/ssh-tunnel.html)

https://superuser.com/questions/303251/how-to-check-if-a-socks5-proxy-works
