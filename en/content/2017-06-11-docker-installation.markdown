Status: published
Date: 2020-01-28 17:07:38
Author: Ben Chuanlong Du
Slug: docker-installation
Title: Install Docker
Category: Software
Tags: software, Docker, installation, Ubuntu, latest, docker-ce, install Docker

## Install Docker on Debian Series of Linux Distributions

You can install Docker on Debian series of Linux distributions
(Debian, Ubuntu, Linux Mint, etc.) 
using the following commands.

    :::bash
    sudo apt-get update
    sudo apt-get install docker.io

## Install the Latest Version of Docker on Debian Series of Linux Distributions

You can install the latest version of Docker CE 
on Debian Series of Linux distributions (Debian, Ubuntu, Linux Mint, etc.)
using the commands below.

    :::bash
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install docker-ce

By default,
the `docker` command requires `sudo` previlage to run
which is a little hassle since you have to type `sudo` every time and type your password for `sudo`.
It is suggested that you add yourself into the `docker` group
so that you can run the `docker` command without `sudo`.

    :::bash
    sudo gpasswd -a $(whoami) docker
    newgrp docker

The command `newgrp docker` make the group `docker` to take effect.
You can check that you are in the `docker` group by issuing the `id` command.
If for whatever reason the group `docker` does take effect,
logout and then login again to make the group `docker` in effect.

## Install Docker in Other Operating Systems

Please refer to the official doc 
[Docker Engine overview](https://docs.docker.com/install/)
on how to install Docker in other operating systems.
