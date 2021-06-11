Status: published
Date: 2016-12-10 09:32:40
Author: Ben Chuanlong Du
Slug: links-docker
Title: General Tips for Docker
Category: Software
Tags: software, Docker, tips, container, entrypoint
Modified: 2021-06-10 09:32:40

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Overwrite Entrypoint

[Difference between Docker ENTRYPOINT and Kubernetes container spec COMMAND?](https://stackoverflow.com/questions/44316361/difference-between-docker-entrypoint-and-kubernetes-container-spec-command)

Docker - Override or remove ENTRYPOINT from a base image
https://stackoverflow.com/questions/41207522/docker-override-or-remove-entrypoint-from-a-base-image

Overriding Docker ENTRYPOINT of a Base Image
https://dzone.com/articles/overriding-docker-entrypoint-of-a-base-image


How To Override Entrypoint Using Docker Run
https://phoenixnap.com/kb/docker-run-override-entrypoint

How to remove entrypoint from parent Image on Dockerfile
https://stackoverflow.com/questions/40122152/how-to-remove-entrypoint-from-parent-image-on-dockerfile/40122359

## Init Process

--init	
Run an init inside the container that forwards signals and reaps processes

https://docs.docker.com/engine/reference/commandline/run/

https://github.com/krallin/tini




## Links

[Private Docker Registry](https://docs.docker.com/registry/deploying/)

[Configure automated builds on Docker Hub](https://docs.docker.com/docker-hub/builds/)

[Configure automated builds with Bitbucket](https://docs.docker.com/docker-hub/bitbucket/)

https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/

https://coderwall.com/p/4g8znw/things-i-learned-while-writing-a-dockerfile

http://stackoverflow.com/questions/25311613/docker-mounting-volumes-on-host

http://stackoverflow.com/questions/26500270/understanding-user-file-ownership-in-docker-how-to-avoid-changing-permissions-o

https://chrisjean.com/fix-apt-get-update-the-following-signatures-couldnt-be-verified-because-the-public-key-is-not-available/

https://github.com/docker/docker/issues/22599

http://stackoverflow.com/questions/28056522/access-host-database-from-a-docker-container

https://docs.docker.com/engine/reference/commandline/tag/

https://docs.docker.com/engine/reference/commandline/push/

## Start Another Docker Container in a Docker Container

https://stackoverflow.com/questions/39468841/is-it-possible-to-start-a-stopped-container-from-another-container

### Communicate with Host

http://stackoverflow.com/questions/23439126/how-to-mount-host-directory-in-docker-container

http://stackoverflow.com/questions/22907231/copying-files-from-host-to-docker-container

http://stackoverflow.com/questions/23935141/how-to-copy-docker-images-from-one-host-to-another-without-via-repository

### UI Related

1. [Running GUI Apps with Docker](http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/)
2. <http://stackoverflow.com/questions/16296753/can-you-run-gui-apps-in-a-docker-container>
2. <https://github.com/kevana/ui-for-docker>
2. <https://www.eclipse.org/community/eclipse_newsletter/2015/june/article3.php>
2. <https://hub.docker.com/r/tiokksar/eclipse/~/dockerfile/>
2. <https://hub.docker.com/r/tiokksar/eclipse/~/dockerfile/>
2. <https://medium.com/google-cloud/my-ide-in-a-container-49d4f177de#.2mhkzmp8a>
2. <https://blog.jessfraz.com/post/docker-containers-on-the-desktop/>
2. <https://store.docker.com/community/images/consol/ubuntu-xfce-vnc>

### Misc

1. <https://getcarina.com/docs/troubleshooting/stop-nonresponsive-running-container/>
2. <https://medium.com/@saturnism>
3. <http://openhome.cc/Gossip/CodeData/DockerLayman/DockerLayman3.html>
4. <https://twitter.com/saturnism/status/645366585981538304>


1. [Docker Reference](https://docs.docker.com/engine/reference/builder/)

2. [Best practices for writing Dockerfiles](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)
