Status: published
Date: 2025-11-23 11:04:17
Modified: 2025-11-23 11:04:17
Author: Benjamin Du
Slug: common-issues-and-solutions-for-github-actions
Title: Common Issues and Solutions for GitHub Actions
Category: Computer Science
Tags: Computer Science, programming, GitHub Actions, CICD, development, issues, solutions

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Error: No space left.
Symptom: A GitHub Actions workflow fails with the error message "No space left".

Possible Solutions:
1. An Azure VM mounts an (ephemeral) disk to `/mnt`
    which is big enough for most CICD pipelines.
    You can leverage `/mnt` to store outputs of your CICD pipelines when necessary.
    [legendu-net/docker_image_builder - config_docker.py](https://github.com/legendu-net/docker_image_builder/blob/dev/config_docker.py)
    is such an example which stores built Docker images into `/mnt/docker`.
    
2. Remove non needed tools.
    Please refer to 
    [apache/flink - free_disk_space.sh](https://github.com/apache/flink/blob/master/tools/azure-pipelines/free_disk_space.sh)
    and
    [legendu-net/docker-base - purge_cache.sh](https://github.com/legendu-net/docker-base/blob/dev/scripts/sys/purge_cache.sh)
    for examples.

## Error: The process '/usr/bin/git' failed with exit code 1

Symptom: A GitHub Actions workflow fail to checkout a branch of a repository 
and throws the following error message.

> Error: The process '/usr/bin/git' failed with exit code 1

Possible Causes and Solutions: It's possible that you use a branch name 
(e.g., used `main` while the repo does not have a `main` branch) which does not exist. 
If so, 
use the correct branch name might fix the issue.
