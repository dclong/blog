Status: published
Date: 2019-05-05 09:10:38
Author: Benjamin Du
Slug: improve-spark-performance
Title: Improve the Performance of Spark
Category: Computer Science
Tags: programming, Computer Science, Spark, tuning, Spark SQL, SQL, performance, database, big data
Modified: 2020-10-05 09:10:38


**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. Use Parquet as the data store format.

    While Spark/Hive supports many different data formats, 
    Parquet is the optimal data format to use.

2. Use partitioned or bucketed table (on the right columns) when the table is large (>100,000 rows).

3. Accelerate table scan by adding proper filter conditions.

    Use proper filter conditions in your SQL statement to avoid full table scan. 
    Proper filter conditions on Partition, Bucket and Sort columns 
    helps Spark SQL engine to fast locate target dataset to avoid full table scan,
    which accelerates execution.

4. Persist a DataFrame which is used multiple times and expensive to recompute.
    Remembe to unpersist it too when the DataFrame is no longer needed. 
    Even Spark evict data from memory using the LRU (least recently used) strategy
    when the caching layer becomes full,
    it is still beneficial to unpersist data as soon as it is no used any more to reduce memory usage.

5. Add cast for join key to use bucket

    Joining columns of different types prevents Spark SQL from doing the best optimization.
    A simple fix is to cast columns to be the same type when joining them.
    For example,
    let's assume `A.id` is `Decimal(18, 0)` 
    and `B.id` is `BigInt`.
    Use

        SELECT 
            A.* 
        FROM
            A
        INNER JOIN 
            B
        ON 
            cast(A.id AS BigInt) = B.id 

    instead of

        SELECT 
            A.* 
        FROM
            A
        INNER JOIN 
            B
        ON 
            A.id = B.id 

5. BroadcastHashJoin, i.e., map-side join is fast. 
    Use BroadcastHashJoin if possible. 
    Notice that BroadcastHashJoin only works for inner joins. 
    If you have a outer join,
    BroadcastHashJoin won't happend even if you explicitly Broadcast a DataFrame.

1. Several smaller queries (achieving the same functionality) is preferred to 
    a big query (using complex features and/or subqueries).
    For example,
    `window_function(...) over (partition by ... order by ...)` 
    can be achieved using a `group by` followed with a inner join.
    The latter approach (using `group by` + `inner join`) runs faster in Spark SQL generally speaking.

2. Spark DataFrame is lazily computed but computed again if needed.
    It can greatly boost the perfromance of your Spark application
    if you cache/persist the intermediate Spark DataFrame 
    which is used in mutliple places.
    Notably,
    if a Spark DataFrame containing randomly generately values
    and is used in multiple places,
    you must cache/persist it to ensure the correct logic
    (otherwise the DataFrame will have different values each time it is used).

3. Enable dynamic allocation but with a limit on the max number of executors.

        :::bash
        ...
        --conf spark.dynamicAllocation.enabled=true \
        --conf spark.dynamicAllocation.maxExecutors=1000 \
        ...

4. Enable adaptive query execution in Spark 3.0+.

        :::bash
        ...
        --conf spark.adaptive.query.execution=true \
        ...

2. Prefer the method `reduceByKey` over the method `groupByKey` when aggregating a RDD object in Spark.

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

2. Notice that BroadcastJoin only works for inner joins. 
    If you have a outer join,
    BroadcastJoin won't happend even if you explicitly Broadcast a DataFrame.

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

