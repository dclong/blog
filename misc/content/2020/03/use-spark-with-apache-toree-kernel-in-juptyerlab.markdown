Status: published
Date: 2020-03-23 17:47:21
Author: Benjamin Du
Slug: use-spark-with-apache-toree-kernel-in-juptyerlab
Title: Use Spark With Apache Toree Kernel in Juptyerlab
Category: Computer Science
Tags: Computer Science, Spark, Scala, Apache Toree, JupyterLab

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


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
