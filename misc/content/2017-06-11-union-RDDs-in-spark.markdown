Status: published
Date: 2019-05-09 19:43:10
Author: Ben Chuanlong Du
Slug: union-RDDs-in-spark
Title: Union RDDs in Spark
Category: Computer Science
Tags: programming, Scala, Spark, RDD, union

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


No deduplication is done (to be efficient) when unioning RDDs/DataFrames in Spark 2.1.0+.

1. Union 2 RDDs.

        df1.union(df2)
        // or for old-fashioned RDD
        rdd1.union(rdd_2)

2. Union multiple RDDs.

        df = spark.union([df1, df2, df3]) // spark is a SparkSession object
        // or for old-fashioned RDD
        rdd = sc.union([rdd1, rdd2, rdd3]) // sc is a SparkContext object
