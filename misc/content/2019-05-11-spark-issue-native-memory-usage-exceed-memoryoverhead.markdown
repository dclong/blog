Status: published
Date: 2020-08-29 22:05:22
Author: Benjamin Du
Slug: spark-issue-native-memory-usage-exceed-memoryOverhead
Title: Spark Issue: Native Memory Usage Exceed MemoryOverhead
Category: Computer Science
Tags: programming, Spark, issue, big data, error, memory, MemoryOverhead

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Symptom

Job aborted due to stage failure: Task 110 in stage 68.0 failed 1 times, 
most recent failure: Lost task 110.0 in stage 68.0:
ExecutorLostFailure (executor 35 exited caused by one of the running tasks) 
Reason: Container killed by YARN for exceeding memory limits. 40.6 GB of 40 GB physical memory used. 
Consider boosting spark.yarn.executor.memoryOverhead.

## Reason

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

## Solution

This may not be an optimum solution, 
but if the memoryOverhead is too small (by default max(0.1*executorMemory, 384M), 
we can still tune it to be 8 to 12G.
Tune `spark.yarn.executor.memoryOverhead` to be larger.

## References

https://stackoverflow.com/questions/37505638/understanding-spark-physical-plan

https://community.hortonworks.com/questions/36266/spark-physical-plan-doubts-tungstenaggregate-tungs.html
