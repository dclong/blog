Status: published
Date: 2018-10-18 09:10:17
Author: Ben Chuanlong Du
Slug: my-docker-images
Title: My Docker Images
Category: Software
Tags: software, Docker, Docker image, Ubuntu, JupyterLab, Lubuntu, dclong
Modified: 2025-05-27 12:02:53


<h2 id="recommended-docker-images">Recommended Docker Images and Tags</h2>

Most of my Docker images have different variants 
(corresponding to tags `latest`, `next`, etc) 
for different use cases.
And each tag might have histocial versions 
with the pattern `mmddhh` 
(`mm`, `dd` and `hh` stand for the month, day and hour) 
for fallback if a tag is broken.
Please refer to the following tag table for more details.

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"> Tag </th>
    <th class="tg-0pky"> Base Image OS </th>
    <th class="tg-0lax"> Comment </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"> latest </td>
    <td class="tg-0lax"> 
        Ubuntu LTS (or newer if necessary and well tested) 
    </td>
    <td class="tg-0lax"> 
        The most recent stable version of the Docker image. 
        <span style="color:green">
            The latest tag is what most users should use.
        </span>
        <br>
        It cares more about user friendliness than Docker image size, load speed and even security.
    </td>
  </tr>
  <tr>
    <td class="tg-0lax"> next </td>
    <td class="tg-0lax"> 
        Ubuntu LTS (or newer if necessary and well tested) 
    </td>
    <td class="tg-0lax">
        The most recent testing version of the Docker image.
        <br>
        New features/tools will be added into the next tag 
        before entering other tags.
    </td>
  </tr>
  <tr>
    <td class="tg-0lax"> 23.04 </td>
    <td class="tg-0lax"> 
        Ubuntu 23.04
    </td>
    <td class="tg-0lax">
        For any of the following situations: <br>
        1. a specific Ubuntu/kernel version is required <br>
        2. trying out newer Ubuntu versions than LTS
    </td>
  </tr>
  <tr>
    <td class="tg-0lax"> mmddhh </td>
    <td class="tg-0lax"> 
        Histoical versions corresponding to the latest tag.
    </td>
    <td class="tg-0lax"> 
        Fallback tags (for latest) if the latest tag is broken.
    </td>
  </tr>
  <tr>
    <td class="tg-0lax"> next_mmddhh </td>
    <td class="tg-0lax"> 
        Histoical versions corresponding to the next tag.
    </td>
    <td class="tg-0lax"> 
        Fallback tags (for next) if the next tag is broken.
    </td>
  </tr>
</tbody>
</table>

