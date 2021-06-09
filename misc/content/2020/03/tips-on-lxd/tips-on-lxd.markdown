Status: published
Date: 2021-01-10 11:45:40
Author: Benjamin Du
Slug: tips-on-lxd
Title: Tips on LXD
Category: Computer Science
Tags: Computer Science, Docker, container, LXD, LXC

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. LXD only works in Linux.
    It is not supported on macOS.

2. LXD does not require a CPU which supports virtualization. 

## [Installation](https://ubuntu.com/tutorials/tutorial-setting-up-lxd-1604#2-install-lxd)

    sudo apt-get install lxd zfsutils-linux
    gpasswd -a $(id -un) lxd
    newgrp lxd

## [Setup LXD](https://ubuntu.com/tutorials/tutorial-setting-up-lxd-1604#3-setup-lxd)

    sudo lxd init

## [Launch a container](https://ubuntu.com/tutorials/tutorial-setting-up-lxd-1604#4-launch-a-container)

    lxc list
    lxc launch ubuntu:16.04
    lxc exec stirring-beagle -- ls -la


## Publish LXD Images

https://ubuntu.com/tutorials/create-custom-lxd-images

https://ubuntu.com/blog/publishing-lxd-images

https://medium.com/@tcij1013/lxc-lxd-cheetsheet-effb5389922d

https://github.com/lxc/lxd/issues/6805

[LXDHub](https://lxdhub.xyz/remote/images/images)

## References

https://github.com/lxc/lxd

https://github.com/lxc/lxd/issues/4015

https://lxdhub.xyz/remote/images/images

[NVidia CUDA inside a LXD container](https://ubuntu.com/blog/nvidia-cuda-inside-a-lxd-container)