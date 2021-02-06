Status: published
Date: 2020-02-20 16:25:13
Author: Benjamin Du
Slug: build-spark-from-source
Title: Build Spark from Source
Category: Computer Science
Tags: programming, Spark, big data, build, source

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

You can download prebuilt binary Spark at 
https://spark.apache.org/downloads.html.
This is where you should get started 
and it will likely satisfy your need most of the time.
However,
below are instructions on how to build Spark from source if you have to.

https://spark.apache.org/docs/latest/building-spark.html

1. Clone Spark 2.4.5.

        :::bash
        git clone --depth 1 --branch 2.4.5 https://github.com/apache/spark.git

2. Use Scala 2.11.

        :::bash
        ./dev/change-scala-version.sh 2.11

3. Run dev/make-distribution.sh

        :::bash
        ./dev/make-distribution.sh \
            --name hadoop2.7 \
            --tgz \
            -Pyarn \
            -Phive \
            -Phive-thriftserver \
            -Phadoop-2.7 \
            -Dhadoop.version=2.7.3 \
            -Dscala-2.11

4. Build Spark.
    
        :::bash
        ./build/mvn \
            -Pyarn \
            -Phive \
            -Phive-thriftserver \
            -Phadoop-2.7 \
            -Dhadoop.version=2.7.3 \
            -Dscala-2.11 \
            -DskipTests \
            clean package

    This will generate a `Spark-2.4.5-*.tgz` file that you use to deploy.
    Just copy it to your Spark client and unzip it to the right location.

5. If you are building Spark for using in your company, 
    you probably need to replace the directory `conf` 
    with the customized one for your company.
