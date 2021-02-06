UUID: c94b42b3-dd2c-4e35-9b2f-74dff7adaed9
Status: published
Date: 2017-07-27 12:16:56
Author: Ben Chuanlong Du
Slug: docker-images-for-remote-desktop
Title: Docker Images for Remote Desktop
Category: Software
Tags: software, docker, remote desktop, KDE, Ubuntu

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

### KDE Plasma

[kdeneon/plasma](https://hub.docker.com/r/kdeneon/plasma/)

### Ubuntu

For vnc, probably not a scaling problem but has to set resolution while starting the docker ...

1. [consol/ubuntu-xfce-vnc](https://store.docker.com/community/images/consol/ubuntu-xfce-vnc)

    works well, seems like a good choice
    ```bash
    docker run -it -p 5901:5901 -p 6901:6901 -e VNC_RESOLUTION=800x600 consol/ubuntu-xfce-vnc
    ```

2. [dorowu/ubuntu-desktop-lxqt-vnc](https://store.docker.com/community/images/dorowu/ubuntu-desktop-lxde-vnc)

    works, novnc in HTML doesn't scale very well
    password: ubuntu

3. [dorowu/ubuntu-desktop-lxde-vnc](https://store.docker.com/community/images/dorowu/ubuntu-desktop-lxde-vnc)

    works, novnc in HTML doesn't scale very well
    password: ubuntu

1. [ensky/ubuntu-nxserver-xfce](https://store.docker.com/community/images/ensky/ubuntu-nxserver-xfce)

    Works, free NX client is a little bit ugly
    had to create a new user, don't know the password

