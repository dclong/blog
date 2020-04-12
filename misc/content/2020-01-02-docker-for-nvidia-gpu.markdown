Status: published
Date: 2020-04-12 13:51:20
Author: Benjamin Du
Slug: docker-for-nvidia-gpu
Title: Docker for Nvidia GPU
Category: Software
Tags: software, Docker, GPU, Nvidia

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. You can use the command `watch nvidia-smi` or `nvtop` to check the usage of GPU.
    `nvtop` is recommended 
    as it presents simple visualizations in addition to the current usage statistics.

        :::bash
        apt-get install nvtop

1. Install Nvidia `cuda-drivers` (or equivalent) on your Linux machine
    following instructions at 
    [CUDA Downloads](https://developer.nvidia.com/cuda-downloads).
    For example,
    you can install Nvidia CUDA Tookit 10.2 on Ubuntu 16.04 using the following commands.

        :::bash
        wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-ubuntu1604.pin
        sudo mv cuda-ubuntu1604.pin /etc/apt/preferences.d/cuda-repository-pin-600
        wget http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda-repo-ubuntu1604-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
        sudo dpkg -i cuda-repo-ubuntu1604-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
        sudo apt-key add /var/cuda-repo-10-2-local-10.2.89-440.33.01/7fa2af80.pub
        sudo apt-get update
        sudo apt-get -y install cuda-drivers

    Notice that instead of doing `sudo apt-get -y install cuda`,
    the last comamnd installs `cuda-drivers` only.
    This is because the CUDA toolkit (the package `cuda`) is not needed on your Linux host machine to run GPU-enabled Docker container
    starting from Docker 19.03.
    Of course, 
    it doesn't hurt to install the package `cuda` which has a whole lot other packages included.

2. Make sure that you have Docker 19.03+ installed on your Linux machine.

3. Install [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) on your Linux machine.
    For example,
    you can install it on Ubuntu 16.04/18.04
    and Debian Jessie/Stretch/Buster using the following comamnds.

        :::bash
        # Add the package repositories
        distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
        curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
        curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
        sudo apt-get update 
        sudo apt-get install -y nvidia-container-toolkit
        sudo systemctl restart docker
        # or depending on whether systemd is used to manage services
        sudo service docker restart

4. Test that GPU-enabled Docker containers can be run correctly.

        :::bash
        docker run --gpus all nvidia/cuda:10.2-base nvidia-smi

5. Extend official Nvidia Docker images to customize your own Docker images for GPU applications if needed.
    [nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04](https://hub.docker.com/layers/nvidia/cuda)
    is the best Docker image to extend, generally speaking.
    If you are using PyTorch (which has built-in CUDA and CUDNN),
    you can use [nvidia/cuda:10.1-base-ubuntu18.04](https://hub.docker.com/layers/nvidia/cuda) to reduce the size of your Docker image.
    [floydhub/dockerfiles](https://github.com/floydhub/dockerfiles)
    and
    [PyTorch Dockerfile](https://github.com/pytorch/pytorch/blob/master/docker/pytorch/Dockerfile)
    are good examples to refer to.
    If you want to use Python packages that do not have built-in CUDA and CUDNN support, 
    you might have to install the library `cuda-10-1` manually.

        :::bash
        sudo apt-get install cuda-10-1

6. Run GPU applications in Docker containers. 
    Please refer to 
    [nvidia-docker#usage](https://github.com/NVIDIA/nvidia-docker#usage) 
    for examples.

## Docker & Ubuntu Repositories

https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/

[nvidia/cuda:10.1-base-ubuntu18.04](https://gitlab.com/nvidia/container-images/cuda/blob/ubuntu18.04/10.1/base/Dockerfile)

[nvidia/cuda:10.1-cudnn-runtime-ubuntu18.04](https://gitlab.com/nvidia/container-images/cuda/blob/ubuntu18.04/10.1/runtime/Dockerfile)

[nvidia/cuda:10.1-cudnn-devel-ubuntu18.04](https://gitlab.com/nvidia/container-images/cuda/blob/ubuntu18.04/10.1/devel/Dockerfile)

## References

[Nvidia CUDA Linux Repositories](https://developer.download.nvidia.com/compute/cuda/repos/)

https://github.com/NVIDIA/nvidia-docker

https://github.com/NVIDIA/nvidia-docker#ubuntu-16041804-debian-jessiestretchbuster

[How Do I Install the Nvidia Driver](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-the-nvidia-driver).

https://www.linuxuprising.com/2019/06/2-tools-for-monitoring-nvidia-gpus-on.html

[How to measure GPU usage?](https://askubuntu.com/questions/387594/how-to-measure-gpu-usage)
