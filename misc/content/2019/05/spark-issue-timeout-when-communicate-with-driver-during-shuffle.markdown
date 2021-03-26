Status: published
Date: 2021-03-24 15:12:11
Author: Benjamin Du
Slug: spark-issue-timeout-when-communicate-with-driver-during-shuffle
Title: Spark Issue: Timeout When Communicate With Driver During Shuffle Caused by Driver OOM
Category: Computer Science
Tags: programming, Spark, issue, big data, eror, driver, shuffle, OOM, timeout, Spark issue

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Symptom

15/12/24 02:04:21 INFO spark.MapOutputTrackerWorker: Doing the fetch; tracker endpoint = AkkaRpcEndpointRef(Actor[akka.tcp://sparkDriver@10.115.58.55:52077/user/MapOutputTracker#-1937024516])

15/12/24 02:06:21 WARN akka.AkkaRpcEndpointRef: Error sending message [message = GetMapOutputStatuses(0)] in 1 attempts

org.apache.spark.rpc.RpcTimeoutException: Futures timed out after [120 seconds]. This timeout is controlled by spark.rpc.askTimeout

at org.apache.spark.rpc.RpcTimeout.org$apache$spark$rpc$RpcTimeout$$createRpcTimeoutException(RpcEnv.scala:214)



15/12/24 02:05:36 ERROR actor.ActorSystemImpl: Uncaught fatal error from thread [sparkDriver-akka.remote.default-remote-dispatcher-24] shutting down ActorSystem [sparkDriver]

java.lang.OutOfMemoryError: Java heap space

at java.util.Arrays.copyOf(Arrays.java:2271)

at java.io.ByteArrayOutputStream.toByteArray(ByteArrayOutputStream.java:178)



## Cause 
  
Driver maintains the partition information of the map output, 
so during the shuffle period, 
it can respond to reducer to find the desired partition. 
When shuffling a large amount of partitions, Driver need to store huge amount of MapOutputStatus object that may cause OOM. 
Based on my experience, we may need 10G memory for 10K partition. 

## Solution:

1. Increase Driver memory and computation power is useful in case you need less than 15G memory 

        :::bash
        --driver-memory 12G
        --conf spark.driver.cores=4 
        --conf spark.akka.threads=32 

2. The ultimate solution is to re-partition the map output when feed to the reduce actions. 
    A simple way is to half the number of input partitions.

        :::scala
        val liveItems = liveItemsPair.reduceByKey(rFindMax, liveItemsPair.partitions.size / 2)

    For example, 
    when we compute 30-day Google live item response, 
    it consumes about 20K partitions, 
    which will require more than 20G memory for the driver. 
    But when we half the partition size for the reducer, 
    we can complete the work with 10G Driver memory.
