UUID: 1ed7fbf4-fbcc-44be-89b3-c4bc2df3970e
Status: published
Date: 2017-04-08 15:47:42
Author: Ben Chuanlong Du
Slug: using-sql-in-r
Title: Using SQL in R
Category: Programming
Tags: programming, CRAN, SQL, database, RJDBC, teradataR, RODBC
Modified: 2017-04-08 15:47:42

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

1. It is suggested that you do not use paste to concatenate SQL queries, 
but rather have a complete SQL query with special marked variables 
and then substitute the marked variables with aproprivate values. 
This makes the SQL code much easier to understand. 
For example,
```R
q = "
select
    id,
    name
from
    table
where
    id in (${IDs})
"
```
You can then substitute `${IDs}` with the right values.  
Some people might against this due to injection attack,
but I really do not think this is a problem 
as database users usually do not have write permissions to public tables.
I value readability more here.

## JDBC

1. `RJDBC` is a usable but has some glitches.

1. You cannot end a SQL statement with a semicolon when using `RJDBC`.
This means that you can send only a single query at a time when using `RJDBC`,
which is not efficient.

2. `RJDBC::dbWriteTable` has a bug for Teradata. 
As an workaround, 
you can generate SQL statement to insert data by yourself
(which is tedious of course). 

3. RJDBC has a bug on schema when checking whether a table exists or not.
For exampel, if there is a (non volatile) table `p_chdu_t.employees`.
'dbExistsTable('employees')' returns `TRUE` 
but `dbExistsTable('p_chdu_t.employees')` returns `FALSE`.
This impacts server functions in RJDBC.

## ODBC

1. RODBC

2. teradataR


