Status: published
Date: 2019-11-20 21:21:08
Author: Benjamin Du
Slug: user-in-docker
Title: User in Docker
Category: Software
Tags: Software, Docker, user, container
Modified: 2019-11-20 21:21:08

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## User switching in Docker

1. `USER some_user` in Dockerfile, some_user has to exists
2. `su` in Dockerfile or shell scripts
3. `docker run --user some_user`


@pedrolucasoliva
i am docker specialist i give you a little hint the --user flag

docker run --user $(id):$(id) -d -p 0.0.0.0:8000:8080 --name codeserver -v "/home/dev/codeserver/.local/share/code-server:/home/coder/.local/share/code-server" -v "/home/dev/projects:/home/coder/project" codercom/code-server:v2
the --user $(id):$(id) will switch the user id of the coder user to your user id and group :)
```

use --user root

https://medium.com/redbubble/running-a-docker-container-as-a-non-root-user-7d2e00f8ee15

https://stackoverflow.com/questions/41100333/difference-between-docker-run-user-and-group-add-parameters

```
USER
root (id = 0) is the default user within a container. The image developer can create additional users. Those users are accessible by name. When passing a numeric ID, the user does not have to exist in the container.

The developer can set a default user to run the first process with the Dockerfile USER instruction. When starting a container, the operator can override the USER instruction by passing the -u option.

-u="", --user="": Sets the username or UID used and optionally the groupname or GID for the specified command.

The followings examples are all valid:
--user=[ user | user:group | uid | uid:gid | user:gid | uid:group ]
Note: if you pass a numeric uid, it must be in the range of 0-2147483647.
```
https://jtreminio.com/blog/running-docker-containers-as-current-host-user/