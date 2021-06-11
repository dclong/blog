Status: published
Date: 2021-01-10 11:45:40
Author: Benjamin Du
Slug: alternatives-to-docker-containers
Title: Alternatives to Docker Containers
Category: Computer Science
Tags: Computer Science, Docker, container, alternative, LXD, LXC
Modified: 2021-01-10 11:45:40

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. LXD and Multipass are alternatives to Docker container.
    Docker is more lightweight than LXD 
    which is more lightweight than Multipass (Docker < LXD < Multipass).


2. Neither Docker nor LXD requires a CPU which supports virtualization. 
    However, 
    Multipass (which is Virtual Machine) requires a CPU that supports virtualization.



To sum up all that we know, both LXD and Docker are containerization technologies. Docker is light-weight, simplistic and is well-suited for isolating applications from each other making it popular among DevOps and developers alike. One app per Docker container.

LXD on the other hand, is much better equipped and is much closer to a complete operating system environment with networking and storage interfaces. You can run multiple Docker containers nested inside LXD, if you want.

## [podman](http://www.legendu.net/misc/blog/tips-on-podman)

Podman is a good container alternative to Docker.


[LXD vs Docker](https://linuxhint.com/lxd-vs-docker/)

[What is the difference between Docker, LXD, and LXC [closed]](https://unix.stackexchange.com/questions/254956/what-is-the-difference-between-docker-lxd-and-lxc)

[Do I need Docker?](https://discuss.linuxcontainers.org/t/do-i-need-docker/605)

[Docker vs LXD](https://www.reddit.com/r/selfhosted/comments/b50h9t/docker_vs_lxd/)