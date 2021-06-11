Status: published
Date: 2019-06-16 23:45:42
Author: Benjamin Du
Slug: tips-on-spark-mllib
Title: Tips on Spark MLlib
Category: Computer Science
Tags: programming, Spark, big data, MLlib, machine learning, AI
Modified: 2019-06-16 23:45:42

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Spark MLlib RDD-based API supports 
    [stratified sampling](https://spark.apache.org/docs/latest/mllib-statistics.html#stratified-sampling)
    but the DataFrame-based API hasn't implemented it yet as of Spark 2.4.3.

sample keys (not rows) with equal probability


## References

https://spark.apache.org/docs/latest/ml-guide.html

https://spark.apache.org/docs/latest/ml-statistics.html
