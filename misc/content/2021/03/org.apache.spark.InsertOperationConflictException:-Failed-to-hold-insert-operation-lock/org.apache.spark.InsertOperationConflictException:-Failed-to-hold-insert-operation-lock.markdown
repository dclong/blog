Status: published
Date: 2021-03-24 14:57:29
Author: Benjamin Du
Slug: spark-issue-InsertOperationConflictException-failed-to-hold-insert-operation-lock
Title: Spark Issue: InsertOperationConflictException: Failed to Hold Insert Operation Lock
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, Spark issue, InsertOperationConflictException, fail, hold, insert operation lock, big data

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Symptom

org.apache.spark.InsertOperationConflictException: Failed to hold insert operation lock ...

## Cause

Multiple Spark applications attempts to write to the same directory at the same time.

## Solution

Resubmit your Spark application with a different output path 
or make sure that it is the only application writing to the output path.  