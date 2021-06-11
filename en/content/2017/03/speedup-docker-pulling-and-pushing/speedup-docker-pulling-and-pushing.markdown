UUID: 709db98e-f0f6-456c-8fbd-248f28157e98
Status: published
Date: 2017-03-29 01:23:50
Author: Ben Chuanlong Du
Slug: speedup-docker-pulling-and-pushing
Title: Speedup Docker Pulling and Pushing
Category: Software
Tags: software, Docker, speedup, performance, DaoCloud
Modified: 2020-01-29 01:23:50

Pulling/pushing Docker images is extremely slow in China. 
There are a few ways to speed up docker pulling/pushing in China.

## Using the Official China Mirror 

Now the best way is to use the offical China mirror.
Please refer to 
[Docker 中国官方镜像加速](https://www.docker-cn.com/registry-mirror)
for details.
You have to restart the Docker daemon in order for the configuration to take effect.
If you are Ubuntu, 
then you can use the following command to restart the daemon.
```
sudo service docker restart
```

## Use the USTC Mirror

It seems to me that the official China mirror is gone.
However, 
there are still other good mirrors that you can use.
For example, 
you can usee the USTC mirror 
by adding the following option into the file `/etc/docker/daemon.json`.

    :::json
    {
        "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn/"]
    }


## Old Way 

One way to speedup Docker visiting is to use [DaoCloud](https://www.daocloud.io/) as a proxy.
All you have to do is simply adding the following line into the file `/etc/default/docker`.
```text
DOCKER_OPTS="--registry-mirror='http://a92c904a.m.daocloud.io'"
```
Please refer to <https://www.daocloud.io/mirror#accelerator-doc> for more details.
