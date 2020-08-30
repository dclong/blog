Status: published
Date: 2020-08-29 22:05:22
Author: Benjamin Du
Slug: spark-issue-duplicated-partitions
Title: Spark Issue: Duplicated Partitions
Category: Computer Science
Tags: programming, Spark, issue, duplicate, overwrite, big data

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

There seems to be an issue in Spark that it might fail to overwrite files 
even if mode of `spark.write` is set to be "overwrite".
