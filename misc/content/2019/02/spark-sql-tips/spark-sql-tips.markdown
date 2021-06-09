Status: published
Date: 2021-02-20 09:03:19
Author: Benjamin Du
Slug: spark-sql-tips
Title: Spark SQL
Category: Computer Science
Tags: programming, big data, Spark, Spark SQL, Hive

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

[Spark SQL Guide](https://docs.databricks.com/spark/latest/spark-sql/index.html)


1. Since a Spark DataFrame is immutable,
    you cannot update or delete records from a physical table (e.g., a Hive table) directly
    using Spark DataFrame/SQL API.
    However, 
    updating/deleting records from a data lake table becomes feasible in Spark
    with the help of Delta Lake.
    There are lots of other cool features introduced in Delta Lake too!

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
    `spark.sql("SHOW tables IN some_schema LIKE '*perf*'")`
    returns a DataFrame with tables in the Hive database.

2. JSON, ORC, Parquet and CSV files can be queried using Spark SQL without creating a table on the Spark DataFrame.

        :::sql
        SELECT
            *
        FROM
            csv.`hdfs://cluster_name/path_to_csv`
        WHERE
            rand() <= 0.01
        DISTRIBUTE BY
            rand()
        SORT BY
            rand()
        LIMIT 10000

3. Position alias is supported in Spark SQL!

4. Spark SQL supports bool expressions/columns. 
    However, you cannot sum a bool expression/column directly.
    You have to either cast it to Int/BigInt or use the old-school case clause.

5. `SELECT * FROM some_table LIMIT 5` runs slow if the table `some_table` is large.
    you can limit the selection to a specific partition (if the table is partitioned) to speed it up.


6. You can use the following code to show the creation code of a Hive table in Spark.

        :::scala
        println(spark.sql("SHOW CREATE TABLE some_table").collect()(0)(0))

7. Check if a table exists.
    If you are using Scala.

        :::scala
        spark.catalog.tableExists(table)

    Or if you are using PySpark.

        :::scala
        spark.catalog._jcatalog.tableExists("schema.table")

    https://stackoverflow.com/questions/46477270/spark-scala-how-can-i-check-if-a-table-exists-in-hive

    https://spark.apache.org/docs/2.1.0/api/java/org/apache/spark/sql/catalog/Catalog.html
    
## Data Types

https://acadgild.com/blog/hive-complex-data-types-with-examples

## Spark SQL Create Table

1. The `CREATE TABLE` clause is equivalent to the method `DataFrame.saveAsTable`,
    which write the DataFrame into a Hive table (format of the Hive table can be specified).
    You can also create (or replace) a global/temporary view, 
    which is lazily computed.
    Notice that a view can be cached too once computed if you explicitly do so
    (by calling `spark.cacheTable` or use Spark SQL hint).

https://www.youtube.com/watch?v=RipzhSw2z70

https://www.revisitclass.com/hadoop/how-to-create-a-table-with-partitions-in-hive/

https://docs.cloudera.com/documentation/enterprise/5-8-x/topics/impala_create_table.html

    :::sql
    CREATE TABLE default.cs_itm_text_featr (
        item_id BigInt,
        vrsn_id String,
        prcs_dt String,
        score_bert Double,
        score_ebert Double,
        score_xlnet Double,
        embd_bert Array<Double>,
        embd_ebert Array<Double>,
        embd_xlnet Array<Double>
    ) USING PARQUET 
    PARTITIONED BY (
        site_id Int,
        auc_end_dt String
    );

    CREATE TABLE cust_sci.image_quality_score (
        item_id BigInt,
        image_url String,
        guid String,
        type String,
        score double,
        prcs_dt String
    ) PARTITIONED BY (
        site_id Int
    ) CLUSTERED BY (
        image_url
    ) into 400 buckets
    ;

## Insert 

https://mapr.com/docs/61/Hive/INSERTINTOnestedMapr-DB-JSONwithHive.html

[Writing Into Dynamic Partitions Using Spark](https://medium.com/a-muggles-pensieve/writing-into-dynamic-partitions-using-spark-2e2b818a007a)

https://dwgeek.com/hive-insert-from-select-statement-and-examples.html/

https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DML#LanguageManualDML-InsertingvaluesintotablesfromSQL

https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.6.5/bk_data-access/content/new-feature-insert-values-update-delete.html

https://docs.databricks.com/spark/latest/spark-sql/language-manual/insert.html

insert complicated data types
1. use a dummy table
2. use with to create a dummy table
3. put it into insert ... select
4. Partition columns need to be handled specially in an INSERT statement
    however,
    cluster columns do not need special handling in an INSERT statement. 
    Considered the table cust_sci.image_quality_score
    which has both partition and cluster columns,
    below is an example inserting query.

        INSERT INTO cust_sci.image_quality_score 
            PARTITION (site_id=0) 
        SELECT
            item_id,
            image_url,
            guid,
            'iipa',
            score,
            '2021-01-28'
        from 
            cust_sci.temp_score_iipa 
        ;

        :::sql
        INSERT INTO cs_itm_text_featr PARTITION (site_id=1, meta_categ_id, auc_start_dt) 
        SELECT 
            2,
            "2020-01-01",
            "0.0.1",
            "2020-05-01",
            0.1,
            0.2,
            0.3,
            Array(0.1, 0.2, 0.3),
            Array(0.2, 0.2, 0.3),
            Array(0.3, 0.4, 0.4),
            10,
            "2020-03-01"
        ;

        :::sql
        WITH DUMMY AS (
        SELECT 
            20,
            "2020-01-01",
            "0.0.1",
            "2020-05-01",
            0.1,
            0.2,
            0.3,
            Array(0.1, 0.2, 0.3),
            Array(0.2, 0.2, 0.3),
            Array(0.3, 0.4, 0.4),
            10,
            "2020-03-01"
        )
        INSERT INTO cs_itm_text_featr PARTITION (site_id=1, meta_categ_id, auc_start_dt) 
        SELECT * FROM DUMMY
        ;

        :::sql
        INSERT INTO cs_itm_text_featr PARTITION (site_id=1, meta_categ_id, auc_start_dt) values (
            110,
            "2020-01-01",
            "0.0.1",
            "2020-05-01",
            0.1,
            0.2,
            0.3,
            Array(0.1, 0.2, 0.3),
            Array(0.2, 0.2, 0.3),
            Array(0.3, 0.3, 0.4),
            10,
            "2020-03-01"
        );

    seems to me that it is not an issue any more ...

https://stackoverflow.com/questions/30446601/hive-inserting-values-to-an-array-complex-type-column

https://community.cloudera.com/t5/Support-Questions/Insert-values-in-Array-data-type-Hive/td-p/120459


SET hive.exec.dynamic.partition=true;
hive> SET hive.exec.dynamic.partition.mode=non-strict;
hive> SET hive.enforce.bucketing =true;​

## Hive Table Partition

https://www.youtube.com/watch?v=KjJJKgeyXVE

https://bigdataprogrammers.com/partition-in-hive/

https://www.youtube.com/watch?v=biH_l14KGqU

https://www.qubole.com/blog/5-tips-for-efficient-hive-queries/

https://www.javatpoint.com/dynamic-partitioning-in-hive

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

    :::sql
    SELECT /*+ COALESCE(5) */ ...
    SELECT /*+ REPARTITION(3) */ ...

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
