Status: published
Date: 2020-10-15 22:55:59
Author: Benjamin Du
Slug: tips-on-sshuttle
Title: Tips on Sshuttle
Category: Computer Science
Tags: Computer Science

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

It’s valid to run sshuttle more than once simultaneously on a single client machine, 
connecting to a different server every time, so you can be on more than one VPN at once.

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