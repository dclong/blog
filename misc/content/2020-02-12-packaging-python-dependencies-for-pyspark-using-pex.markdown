Status: published
Date: 2020-06-07 14:44:03
Author: Benjamin Du
Slug: packaging-python-dependencies-for-pyspark-using-pex
Title: Packaging Python Dependencies for PySpark Using Pex
Category: Computer Science
Tags: programming, PySpark, Python, dependency, packaging, pex

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## General Tips on Using pex with PySpark

1. Please refer to [Tips on pex](http://www.legendu.net/misc/blog/tips-on-pex/)
    on tips about pex.

2. If the pex environment file inherits the contents of `sys.path`,
    it need not to have `pyspark` installed in it. 
    Otherwise (the default), 
    the pex environment file need to have `pyspark` installed in it. 

## The pex Root Directory

By default,
the pex root directory is `~/.pex`.
Some Spark cluster might not be configured correctly 
for the default pex root to work well.
For example,
some Spark clusters configure `$HOME` to be `/home`
which makes the default pex root directory to be `/home/.pex`.
This causes [permission issues](https://github.com/pantsbuild/pex/issues/359)
as users do not have previleges to create the directory on the master and executor containers.
If this happens, 
you have to set the environment variable `PEX_ROOT` 
to a writable location using thee option `--conf` 
when submitting your PySpark application.
Notice that you have to set the environment variable 
for both executors and the master 
if you submit your spark application in the `cluster` deploy mode (`--deploy-mode cluster`).
For more discussions please refer to
[this issue](https://github.com/pantsbuild/pex/issues/905)
.

    :::bash
    #!/bin/bash

    /apache/spark2.3/bin/spark-submit \
        --files "file:///apache/hive/conf/hive-site.xml,file:///apache/hadoop/etc/hadoop/ssl-client.xml,file:///apache/hadoop/etc/hadoop/hdfs-site.xml,file:///apache/hadoop/etc/hadoop/core-site.xml,file:///apache/hadoop/etc/hadoop/federation-mapping.xml" \
        --master yarn \
        --deploy-mode cluster \
        --queue YOUR_QUEUE \
        --num-executors 200 \
        --executor-memory 10G \
        --driver-memory 15G \
        --executor-cores 4 \
        --conf spark.yarn.maxAppAttempts=2 \
        --conf spark.dynamicAllocation.enabled=true \
        --conf spark.dynamicAllocation.maxExecutors=1000 \
        --conf spark.network.timeout=300s \
        --conf spark.executor.memoryOverhead=2G \
        --conf spark.pyspark.driver.python=./env.pex \
        --conf spark.pyspark.python=./env.pex \
        --conf spark.executorEnv.PEX_ROOT=./tmp \
        --conf spark.yarn.appMasterEnv.PEX_ROOT=./tmp \
        --files env.pex \
        $1

## Py4JException: Constructor org.apache.spark.api.python.PythonAccumulatorV2 Does Not Exist

You might run into the following error when using pex with PySpark.

> Py4JError: An error occurred while calling None.org.apache.spark.api.python.PythonAccumulatorV2. Trace:
> py4j.Py4JException: Constructor org.apache.spark.api.python.PythonAccumulatorV2([class java.lang.String, class java.lang.Integer, class java.lang.String]) does not exist

This means that PySpark libraries are not visible to pex. 
There are a few ways to fix this issue.

1. You can install the Package package `findspark`
    and use it help to locate the home directory of Spark. 

        :::python
        import findspark
        findspark.init()

    Or if you know the home directory of Spark.
        :::python
        import findspark
        findspark.init("/apache/spark")

    The first way finds the home directory of Spark automatically 
    if Spark is installed into a standard location. 
    This generally not the situation when you run submit your Spark application to a cluster 
    since containers and temporary directories are created for your application to run.
    The second way requires you to know the home directory of Spark.
    This is not feasible either generally speaking if you submit your Spark application to a cluster.
    To sum up, 
    this method is not really useful in practice.

2. Build your pex environment file with the option `--inherit-path=prefer`
    (`--inherit-path=fallback` might not work well).

3. Export the environment variable `PEX_INHERIT_PATH` to be `prefer` at run time.

        :::bash
        #!/bin/bash

        /apache/spark2.3/bin/spark-submit \
            --files "file:///apache/hive/conf/hive-site.xml,file:///apache/hadoop/etc/hadoop/ssl-client.xml,file:///apache/hadoop/etc/hadoop/hdfs-site.xml,file:///apache/hadoop/etc/hadoop/core-site.xml,file:///apache/hadoop/etc/hadoop/federation-mapping.xml" \
            --master yarn \
            --deploy-mode cluster \
            --queue YOUR_QUEUE \
            --num-executors 200 \
            --executor-memory 10G \
            --driver-memory 15G \
            --executor-cores 4 \
            --conf spark.yarn.maxAppAttempts=2 \
            --conf spark.dynamicAllocation.enabled=true \
            --conf spark.dynamicAllocation.maxExecutors=1000 \
            --conf spark.network.timeout=300s \
            --conf spark.executor.memoryOverhead=2G \
            --conf spark.pyspark.driver.python=./env.pex \
            --conf spark.pyspark.python=./env.pex \
            --conf spark.executorEnv.PEX_ROOT=./tmp \
            --conf spark.yarn.appMasterEnv.PEX_ROOT=./tmp \
            --conf spark.executorEnv.PEX_INHERIT_PATH=prefer \
            --conf spark.yarn.appMasterEnv.PEX_INHERIT_PATH=prefer \
            --files env.pex \
            $1

## Issues

Spark works well but the Hive metastore is not recognized.
For more details,
please refer to 
[this issue](https://github.com/pantsbuild/pex/issues/904)
.

## References

https://github.com/pantsbuild/pex

https://medium.com/criteo-labs/packaging-code-with-pex-a-pyspark-example-9057f9f144f3

[Run pyspark scripts with python3 instead of pyspark](https://hang-hu.github.io/spark/2018/10/31/Run-pyspark-scripts-with-python3-instead-of-pyspark.html)

https://github.com/pantsbuild/pex/issues/746