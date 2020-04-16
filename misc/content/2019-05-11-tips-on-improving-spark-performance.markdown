Status: published
Date: 2019-06-17 00:10:10
Author: Benjamin Du
Slug: tips-on-improving-spark-performance
Title: Tips on Improving Spark Performance
Category: Computer Science
Tags: programming, Spark, performance, tuning

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. Prefer the method `reduceByKey` over the method `groupByKey` when aggregating a RDD object in Spark.

2. Be cautious about the method `RDD.collect` as it retrieves all data in an RDD/DataFrame to the driver.
    This will likely cause an out-of-memory issue if the RDD/DataFrame is big.
    Even if not, 
    it will make your Spark application run slowly.

## Data Serialization

According to https://spark.apache.org/docs/latest/tuning.html#data-serialization,
Spark 2.0.0+ internally uses the Kryo serializer 
when shuffling RDDs with simple types, arrays of simple types, or string type 
and Spark automatically includes Kryo serializers for the many commonly-used core Scala classes 
covered in the AllScalaRegistrar from the Twitter chill library. 
So unless one uses customized classes inside RDD/DataFrame, 
there is little benefit to switch to kryo for serialization.
When you do use customized classes and/or complicated nested data structures in big DataFrames, 
you might want to consider using the Kryo serializer.

## Joins

1. Spark automatically decides which kind of joins (Broadcast Join, Sort Merge Join, Bucket Join) to perform. 
  Generally speaking,
  you should not change the default threshold for deciding which join to use.

2. Do NOT split a medium sized table and boradcast each splitted part. 
  Just let Spark pick the right join (which will be the Sort Merge Join) in this case.
  Also notice that the splitting tricky might not work in non-inner joins.

3. Make sure that keys to join in Spark DataFrames have the same type!
  When joining 2 large DataFrames in Spark, 
  Bucket Join is usually the best approach.
  However, 
  if the keys in the 2 DataFrame have inconsistent types 
  the bucket table will do a type cast 
  which makes Spark think the value of the original column is not enough resulting in Sort Merge Join (instead of Bucket Join).

## Speculation

1. Generally speaking, 
  it is not a good idea to turn on speculation in Spark. 
  The reason is that is is usually very tricky to define "slowness".
  There are 3 levels of time out: process -> node -> rack
  through `spark.locality.wait.<level_name>`.
  The default setting is 3s in the global timeout setting (`spark.locality.wait`)
  which is comparatively too short in shared computer clusters in many companies.


## UDFs vs map/flatMap

1. Most spark operations are column-oriented. 
  If you want to do some operation that is hard to expression as column expressions
  but is rather very easy to express as row expressions,
  you can either use UDFs or the `map`/`flatMap` methods.
  Currently, 
  the methods `map`/`flatMap` of DataFrame are still experimental
  so you'd use UDFs at this time.

## When to Reshuffle

1. Situations (e.g., merging small files or splitting huge files) that requires explicitly increasing or decreasing the number of RDD partiitons.

2. Before multiple bucket joins, it is usually benefical to repartition DataFrames by the same key.

[Cost Based Optimizer in Apache Spark 2.2](https://databricks.com/blog/2017/08/31/cost-based-optimizer-in-apache-spark-2-2.html)


## References

[Tuning Spark](https://spark.apache.org/docs/latest/tuning.html)

https://github.com/databricks/spark-knowledgebase

