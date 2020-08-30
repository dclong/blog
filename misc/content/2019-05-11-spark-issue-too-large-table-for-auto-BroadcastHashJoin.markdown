Status: published
Date: 2020-08-29 22:05:22
Author: Benjamin Du
Slug: spark-issue-too-large-table-for-auto-BroadcastHashJoin
Title: Spark Issue: Too Large Table for Auto BroadcastHashJoin
Category: Computer Science
Tags: programming, Spark, issue, big data, error, BroadcastHashJoin, broadcast

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

16/04/17 11:17:36 ERROR scheduler.TaskSetManager: Total size of serialized results of 126 tasks (1137.3 MB) is bigger than spark.driver.maxResultSize (1024.0 MB)
16/04/17 11:17:36 ERROR yarn.ApplicationMaster: User class threw exception: org.apache.spark.SparkException: 
Job aborted due to stage failure: Total size of serialized results of 114 tasks (1029.0 MB) is bigger than spark.driver.maxResultSize (1024.0 MB)
org.apache.spark.SparkException: Job aborted due to stage failure: Total size of serialized results of 114 tasks (1029.0 MB) is bigger than spark.driver.maxResultSize (1024.0 MB)

OR

16/04/17 11:23:15 INFO executor.Executor: Finished task 196.0 in stage 6.0 (TID 610). 9455052 bytes result sent to driver
16/04/17 11:23:46 WARN netty.NettyRpcEndpointRef: Error sending message [message = Heartbeat(157,[Lscala.Tuple2;@56be55da,BlockManagerId(157, 45017))] in 1 attempts
org.apache.spark.rpc.RpcTimeoutException: Futures timed out after [10 seconds]. This timeout is controlled by spark.executor.heartbeatInterval

 

## Cause

When the BroadcastHashJoin is executed, 
for some reason,
the driver clones N copies (N is the number of executors) of the broadcasted table size, 
(in my case: 75MB) 
and broadcast it to each executor. 
If the N is like 300, 
the total memory required for driver is at least: 75MB * 300 = 22.5GB, 
larger than the executor memory.
It will cause driver no-response (OOM).

## Solution

Do not use BroadcastHashJoin

1. For SparkSQL (HiveContext): setting spark.sql.autoBroadcastJoinThreshold=10MB (or less)

2. For SparkSQL (SQLContext): do not call functions.broadcast()

3. For RDD: do not use broadcast variable
