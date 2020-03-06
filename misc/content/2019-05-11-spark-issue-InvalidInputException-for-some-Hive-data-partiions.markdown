Status: published
Date: 2019-05-11 02:50:52
Author: Benjamin Du
Slug: spark-issue-InvalidInputException-for-some-Hive-data-partiions
Title: Spark Issue Invalidinputexception for Some Hive Data Partiions
Category: Computer Science
Tags: programming, Spark, issue, big data

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

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

Solution: add this 'hidden' parameter to the submit job to force check the path

    --conf spark.sql.hive.verifyPartitionPath=true
