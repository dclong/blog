Status: published
Date: 2020-12-19 11:39:17
Author: Benjamin Du
Slug: check-the-memory-limit-of-a-docker-container
Title: Check the Memory Limit of a Docker Container
Category: Computer Science
Tags: Computer Science, Docker, container, memroy limit, cgroup, cgget

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Docker 1.13+ 

Docker 1.13+ mounts the container's cgroup to /sys/fs/cgroup (this could change in future versions). 
You can check the limit using

    :::bash
    cat /sys/fs/cgroup/memory/memory.limit_in_bytes

## Older Version of Docker 

1. Install [cgroup-tools](https://github.com/mk-fg/cgroup-tools).

        :::bash
        wajig update
        wajig install cgroup-tools

2. Query the memory limit of the Docker container.

        :::bash
        cgget -n --values-only --variable memory.limit_in_bytes /

Notice that if a memory limit is not, 
both of the above methods will return a extremely large number.
So to be safe, 
you'd take the minimum value before the above result and the memory of the host
which can be get from the file `/proc/memoinfo`.

## References

https://stackoverflow.com/questions/42187085/check-mem-limit-within-a-docker-container