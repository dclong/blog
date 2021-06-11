Status: published
Date: 2020-10-04 09:59:49
Author: Benjamin Du
Slug: tips-on-sshuttle
Title: Tips on sshuttle
Category: Computer Science
Tags: Computer Science, sshuttle, VPN, SSH, internet, web, network, SSH tunnel
Modified: 2021-01-04 09:59:49

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
    pip3 install sshuttle

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

## Reverse Traffic Forwarding 

[[question] "server" on the local system, "client" on the remote system?](https://github.com/sshuttle/sshuttle/issues/421)

## sshuttle in Docker 

[how to let docker container work with sshuttle?](https://stackoverflow.com/questions/29838892/how-to-let-docker-container-work-with-sshuttle)

[Installing iptables in docker container based on alpinelinux](https://stackoverflow.com/questions/41706983/installing-iptables-in-docker-container-based-on-alpinelinux)

[Error running sshuttle in Docker container](https://github.com/sshuttle/sshuttle/issues/546)

[Docker ubuntu 20.04 container OSError: [Errno 18] Invalid cross-device link: '/etc/hosts' -> '/etc/hosts.sbak'](https://github.com/sshuttle/sshuttle/issues/518)

--cap-add=NET_ADMIN
--cap-add=NET_RAW

    docker run -d \
        --hostname jupyterhub-ds \
        --log-opt max-size=50m \
        --memory=$(($(head -n 1 /proc/meminfo | awk '{print $2}') * 4 / 5))k \
        --cpus=$((`nproc` - 1)) \
        --cap-add=NET_ADMIN \
        --cap-add=NET_RAW \
        -p 3000:8000 \
        -e DOCKER_USER=`id -un` \
        -e DOCKER_USER_ID=`id -u` \
        -e DOCKER_PASSWORD=`id -un` \
        -e DOCKER_GROUP_ID=`id -g` \
        -e DOCKER_ADMIN_USER=`id -un` \
        -v `pwd`:/workdir \
        -v `dirname $HOME`:/home_host \
        dclong/jupyterhub-ds /scripts/sys/init.sh

## References

[sshoot](https://github.com/albertodonato/sshoot)

[sshuttle](https://github.com/sshuttle/sshuttle)

[sshuttle Documentation](https://sshuttle.readthedocs.io/en/stable/index.html)

[sshuttle: A Poor man’s VPN Over SSH](https://www.unixmen.com/sshuttle-poor-mans-vpn-ssh/)

[Using Sshuttle as a service](https://medium.com/@mike.reider/using-sshuttle-as-a-service-bec2684a65fe)

[How to use SSH as a VPN with sshuttle](https://www.techrepublic.com/article/how-to-use-ssh-as-a-vpn-with-sshuttle/)

[Use sshuttle to build a poor man’s VPN](https://fedoramagazine.org/use-sshuttle-to-build-a-poor-mans-vpn/)

[Chaining sshuttle commands over two hops](https://serverfault.com/questions/826585/chaining-sshuttle-commands-over-two-hops)