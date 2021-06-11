Status: published
Date: 2020-07-14 09:41:49
Author: Ben Chuanlong Du
Slug: docker-images-for-programming-languages
Title: Docker Images for Programming Languages
Category: Computer Science
Tags: programming, Docker, Python, Scala
Modified: 2020-07-14 09:41:49

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Python 

### [continuumio/miniconda3](https://hub.docker.com/r/continuumio/miniconda3)

- It is hard to figure out the version of Python from the version of the Docker image.

### [continuumio/anaconda3](https://hub.docker.com/r/continuumio/anaconda3/)

- It is hard to figure out the version of Python from the version of the Docker image.

### [Python](https://hub.docker.com/_/python)

- Different versions of Python with the Debian Linux OS in Docker image.
- Easy to figure out the version of Python from the version of the Docker image.
    It is perticularly good if you need a specific (especially old) version of Python. 

### [dclong/python](https://hub.docker.com/r/dclong/python)

- Python 3.8 with Ubuntu 20.04 in Docker.

- Extra useful Python packages 
    (e.g., [xinstall](https://github.com/dclong/xinstall),
    mypy, pylint, yapf, pytest and ipython)
    installed.

- Extra essentiall tools (SSH, Git, Wajig, sudo etc.) installed.

- Ready for development and serve as the ancester image for 
    [dclong/jupyterhub-ds](https://github.com/dclong/docker-jupyterhub-ds)


## Scala

http://www.slideshare.net/marcuslonnberg/ship-your-scala-code-often-and-easy-with-docker

http://blog.codacy.com/2015/07/16/dockerizing-scala/

https://velvia.github.io/Docker-Scala-Sbt/

https://github.com/stevenalexander/docker-scala-ide
