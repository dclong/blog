Status: published
Date: 2020-03-05 11:08:32
Author: Benjamin Du
Slug: init-for-docker-containers
Title: Init for Docker Containers
Category: Software
Tags: software, Docker, container, init, s6, s6-overlay, tini, Supervisord, dumb-init
Modified: 2020-03-05 11:08:32

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


The article [Choosing an init process for multi-process containers](https://ahmet.im/blog/minimal-init-process-for-containers/)
has very detailed comparisons among different init options. 
[s6](https://skarnet.org/software/s6/) is recommended as thee best init for Docker.
The [s6-overlay-builder](https://github.com/just-containers/s6-overlay)
project is a series of init scripts and utilities to ease creating Docker images using s6 as a process supervisor.




## [tini](https://github.com/krallin/tini)
A tiny but valid `init` for containers

## [dumb-init](https://github.com/Yelp/dumb-init)

A minimal init system for Linux containers.

## References

[Supervisor with Docker: Lessons learned](https://advancedweb.hu/supervisor-with-docker-lessons-learned/)