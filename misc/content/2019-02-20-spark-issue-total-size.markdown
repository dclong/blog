Status: published
Date: 2020-08-29 22:05:22
Author: Benjamin Du
Slug: spark-issues-and-solutions
Title: Spark Issue: Total Size of Serialized Results Is Bigger than spark.driver.maxResultSize
Category: Computer Science
Tags: programming, Spark, issues, solutions, big data, error

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
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

