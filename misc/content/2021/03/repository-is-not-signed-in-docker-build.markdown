Status: published
Date: 2021-03-26 14:44:52
Author: Benjamin Du
Slug: repository-is-not-signed-in-docker-build
Title: Docker Issue: Repository Is Not Signed in Docker Build
Category: Computer Science
Tags: Computer Science, software, container, Docker, repository, not siged, Ubuntu, apt, apt-get, build, Docker issue, issue

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Docker has a limit on maximum apt cache size on the host system.
The issue can be fixed by running the following command.

    :::bash
    docker image prune -f

## References

[Repository is not signed in docker build](https://stackoverflow.com/questions/59139453/repository-is-not-signed-in-docker-build)

[apt update throws signature error in Ubuntu 20.04 container on arm](https://askubuntu.com/questions/1263284/apt-update-throws-signature-error-in-ubuntu-20-04-container-on-arm)