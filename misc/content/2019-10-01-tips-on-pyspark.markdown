Status: published
Date: 2020-11-15 10:32:52
Author: Benjamin Du
Slug: tips-on-pyspark
Title: Tips on PySpark
Category: Computer Science
Tags: programming, PySpark, Python, Spark, tips, HPC, high performance computing

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. PySpark 2.4 and older does not support Python 3.8.
    You have to use Python 3.7 with PySpark 2.4 or older.

2. It can be extremely helpful to run a PySpark application locally to detect possible issues
    before submitting it to the Spark cluster.

        :::bash
        #!/usr/bin/env bash
        PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
        /path/to/spark-2.3.1-bin-hadoop2.7/bin/spark-submit \
            --conf spark.yarn.maxAppAttempts=1 \
            --conf spark.pyspark.driver.python=.venv/bin/python3 \
            --conf spark.pyspark.python=.venv/bin/python3 \
            script_to_run.py --arg1 v1 --arg2 v2

2. You can run PySpark interactively using the `pyspark` command
  and submit a PySpark job to the cluster using the `spark-submit` command.
	For more details, 
	please refer to
	[Launching Applications with spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit).
    Below is an example of shell script for submitting a PySpark job using `spark-submit`.

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
            --conf spark.pyspark.driver.python=/usr/share/anaconda3/bin/python \
            --conf spark.pyspark.python=/usr/share/anaconda3/bin/python \
            /path/to/_pyspark.py

    If you use a conda-pack Python environment named `env.tar.gz`,
    you can submit a PySpark application using the following shell script.

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
            --conf spark.pyspark.driver.python=./env/bin/python \
            --conf spark.pyspark.python=./env/bin/python \
            --archives env.tar.gz#env \
            $1

    And below is a simple example of `_pyspark.py`.

        :::Python
        from pyspark.sql import SparkSession
        from pyspark.sql.functions import *

        spark = SparkSession.builder.appName('Test PySpark').enableHiveSupport().getOrCreate()
        sql = """
                SELECT * 
                FROM some_table 
                TableSample (100000 Rows)
            """
        spark.sql(sql).write.mode("overwrite").parquet("output")

    Notice that I have prefixed an underscore to the name of the file.
    This is a simple but useful trick to avoid unintentional module conflictions in Python. 
    For example, 
    if you name your PySpark script `pyspark.py`,
    your PySpark application will fail to work 
    as your script `pyspark.py` is loaded as a module named `pyspark` 
    which hides the official `pyspark` module in Python.
    It is suggestion that adopt the trick of "prefixing an underscore to file names"
    when submitting a PySpark job.

3. If you have multiple versions of Spark installed,
    the exported Spark environment variables might intervent with each other 
    and cause some of them fail to work.
    For example, 
    if you have both a cluster version of Spark and a local version of Spark installed,
    you might failed to submit Spark applications using `spark-submit`.
    One simple fix to this problem is 
    to manually configure a right version of the `PATH` environemnt varible 
    before you invoke the command `spark-submit` of the local version of Spark.

        :::bash
        PATH=/bin:/sbin:/usr/bin:/usr/sbin /path/to/spark-submit ...

    As a matter of fact,
    this is the way to fix most PATH related issues in Linux/Unix.

2. PySpark does not support converting `$"col"` to a Column implicitly. 
    However, 
    the function `pyspark.sql.functions.col` works the same as in Spark.

