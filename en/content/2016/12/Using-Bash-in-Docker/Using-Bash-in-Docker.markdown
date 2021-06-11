UUID: 74e54add-e64d-4e6d-897a-cd7bf33d9b50
Status: published
Date: 2016-12-14 13:54:14
Author: Ben Chuanlong Du
Slug: Using-Bash-in-Docker
Title: Using Bash in Docker
Category: Software
Tags: software, docker, bash, shell
Modified: 2017-01-14 13:54:14


If the docker container was started using `/bin/bash` 
(you can check using `docker ps`) command you can access it using `attach`. 
```bash
docker attach container_name_or_id
```
If the docker container was started but not with `/bin/bash`,
you have to create a bash instance inside the container using `exec`.
```bash
docker exec -it container_name_or_id /bin/bash 
```
Notice that `attach` does not create a new instance of bash 
but use the already created one in the corresponding docker container.
However, 
both `exec` and `run` create new bash instances.

## Examples
```
docker exec -it -u dclong jupyterlab-py jupyter nbconvert --to html --execute --ExecutePreprocessor.timeout=600 /workdir/spend.ipynb 
```