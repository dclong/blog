Status: published
Date: 2020-08-29 22:05:22
Author: Benjamin Du
Slug: spark-issue-table-not-found
Title: Spark Issue: Table Not Found
Category: Computer Science
Tags: programming, Spark, issue, big data, error

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Solution: include Hive configuration of the Spark cluster when submitting Spark jobs.

    --files "/apache/spark_scala211/conf/hive-site.xml"
