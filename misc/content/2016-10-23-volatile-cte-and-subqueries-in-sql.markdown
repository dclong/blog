Status: published
Date: 2020-05-22 14:48:00
Author: Ben Chuanlong Du
Title: Volatile CTE and Subqueries in SQL
Slug: volatile-cte-and-subqueries-in-sql
Category: Computer Science
Tags: programming, CTE, SQL, volatile, with, subquery, sub query

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. A volatile table persistents in the duration of the connection that creates it
    while a CTE is only accessible by the query following it.
    That is the scope of CTE is narrower and is safer.

1. If performance is a concern, use volatile (temp) tables.

2. Always use CTE (with clause) instead of sub queries.
