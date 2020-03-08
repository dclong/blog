Status: published
Date: 2020-03-07 21:44:53
Author: Benjamin Du
Slug: docker-issues-and-solutions
Title: Docker Issues and Solutions
Category: Software
Tags: Software, Docker, issue, solution

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Docker fail to register layer  ... no such file or directory

1. Remove `/var/lib/docker/*`.

        :::bash
        sudo rm -rf /var/lib/docker/*

    If you have a non-standard Docker location configured,
    then rmeove that location instead.

2. Restart Docker.

        :::bash
        sudo service docker restart