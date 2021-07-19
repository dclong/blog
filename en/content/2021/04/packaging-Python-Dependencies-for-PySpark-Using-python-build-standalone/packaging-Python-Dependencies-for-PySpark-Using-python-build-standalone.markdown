Status: published
Date: 2021-04-26 09:48:16
Author: Benjamin Du
Slug: packaging-Python-Dependencies-for-PySpark-Using-python-build-standalone
Title: Packaging Python Dependencies for PySpark Using Python-Build-Standalone
Category: Computer Science
Tags: Computer Science, programming, Python, portable, standalone, python-build-standalone, Docker, environment
Modified: 2021-07-18 22:12:43

You can build a portable Python environment 
following steps below.

1. Install [python-build-standalone](https://github.com/indygreg/python-build-standalone).

2. Install Python packages using pip of the installed python-build-standalone distribution.

3. Pack the whole python-build-standalone directory into a compressed file, e.g., `env.tar.gz`.


The GitHub repo
[dclong/python-portable](https://github.com/dclong/python-portable)
has good examples of building portable Python environments 
leveraging the Docker image
[dclong/python-portable](https://github.com/dclong/docker-python-portable)
(which has python-build-standalone installed).

## Submit a PySpark Application Using a Portable Python Environment

Below is an example shell script for sumitting a PySpark job 
using a pre-built portable Python environment named `env.tar.gz`.

    :::bash
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
        --conf spark.pyspark.driver.python=./env/bin/python \
        --conf spark.pyspark.python=./env/bin/python \
        --archives env.tar.gz#env \
        $1

And below is a simple example of `_pyspark.py`.

    :::Python
    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName('Test PySpark').enableHiveSupport().getOrCreate()
    sql = """
            SELECT * 
            FROM some_table 
            TableSample (100000 Rows)
        """
    spark.sql(sql).write.mode("overwrite").parquet("output")

## References

- [Packaging Python Dependencies for PySpark Using Conda-Pack](http://www.legendu.net/en/blog/packaging-python-dependencies-for-pyspark-using-conda-pack)

- [Packaging Python Dependencies for PySpark Using Pex](http://www.legendu.net/misc/blog/packaging-python-dependencies-for-pyspark-using-pex)