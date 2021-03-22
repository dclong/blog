Status: published
Date: 2021-03-22 11:01:18
Author: Benjamin Du
Slug: spark-issue-executor-out-of-memory-when-running-large-table-join
Title: Spark Issue: Executor Out of Memory When Running Large Table Join
Category: Computer Science
Tags: programming, Spark, issue, big data, error, OOM, Out of Memory, Spark issue

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Symptom 

### Symptom 1

16/04/22 04:27:18 WARN yarn.YarnAllocator: Container marked as failed: container_1459803563374_223497_02_000067 on host.
Exit status: 143. Diagnostics: Container [pid=30502,containerID=container_1459803563374_223497_02_000067] is running beyond physical memory limits. 
Current usage: 13.8 GB of 13.8 GB physical memory used; 14.6 GB of 28.9 GB virtual memory used. Killing container.
Dump of the process-tree for container_1459803563374_223497_02_000067 :
|- PID PPID PGRPID SESSID CMD_NAME USER_MODE_TIME(MILLIS) SYSTEM_TIME(MILLIS) VMEM_USAGE(BYTES) RSSMEM_USAGE(PAGES) FULL_CMD_LINE
|- 30502 18022 30502 30502 (bash) 0 0 22773760 347 /bin/bash -c LD_LIBRARY_PATH=/apache/hadoop/lib/native:/apache/hadoop/lib/native/Linux-amd64-64: 
/usr/java/latest/bin/java -server -XX:OnOutOfMemoryError='kill %p' 
-Xms12288m -Xmx12288m -Djava.io.tmpdir=/hadoop/6/scratch/local/usercache/dclong/appcache/application_1459803563374_223497/container_1459803563374_223497_02_000067/tmp 
'-Dspark.driver.port=35848' '-Dspark.ui.port=0' '-Dspark.akka.threads=32' 
-Dspark.yarn.app.container.log.dir=/hadoop/10/scratch/logs/application_1459803563374_223497/container_1459803563374_223497_02_000067 
-XX:MaxPermSize=256m org.apache.spark.executor.CoarseGrainedExecutorBackend 
--driver-url spark://CoarseGrainedScheduler@10.115.16.50:35848 --executor-id 33 
--cores 3 --app-id application_1459803563374_223497 
--user-class-path file:/hadoop/6/scratch/local/usercache/dclong/appcache/application_1459803563374_223497/container_1459803563374_223497_02_000067/__app__.jar 
--user-class-path file:/hadoop/6/scratch/local/usercache/dclong/appcache/application_1459803563374_223497/container_1459803563374_223497_02_000067/hbase-client-0.98.0-21.jar 
--user-class-path file:/hadoop/6/scratch/local/usercache/dclong/appcache/application_1459803563374_223497/container_1459803563374_223497_02_000067/hbase-server-0.98.0-21.jar 
--user-class-path file:/hadoop/6/scratch/local/usercache/dclong/appcache/application_1459803563374_223497/container_1459803563374_223497_02_000067/datanucleus-api-jdo-3.2.6.jar 
--user-class-path file:/hadoop/6/scratch/local/usercache/dclong/appcache/application_1459803563374_223497/container_1459803563374_223497_02_000067/datanucleus-core-3.2.10.jar 
--user-class-path file:/hadoop/6/scratch/local/usercache/dclong/appcache/application_1459803563374_223497/container_1459803563374_223497_02_000067/datanucleus-rdbms-3.2.9.jar 
--user-class-path file:/hadoop/6/scratch/local/usercache/dclong/appcache/application_1459803563374_223497/container_1459803563374_223497_02_000067/mysql-connector-java-5.1.33.jar 
--user-class-path file:/hadoop/6/scratch/local/usercache/dclong/appcache/application_1459803563374_223497/container_1459803563374_223497_02_000067/spark-avro_2.11-2.0.1.jar 
--user-class-path file:/hadoop/6/scratch/local/usercache/dclong/appcache/application_1459803563374_223497/container_1459803563374_223497_02_000067/spark-csv_2.11-1.3.0.jar 
--user-class-path file:/hadoop/6/scratch/local/usercache/dclong/appcache/application_1459803563374_223497/container_1459803563374_223497_02_000067/commons-csv-1.2.jar 1> 
/hadoop/10/scratch/logs/application_1459803563374_223497/container_1459803563374_223497_02_000067/stdout 2> /hadoop/10/scratch/logs/application_1459803563374_223497/container_1459803563374_223497_02_000067/stderr
|- 30524 30502 30502 30502 (java) 23870 3795 15701848064 3605090 /usr/java/latest/bin/java -server -XX:OnOutOfMemoryError=kill %p -Xms12288m -Xmx12288m -Djava.io.tmpdir=/hadoop/6/scratch/local/usercache/b_pandaren_kwdm/appcache/application_1459803563374_223497/container_1459803563374_223497_02_000067/tmp -Dspark.driver.port=35848 -Dspark.ui.port=0 -Dspark.akka.threads=32 -Dspark.yarn.app.container.log.dir=/hadoop/10/scratch/logs/application_1459803563374_223497/container_1459803563374_223497_02_000067 -XX:MaxPermSize=256m org.apache.spark.executor.CoarseGrainedExecutorBackend 
Container killed on request. Exit code is 143
Container exited with a non-zero exit code 143

