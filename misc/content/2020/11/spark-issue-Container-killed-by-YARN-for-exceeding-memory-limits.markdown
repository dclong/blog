Status: published
Date: 2021-03-23 18:00:30
Author: Benjamin Du
Slug: spark-issue-Container-killed-by-YARN-for-exceeding-memory-limits
Title: Spark Issue: Container Killed by Yarn for Exceeding Memory Limits
Category: Computer Science
Tags: Computer Science, Spark, big data, YARN, memory, vmem, pmem, virtual memory, Spark issue

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Symptoms

Container killed by YARN for exceeding memory limits.  
22.0 GB of 19 GB physical memory used. 
Consider boosting `spark.yarn.executor.memoryOverhead` 
or disabling `yarn.nodemanager.vmem-check-enabled` 
because of [YARN-4714](https://issues.apache.org/jira/browse/YARN-4714).


Job aborted due to stage failure: Task 110 in stage 68.0 failed 1 times, 
most recent failure: Lost task 110.0 in stage 68.0:
ExecutorLostFailure (executor 35 exited caused by one of the running tasks) 
Reason: Container killed by YARN for exceeding memory limits. 40.6 GB of 40 GB physical memory used. 
Consider boosting spark.yarn.executor.memoryOverhead.


[Spark on Yarn and virtual memory error](https://a-ghorbani.github.io/2016/12/23/spark-on-yarn-and-java-8-and-virtual-memory-error)
and
[Container killed by YARN for exceeding memory limits](https://www.cnblogs.com/zz-ksw/p/11403622.html)
have good discussions on solutions to fix the issue including some low-level explanation of the issue.

## Possible Causes 

1. A bug ([YARN-4714](https://issues.apache.org/jira/browse/YARN-4714)) in YARN.

2. Too much usage of **off-heap** memory. 
  Spark Tungsten leverages off-heap memory a lot to boost performance. 
  Some Java operations (especially IO related) also levarages off-heap memory.
  Usage of off-heap memory in Spark 2 (this has been changed in Spark 3) 
  is control by `spark.yarn.executor.memoryOverhead`.
  Generally speaking,
  it is hard to control the usage of off-heap memory 
  unless the corresponding Java operations provide such options.
  The JVM option `MaxDirectMemorySize` specifies the maximum total size of `java.nio` (New I/O package) direct buffer allocations (off-heap memory),
  which is used with network data transfer and serialization activity.

2. data skew (e.g., big data table but not partitioned)

## Possible Solutions 

1. Increase memory overhead.

        :::bash
        --conf spark.yarn.executor.memoryOverhead=8G

2. Reducing the number of executor cores (which helps reducing memory consumption).

3. Increase the number of partitions (which makes each task smaller and helps reducing memory consumption).

4. Configure the JVM option `MaxDirectMemorySize` 
    if your Spark application involves reading Parquet files and/or encoding/decoding BASE64 string, etc.     
    By default,
    `MaxDirectMemorySize` is close to the size of heap memory size.
    So, if `MaxDirectoryMemorySize` is not set, 
    Spark containers might use too much off-heap memory.

        :::bash
        --conf spark.executor.extraJavaOptions=-XX:MaxDirectMemorySize=8G

## References 

[Solving “Container Killed by Yarn For Exceeding Memory Limits” Exception in Apache Spark](https://medium.com/analytics-vidhya/solving-container-killed-by-yarn-for-exceeding-memory-limits-exception-in-apache-spark-b3349685df16)

[How do I resolve the error "Container killed by YARN for exceeding memory limits" in Spark on Amazon EMR?](https://aws.amazon.com/premiumsupport/knowledge-center/emr-spark-yarn-memory-limit/#:~:text=Memory%20overhead%20is%20the%20amount,libraries%2C%20or%20memory%20mapped%20files.)

[“Container killed by YARN for exceeding memory limits. 10.4 GB of 10.4 GB physical memory used” on an EMR cluster with 75GB of memory](https://stackoverflow.com/questions/40781354/container-killed-by-yarn-for-exceeding-memory-limits-10-4-gb-of-10-4-gb-physic)

[https://www.youtube.com/watch?v=t97VJtPAL2s](How do I resolve the error Container killed by YARN for exceeding memory limits in Spark on EMR?)

[Turn the virtual memory check to be off by default](https://issues.apache.org/jira/browse/YARN-2225)

[[Java 8] Over usage of virtual memory](https://issues.apache.org/jira/browse/YARN-4714)

[Yarn memory limit](https://www.xspdf.com/resolution/50926958.html)

https://stackoverflow.com/questions/37505638/understanding-spark-physical-plan

https://community.hortonworks.com/questions/36266/spark-physical-plan-doubts-tungstenaggregate-tungs.html

[Apache Spark and off-heap memory](https://www.waitingforcode.com/apache-spark/apache-spark-off-heap-memory/read#off-heap_memory_and_Project_Tungsten)

[Decoding Memory in Spark — Parameters that are often confused](https://medium.com/walmartglobaltech/decoding-memory-in-spark-parameters-that-are-often-confused-c11be7488a24)