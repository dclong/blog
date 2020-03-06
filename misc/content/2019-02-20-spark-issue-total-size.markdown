Status: published
Date: 2019-02-20 20:37:59
Author: Benjamin Du
Slug: spark-issues-and-solutions
Title: Total Size of Serialized results is bigger than spark.driver.maxResultSize
Category: Computer Science
Tags: programming, Spark, issues, solutions, big data

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Issue

Total size of serialized results is bigger than spark.driver.maxResultSize

## Solutions

1. Eliminate unnecessary `broadcast` or `collect`.

2. Make `spark.driver.maxResultSize` larger.

    - set by SparkConf: `conf.set("spark.driver.maxResultSize", "3g")`

    - set by spark-defaults.conf: `spark.driver.maxResultSize 3g`

    - set when calling spark-submit: `--conf spark.driver.maxResultSize=3g`


## References

https://spark.apache.org/docs/latest/configuration.html

https://www.hackingnote.com/en/spark/trouble-shooting/total-size-is-bigger-than-maxResultSize

https://issues.apache.org/jira/browse/SPARK-17556

https://forums.databricks.com/questions/66/how-do-i-work-around-this-error-when-using-rddcoll.html

https://stackoverflow.com/questions/46763214/total-size-of-serialized-results-of-tasks-is-bigger-than-spark-driver-maxresults


