Status: published
Date: 2019-12-20 10:19:20
Author: Ben Chuanlong Du
Slug: docker-on-mac
Title: Docker on Mac
Category: Software
Tags: Software, Docker, Mac

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. It is suggested that you install the offical docker app on Mac
    instead of installing docker using MacPorts/Homebrew.
    Docker installed using MacPorts/Homebrew might have issues to start. 

2. By default, 
    Docker Desktop for Mac is set to use 2GB runtime memory, 
    allocated from the total available memory on your Mac.
    This might not be enough in some situations (e.g., when you run the BeakerX kernel in Jupyter/Lab notebook),
    and the issue becomes even more serious when you handle large data in Docker on Mac.
    You need to keep in mind of the limitation of memory that Docker can use when running on Mac.
    Avoid using Docker for handling large data on Mac if you can.
    Running Docker on Linux is a much better alternative.
    If you do have to stick with Docker on Mac,
    you can increase the memory and swap that Docker can use in advanced settings of Docker.
    ![Docker Advanced Settings](https://user-images.githubusercontent.com/824507/71281147-0b0ce780-2312-11ea-87cd-349ab77d5479.png)

3. Default file location for user settings is
    `~/Library/Containers/com.docker.docker/Data/database/com.docker.driver.amd64-linux/etc/docker/daemon.json`
    However,
    you shouldn't edit it directly. 
    Instead, 
    You should go to the whale icon in the taskbar > Preferences > Daemon > Advanced.


## Advanced Settings

CPUs: By default, 
Docker Desktop for Mac is set to use half the number of processors available on the host machine. 
To increase processing power, set this to a higher number; to decrease, lower the number.

Memory: By default, 
Docker Desktop for Mac is set to use 2 GB runtime memory, 
allocated from the total available memory on your Mac. 
To increase RAM, set this to a higher number; to decrease it, lower the number.

Swap: Configure swap file size as needed. The default is 1 GB.

## References

https://docs.docker.com/docker-for-mac/

https://docs.docker.com/compose/completion/

