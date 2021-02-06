Status: published
Date: 2019-10-22 00:39:04
Author: Benjamin Du
Slug: tips-on-dockerswarm
Title: Tips on Dockerswarm
Category: Software
Tags: Software, Docker, Docker Swarm
https://zonca.github.io/2016/05/jupyterhub-docker-swarm.html

https://ender74.github.io/Sharing-Volumes-With-Docker-Swarm/

## Volume

    :::bash
    docker service create \
        --name nginx \
        --mount type=bind,source=`pwd`/static-site,target=/usr/share/nginx/html \
        -p 80:80 nginx
        https://boxboat.com/2016/08/12/mounting-volumes-docker-swarm-1-12/

https://stackoverflow.com/questions/42672171/volume-is-not-shared-between-nodes-of-docker-swarm

Volumes created in docker swarm via default driver are local to the node. So if you put both containers on the same host they will have a shared volume. But when you put your containers on different nodes, there will be a separate volume created on each node.

Now in order to achieve bind mounts/volumes across multiple nodes you have these options:

Use a cluster filesystem like glusterfs, ceph and ... across swarm nodes, then use bind mounts in your service defenition pointing to shared fs.


Switch to Kubernetes and take advantage of automated volume provisioning using multiple backends via Storage classes and claims.
http://storidge.com/blog/persistence-for-docker-swarm/

https://blog.octo.com/en/kubernetes-vs-swarm-volumes/

## GlusterFS

http://embaby.com/blog/using-glusterfs-docker-swarm-cluster/
