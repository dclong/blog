Status: published
Date: 2019-05-11 01:34:21
Author: Benjamin Du
Slug: spark-issue-task-not-serializable
Title: Spark Issue Task Not Serializable
Category: Computer Science
Tags: programming

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Error Message

> org.apache.spark.SparkException: Job aborted due to stage failure: Task not serializable: java.io.NotSerializableException: ...

## Possible Causes

Some object sent to works from the driver is not serializable. 

## Solutions

1. Don't send the non-serializable object to workers.

2. Use a serializable version if you do want to send the object to workders.

## References

https://github.com/databricks/spark-knowledgebase/blob/master/troubleshooting/javaionotserializableexception.md
