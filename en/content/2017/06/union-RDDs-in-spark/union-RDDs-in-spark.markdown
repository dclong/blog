Status: published
Date: 2020-11-03 23:49:38
Author: Ben Chuanlong Du
Slug: union-RDDs-in-spark
Title: Union RDDs in Spark
Category: Computer Science
Tags: programming, Scala, Spark, RDD, union
Modified: 2020-11-03 23:49:38


No deduplication is done (to be efficient) when unioning RDDs/DataFrames in Spark 2.1.0+.

1. Union 2 RDDs.

        df1.union(df2)
        // or for old-fashioned RDD
        rdd1.union(rdd_2)

2. Union multiple RDDs.

        df = spark.union([df1, df2, df3]) // spark is a SparkSession object
        // or for old-fashioned RDD
        rdd = sc.union([rdd1, rdd2, rdd3]) // sc is a SparkContext object

## References 

[Union DataFrames in Spark](http://www.legendu.net/misc/blog/spark-dataframe-union)

[Union DataFrames in Spark](http://www.legendu.net/en/blog/spark-dataframe-union)