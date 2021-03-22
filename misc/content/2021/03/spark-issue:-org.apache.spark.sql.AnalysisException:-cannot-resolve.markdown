Status: published
Date: 2021-03-22 10:21:18
Author: Benjamin Du
Slug: spark-issue:-org.apache.spark.sql.AnalysisException:-cannot-resolve
Title: Spark Issue: Org.Apache.Spark.Sql.Analysisexception: Cannot Resolve
Category: Computer Science
Tags: Computer Science, programming, Spark, issue, AnalysisException, cannot resolve, Spark issue, big data

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Symptom

org.apache.spark.sql.AnalysisException: cannot resolve ...

## Cause

Miss-spell a column name or refer to a column which does not exist in the DataFrame.

## Solution

Correct the column name or add the missing column in the `select` method before using it.
