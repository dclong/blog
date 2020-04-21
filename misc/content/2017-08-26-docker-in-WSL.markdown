UUID: 045df550-e675-4a90-a9f2-0081631b165d
Status: published
Date: 2017-10-22 12:28:14
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

