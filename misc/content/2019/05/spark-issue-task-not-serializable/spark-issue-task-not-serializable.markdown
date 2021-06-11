Status: published
Date: 2021-03-22 10:11:48
Author: Benjamin Du
Slug: spark-issue-task-not-serializable
Title: Spark Issue: Task Not Serializable
Category: Computer Science
Tags: programming, Spark, issue, serialiation, error, big data, Spark issue
Modified: 2021-03-22 10:11:48

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Please refer to
[Spark Issue: _Pickle.Picklingerror: Args[0] from __Newobj__ Args Has the Wrong Class](http://www.legendu.net/misc/blog/spark-issue:-_pickle.PicklingError:-args[0]-from-__newobj__-args-has-the-wrong-class)
for a similar serialization issue in PySpark.

## Error Message

> org.apache.spark.SparkException: Job aborted due to stage failure: Task not serializable: java.io.NotSerializableException: ...

## Possible Causes

Some object sent to works from the driver is not serializable. 

## Solutions

1. Don't send the non-serializable object to workers.

2. Use a serializable version if you do want to send the object to workders.

## References

https://github.com/databricks/spark-knowledgebase/blob/master/troubleshooting/javaionotserializableexception.md
