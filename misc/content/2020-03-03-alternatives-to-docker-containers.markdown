Status: published
Date: 2020-03-03 21:30:11
Author: Benjamin Du
Slug: alternatives-to-docker-containers
Title: Alternatives to Docker Containers
Category: Computer Science
Tags: programming

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


1. LXD and Multipass are alternatives to Docker container.
    Docker is more lightweight than LXD 
    which is more lightweight than Multipass (Docker < LXD < Multipass).


2. Neither Docker nor LXD requires a CPU which supports virtualization. 
    However, 
    Multipass (which is Virtual Machine) requires a CPU that supports virtualization.



To sum up all that we know, both LXD and Docker are containerization technologies. Docker is light-weight, simplistic and is well-suited for isolating applications from each other making it popular among DevOps and developers alike. One app per Docker container.

LXD on the other hand, is much better equipped and is much closer to a complete operating system environment with networking and storage interfaces. You can run multiple Docker containers nested inside LXD, if you want.



[LXD vs Docker](https://linuxhint.com/lxd-vs-docker/)

[What is the difference between Docker, LXD, and LXC [closed]](https://unix.stackexchange.com/questions/254956/what-is-the-difference-between-docker-lxd-and-lxc)

[Do I need Docker?](https://discuss.linuxcontainers.org/t/do-i-need-docker/605)

[Docker vs LXD](https://www.reddit.com/r/selfhosted/comments/b50h9t/docker_vs_lxd/)