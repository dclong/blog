Status: published
Date: 2020-10-30 09:27:28
Author: Benjamin Du
Slug: Use-tablesample-in-sql
Title: Use TableSample in SQL
Category: Computer Science
Tags: programming, SQL, Spark, Spark SQL, PostgreSQL, TableSample

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

The limit clause (or the method `DataFrame.limit` if you are using Spark)
is a better alternative if randomness is not critical.

## PostgreSQL

    :::sql
    SELECT id from table TABLESAMPLE BERNOULLI(10) WHERE age < 20 LIMIT 30;

CANNOT use

    :::sql
    SELECT id from table WHERE age < 20 TABLESAMPLE BERNOULLI(10) LIMIT 30;

Notice that `WHERE` is applied after `TABLESAMPLE`.
If you want to filter a table first and then do a sampling, 
you can create a temporary table first.

## Spark SQL

Similar to PostgreSQL.
However, 
Spark has DataFrame APIs
and you can use the method `DataFrame.sample` to achieve the same purpose.
Notice that `DataFrame.sample` accepts only fraction (double value between 0 and 1)
instead of number of rows (integer value) as the parameter.
As a matter of fact,
sampling a specific number of rows in Spark does not performance a simple random sampling,
it is implemented as `LIMIT`
It is suggested that you always sample a fraction instead of sampling a specific number of rows in Spark 
if randomness is important. 

    # avoid 
    select * from table_name TABLESAMPLE (100 ROWS) 
    # use the following instead
    select * from table_name TABLESAMPLE (1 PCT) 

## References

- [Sample Rows from a Spark DataFrame](http://www.legendu.net/en/blog/spark-dataframe-sample)

- [SQL Equivalent](http://www.legendu.net/misc/blog/sql-equivalent)

- https://stackoverflow.com/questions/51502443/is-sample-n-really-a-random-sample-when-used-with-sparklyr