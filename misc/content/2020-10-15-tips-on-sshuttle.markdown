Status: published
Date: 2020-10-19 00:51:53
Author: Benjamin Du
Slug: tips-on-sshuttle
Title: Tips on sshuttle
Category: Computer Science
Tags: Computer Science, sshuttle, VPN, SSH, internet, web, network

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. `sudo` permission is required to run sshuttle. 

1. It's valid to run sshuttle more than once simultaneously on a single client machine, 
    connecting to a different server every time, so you can be on more than one VPN at once.

2. It is common in enterprise environments that a SSH tunnel to a production server needs to go through a bastion server.
    There is no way to configure this in sshuttle directly,
    however, 
    this is doable in the configuration file of SSH.
    For more discussions,
    please refer to
    [[Question]: SSH proxy](https://github.com/sshuttle/sshuttle/issues/540)
    and
    [Configure SSH to Use a Proxy Server](http://www.legendu.net/en/blog/configure-ssh-to-use-a-proxy-server/)
    .

## Installation 

    :::bash
    wajig install iptables 
    pip3 install shuttle

## Configuration 

    {
    "HopServerA": [
        "12.182.293.180/32",
        "129.33.78.18/32",
        "129.13.280.0/24",
        "sftp.somehost.com"
    ],
    "HopServerB": [
        "11.38.26.0/24"
    ]
    }

## References

[sshoot](https://github.com/albertodonato/sshoot)

[sshuttle](https://github.com/sshuttle/sshuttle)

[sshuttle Documentation](https://sshuttle.readthedocs.io/en/stable/index.html)

[sshuttle: A Poor man’s VPN Over SSH](https://www.unixmen.com/sshuttle-poor-mans-vpn-ssh/)

[Using Sshuttle as a service](https://medium.com/@mike.reider/using-sshuttle-as-a-service-bec2684a65fe)

[How to use SSH as a VPN with sshuttle](https://www.techrepublic.com/article/how-to-use-ssh-as-a-vpn-with-sshuttle/)

[Use sshuttle to build a poor man’s VPN](https://fedoramagazine.org/use-sshuttle-to-build-a-poor-mans-vpn/)

[Chaining sshuttle commands over two hops](https://serverfault.com/questions/826585/chaining-sshuttle-commands-over-two-hops)