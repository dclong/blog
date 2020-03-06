Status: published
Date: 2020-02-19 15:56:43
Author: Benjamin Du
Slug: Use-tablesample-in-sql
Title: Use TableSample in SQL
Category: Computer Science
Tags: programming, SQL, Spark, Spark SQL, PostgreSQL, TableSample

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

The limit clause (or the method `DataFrame.limit` if you are using Spark)
is a better alternative if randomness is not critical.

## PostgreSQL

    :::sql
    SELECT id from table TABLESAMPLE BERNOULLI(10) WHERE age < 20 LIMIT 30;

CANNOT use

    :::sql
    SELECT id from table WHERE age < 20 TABLESAMPLE BERNOULLI(10) LIMIT 30;

One possible way is to create a temporary table first. 

## Spark SQL

Similar to PostgreSQL.
However, 
Spark has DataFrame APIs
and you can use the method `DataFrame.sample` to achieve the same purpose.
Notice that `DataFrame.sample` accepts only fraction (double value between 0 and 1)
instead of number of rows (integer value) as the parameter.
