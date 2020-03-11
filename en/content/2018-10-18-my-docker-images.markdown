Status: published
Date: 2020-03-11 14:56:56
Author: Ben Chuanlong Du
Slug: my-docker-images
Title: My Docker Images
Category: Software
Tags: software, Docker, Docker image, Ubuntu, JupyterLab, Lubuntu, dclong

## Tips

1. The `dclong/jupyterlab` Docker image is well maintained (which is the base image of `dclong/jupyterhub`), 
    however, 
    many of the `dclong/jupyterlab-*` Docker images are not maintained any more.
    Please use the corresponding `dclong/jupyterhub-*`  Docker images instead.

2. There is an issue with the `dclong/xubuntu*` Docker images due to Xfce on Ubuntu 18.04.
    It is suggested that you use the corresponding `dclong/lubuntu*` Docker images instead,
    which are based on LXQt.

## Usage

### Install Docker

You must have Docker installed.
If you are on Ubuntu,
the just use the command below to install the community edition of Docker.

    :::bash
    sudo apt-get install docker.io

If you'd rather install the enterprise edition
or if you are on other platforms,
please refer to the offical Docker doc [Install Docker](https://docs.docker.com/install/).

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

### Start a Container

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
    docker run -d \
        --name jupyterhub-ds \
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
        dclong/jupyterhub-ds

The following command (only works on Linux) does the same as the above one 
except that it limits the use of CPU and memory.

    :::bash
    docker run -d \
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
        dclong/jupyterhub-ds

## Debug Docker Containers

You can change the option `docker run -d ...` to `docker run -it ...` 
to show logs of processes in the Docker container which helps debugging. 
If you have already started a Docker container using `docker run -d ...`,
you can use the command 
[docker logs](https://docs.docker.com/engine/reference/commandline/logs/)
to get the log of the container
(which contains logs of all processes in it).

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


## Use the JupyterHub Server

1. Open your browser and and visit `your_host_ip:8000`
    where `your_host_ip` is the URL/ip address of your server.

2. Login to the JupyterHub server 
    using your user name (by default your user name on the host machine)
    and password (by default your user name on the host machine). 

3. It is strongly suggested (for security reasons) that you change your password (using the command `passwd`)
    in the container.

4. Enjoy JupyterLab notebook!

## Add a New User to the JupyterHub Server

By default,
any user in the Docker container can visit the JupyterHub server.
So if you want to grant access to a new user,
just create an account for him in the Docker container.
You can of course use the well know commands `useradd`, `adduser`, etc. to achive it.
To make things easier for you,
there are some shell scripts in the directory `/scripts/` to create usres for you.

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

## Easy Install of Other Kernels

Install and configure PySpark for use with the Python kernel.

    :::bash
    xinstall spark -ic && xinstall pyspark -ic

Install the evcxr Rust kernel.

    :::bash
    xinstall evcxr -ic

Install the Almond Scala kernel.

    :::bash
    xinstall almond -ic

Install the ITypeScript kernel.

    :::bash
    xinstall its -ic

Many other software/tools can be easily install by xinstall.
Please refer to [dclong/xinstall](https://github.com/dclong/xinstall)
for more details.

## Use Spark in JupyterLab Notebook

### Spark - The BeakerX Scala Kernel

Currently [dclong/jupyterhub-ds](https://hub.docker.com/r/dclong/jupyterhub-ds/) uses the BeakerX Scala kernel.
Most of the Spark/Scala examples (unde the tag [Spark](http://www.legendu.net/misc/tag/spark.html)) 
on this blog are based on the BeakerX Scala kernel.

1. Open a JupyterLab notebook with the BeakerX Scala kernel from the launcher.

2. Download Spark (say, 2.3.1) dependencies. 

        :::scala
        %%classpath add mvn
        org.apache.spark spark-core_2.11 2.3.1
        org.apache.spark spark-sql_2.11 2.3.1

3. Create a SparkSession object.

        :::scala
        import org.apache.spark.sql.SparkSession
        import org.apache.spark.sql.functions._

        val spark = SparkSession.builder()
            .master("local[2]")
            .appName("Spark Example")
            .config("spark.some.config.option", "some-value")
            .getOrCreate()

        import spark.implicits._

4. Use Spark as usual. 

        :::scala
        val df = Range(0, 10).toDF
        df.show

### Spark - The Almond Scala Kernel

Currently [dclong/jupyterhub-almond](https://hub.docker.com/r/dclong/jupyterhub-almond/) uses the Almond Scala kernel.

1. Open a JupyterLab notebook with the Almond Scala kernel from the launcher.

2. Download Spark (say, 2.3.1) dependencies. 

        :::scala
        interp.load.ivy("org.apache.spark" % "spark-core_2.11" % "2.3.1")

3. Create a SparkSession object.

        :::scala
        import org.apache.spark.sql.SparkSession
        import org.apache.spark.sql.functions._

        val spark = SparkSession.builder()
            .master("local[2]")
            .appName("Spark Example")
            .config("spark.some.config.option", "some-value")
            .getOrCreate()

        import spark.implicits._

4. Use Spark as usual. 

        :::scala
        val df = Range(0, 10).toDF
        df.show

Please refer to 
[almond-sh/examples](https://github.com/almond-sh/examples/blob/master/notebooks/spark.ipynb)
for more details.

### Spark - Apache Toree

Currently [dclong/jupyterhub-toree](https://hub.docker.com/r/dclong/jupyterhub-toree/) uses the Apache Toree Scala kernel.

The Docker image 
[dclong/jupyterhub-toree](https://github.com/dclong/docker-jupyterhub-toree)
has Spark and Apache Toree installed and configured.
Since Spark is already installed in it, 
you don't need to download and install Spark by yourself.
By default, 
a Spark Session object named `spark` is created automatically just like spark-shell.
So, you can use Spark/Scala out-of-box in a JupyterLab notebook with the `Scala - Apache Toree` kernel.

1. Open a JupyterLab notebook with the `Scala - Apache Toree` kernel from the launcher.

2. Use Spark as usual.
        
        :::scala
        val df = Range(0, 10).toDF
        df.show

### PySpark - pyspark and findspark

The Docker image
[dclong/jupyterhub-toree](https://github.com/dclong/docker-jupyterhub-toree)
supports PySpark 2.4 out-of-box.
To use PySpark in a container of the Docker image
[dclong/jupyterhub-ds](https://github.com/dclong/docker-jupyterhub-ds)
you need to install Spark and the Python package `pyspark` first,
which can be achieved using the following command.

    :::bash
    xinstall --sudo spark -ic && xinstall pyspark -ic

Follow the steps below to use PySpark after it is installed.

1. Open a JupyterLab notebook with the Python kernel from the launcher.

2. Find and initialize PySpark.

        :::python
        import findspark
        # A symbolic link of the Spark Home is made to /opt/spark for convenience
        findspark.init('/opt/spark')

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

- [dclong/deepin_b](https://hub.docker.com/r/dclong/deepin_b/)  

    - [dclong/deepin_cn](https://hub.docker.com/r/dclong/deepin_cn/)  

        - [dclong/deepin](https://hub.docker.com/r/dclong/deepin/)  

- [dclong/ubuntu_b](https://hub.docker.com/r/dclong/ubuntu_b/)  

    > OS: Ubuntu 19.04  
    > Time Zone: US Pacific Time  
    > Desktop Environment: None  
    > Remote Desktop: None  

    - [dclong/samba](https://hub.docker.com/r/dclong/samba/)  

    - [dclong/nfs](https://hub.docker.com/r/dclong/nfs/)  

    - [dclong/nodejs](https://hub.docker.com/r/dclong/nodejs/)  

        - [dclong/typescript](https://hub.docker.com/r/dclong/typescript/)  

    - [dclong/jdk](https://hub.docker.com/r/dclong/jdk/)  

        - [dclong/scala](https://hub.docker.com/r/dclong/scala/)  

            - [dclong/hadoop](https://hub.docker.com/r/dclong/hadoop/)  

              - [dclong/hive](https://hub.docker.com/r/dclong/hive/)  

                  - [dclong/spark](https://hub.docker.com/r/dclong/spark/)  

                  - [dclong/zeppelin](https://hub.docker.com/r/dclong/zeppelin/)  

        - [dclong/h2o](https://hub.docker.com/r/dclong/h2o/)  

    - [dclong/r-base](https://hub.docker.com/r/dclong/r-base/)  

        - [dclong/r-pop](https://hub.docker.com/r/dclong/r-pop/)  

            - [dclong/rstudio](https://hub.docker.com/r/dclong/rstudio/)  

    - [dclong/qt5](https://hub.docker.com/r/dclong/qt5/)  

    - [dclong/conda](https://hub.docker.com/r/dclong/conda/)  

        - [dclong/conda-build](https://hub.docker.com/r/dclong/conda-build/)  

        - [dclong/conda-yarn](https://hub.docker.com/r/dclong/conda-yarn/)  

    - [dclong/tdodbc](https://hub.docker.com/r/dclong/tdodbc/)  

        - [dclong/tdodbc-py](https://hub.docker.com/r/dclong/tdodbc-py/)  

    - [dclong/python](https://hub.docker.com/r/dclong/python/)  

        > Python 3.7  

        - [dclong/python-jdk](https://hub.docker.com/r/dclong/python-jdk/)  

        - [dclong/python-nodejs](https://hub.docker.com/r/dclong/python-nodejs/)  

        - [dclong/mlflow](https://hub.docker.com/r/dclong/mlflow/)  

        - [dclong/flask](https://hub.docker.com/r/dclong/flask/)  

        - [dclong/dryscrape](https://hub.docker.com/r/dclong/dryscrape/)  

        - [dclong/cuda](https://hub.docker.com/r/dclong/cuda/)  

            - [dclong/cuda_b](https://hub.docker.com/r/dclong/cuda_b/)  

                - [dclong/cuda-pytorch](https://hub.docker.com/r/dclong/cuda-pytorch/)  

                - [dclong/cuda-autogluon](https://hub.docker.com/r/dclong/cuda-autogluon/)  

                    - [dclong/cuda-ai](https://hub.docker.com/r/dclong/cuda-ai/)  

        - [dclong/jupyter](https://hub.docker.com/r/dclong/jupyter/)  

             > Jupyter Notebook: 6.0.2  

            - [dclong/jupyter-nodejs](https://hub.docker.com/r/dclong/jupyter-nodejs/)  

                 > NodeJS: LTS

                - [dclong/jupyter-jdk](https://hub.docker.com/r/dclong/jupyter-jdk/)  

                    - [dclong/vscode-server](https://hub.docker.com/r/dclong/vscode-server/)  

                - [dclong/jupyterlab](https://hub.docker.com/r/dclong/jupyterlab)  

                     > JupyterLab: 1.2.3

                    - [dclong/jupyterhub](https://hub.docker.com/r/dclong/jupyterhub/)  

                         > JupyterHub: 1.0.0  

                        - [dclong/jupyterhub-ts](https://hub.docker.com/r/dclong/jupyterhub-ts/)  

                        - [dclong/jupyterhub-julia](https://hub.docker.com/r/dclong/jupyterhub-julia/)  

                        - [dclong/jupyterhub-cuda](https://hub.docker.com/r/dclong/jupyterhub-cuda/)  

                            - [dclong/jupyterhub-cuda_b](https://hub.docker.com/r/dclong/jupyterhub-cuda_b/)  

                                - [dclong/jupyterhub-pytorch](https://hub.docker.com/r/dclong/jupyterhub-pytorch/)  

                                - [dclong/jupyterhub-autogluon](https://hub.docker.com/r/dclong/jupyterhub-autogluon/)  

                                    - [dclong/jupyterhub-ai](https://hub.docker.com/r/dclong/jupyterhub-ai/)  

                        - [dclong/jupyterhub-jdk](https://hub.docker.com/r/dclong/jupyterhub-jdk/)  

                            > OpenJDK 8  
                            > Maven: 3.6.0  

                            - [dclong/jupyterhub-py](https://hub.docker.com/r/dclong/jupyterhub-py/)  

                                > numpy scipy pandas dask  
                                > torch torchvision tensorflow keras h2o  
                                > gensim nltk  
                                > scikit-learn xgboost  
                                > matplotlib seaborn bokeh plotly  
                                > tabulate  
                                > JayDeBeApi pymysql pymongo sqlalchemy  
                                > pysocks requests[socks] Scrapy beautifulsoup4 wget  ansible  

                                - [dclong/jupyterhub-beakerx](https://hub.docker.com/r/dclong/jupyterhub-beakerx/)  

                                    > SQL (based on JDBC) via BeakerX 1.4.1  
                                    > Scala 2.11.12 via BeakerX 1.4.1  
                                    > Java 8, Clojure, Groovy, Kotlin via BeakerX 1.4.1  

                                    - [dclong/jupyterhub-ds](https://hub.docker.com/r/dclong/jupyterhub-ds/)  

                                        - [dclong/gitpod](https://hub.docker.com/r/dclong/gitpod/)

    - [dclong/ubuntu_cn](https://hub.docker.com/r/dclong/ubuntu_cn/)  

        - [dclong/lubuntu](https://hub.docker.com/r/dclong/lubuntu/)  

            - [dclong/lubuntu-qt5](https://hub.docker.com/r/dclong/lubuntu-qt5/)  

                - [dclong/lubuntu-pyside2](https://hub.docker.com/r/dclong/lubuntu-pyside2/)  

            - [dclong/lubuntu-nodejs](https://hub.docker.com/r/dclong/lubuntu-nodejs/)  

            - [dclong/lubuntu-jdk](https://hub.docker.com/r/dclong/lubuntu-jdk/)  

                - [dclong/lubuntu-scala](https://hub.docker.com/r/dclong/lubuntu-scala/)  
                    - [dclong/lubuntu-intellij](https://hub.docker.com/r/dclong/lubuntu-intellij/)  

        - [dclong/xubuntu](https://hub.docker.com/r/dclong/xubuntu/)  
            - [dclong/xubuntu-nodejs](https://hub.docker.com/r/dclong/xubuntu-nodejs/)  
            - [dclong/xubuntu-jdk](https://hub.docker.com/r/dclong/xubuntu-jdk/)  
                - [dclong/xubuntu-scala](https://hub.docker.com/r/dclong/xubuntu-scala/)  
                    - [dclong/xubuntu-intellij](https://hub.docker.com/r/dclong/xubuntu-intellij/)  

## Build my Docker Images

Run the Python code below to build my Docker images.
The python package [dsutil](https://github.com/dclong/dsutil) is required.

    :::python
    #!/usr/bin/env python3
    from dsutil import docker

    docker.remove()
    docker.remove_images(tag="^2[0-9]{5}")
    tag_build = "next"
    no_cache = False
    docker.build_images("dclong/conda-build", no_cache=no_cache, tag_build=tag_build)
    docker.build_images("dclong/vscode-server", tag_build=tag_build)
    docker.build_images("dclong/gitpod", tag_build=tag_build)
    docker.build_images("dclong/jupyterhub-pytorch", tag_build=tag_build)
    docker.build_images("dclong/jupyterhub-ai", tag_build=tag_build)
    docker.remove()

## Known Issues 

1. The subprocess managment issue.
    This is not an issue at all in most use cases.
    This Docker image launch service using a shell script
    so there won't be orphan subprocesses
    when the process of the Docker container is killed.
    However, launching by shell script is not the best way for managing processes.
    Please refer to [A Simple Init System](https://blog.phusion.nl/2015/01/20/docker-and-the-pid-1-zombie-reaping-problem/#asimpleinitsystem)
    for more details.
    I might switch to the [Supervisor](https://github.com/Supervisor/supervisor) for process management
    or use the base image of [pushion/baseimage](https://hub.docker.com/r/phusion/baseimage/) in future.
