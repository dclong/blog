Status: published
Date: 2021-02-08 14:45:17
Author: Ben Chuanlong Du
Slug: docker-on-windows
Title: Docker on Windows
Category: Software
Tags: Software, Docker, Widnows, Windows 10, Hyper-V, Virtualization
Modified: 2021-02-08 14:45:17
It is suggested that you use Docker in WSL 
rather than using Docker for Windows.


While Docker can be used on Windows (10 and later) now, 
there are all kinds of issues. 
It is suggested that you avoid running Docker on Windows at this time 
unless you absolutely have to.

## Installtion

1. Docker is natively supported on Win 10 and later. 
However, 
you need to enable Hyper-V and Virtualization (enabled by default usually).
Follow the steps below to enable Hyper-V.

    a. In the Control Panel, click Programs > Programs and Features.

    b. Click Turn Windows features on or off.

    c. Click Hyper-V, click OK, and then click Close.

## Usage

1. Best to run Docker commands in CMD rather than in cygwin.
First, 
Cygwin paths (when mounting volumes) are not recognized by Docker on Windows.
Second, 
some docker commands will simply fail.

## Tips


### Mounting Host Directories on Windows

https://rominirani.com/docker-on-windows-mounting-host-directories-d96f3f056a2c

### Portainer

Portainer is an open-source management UI for Docker, 
including Docker Swarm environment. 
Portainer makes it easier for you to manage your Docker containers, 
it allows you to manage containers, images, networks, and volumes from the web-based Portainer dashboard.

## Issues 

1. It seems that file permission mapping does NOT work on Windows.
(not sure, need to confirm ...)

2. There is issue to mount volumes to a docker container on Windows. 

## References