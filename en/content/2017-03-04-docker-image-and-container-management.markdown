Status: published
Date: 2020-04-06 14:53:34
Author: Ben Chuanlong Du
Slug: docker-image-and-container-management
Title: Manage Docker Images and Containers 
Category: Software
Tags: software, Docker, Docker image, container, management, remove

It is suggested that you use [osquery](https://osquery.io/)
to query Docker images, containers, etc.

## Remove Containers

Note that running containers will NOT be removed by default.
This is what users want generally speaking. 
You can use the option `-f` to force removing running containers,
but use it with caution and at your own risk.

1. Remove all existing containers (not images).

        docker rm $(docker ps -aq)
        # or you can use pipe
        docker ps -aq | xargs docker rm
        # or you can osquery
        osqueryi "select id from docker_containers" --list --header=false | xargs docker rm

2. Remove exited containers.

        docker ps -aqf status=exited | xargs docker rm
        osqueryi "select id from docker_containers where state=exited" --list --header=false | xargs docker rm


## Remove Images

Note that images required by running containers will NOT be removed by default.
This is what users want generally speaking. 
You can use the option `-f` to force removing images,
but use it with caution and at your own risk.

1. Remove images without names (with the help of `awk`).

```bash
docker images | awk '{ if ($1 == "<none>") print $3 }' | xargs docker rmi
```


2. Remove images without versions (with the help of `awk`).

    ```bash
    docker images | awk '{ if ($2 == "<none>") print $3 }' | xargs docker rmi
    ```


3. Remove images without names or versions (with the help of `awk`).

        docker images | awk '{ if ($1 == "<none>" || $2 == "<none>") print $3 }' | xargs docker rmi

4. Remove images without names or versions (with the help of `osquery`).

        osqueryi "select id from docker_images where tags = ''" --list --header=false | xargs docker rmi

5. Remove all images belong to the eclipse organization with the help of `sed` and `q`. 

        docker images sed 's/ \+/\t/g' q -tH "select [image id] from - where repository like 'eclipse/%'" xargs docker rmi 

6. Remove all images belong to the eclipse organization with the help of `osquery`. 

        osqueryi "select id from docker_images where tags like 'eclipse/%'" --list --header=false | xargs docker rmi

7. You can force removing an image with the `--force` option.

        docker rmi ubuntu --force

8. If you have multiple tags on the same docker image, 
    you cannot remove the docker image by image id (without using `--force`.)
    One way (without using `--force`) is to specify the tag name to remove.

## Get Container ID Inside Container

You can get the container ID inside the docker container 
by running the following command.

    cat /proc/self/cgroup | grep -o  -e "docker-.*.scope" | head -n 1 | sed "s/docker-\(.*\).scope/\\1/"

Or another simpler way is to run

    echo $HOSTNAME

But it will not work in the following two cases. 

1. if hostname is explicitly specified with `--hostname` flag. 

2. when using `--net=host` mode.


## Import/Export Docker Container/Images

[Moving Docker Containers and Images Around](https://blog.giantswarm.io/moving-docker-container-images-around/)

1. Save a docker image to a tar.gz file.

        docker save image | gzip > image.tar.gz


2. Load a docker image from tar file.

        docker load < image.tar


## Kill a Process in a Container

```sh
docker exec container_name kill process_name
```
## Volume

1. ALWAYS create a directory in the Docker container first
    before you mount a volume into it.
    If the directory (to mount into) in the Docker container does not exists,
    it will be created automatically by the root user
    (unless you specified a different user to run the Docker container).
    The newly created directory is owned by the root,
    which might not be as expected.

2. AVOID mounting a volume into your home directory in the Docker container.

    - You might screw up the permission of your home directory in the Docker container.

    - If you mount your home on the host into your home in the Docker container,
        you might accidentally overwrite things in your home directory on the host.

    It is recommend that you always mount a volume to `/some_dir` and then link to home if needed.

3. When you mount a volume from the host to a Docker container,
    make sure that you have the right permissions to the directory on the host,
    o.w., you might run into various issues (such as the Docker container fails to start).

4. You following instructions in 
        [this discussion](https://stackoverflow.com/questions/30642844/how-to-list-docker-mounted-volumes-from-within-the-container)
    to list mounted volumens.
    Another way is to use [osquery](https://osquery.io/).

## Permission

1. It is suggested that you have your user name added into the `docker` group
    so that you can run Docker commands without using `sudo`.

2. Inside a Docker container,
    files created belong to the user in the Docker container.
    If the files are created in a mounted host directory,
    then on the host these files belong to the user with the same user ID.

## Port

1. Do NOT forget to forward ports from the host to the Docker containers
    while using docker containers.
    For example,
    if you run a Flask application in a Docker,
    you have to forward a port on the host to the port 5000 in the Docker container.
    If you run multiple services in a Docker container (not recommended),
    you have to forward all needed ports into the Docker container.

## Sharing Files

Copying file between a docker container and the host.
```Bash
docker cp foo.txt mycontainer:/foo.txt
docker cp mycontainer:/foo.txt foo.txt
```

## Misc

1. By default log in a Docker container is redirected to the standard output.
    However,
    you won't be able to see the log if you start the Docker container as a deamon (using the `-d` option).
    For debugging purposes,
    it is suggested that you use the `-it` options instead the `-d` option.
    A more general and robust way is of course to redirect log of applications to a file.

1. Multiple running instances of the same Docker image
    do not interact with each other.
    The are running isolated.

2. Amazon AWS is blocked in China (currently).
    Do NOT run Docker services on Amazon if your users are in the mainland of China.

## Issues & Solutions

### Issue/Error 1

> docker: Error response from daemon: Get https://registry-1.docker.io/v2/dclong/jupyterlab-rstudio/manifests/latest: dial tcp 50.17.62.194:443: getsockopt: connection refused

First retry starting the Docker container.
If it still does not work
then restart the Docker daemon using the command below will resolve the issue.

        service docker restart

## Issue/Error 2

> Jupyter notebook connection failed

Due to proxy!!! Connect without proxy works!!!

https://stackoverflow.com/questions/31280465/ipython-notebook-connection-failed-issue

## Issue/Error 3

> Docker Error: Returned a Non-zero Code: 137

This issue is due to out of memory error.
To fix it,
you can either add more RAM or add more swap memory.

https://samwize.com/2016/05/19/docker-error-returned-a-non-zero-code-137/
