UUID: dc85f9a3-6f9b-46b3-9b6e-115ea581b6aa
Status: published
Date: 2016-10-16 09:03:52
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


Logically any `SELECT` is processed in following order:

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
`where`, `group by`, `having`, `olap functions` or `quality`
the column list is not yet created, 
thus using an alias should fail.

However, there are a few exceptions.  
Both Teradata SQL and MySQL allows using column aliases in
`where`, `group by`, `having`, `olap functions` and `qualify`.
Even if column aliases are allowed in Teradata and MySQL, 
you should never alias to an existing column name 
to avoid confusing the optimizer and/or end user).
If you do alias to an existing column name in Teradata,
the original column instead of the alias is used 
in `where`, `group byy`, `having`, `olap functions` and `qualify`.

## Allow Column Alias 

1. Teradata SQL
2. MySQL

## Disallow Column Alias 

1. Oracle SQL
