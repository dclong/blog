Status: published
Date: 2019-05-11 02:50:52
Author: Benjamin Du
Slug: spark-issue-table-not-found
Title: Spark Issue Table Not Found
Category: Computer Science
Tags: programming, Spark, issue, big data

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

Solution: include Hive configuration of the Spark cluster when submitting Spark jobs.

    --files "/apache/spark_scala211/conf/hive-site.xml"
