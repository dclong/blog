Status: published
Date: 2021-03-30 16:28:59
Author: Benjamin Du
Slug: work-with-multiple-spark-installations
Title: Work With Multiple Spark Installations
Category: Computer Science
Tags: Computer Science, programming, Spark, big data, multiple, installation

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## spark-submit and spark-shell

Overwrite the PATH environment variable before invoking `spark-submit` and/or `spark-shell` 
often resolves the issue.

## Spark in Jupyter/Lab Notebooks

Remove or reset the environment variable `HADOOP_CONF_DIR` resolves the issue.

    :::python
    import os
    os.environ["HADOOP_CONF_DIR"] = ""
    import findspark
    findspark.init("/opt/spark-3.1.1-bin-hadoop3.2/")
    from pyspark.sql import SparkSession, DataFrame
    spark = SparkSession.builder.appName("PySpark_Notebook") \
        .enableHiveSupport().getOrCreate()
    ...

## More Spark Related Environment Variables

- HADOOP_CONF_DIR
- SPARK_HOME
- HADOOP_HOME
- HIVE_HOME
- PIG_HOME
- HBASE_HOME