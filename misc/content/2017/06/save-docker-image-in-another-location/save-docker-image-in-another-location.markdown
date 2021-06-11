Status: published
Date: 2020-01-28 19:41:40
Author: Ben Chuanlong Du
Slug: save-docker-image-in-another-location
Title: Save Docker Image in Another Location
Category: Software
Tags: software, Docker, location
Modified: 2020-01-28 19:41:40

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Docker images are saved in `/var/lib/docker`. 
You can link the directory to another place to save images elsewhere.
Another way is to change the configuration file of Docker.
For example, 
you can add the following into `/etc/default/docker` 
to save docker images into `/mnt` (instead of the default location).
```
DOCKER_OPTS="-dns 8.8.8.8 -dns 8.8.4.4 -g /mnt"
```

1. symbolic link

2. bind mount (check 
    [Specifying a default Docker storage directory by using bind mount](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/installing/docker_dir.html)
    for more details)

3. Add the options into the file `/etc/docker/daemon.json`.

        :::json
        {
            "data-root": "/new/data/root/path"
        }

Restart Docker after whichever approach you take.

    :::bash
    sudo systemctl restart docker



## References

https://forums.docker.com/t/how-do-i-change-the-docker-image-installation-directory/1169

https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/installing/docker_dir.html

https://stackoverflow.com/questions/19234831/where-are-docker-images-stored-on-the-host-machine