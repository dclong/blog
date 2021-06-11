Status: published
Date: 2019-06-20 23:52:35
Author: Benjamin Du
Slug: network-in-docker-containers
Title: Network in Docker Containers
Category: Software
Tags: Software, Docker container, network, DNS, proxy
Modified: 2020-10-20 23:52:35

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. DNS is a common issue in Docker containers, 
  especially behind a corporate firewall.
  While the Linux way of handling DNS is to configure the file `/etc/resolv.conf` 
  (or via other related configuration files or tools),
  the Docker way is to pass DNS servers via the option `--dns`
  (which will be added to `/etc/resolv.conf`) 
  when starting the Docker container.
  Multiple DNS servers can be passed using multiple `--dsn` options.


2. Due to possible DNS issues in Docker containers, 
  it is suggested that you use IP addresses instead of URL names where possible. 
  Notably, `127.0.0.1` is preferred over `localhost` in various configure files (e.g., ProxyChains).


## Configure Proxy for Docker Containers

https://docs.docker.com/network/proxy/

## Configure Proxy for Docker Daemon

https://stackoverflow.com/questions/23111631/cannot-download-docker-images-behind-a-proxy

https://docs.docker.com/config/daemon/systemd/

If you set up http_proxy, https_proxy and restart the Docker daemon, 
it should work.

## Docker Networks

[What does --net=host option in Docker command really do?](https://stackoverflow.com/questions/43316376/what-does-net-host-option-in-docker-command-really-do)

[Docker Networking 101 – Host mode](http://www.dasblinkenlichten.com/docker-networking-101-host-mode/)

[Use host networking](https://docs.docker.com/network/host/)



## References

https://docs.docker.com/config/containers/container-networking/

https://docs.docker.com/v17.09/engine/userguide/networking/work-with-networks/#basic-container-networking-example

https://docs.docker.com/v17.09/engine/userguide/networking/

https://docs.docker.com/v17.09/engine/userguide/networking/configure-dns/

https://docs.docker.com/v17.09/engine/userguide/networking/default_network/configure-dns/

https://docs.docker.com/install/linux/linux-postinstall/#specify-dns-servers-for-docker

https://stackoverflow.com/questions/44761246/temporary-failure-in-name-resolution-errno-3-with-docker

https://stackoverflow.com/questions/24151129/network-calls-fail-during-image-build-on-corporate-network

https://github.com/moby/moby/issues/26330

https://stackoverflow.com/questions/44761246/temporary-failure-in-name-resolution-errno-3-with-docker?rq=1

[Can't install pip packages inside a docker container with Ubuntu](https://stackoverflow.com/questions/28668180/cant-install-pip-packages-inside-a-docker-container-with-ubuntu)
