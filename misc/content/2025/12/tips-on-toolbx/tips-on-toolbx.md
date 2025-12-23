Status: published
Date: 2025-12-14 16:59:01
Modified: 2025-12-22 18:38:50
Author: Benjamin Du
Slug: tips-on-toolbx
Title: Tips on Toolbx
Category: Computer Science
Tags: Computer Science, programming, toolbx, toolbox, DistroBox, icon, Docker, image

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

I personally devoted effort on
[Docker images](https://www.legendu.net/en/blog/my-docker-images/)
which makes it easy to develop in Docker containers.

- Create a user with same uid/gid as the user on the host on the fly 
    so that permissions are handled seamlessly.
- Lots of useful tools are pre-installed and configured.

Toolbx / DistroBox share similarities with my effort on Docker images.
Of course, 
Toolbx / DistroBox are superior in many ways.

- Toolbx / DistroBox are NOT based on Docker but rather podman (which is more secure).
- Toolbx / DistroBox have seamless integraito with the host.
    Tools installed in Toolbx / DistroBox feel native.

However, 
my Docker images does have some advantages as well.

- Lots of useful tools are pre-installed and configured.
- Can create more users after launching the Docker container 
    and thus allow multiple users to collaborated in the same Docker container.
- Have a built-in command-line tool
    [icon](https://github.com/legendu-net/icon)
    which makes it easy to install and configure tools (especially in Docker containers)
    .
    Of course,
    icon can be used with Toolbx / DistroBox as well.
  
## Toolbox

https://github.com/containers/toolbox

toolbox create --distro ubuntu --release 24.04

## DistroBox

https://github.com/ranfdev/DistroShelf

https://distrobox.it/#quick-start
