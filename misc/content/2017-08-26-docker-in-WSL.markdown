Status: published
Date: 2020-07-10 09:05:45
Author: Ben Chuanlong Du
Slug: docker-in-WSL
Title: Docker in WSL
Category: Software
Tags: software, Docker, WSL, Windows, Bash, BashOnWindows, Bash on Windows

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Docker can be installed in WSL starting from the Win 10 Creator update,
    however, 
    there are still all kinds of issues running Docker in WSL.

2. The most important part is dockerd will only run on an elevated console (run as Admin) 
    and cgroup should be always mounted before running the docker daemon.


## Use Docker on Windows in WSL

### Install Docker on Windows

To install the Docker engine on Windows, 
just go to docker.com and download the appropriate distribution. 
Also, 
make sure hardware virtualization is enabled and Hyper-V is installed, 
lest the engine won’t start.

### Run Docker in WSL

With Windows 10 Creators Update*, 
accomplishing all of this has become a lot simpler, 
since it allows you to run Windows executables from Bash. 
Just add these two lines to your .bashrc and you are done!

    PATH="$HOME/bin:$HOME/.local/bin:$PATH"
    PATH="$PATH:/mnt/c/Program\ Files/Docker/Docker/resources/bin"

## Related Articles 

[Running Docker containers on Bash on Windows](https://blog.jayway.com/2017/04/19/running-docker-on-bash-on-windows/)

## References

https://towardsdatascience.com/dual-boot-is-dead-windows-and-linux-are-now-one-27555902a128