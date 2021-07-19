Status: published
Date: 2021-04-30 12:13:17
Author: Benjamin Du
Slug: packaging-python-dependencies-for-pyspark-using-conda-pack
Title: Packaging Python Dependencies for PySpark Using Conda-Pack
Category: Computer Science
Tags: programming, PySpark, Python, conda, conda-pack, dependency, Spark, big data, portable
Modified: 2021-07-18 22:12:43


[python-build-standalone](https://github.com/indygreg/python-build-standalone)
is a better alternative to conda-pack on managing Python dependencies for PySpark.
Please refer to 
[Packaging Python Dependencies for PySpark Using python-build-standalone](http://www.legendu.net/en/blog/packaging-Python-Dependencies-for-PySpark-Using-python-build-standalone)
for tutorials on how to use
[python-build-standalone](https://github.com/indygreg/python-build-standalone)
to manage Python dependencies for PySpark.

## Build Portable Python Environments Using conda-pack

Please refer to the GitHub repo
[dclong/conda_environ](https://github.com/dclong/conda_environ)
for instructions
which leverages the Docker image
[dclong/conda](https://github.com/dclong/docker-conda)
to build portable conda environments.

## Submit a PySpark Application Using conda Environment

Below is an example shell script for sumitting a PySpark job 
using a pre-built conda-pack Python environment named `env.tar.gz`.

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

- [Packaging Python Dependencies for PySpark Using Python-Build-Standalone](http://www.legendu.net/en/blog/packaging-Python-Dependencies-for-PySpark-Using-python-build-standalone)

- [Packaging Python Dependencies for PySpark Using Pex](http://www.legendu.net/misc/blog/packaging-python-dependencies-for-pyspark-using-pex)

- [Usage with Apache Spark on YARN](https://conda.github.io/conda-pack/spark.html)

- https://github.com/jcrist/skein/