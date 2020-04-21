UUID: d312b5b7-20b3-4441-bb39-0c1d8a4b33c8
Status: published
Date: 2016-10-23 12:35:49
Author: Ben Chuanlong Du
Slug: volatile-cte-and-subqueries-in-sql
Title: Volatile Cte and Subqueries in SQL
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
