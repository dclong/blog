Status: published
Date: 2019-06-21 23:37:16
Author: Ben Chuanlong Du
Slug: docker-images-for-zeppelin
Title: Docker Images for Zeppelin
Category: Software
Tags: software, Docker, Docker image, Zeppelin, big data, Spark 
Modified: 2019-06-21 23:37:16

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Official Zeppelin Docker Image

1. Pull the official Zeppelin Docker image. 

        docker pull apache/zeppelin

2. Launch the image in a container.

        docker run -d -p 8080:8080 \
            -v $PWD/logs:/logs \
            -v $PWD/notebook:/notebook \
            -e ZEPPELIN_LOG_DIR='/logs' \
            -e ZEPPELIN_NOTEBOOK_DIR='/notebook' \
            --name zeppelin \
            apache/zeppelin:0.7.2

    If you have trouble accessing localhost:8080 in the browser, Please clear browser cache.
