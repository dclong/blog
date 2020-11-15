Status: published
Date: 2020-11-14 20:37:13
Author: Ben Chuanlong Du
Slug: column-alias-in-sql
Title: Column Alias in SQL
Category: Computer Science
Tags: programming, SQL, column alias, Teradata, Oracle

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. Logically any `SELECT` is processed in following order:

    1. from
    2. where
    3. group by
    4. having
    5. olap functions
    6. qualify
    7. select 
    8. sample
    9. order by

    Besides the proprietary `QUALIFY/SAMPLE` every DBMS will do it exactly the same.
    When you use a column alias in
    `where`, `group by`, `having`, window function or `qualify`
    the column list is not yet created, 
    thus using an alias should fail.
    However, 
    there are a few exceptions.  
    Both Teradata SQL and MySQL allows using column aliases in
    `where`, `group by`, `having`, `olap functions` and `qualify`.
    For those SQL variants which do not support using a column alias
    in `where`, `group by`, `having`, window functions or `qualify`,
    you can use subqueries instead.
    In some situations, 
    Spark SQL has an extra use DataFrame APIs which does not run into column alias issues.

2. Even if column aliases are allowed in Teradata and MySQL, 
    you should never alias to an existing column name 
    to avoid confusing the optimizer and/or end user).
    If you do alias to an existing column name in Teradata,
    the original column instead of the alias is used 
    in `where`, `group byy`, `having`, window function or `qualify`.

## Allow Column Alias 

1. Teradata SQL
2. MySQL

## Disallow Column Alias 

1. Spark SQL
2. Oracle SQL
