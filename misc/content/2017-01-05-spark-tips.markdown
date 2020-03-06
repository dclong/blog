Status: published
Date: 2020-02-20 15:13:31
Author: Ben Chuanlong Du
Slug: spark-tips
Title: Spark Tips
Category: Computer Science
Tags: programming, Spark, big data, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**
## General Tips

1. If you have a really large Spark job which fails with high chance due too large complexity,
    you can check whether there are independent sub jobs in the big job.
    If so,
    it is often a good idea to submit separate Spark applications for each independent sub jobs.
    One typical example is when you do a large simulation. 
    Each iterator in the simulation can be seen as an independent job (of other iterators).
    If the whole simulation is too large and fails with high chance,
    you can break down the simulation into smaller piece.
    One useful trick is to use hash and/or modulus to help you cut the large job into smaller and reproducible ones. 
    You can then submit a Spark application for each of the smaller jobs.
    The advantage of this approach is 2 fold.
    First, 
    each of the smaller jobs can run reliably and have a much higher chance to suceed. 
    Second, 
    shall any of the smaller jobs fail, 
    you run rerun that specific job (this is why reproducible is important) instead of rerunning the whole large simulation.


## Sharing Variables

Spark supports two types of shared variables: broadcast variables,
which can be used to cache a value in memory on all nodes,
and accumulators,
which are variables that are only “added” to, such as counters and sums.


## Spark Submit

1. After submitting a Spark application, 
    if the network connection get lots, 
    the Spark application submitted will be killed.
    You can nohup or tmux to submit your Spark application 
    so that loss of network connection won't kill your Spark application.
    Or another way is to just submit your Spark application
    from a server that has very stable network connection.

2. If you are sure that your Spark application is production ready,
    it is better to submit it with the option `--deploy-mode cluster`.
    However the default option (`--deploy-mode client`) is good for debugging.
    And also, `--deploy-mode client` is much faster to submit generally speaking.
    It is suggested that you use `--deploy-mode client` for ad hoc Spark applications
    and `--deploy-mode cluster` for production ready applications that need to be run many times.

        :::bash
        #!/bin/bash
        /apache/spark2.3/bin/spark-submit \
            --files "file:///apache/hive/conf/hive-site.xml,file:///apache/hadoop/etc/hadoop/ssl-client.xml,file:///apache/hadoop/etc/hadoop/hdfs-site.xml,file:///apache/hadoop/etc/hadoop/core-site.xml,file:///apache/hadoop/etc/hadoop/federation-mapping.xml" \
            --master yarn \
            --deploy-mode cluster \
            --queue your_queue \
            --num-executors 200 \
            --executor-memory 10G \
            --driver-memory 15G \
            --executor-cores 4 \
            --conf spark.yarn.maxAppAttempts=2 \
            --conf spark.dynamicAllocation.enabled=true \
            --conf spark.dynamicAllocation.maxExecutors=1000 \
            --conf spark.network.timeout=300s \
            --conf spark.executor.memoryOverhead=2G \
            --class your.package.SomeClass \
            --jars /path/to/jar/dependencies \
            /path/to/compiled/jar arg1 arg2 ...

    If you have used Kotlin in your Spark application,
    you need to include `kotlin-stdlib.jar` via the `--jars` option.

        :::bash
        #!/bin/bash
        /apache/spark2.3/bin/spark-submit \
            --files "file:///apache/hive/conf/hive-site.xml,file:///apache/hadoop/etc/hadoop/ssl-client.xml,file:///apache/hadoop/etc/hadoop/hdfs-site.xml,file:///apache/hadoop/etc/hadoop/core-site.xml,file:///apache/hadoop/etc/hadoop/federation-mapping.xml" \
            --master yarn \
            --deploy-mode cluster \
            --queue your_queue \
            --num-executors 200 \
            --executor-memory 10G \
            --driver-memory 15G \
            --executor-cores 4 \
            --conf spark.yarn.maxAppAttempts=2 \
            --conf spark.dynamicAllocation.enabled=true \
            --conf spark.dynamicAllocation.maxExecutors=1000 \
            --conf spark.network.timeout=300s \
            --conf spark.executor.memoryOverhead=2G \
            --class your.package.SomeClass \
            --jars /path/to/kotlin-stdlib.jar \
            /path/to/compiled/jar arg1 arg2 ...

## Spark Shell

1. The `--jars` option of `spark-shell` can be used to add JAR dependencies.

2. `spark-shell` accepts `--queue` (for specifying the queue to submit jobs) as parameter!
If you run `spark-shell` and encounter the issue of "ERROR SparkContext: Error initializing SparkContext" 
due to "application submitted by user to unknown queue",
you have to pass the queue that you can access to `spark-shell`.

        :::bash
        spark-shell --queue my_queue

## Spark Cluster Master URL

https://spark.apache.org/docs/latest/submitting-applications.html#master-urls


## References

https://developer.ibm.com/hadoop/2016/07/18/troubleshooting-and-tuning-spark-for-heavy-workloads/

http://blog.prabeeshk.com/blog/2014/10/31/install-apache-spark-on-ubuntu-14-dot-04/

http://mbonaci.github.io/mbo-spark/

http://www.simonouellette.com/blog/spark-join-when-not-to-use-it

https://bzhangusc.wordpress.com/2015/11/20/use-sbt-console-as-spark-shell/

https://spark-summit.org/2015/events/interactive-graph-analytics-with-spark/

https://www.slideshare.net/SparkSummit/understanding-memory-management-in-spark-for-fun-and-profit

