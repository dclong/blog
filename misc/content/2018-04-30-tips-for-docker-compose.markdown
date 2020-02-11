Status: published
Date: 2020-02-11 15:32:01
Author: Ben Chuanlong Du
Slug: tips-for-docker-compose
Title: Tips for Docker Compose
Category: Software
Tags: software, Docker Compose, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


wajig install docker-compose

brew install docker-compose

docker-compose sounds really interesting to me ...

https://github.com/docker/compose

https://github.com/jupyter-incutbator/dashboards_setup/tree/master/docker_deploy

```
version: '3'
services:
  jupyterhub-ds:
    image: "dclong/jupyterhub-ds"
    ports:
      - "8000:8000"
    environment:
      - DOCKER_USER=dclong
      - DOCKER_USER_ID=1000
      - DOCKER_PASSWORD=dclong
      - DOCKER_GROUP_ID=1000
      - DOCKER_ADMIN_USER=dclong
    entrypoint: /scripts/sys/init.sh
```

## Shell Commands

Shell commands cannot be used in a Docker-Compose file or a `env` file directly,
which is a big limitation of Docker-Compose.

https://github.com/docker/compose/issues/4081

## Environment Variables

https://docs.docker.com/compose/environment-variables/

## NFS

https://forums.docker.com/t/docker-swarm-nfs-mount/39007

https://stackoverflow.com/questions/45282608/how-to-directly-mount-nfs-share-volume-in-container-using-docker-compose-v3

## References

https://docs.docker.com/compose/install/

[Using Docker-Compose, how to execute multiple commands](https://stackoverflow.com/questions/30063907/using-docker-compose-how-to-execute-multiple-commands)
