Status: published
Date: 2019-08-29 02:14:51
Author: Benjamin Du
Slug: spark-issue-duplicated-partitions
Title: Spark Issue Duplicated Partitions
Category: Computer Science
Tags: programming, Spark, issue, duplicate, overwrite

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

There seems to be an issue in Spark that it might fail to overwrite files even if mode of `spark.write` is set to be "overwrite".