<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"> Docker Image </th>
    <th class="tg-0pky"> Comment </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><a href="https://github.com/legendu-net/docker-vscode-server" target="_blank" rel="noopener noreferrer">dclong/vscode-server</a></td>
    <td class="tg-0lax">Cloud IDE <a href="https://github.com/coder/code-server" target="_blank" rel="noopener noreferrer">code-server</a> (based on VSCode)</td>
  </tr>
  <tr>
    <td class="tg-0lax"><a href="https://github.com/legendu-net/docker-jupyterhub-ds" target="_blank" rel="noopener noreferrer">dclong/jupyterhub-ds</a></td>
    <td class="tg-0lax">Traditional ML</td>
  </tr>
  <tr>
    <td class="tg-0lax"><a href="https://github.com/legendu-net/docker-jupyterhub-pytorch" target="_blank" rel="noopener noreferrer">dclong/jupyterhub-pytorch</a></td>
    <td class="tg-0lax">Deep Learning</td>
  </tr>
  <tr>
    <td class="tg-0lax"><a href="https://github.com/legendu-net/docker-python-portable" target="_blank" rel="noopener noreferrer">dclong/python-portable</a></td>
    <td class="tg-0lax">Build portable Python using <a href="https://github.com/indygreg/python-build-standalone" target="_blank" rel="noopener noreferrer">python-build-standalone</a></td>
  </tr>
  <tr>
    <td class="tg-0lax"><a href="https://github.com/legendu-net/docker-jupyterhub-sagemath" target="_blank" rel="noopener noreferrer">dclong/jupyterhub-sagemath</a></td>
    <td class="tg-0lax">Math / Calculus</td>
  </tr>
  <tr>
    <td class="tg-0lax">
        <a href="https://hub.docker.com/layers/dclong/jupyterhub-ds/blog_071520/images/sha256-f6f9f15d18a856786c37a370157e81c9e0acbc80050656858be9330c6213b5fe?context=repo" target="_blank" rel="noopener noreferrer">dclong/jupyterhub-ds:blog_071520</a>
    </td>
    <td class="tg-0lax">
        For publishing <a href="https://github.com/legendu-net/blog" target="_blank" rel="noopener noreferrer">legendu.net/blog</a>
        using CICD. 
    </td>
  </tr>
  <tr>
    <td class="tg-0lax"><a href="https://github.com/legendu-net/docker-gitpod" target="_blank" rel="noopener noreferrer">dclong/gitpod</a></td>
    <td class="tg-0lax">Editing other GitHub repos using GitPod</td>
  </tr>
  <tr>
    <td class="tg-0lax">
        <a href="https://github.com/legendu-net/docker-jupyterhub-kotlin" target="_blank" rel="noopener noreferrer">dclong/jupyterhub-kotlin</a> <br>
        <a href="https://github.com/legendu-net/docker-jupyterhub-ganymede" target="_blank" rel="noopener noreferrer">dclong/jupyterhub-ganymede</a>
    </td>
    <td class="tg-0lax">JVM languages</td>
  </tr>
  <tr>
    <td class="tg-0lax">
        <a href="https://github.com/legendu-net/docker-rustpython" target="_blank" rel="noopener noreferrer">dclong/rustpython</a>
    </td>
    <td class="tg-0lax">
        RustPython
    </td>
  </tr>
</tbody>
</table>

## Usage

### Install Docker

