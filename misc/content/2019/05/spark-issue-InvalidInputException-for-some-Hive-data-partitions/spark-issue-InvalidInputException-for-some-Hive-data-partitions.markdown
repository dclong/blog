Status: published
Date: 2019-05-22 09:55:40
Author: Benjamin Du
Slug: spark-issue-InvalidInputException-for-some-Hive-data-partitions
Title: Spark Issue: InvalidInputException for Some Hive Data Partitions
Category: Computer Science
Tags: programming, Spark, issue, big data, error, InvalidInputException, Hive, Spark issue, partition
Modified: 2021-03-22 09:55:40

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Symptom

15/12/29 17:22:27 ERROR yarn.ApplicationMaster: User class threw exception: org.apache.hadoop.mapred.InvalidInputException: Input path does not exist.
org.apache.hadoop.mapred.InvalidInputException: Input path does not exist.
at org.apache.hadoop.mapred.FileInputFormat.singleThreadedListStatus(FileInputFormat.java:285)
at org.apache.hadoop.mapred.FileInputFormat.listStatus(FileInputFormat.java:228)
at org.apache.hadoop.mapred.SequenceFileInputFormat.listStatus(SequenceFileInputFormat.java:45)
at org.apache.hadoop.mapred.FileInputFormat.getSplits(FileInputFormat.java:304)
at org.apache.spark.rdd.HadoopRDD.getPartitions(HadoopRDD.scala:207)

## Cause

For some reason the HDFS path registered in the Hive meta store 
does not exist in the physical path - (Infra team should take care of this)

Solution: add the following configuration to force checking partition paths
when submiting Spark jobs.

    :::bash
    --conf spark.sql.hive.verifyPartitionPath=true
