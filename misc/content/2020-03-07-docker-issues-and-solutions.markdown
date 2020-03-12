Status: published
Date: 2020-03-11 17:23:38
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

## Error saving credentials: error storing credentials in Ubuntu 18.04 LTS

Installing `gnupg2` and `pass` fixes the issue.

    :::bash
    wajig install gnupg2 pass

## Container exits with non-zero exit code 137

Please refer to
[The Non-Zero Exit Code 137 While Building a Docker Image](http://www.legendu.net/misc/blog/the-non-zero-exit-code-137-while-building-a-docker-image/)
for more details.

## References

https://github.com/docker/cli/issues/1136
