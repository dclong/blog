Status: published
Date: 2016-10-25 18:45:40
Author: Ben Chuanlong Du
Title: Volatile CTE and Subqueries in SQL
Slug: volatile-cte-and-subqueries-in-sql
Category: Computer Science
Tags: programming, CTE, SQL, volatile, with, subquery, sub query
Modified: 2020-10-25 18:45:40

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. A volatile table persistents in the duration of the connection that creates it
    while a CTE is only accessible by the query following it.
    That is the scope of CTE is narrower and is safer.

1. If performance is a concern, use volatile (temp) tables.

2. Always use a CTE (with clause) instead of a sub query when applicable
    as a CTE is more flexible (can be recursive),
    is reusable,
    and is more readable.

3. A CTE can be recursive and is reusable.

## References

https://www.alisa-in.tech/post/2019-10-02-ctes/

https://stackoverflow.com/questions/706972/difference-between-cte-and-subquery

https://learnsql.com/blog/sql-subquery-cte-difference/

[Common Table Expression (CTE)](http://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-cte.html)