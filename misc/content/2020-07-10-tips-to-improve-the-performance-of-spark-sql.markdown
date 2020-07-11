Status: published
Date: 2020-07-10 19:16:59
Author: Benjamin Du
Slug: tips-to-improve-the-performance-of-spark-sql
Title: Tips to Improve the Performance of Spark SQL
Category: Computer Science
Tags: Computer Science

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

4. Persist a DataFrame which is used multiple times.

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