## Symptom 2

16/04/23 23:12:20 INFO broadcast.TorrentBroadcast: Started reading broadcast variable 46
16/04/23 23:12:31 INFO executor.CoarseGrainedExecutorBackend: Driver commanded a shutdown
16/04/23 23:12:31 ERROR shuffle.RetryingBlockFetcher: Exception while beginning fetch of 1 outstanding blocks
java.io.IOException: Failed to connect to 10.115.45.46:40458
        at org.apache.spark.network.client.TransportClientFactory.createClient(TransportClientFactory.java:216)
        at org.apache.spark.network.client.TransportClientFactory.createClient(TransportClientFactory.java:167)
        at org.apache.spark.network.netty.NettyBlockTransferService$$anon$1.createAndStart(NettyBlockTransferService.scala:90)
        at org.apache.spark.network.shuffle.RetryingBlockFetcher.fetchAllOutstanding(RetryingBlockFetcher.java:140)
        at org.apache.spark.network.shuffle.RetryingBlockFetcher.start(RetryingBlockFetcher.java:120)
        at org.apache.spark.network.netty.NettyBlockTransferService.fetchBlocks(NettyBlockTransferService.scala:99)
        at org.apache.spark.network.BlockTransferService.fetchBlockSync(BlockTransferService.scala:89)
        at org.apache.spark.storage.BlockManager$$anonfun$doGetRemote$2.apply(BlockManager.scala:588)
        at org.apache.spark.storage.BlockManager$$anonfun$doGetRemote$2.apply(BlockManager.scala:585)
        at scala.collection.mutable.ResizableArray$class.foreach(ResizableArray.scala:59)
        at scala.collection.mutable.ArrayBuffer.foreach(ArrayBuffer.scala:48)
        at org.apache.spark.storage.BlockManager.doGetRemote(BlockManager.scala:585)
        at org.apache.spark.storage.BlockManager.getRemoteBytes(BlockManager.scala:578)
        at org.apache.spark.broadcast.TorrentBroadcast$$anonfun$org$apache$spark$broadcast$TorrentBroadcast$$readBlocks$1.org$apache$spark$broadcast$TorrentBroadcast$$anonfun$$getRemote$1(TorrentBroadcast.scala:127)
        at org.apache.spark.broadcast.TorrentBroadcast$$anonfun$org$apache$spark$broadcast$TorrentBroadcast$$readBlocks$1$$anonfun$1.apply(TorrentBroadcast.scala:137)
        at org.apache.spark.broadcast.TorrentBroadcast$$anonfun$org$apache$spark$broadcast$TorrentBroadcast$$readBlocks$1$$anonfun$1.apply(TorrentBroadcast.scala:137)
        at scala.Option.orElse(Option.scala:289)
        at org.apache.spark.broadcast.TorrentBroadcast$$anonfun$org$apache$spark$broadcast$TorrentBroadcast$$readBlocks$1.apply$mcVI$sp(TorrentBroadcast.scala:137)
        at org.apache.spark.broadcast.TorrentBroadcast$$anonfun$org$apache$spark$broadcast$TorrentBroadcast$$readBlocks$1.apply(TorrentBroadcast.scala:120)
        at org.apache.spark.broadcast.TorrentBroadcast$$anonfun$org$apache$spark$broadcast$TorrentBroadcast$$readBlocks$1.apply(TorrentBroadcast.scala:120)
        at scala.collection.immutable.List.foreach(List.scala:381)
        at org.apache.spark.broadcast.TorrentBroadcast.org$apache$spark$broadcast$TorrentBroadcast$$readBlocks(TorrentBroadcast.scala:120)
        at org.apache.spark.broadcast.TorrentBroadcast$$anonfun$readBroadcastBlock$1.apply(TorrentBroadcast.scala:175)
        at org.apache.spark.util.Utils$.tryOrIOException(Utils.scala:1219)
        at org.apache.spark.broadcast.TorrentBroadcast.readBroadcastBlock(TorrentBroadcast.scala:165)
        at org.apache.spark.broadcast.TorrentBroadcast._value$lzycompute(TorrentBroadcast.scala:64)
        at org.apache.spark.broadcast.TorrentBroadcast._value(TorrentBroadcast.scala:64)
        at org.apache.spark.broadcast.TorrentBroadcast.getValue(TorrentBroadcast.scala:88)
        at org.apache.spark.broadcast.Broadcast.value(Broadcast.scala:70)
        at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:62)
        at org.apache.spark.scheduler.Task.run(Task.scala:89)
        at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:214)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
        at java.lang.Thread.run(Thread.java:745)
