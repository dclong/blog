Status: published
Date: 2019-11-17 12:24:36
Author: Benjamin Du
Slug: use-snap-apps-in-docker
Title: Use Snap Apps in Docker
Category: Software
Tags: Software, Docker, Kata Container, snap apps
Modified: 2019-11-17 12:24:36

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Snap app is not 
(and [will probably never be](https://bugs.launchpad.net/snappy/+bug/1841327)) 
compatible with Docker by default.
However, 
there are some hackings to make snap app to work in Docker.
Also, 
[Kata Container](https://katacontainers.io/)
is a good (lightweight, container-like performance) VM alternative to Docker
if you do not like limitations and potential security issues of Docker.

## References

https://ograblog.wordpress.com/2017/06/02/dock-a-snap/

https://github.com/ogra1/snapd-docker

https://forum.snapcraft.io/t/snapd-in-docker/177
