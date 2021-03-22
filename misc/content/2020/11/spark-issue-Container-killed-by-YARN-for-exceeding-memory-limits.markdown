Status: published
Date: 2021-03-22 11:01:18
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

DataFrame and Spark Tunsten leverage off-heap a lot to boost performance. Checking the Spark SQL physical plan, the Aggregation and Sort are all happened in Off-Heap. 

    org.apache.spark.sql.catalyst.errors.package$TreeNodeException: execute, tree:
    TungstenAggregate(key=[], functions=[(count(1),mode=Final,isDistinct=false)], output=[count#983L])
    +- TungstenExchange SinglePartition, None
      +- TungstenAggregate(key=[], functions=[(count(1),mode=Partial,isDistinct=false)], output=[count#988L])
        +- Project
          +- Sort [ocsQltyScr#845L DESC], true, 0
            +- ConvertToUnsafe
              +- Exchange rangepartitioning(ocsQltyScr#845L DESC,400), None
                +- ConvertToSafe
                  +- Project [ocsQltyScr#845L]
                    +- Filter (rank#977 = 1)
                      +- Window

1. due to bug in YARN 

2. data skew (e.g., big data table but not partitioned)

## Solutions 

Increase Memory Overhead `spark.yarn.executor.memoryOverhead` 

Reducing the number of Executor Cores

Increase the number of partitions

Increase Driver or Executor Memory

## References 

[Solving “Container Killed by Yarn For Exceeding Memory Limits” Exception in Apache Spark](https://medium.com/analytics-vidhya/solving-container-killed-by-yarn-for-exceeding-memory-limits-exception-in-apache-spark-b3349685df16)

[“Container killed by YARN for exceeding memory limits. 10.4 GB of 10.4 GB physical memory used” on an EMR cluster with 75GB of memory](https://stackoverflow.com/questions/40781354/container-killed-by-yarn-for-exceeding-memory-limits-10-4-gb-of-10-4-gb-physic)

[https://www.youtube.com/watch?v=t97VJtPAL2s](How do I resolve the error Container killed by YARN for exceeding memory limits in Spark on EMR?)

[Turn the virtual memory check to be off by default](https://issues.apache.org/jira/browse/YARN-2225)

[[Java 8] Over usage of virtual memory](https://issues.apache.org/jira/browse/YARN-4714)

[Yarn memory limit](https://www.xspdf.com/resolution/50926958.html)

https://stackoverflow.com/questions/37505638/understanding-spark-physical-plan

https://community.hortonworks.com/questions/36266/spark-physical-plan-doubts-tungstenaggregate-tungs.html