Caused by: java.net.ConnectException: Connection refused: 10.115.45.46:40458
        at sun.nio.ch.SocketChannelImpl.checkConnect(Native Method)
        at sun.nio.ch.SocketChannelImpl.finishConnect(SocketChannelImpl.java:739)
        at io.netty.channel.socket.nio.NioSocketChannel.doFinishConnect(NioSocketChannel.java:224)
        at io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.finishConnect(AbstractNioChannel.java:289)
        at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:528)
        at io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized(NioEventLoop.java:468)
        at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:382)
        at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:354)
        at io.netty.util.concurrent.SingleThreadEventExecutor$2.run(SingleThreadEventExecutor.java:111)
        ... 1 more
16/04/23 23:12:31 ERROR shuffle.RetryingBlockFetcher: Exception while beginning fetch of 3 outstanding blocks
java.lang.NullPointerException: group
        at io.netty.bootstrap.AbstractBootstrap.group(AbstractBootstrap.java:80)
        at org.apache.spark.network.client.TransportClientFactory.createClient(TransportClientFactory.java:189)
        at org.apache.spark.network.client.TransportClientFactory.createClient(TransportClientFactory.java:167)
        at org.apache.spark.network.netty.NettyBlockTransferService$$anon$1.createAndStart(NettyBlockTransferService.scala:90)
        at org.apache.spark.network.shuffle.RetryingBlockFetcher.fetchAllOutstanding(RetryingBlockFetcher.java:140)
        at org.apache.spark.network.shuffle.RetryingBlockFetcher.start(RetryingBlockFetcher.java:120)
        at org.apache.spark.network.netty.NettyBlockTransferService.fetchBlocks(NettyBlockTransferService.scala:99)
        at org.apache.spark.storage.ShuffleBlockFetcherIterator.sendRequest(ShuffleBlockFetcherIterator.scala:152)
        at org.apache.spark.storage.ShuffleBlockFetcherIterator.fetchUpToMaxBytes(ShuffleBlockFetcherIterator.scala:316)
        at org.apache.spark.storage.ShuffleBlockFetcherIterator.next(ShuffleBlockFetcherIterator.scala:296)
        at org.apache.spark.storage.ShuffleBlockFetcherIterator.next(ShuffleBlockFetcherIterator.scala:51)
        at scala.collection.Iterator$$anon$11.next(Iterator.scala:370)
        at scala.collection.Iterator$$anon$12.hasNext(Iterator.scala:396)
        at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:369)
        at org.apache.spark.util.CompletionIterator.hasNext(CompletionIterator.scala:32)
        at org.apache.spark.InterruptibleIterator.hasNext(InterruptibleIterator.scala:39)
        at scala.collection.Iterator$$anon$11.hasNext(Iterator.scala:369)
        at org.apache.spark.sql.execution.UnsafeExternalRowSorter.sort(UnsafeExternalRowSorter.java:167)
        at org.apache.spark.sql.execution.Sort$$anonfun$1.apply(Sort.scala:90)
        at org.apache.spark.sql.execution.Sort$$anonfun$1.apply(Sort.scala:64)
        at org.apache.spark.rdd.RDD$$anonfun$mapPartitionsInternal$1$$anonfun$apply$21.apply(RDD.scala:728)
        at org.apache.spark.rdd.RDD$$anonfun$mapPartitionsInternal$1$$anonfun$apply$21.apply(RDD.scala:728)
        at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:38)
        at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:306)
        at org.apache.spark.rdd.RDD.iterator(RDD.scala:270)
        at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:38)
        at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:306)
        at org.apache.spark.rdd.RDD.iterator(RDD.scala:270)
        at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:38)
        at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:306)
        at org.apache.spark.rdd.RDD.iterator(RDD.scala:270)
        at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:38)
        at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:306)
        at org.apache.spark.rdd.RDD.iterator(RDD.scala:270)
        at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:38)
        at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:306)
        at org.apache.spark.rdd.RDD.iterator(RDD.scala:270)
        at org.apache.spark.rdd.ZippedPartitionsRDD2.compute(ZippedPartitionsRDD.scala:88)
        at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:306)
        at org.apache.spark.rdd.RDD.iterator(RDD.scala:270)
        at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:38)
        at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:306)
        at org.apache.spark.rdd.RDD.iterator(RDD.scala:270)
        at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:38)
        at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:306)
        at org.apache.spark.rdd.RDD.iterator(RDD.scala:270)
        at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:66)
        at org.apache.spark.scheduler.Task.run(Task.scala:89)
        at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:214)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
        at java.lang.Thread.run(Thread.java:745)
16/04/23 23:12:31 INFO shuffle.RetryingBlockFetcher: Retrying fetch (1/3) for 1 outstanding blocks after 5000 ms

## Cause

1. The buffer between the JVM heap size and the amount of memory requested from YARN is too small.

2. The netty transfer service will use off-heap buffers (whereas the NIO service doesn't).

Note: this issue will only happen when some table size is larger than 50GB.

## Solution

The current state of the art is to increase 
One way is to increase `spark.yarn.executor.memoryOverhead` until the job stops failing. 

    --conf spark.yarn.executor.memoryOverhead=2048M

## References

http://stackoverflow.com/questions/29850784/what-are-the-likely-causes-of-org-apache-spark-shuffle-metadatafetchfailedexcept 

http://apache-spark-developers-list.1001551.n3.nabble.com/Lost-executor-on-YARN-ALS-iterations-td7916.html 

https://issues.apache.org/jira/browse/SPARK-4516?focusedCommentId=14220157&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14220157