Please refer to
[Install Docker](http://www.legendu.net/en/blog/docker-installation/)
for instructions on how to install and configure Docker.

### Pull the Docker Image

Taking `dclong/jupyterhub-ds` as an example,
you can pull it using the command below.

    :::bash
    docker pull dclong/jupyterhub-ds

For people in mainland of China,
please refer to the post
[Speedup Docker Pulling and Pushing](http://www.legendu.net/en/blog/speedup-docker-pulling-and-pushing/)
on ways to speed up pushing/pulling of Docker images.
If you don't bother,
then just use the command below.

    :::bash
    docker pull registry.docker-cn.com/dclong/jupyterhub-ds

### Start a Container using `ldc`

The recommended way to start containers for Docker images `dclong/*`
is to use the `ldc` command which comes with 
[icon](https://github.com/legendu-net/icon)
.

### Start a Container Manually

Below are explanation of some environment variable passed by the option `-e` to the Docker command.
Keep the default if you don't know what are the best to use.
`DOCKER_PASSWORD` is probably the only one you want to and should change.

- `DOCKER_USER`: The user to be created (dynamically) in the Docker container.
    The shell command `id -un` gets the name of the current user (on the host),
    so the option `-e DOCKER_USER=$(id -un)` instructs the script `/scripts/sys/init.sh`
    to create a user in the Docker container whose name is the same as the current user on the host.
    <font color="red">
    WARNING: the shell script `/scripts/sys/init.sh` cannot create a user named `root` 
    as it already exists in the Docker container.
    If you start a Docker container using `root`, 
    make sure to pass a different user name to the envrionment variable `DOCKER_USER`,
    e.g., `-e DOCKER_USER=dclong`.
    </font>
    For more discussion, 
    please refer to [this issue](https://github.com/dclong/docker-jupyterhub/issues/3).
- `DOCKER_USER_ID`: The ID of the user to be created in the Docker container.
    The shell command `id -u` gets the user ID of the current user (on the host),
    so the option `-e DOCKER_USER_ID=$(id -u)` instructs the script `/scripts/sys/init.sh`
    to create a user in the Docker container whose user ID is the same as the user ID of the current user on the host.
    This means that the user in the Docker container is essentailly the current user on the host,
    which helps resolve file permissions between the Docker container and the host.
    This option is similar to the option `--user` of the command `docker run`,
    and you want to keep it unchanged, generally speaking.
- `DOCKER_PASSWORD`: The password of the user to be created in the Docker container.
    The shell command `id -un` get the name of the current user (on the host),
    so the option `-e DOCKER_PASSWORD=$(id -un)` instructs the script `/scripts/sys/init.sh`
    to create a user in the Docker container whose password is the name of the current user on the host.
    <font color="red">
    WARNING: You'd better change the default value for security reasons.
    Of course, users can always change it later using the command `passwd` inside the Docker container.
    </font>
- `DOCKER_GROUP_ID`: The group ID of the user to be created in the Docker container.
    The shell command `id -g` gets the group ID of the current user (on the host),
    so the option `-e DOCKER_GROUP_ID=$(id -g)` instructs the script `/scripts/sys/init.sh`
    to create a user in the Docker container whose group ID is the same as the group ID of the current user on the host.
    You want to keep this option unchanged, generally speaking.
- `DOCKER_ADMIN_USER`: This environment variable applies to Docker images `dclong/jupyterhub*` only. 
    It specifies the admin user of the JupyterHub server.
    It should be the same as `DOCKER_USER` generally speaking.
- `USER_MEM_LIMIT`: This environment variable applies to Docker images `dclong/jupyterhub*` only.
    It limits the memory that each user can use.
    Note: this optional is not in effect currently.

The root directory of JupyterLab/Jupyter notebooks is `/workdir` in the container.
You can mount directory on the host to it as you wish.
Below are illustration using the Docker image `dclong/jupyterhub-ds`.

The following command starts a container 
and mounts the current working directory and `/home` on the host machine 
to `/workdir` and `/home_host` in the container respectively.

    :::bash
    docker run -d --init \
        --platform linux/amd64 \
        --hostname jupyterhub-ds \
        --log-opt max-size=50m \
        -p 8000:8000 \
        -p 5006:5006 \
        -e DOCKER_USER=`id -un` \
        -e DOCKER_USER_ID=`id -u` \
        -e DOCKER_PASSWORD=`id -un` \
        -e DOCKER_GROUP_ID=`id -g` \
        -e DOCKER_ADMIN_USER=`id -un` \
        -v `pwd`:/workdir \
        -v `dirname $HOME`:/home_host \
        dclong/jupyterhub-ds /scripts/sys/init.sh

The following command (only works on Linux) does the same as the above one 
except that it limits the use of CPU and memory.

    :::bash
    docker run -d --init \
        --platform linux/amd64 \
        --name jupyterhub-ds \
        --log-opt max-size=50m \
        --memory=$(($(head -n 1 /proc/meminfo | awk '{print $2}') * 4 / 5))k \
        --cpus=$((`nproc` - 1)) \
        -p 8000:8000 \
        -p 5006:5006 \
        -e DOCKER_USER=`id -un` \
        -e DOCKER_USER_ID=`id -u` \
        -e DOCKER_PASSWORD=`id -un` \
        -e DOCKER_GROUP_ID=`id -g` \
        -e DOCKER_ADMIN_USER=`id -un` \
        -v `pwd`:/workdir \
        -v `dirname $HOME`:/home_host \
        dclong/jupyterhub-ds /scripts/sys/init.sh

## Add a New User Inside a Docker Container

You can of course use the well know commands `useradd`, `adduser`, etc. to achive it.
To make things easier for you,
there are some shell scripts in the directory `/scripts/sys/` to create usres for you.

- `/scripts/sys/create_user.sh`: Create a new user. It's the base script for creating users.
- `/scripts/sys/create_user_group.sh`: Create a new user with the given (existing) group.
- `/scripts/sys/create_user_nogroup.sh`: Create a new user with group name `nogroup`.
- `/scripts/sys/create_user_docker.sh`: Create a new user with group name `docker`.

You can use the option `-h` to print help doc for these commands.

    :::bash
    /scripts/sys/create_user_nogroup.sh -h
    Create a new user with the group name "nogroup".
    Syntax: create_user_nogroup user user_id [password]
    Arguments:
    user: user name
    user_id: user id
    password: Optional password of the user. If not provided, then the user name is used as the password.

Now suppose you want to create a new user `dclong` with user ID `2000` and group name `nogroup`,
you can use the following command.

    :::bash
    sudo /scripts/sys/create_user_nogroup.sh dclong 2000

Since we didn't specify a password for the user,
the default password (same as the user name) is used.


## Use the JupyterHub Server

1. Open your browser and and visit `your_host_ip:8000`
    where `your_host_ip` is the URL/ip address of your server.

2. Login to the JupyterHub server 
    using your user name (by default your user name on the host machine)
    and password (by default your user name on the host machine). 

3. It is strongly suggested (for security reasons) that you change your password (using the command `passwd`)
    in the container.

4. Enjoy JupyterLab notebook!

## Get Information of Running Jupyter/Lab Servers

If you are using the Jupyter/Lab server instead of JupyterHub,
you will be asked for a token at login.
If you have started the Docker container in interactive mode (option `-i` instead of `-d`),
the token for login is printed to the console.
Otherwise,
the tokens (and more information about the servers) can be found 
by running the following command outside the Docker container.

    :::bash
    docker exec jupyterlab /scripts/list_jupyter.py

The above command tries to be smart in the sense that 
it first figures out the user that started the JupyterLab server 
and then query running Jupyter/Lab servers of that user.
An equivalently but more specifically command 
(if the Docker is launched by the current user in the host)
is as below

    :::bash
    docker exec -u $(id -un) jupyterlab /scripts/sys/list_jupyter.py

If you are inside the Docker container, 
then run the following command to get the tokens (and more information about the servers).

    :::bash
    /scripts/list_jupyter.py

Or equivalently if the Jupyter/Lab server is launched by the current user,

    :::bash
    /scripts/sys/list_jupyter.py

To sum up, 
most of time you can rely on `/scripts/list_jupyter.py`
to find the tokens of the running Jupyter/Lab servers,
no matter you are root or the user that launches the Docker/JupyterLab server,
and no matter you are inside the Docker container or not.
Yet another way to get information of the running JupyterLab server 
is to check the log. 
Please refer to the section 
[Debug Docker Containers](http://www.legendu.net/en/blog/my-docker-images/#debug-docker-containers)
for more information.

## Add a New User for JupyterHub

By default,
any user in a Docker container of `dclong/jupyterhub-*` can visit the JupyterHub server.
So if you want to grant access to a new user,
just create an account for him in the Docker container.
Please refer to 
[Add a New User Inside a Docker Container](https://www.legendu.net/en/blog/my-docker-images/#add-a-new-user-inside-a-docker-container)
on how to create a new user inside a Docker container.

## Easy Install of Other Kernels

Install and configure PySpark for use with the Python kernel.

    :::bash
    icon spark -ic && icon pyspark -ic

Install the evcxr Rust kernel.

    :::bash
    icon evcxr -ic

Install the Almond Scala kernel.

    :::bash
    icon almond -ic

Install the ITypeScript kernel.

    :::bash
    icon its -ic

Many other software/tools can be easily install by 
[icon](https://github.com/legendu-net/icon)
.

## Debug Docker Containers

You can change the option `docker run -d ...` to `docker run -it ...` 
to show logs of processes in the Docker container which helps debugging. 
If you have already started a Docker container using `docker run -d ...`,
you can use the command 
[docker logs](https://docs.docker.com/engine/reference/commandline/logs/)
to get the log of the container
(which contains logs of all processes in it).

## Use Spark in JupyterLab Notebooks

- [Use Spark with the Almond Scala Kernel in JupyterLab](http://www.legendu.net/misc/blog/spark-almond-jupyterlab/)

- [Use Spark With the BeakerX Scala Kernel](http://www.legendu.net/misc/blog/use-spark-with-the-beakerx-scala-kernel/)

It is suggested that you use the Almond Scala kernel. 
I will gradually drop support of the BeakerX Scala kernel in my Docker images. 

## PySpark - pyspark and findspark

To use PySpark in a container of the Docker image
[dclong/jupyterhub-ds](https://github.com/dclong/docker-jupyterhub-ds)
you need to install Spark and the Python package `pyspark` first,
which can be achieved using the following command.

    :::bash
    icon spark -ic --loc /opt/  
    icon pyspark -ic

Follow the steps below to use PySpark after it is installed.

1. Open a JupyterLab notebook with the Python kernel from the launcher.

2. Find and initialize PySpark.

        :::python
        import findspark
        # A symbolic link of the Spark Home is made to /opt/spark for convenience
        findspark.init("/opt/spark")

        from pyspark.sql import SparkSession
        spark = SparkSession.builder.appName('PySpark Example').enableHiveSupport().getOrCreate()

3. Use Spark as usual.
    
        :::python
        df1 = spark.table("some_hive_table")
        df2 = spark.sql("select * from some_table")
        ...

## Remote Connection to Desktop in the Container

If you are running a Docker container with a desktop environment (`dclong/lubuntu*` or `dclong/xubuntu*`),
you can connect to the desktop environment in the Docker container using NoMachine.

1. Download the NoMachine client from <https://www.nomachine.com/download>.
2. Install the NoMachine client on your computer.
3. Create a new connection from your computer 
    to the desktop environment in the Docker image using the NX protocol and port 4000.
    You will be asked for a user name and password.
    By default,
    the user name used to start the Docker container on the host machine 
    is used as both the user name and password in the Docker container.

## List of Images and Detailed Information

- [dclong/base](https://hub.docker.com/r/dclong/base/)  

    > OS: Ubuntu LTS
    > Time Zone: US Pacific Time  
    > Desktop Environment: None  
    > Remote Desktop: None  

    - [dclong/samba](https://hub.docker.com/r/dclong/samba/)  

    - [dclong/nfs](https://hub.docker.com/r/dclong/nfs/)  

    - [dclong/nodejs](https://hub.docker.com/r/dclong/nodejs/)  

        - [dclong/typescript](https://hub.docker.com/r/dclong/typescript/)  

    - [dclong/jdk](https://hub.docker.com/r/dclong/jdk/)  

    - [dclong/python-portable](https://hub.docker.com/r/dclong/python-portable/)  

    - [dclong/python](https://hub.docker.com/r/dclong/python/)  

        > Python 3.12.x  

        - [dclong/python-jdk](https://hub.docker.com/r/dclong/python-jdk/)  

        - [dclong/mlflow](https://hub.docker.com/r/dclong/mlflow/)  

        - [dclong/dryscrape](https://hub.docker.com/r/dclong/dryscrape/)  

        - [dclong/python-nodejs](https://hub.docker.com/r/dclong/python-nodejs/)  

            - [dclong/jupyterlab](https://hub.docker.com/r/dclong/jupyterlab)  

                > JupyterLab: latest stable version

                - [dclong/jupyterhub](https://hub.docker.com/r/dclong/jupyterhub/)  

                    > JupyterHub: latest stable version

                    - [dclong/jupyterhub-ts](https://hub.docker.com/r/dclong/jupyterhub-ts/)  

                    - [dclong/jupyterhub-julia](https://hub.docker.com/r/dclong/jupyterhub-julia/)  

                        > Julia stable.

                    - [dclong/jupyterhub-cuda](https://hub.docker.com/r/dclong/jupyterhub-cuda/)  

                        - [dclong/jupyterhub-pytorch](https://hub.docker.com/r/dclong/jupyterhub-pytorch/)  

                    - [dclong/jupyterhub-jdk](https://hub.docker.com/r/dclong/jupyterhub-jdk/)  

                        > OpenJDK: 11  
                        > Maven: 3.6.x  

                        - [dclong/jupyterhub-more](https://hub.docker.com/r/dclong/jupyterhub-more/)  

                            > Go  
                            > Rust  
                            > JavaScript/ TypeScript  

                            - [dclong/vscode-server](https://hub.docker.com/r/dclong/vscode-server/)  

                                > [code-server](https://github.com/cdr/code-server): latest stable version

                            - [dclong/jupyterhub-ds](https://hub.docker.com/r/dclong/jupyterhub-ds/)  

                                > Python packages:  
                                >     - loguru pysnooper  
                                >     - numpy scipy pandas pyarrow  
                                >     - scikit-learn lightgbm  
                                >     - graphviz matplotlib bokeh holoviews[recommended] hvplot  
                                >     - tabulate  
                                >     - JPype1 sqlparse  
                                >     - requests[socks] lxml notifiers  
                                >     - dsutil  

                                - [dclong/gitpod](https://hub.docker.com/r/dclong/gitpod/)

    - [dclong/rust](https://hub.docker.com/r/dclong/rust/)  

        - [dclong/rustpython](https://hub.docker.com/r/dclong/rustpython/)  

    - [dclong/ubuntu_cn](https://hub.docker.com/r/dclong/ubuntu_cn/)  

        - [dclong/lubuntu](https://hub.docker.com/r/dclong/lubuntu/)  

            - [dclong/lubuntu-pyside2](https://hub.docker.com/r/dclong/lubuntu-pyside2/)  

            - [dclong/lubuntu-jdk](https://hub.docker.com/r/dclong/lubuntu-jdk/)  

## Build my Docker Images

My Docker images are auto built leveraging GitHub Actions workflow 
in the GitHub repository 
[docker_image_builder](https://github.com/dclong/docker_image_builder)
.

## Tips for Maintaining Docker Images (for My own Reference)

1. Do NOT update the `latest` tag 
    until you have fully tested the corresponding `next` tag.

2. Do NOT add new features or tools unless you really need them.

3. It generally a good idea to restrict versions of non-stable packages to be a specific (working) version 
    or a range of versions that is unlike to break.

4. If you REALLY have to update some Bash script a Docker image,
    do not update it in the GitHub repository directly 
    and build the Docker image to test whether it works.
    Instead,
    make a copy of the Bash script outside the Docker container, 
    update it, 
    and mount it into the container to test whether it work.
    If the updated Bash script work as you expected,
    then go ahead to update it in the GitHub repository.

## On Failure of GitHub Actions Workflow for Building Docker Images

1. If the Docker image buidling workflow fails due to network issues,
    it might not work to rerun failed pipelines in GitHub Actions
    (as the network issue is like due to probalematic network nodes
    and retrying failed pipelines sending jobs to the same nodes).
    In such situtions,
    it is better to trigger a new run of the workflow.

## Known Issues 

1. NeoVim fails to work 
    if a Docker image (with NeoVim installed) is run on **Mac with the M1 chip**
    even if you pass the option `--platform linux/amd64` to `docker run`.
    A possible fix is to manually uninstall NeoVim using the following command

        :::bash
        wajig purge neovim

    and then install Vim instead.
        
        :::bash
        wajig install vim

2. The command `wajig` fails to cache password 
    if a Docker image (with `wajig` installed) is run on **Mac with the M1 chip**
    even if you pass the option `--platform linux/amd64` to `docker run`.
    Fortunately, 
    this is not a big issue.

3. There is an issue with the `dclong/xubuntu*` Docker images due to Xfce on Ubuntu 18.04.
    It is suggested that you use the corresponding `dclong/lubuntu*` Docker images instead (which are based on LXQt)
    if a desktop environment is needed.

