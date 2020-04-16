Status: published
Date: 2019-10-31 11:28:19
Author: Benjamin Du
Slug: spark-sql-tips
Title: Spark SQL Tips
Category: Computer Science
Tags: programming, big data, Spark, Spark SQL

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

[Spark SQL Guide](https://docs.databricks.com/spark/latest/spark-sql/index.html)


0. It is suggested that you use Spark SQL syntax as much as possible 
  instead of the the Spark DataFrame syntax (even though DataFrame provides more static syntax check)
  as SQL is a universal language.

1. `spark.sql` accepts only a single SQL statement (`;` is not allowed in the statement) 
    and returns a DataFrame. 
    When the SQL statement passed in is a Data Query Language (DQL), such as `select`,
    the result of the query is returned as a DataFrame.
    When the SQL statement passed in is a Data Definition Language (DDL) or Data Manipulation Language (DML), 
    such as `create`,
    an empty DataFrame is returned.

1. Spark SQL follows hive sql syntax.
    For example,
    `spark.sql("show tables in some_schema like '*perf*'")`
    returns a DataFrame with tables in the Hive database.

2. JSON, ORC, Parquet and CSV files can be queried using Spark SQL without creating a table on the Spark DataFrame.

        :::sql
        select
            *
        from
            csv.`hdfs://cluster_name/path_to_csv`
        where
            rand() <= 0.01
        distribute by
            rand()
        sort by
            rand()
        limit 10000

3. Position alias is supported in Spark SQL!

4. Spark SQL supports bool expressions/columns. 
  However, you cannot sum a bool expression/column directly.
  You have to either cast it to Int/BigInt or use the old-school case clause.

5. `select * from some_table limit 5` runs slow if the table `some_table` is large.
  you can limit the selection to a specific partition (if the table is partitioned) to speed it up.


6. You can use the following code to show the creation code of a Hive table in Spark.
```
println(spark.sql("show create table some_table").collect()(0)(0))
```

## Spark SQL Create Table

1. The `CREATE TABLE` clause is equivalent to the method `DataFrame.saveAsTable`,
  which write the DataFrame into a Hive table (format of the Hive table can be specified).
  You can also create (or replace) a global/temporary view, 
  which is lazily computed.
  Notice that a view can be cached too once computed if you explicitly do so
  (by calling `spark.cacheTable` or use Spark SQL hint).

## Union

The following queries work.

    :::sql
    SELECT * FROM db.table WHERE col IS NULL
    UNION
    SELECT * FROM db.table WHERE col < 0

    :::sql
    (SELECT * FROM db.table WHERE col IS NULL LIMIT 10)
    UNION
    (SELECT * FROM db.table WHERE col < 0 LIMIT 10)

    :::sql
    (SELECT * FROM db.table WHERE col IS NULL LIMIT 10)
    UNION ALL
    (SELECT * FROM db.table WHERE col < 0 LIMIT 10)

However, the following one does not.

      :::sql
      SELECT * FROM db.table WHERE col IS NULL LIMIT 10
      UNION
      SELECT * FROM db.table WHERE col < 0 LIMIT 10

It is suggested that you always enclose subqueries in parentheses!

## Spark SQL Hint

1. You can use 
  [Spark SQL hint](https://docs.databricks.com/spark/latest/spark-sql/language-manual/select.html#hints)
  to fine control the behavior of Spark application.
  Specially, 
  a hint for skew join is supported in Spark Spark!
  You can use it to help Spark optimizing the joining when the involved columns are skewed.

### COALESCE and REPARTITION Hints

```
SELECT /*+ COALESCE(5) */ ...

SELECT /*+ REPARTITION(3) */ ...
```
### Join Hints
```
SELECT /*+ MAPJOIN(b) */ ...

SELECT /*+ BROADCASTJOIN(b) */ ...

SELECT /*+ BROADCAST(b) */ ...

SELECT /*+ RANGE_JOIN(points, 10) */ *
FROM points JOIN ranges ON points.p >= ranges.start AND points.p < ranges.end;

SELECT /*+ RANGE_JOIN(r1, 0.1) */ *
FROM (SELECT * FROM ranges WHERE ranges.amount < 100) r1, ranges r2
WHERE r1.start < r2.start + 100 AND r2.start < r1.start + 100;

SELECT /*+ RANGE_JOIN(C, 500) */ *
FROM a
  JOIN b ON (a.b_key = b.id)
  JOIN c ON (a.ts BETWEEN c.start_time AND c.end_time)
```
### Skew Hint
```
SELECT /*+ SKEW('orders') */ * FROM customers, orders WHERE o_custId = c_custId
SELECT /*+ SKEW('orders'), BROADCAST(demographic) */ * FROM orders, customers, demographic WHERE o_custId = c_custId AND c_demoId = d_demoId
```

## Spark SQL Examples

    :::SQL
    CREATE TABLE trans (
         col1 TYPE1,
         col2 TYPE2,
         col3 TYPE3
    ) USING Parquet OPTIONS (
      `serialization.format` '1',
      path 'viewfs://...'
    )

    CREATE TABLE trans 
        USING Parquet
        LOCATION '/path/to/table' AS
    SELECT * FROM some_table WHERE id = 1
  
## References

https://stackoverflow.com/questions/41254011/sparksql-read-parquet-file-directly

http://www.joefkelley.com/736/

https://jaceklaskowski.gitbooks.io/mastering-spark-sql/spark-sql-hint-framework.html#specifying-query-hints