3. [Pandas UDFs](https://spark.apache.org/docs/latest/sql-pyspark-pandas-with-arrow.html#pandas-udfs-aka-vectorized-udfs)
    sounds interesting!

5. [pyspark-stubs](https://github.com/zero323/pyspark-stubs)
    can be leveraged for static type checking for PySpark project.

## Use PySpark in Jupyter/Lab Notebooks

1. The trick is to use the Python library `findspark` to find and initiate Spark for use in notebook. 

        :::bash
        import findspark
        findspark.init("/opt/spark")
        from pyspark.sql import SparkSession, DataFrame
        spark = SparkSession.builder.appName("PySpark_Notebook") \
            .enableHiveSupport().getOrCreate()

2. When working with relatively large data in a local version of Spark in Jupyter/Lab notebook,
    you might easily encounter OOM errors. 
    The trick to increase the driver memory using the option `.config("spark.driver.memory", "50g")`.

        :::python
        import findspark
        findspark.init("/opt/spark")
        from pyspark.sql import SparkSession, DataFrame
        spark = SparkSession.builder.appName("PySpark_Notebook") \
            .config("spark.driver.memory", "50g") \
            .enableHiveSupport().getOrCreate()
        
3. The command-line option `--jars` is equivalent to `spark.jars` when you use `--conf`.
    This means that you can use `.config("spark.jars", "/path/to/file.jar")` 
    to add JARs to a Spark/PySpark application in Jupyter/Lab notebook.

        :::python
        import findspark
        findspark.init("/opt/spark")
        from pyspark.sql import SparkSession, DataFrame
        spark = SparkSession.builder.appName("PySpark_Notebook") \
            .config("spark.jars", "/path/to/file.jar") \
            .config("spark.driver.memory", "50g") \
            .enableHiveSupport().getOrCreate()

3. If you want to leverage a Spark cluster in a Jupyter/Lab notebook,
    there are a few things (Hadoop queue, driver IP and driver port) you need to configure.
    Below is an illustration.
    
        :::python
        import socket
        import findspark
        findspark.init("/apache/spark2.3")
        from pyspark.sql import SparkSession, DataFrame
        spark = SparkSession.builder.master("yarn").appName("PySpark_Cluster") \
            .config("spark.yarn.queue", "your-hadoop-queue>") \
            .config("spark.driver.host", socket.gethostbyname(socket.gethostname())) \
            .config("spark.driver.port", "30202") \
            .enableHiveSupport().getOrCreate()

    Notice that the SparkContext object will be expired after inactive for a while.
    It won't help if you run the above code again in notebook
    because a SparkSession (even if it is invalid any more due to expiration of the underlying SparkContext) has already been created.
    You can of course restart the Python kernel and then create a new SparkSession.
    However, 
    you will lose all Python objects in the notebook by doing this.
    A better alternative is to manually stop the SparkSession by calling `spark.stop()` 
    and then run the above code in notebook again.
    This way, the Python objects (e.g., pandas DataFrame you have created)
    will still be alive for you to use.

## Dependencies

[PEX](https://github.com/pantsbuild/pex)
sounds like a good tool!

1. Create a directory named `lib`.

        :::bash
        mkdir lib

2. Install dependencies into the library.

        :::bash
        pip3 install -r requirements.txt -t lib

3. Zip the library.

        :::bash
        cd lib
        zip -r ../lib.zip .

4. Call `SparkContext.addPyFile` to add the zip file before using the packages/moduels.

        :::bash
        spark.sparkContext.addPyFile("/path/to/python/file")

Issues:

1. This approach works with only pure Python package.
    No dependecny on C/C++, Fortran is allowed.
    It is OK for a Python package to rely on JAR files.

2. No easy way to exclude dependencies.

3. Does wheel work or not with this approach?

## References

[awesome-spark](https://github.com/awesome-spark/awesome-spark)

https://spark.apache.org/docs/latest/api/python/pyspark.sql.html

https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame

https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.Column

https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#module-pyspark.sql.functions

[Managing dependencies and artifacts in PySpark](https://bytes.grubhub.com/managing-dependencies-and-artifacts-in-pyspark-7641aa89ddb7)

https://stackoverflow.com/questions/51450462/pyspark-addpyfile-to-add-zip-of-py-files-but-module-still-not-found

https://becominghuman.ai/real-world-python-workloads-on-spark-standalone-clusters-2246346c7040

https://community.cloudera.com/t5/Community-Articles/Running-PySpark-with-Conda-Env/ta-p/247551

https://stackoverflow.com/questions/36461054/i-cant-seem-to-get-py-files-on-spark-to-work

[Best Practices Writing Production-Grade PySpark Jobs](https://developerzen.com/best-practices-writing-production-grade-pyspark-jobs-cb688ac4d20f)

[Packaging code with PEX — a PySpark example](https://medium.com/criteo-labs/packaging-code-with-pex-a-pyspark-example-9057f9f144f3)

