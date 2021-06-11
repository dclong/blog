Status: published
Date: 2020-06-21 10:46:43
Author: Benjamin Du
Slug: shell-in-docker
Title: Shell in Docker
Category: Computer Science
Tags: Computer Science, Docker, shell, container, bash, RUN, ENV, environment variable
Modified: 2020-06-21 10:46:43

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Configure the Shell for the `RUN` Command

https://docs.docker.com/engine/reference/builder/#shell

## Configure the Default Shell for Terminals in Docker Containers

Just set the SHELL environment variable in the Docker image.

    :::bash
    ENV SHELL=/bin/bash