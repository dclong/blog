Status: published
Date: 2021-03-22 09:53:20
Author: Benjamin Du
Slug: spark-issue-table-not-found
Title: Spark Issue: Table not found
Category: Computer Science
Tags: programming, Spark, issue, big data, error, Spark issue, hive-site.xml

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Symptom 1

org.apache.spark.sql.AnalysisException: Table not found

## Symptom 2

java.lang.RuntimeException: Table Not Found: my_rdd

## Cause 1

Miss-spelled a table name.

## Solution 1

Correct miss-spelling.

## Cause 2

Forgot to submit a `hive-site.xml` together with the Spark application.

## Solution 2

Include Hive configuration of the Spark cluster when submitting Spark jobs.

    :::bash
    --files "/apache/spark/conf/hive-site.xml"
