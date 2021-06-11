UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2014-10-10 11:25:18
Author: Benjamin Du
Slug: understand-execuation-of-sql-statements
Title: Understand Execuation of SQL Statements
Category: Computer Science
Tags: programming, SQL, join on, having, where, group by, null value
Modified: 2016-06-10 11:25:18


A SQL statement selects rows and columns from a big (rectangular) table. 
You put columns that you want to select after `select` 
and rows you want to select after `from`.
A SQL statement is executed as follows.
First, 
the (inner|left|right|full) `join (on)` is executed if any (see more explanation later).
Second, 
the `where` condition is executed. Conditions before grouping (aggregation) must go into the `where` clause.
Third, 
`group by (having)` is executed. 
Conditions after grouping (aggregation) must go into the `having` clause.
Fourth, 
the `sort by` statement is executed if any.
Last, columns (specified in the `from` clause) are selected.

An `inner join` first creates a cross join of tables in the `join` clause 
(i.e., a Cartesian product of rows from tables in the `join` clause), 
then it selects rows satisfying the `on` condition from the cross join result. 
A `left/right/full join` consists of 2 sub steps. 
First, an `inner join (on)` is performed. 
Second, unmatched rows in the left/right/both table(s) are appended into the resulting table of `inner join (on)`. 
This means that all rows in the left/right/both table(s) will be in the resulting table
if there is no `where` or `having` condition in the query.
Notice that unmatched rows in the left/right/both table(s) uses `NULL` values for columns in the other table,
which is different from the Cartesian product (which uses values of the matched row). 
After joining, 
the `where` clause is executed. 
This means that the `where` condition is executed after the `on` condition in `join`. 
For an `inner join`, 
the `where` condition can be put in the `on` condition 
using `and` because no extras (unmatched rows) are appended after the `on` condition is executed. 
However, for a `left/right/full join` (extra unmatched rows are appended after `on` condition is executed) 
the `where` condition cannot be combined with the `on` condition (using `and`), generally speaking. 
For example,
```SQL
select *
from 
    A
inner join 
    B
on
    A.id = B.id
where 
    B.id > 10
;
```
returns the same result as 
```SQL
select *
from 
    A
inner join 
    B
on
    A.id = B.id and B.id > 10
;
```
However, 
```SQL
select *
from 
    A
left join 
    B
on
    A.id = B.id
where 
    B.id is null
;
```
returns different result from
```SQL
select *
from 
    A
left join 
    B
on
    A.id = B.id
where 
    B.id is null
;
```
generally speaking. 
For good practice, you'd better separate the `where` and `on` conditions.

Let's see some real examples to better understand the execution of SQL code.
Suppose we have 2 tables A and B (see below) both of which contain only 1 integer column named `id`.

|id|
|--:|
|1|
|2|
|3|
|4|
|5|
|6|
|7|
|8|
|9|
|10|
|11|
|12|
|13|
|14|
|15|

|id|
|--:|
|1|
|2|
|3|
|4|
|5|
|6|
|7|
|8|
|9|
|10|
|12|
|15|

The following presents some join queries and corresponding results.
Note that question marks (`?`) stand for null values in the following results.
```SQL
/*
A inner join B
Only matched rows are kept, which is easy to understand.
*/
select 
    A.id,
    B.id
from
    A
inner join
    B
on
    A.id = B.id
;
```
||A.id|B.id|
|::|:---:|:---:|
|1|6|6|
|2|3|3|
|3|10|10|
|4|12|12|
|5|9|9|
|6|4|4|
|7|5|5|
|8|1|1|
|9|15|15|
|10|8|8|
|11|2|2|
|12|7|7|
```SQL
/*
A left join B
Unmatched rows in A are kept but B.id is null for these unmatched rows.
*/
select 
    A.id,
    B.id
from
    A
left join
    B
on
    A.id = B.id
;
```
Notice `B.id` is set to null for rows in table A that do not have matching rows in table B.

||A.id|B.id|
|::|:---:|:---:|
|1|11|?|
|2|6|6|
|3|13|?|
|4|3|3|
|5|10|10|
|6|12|12|
|7|9|9|
|8|4|4|
|9|5|5|
|10|1|1|
|11|15|15|
|12|14|?|
|13|8|8|
|14|2|2|
|15|7|7|
```SQL
select 
    A.id,
    B.id
from
    A
left join
    B
on
    A.id = B.id
and 
   B.id > 10 
;
```
||A.id|B.id|
|::|:--:|:--:|
|1|11|?|
|2|6|?|
|3|13|?|
|4|3|?|
|5|10|?|
|6|12|12|
|7|9|?|
|8|4|?|
|9|5|?|
|10|1|?|
|11|15|15|
|12|14|?|
|13|8|?|
|14|2|?|
|15|7|?|
```SQL
/*
Use where to further select records after inner join.
Together with the query above, 
it shows the different between `on condition1 and condition2` and `on condition1 where condition2`.
*/
select 
    A.id,
    B.id
from
    A
left join
    B
on
    A.id = B.id
where 
   A.id > 10 
;
```
||id|id|
|::|:--:|:--:|
|1|11|?|
|2|13|?|
|3|12|12|
|4|15|15|
|5|14|?|
```SQL
/*
Use where to further select records. 
Notice that rows with B.id being `null` are dropped 
because they are not eligible for condition `B.id >10`.
*/
select 
    A.id,
    B.id
from
    A
left join
    B
on
    A.id = B.id
where 
   B.id > 10 
;
```
||A.id|B.id|
|::|:--:|:--:|
|1|12|12|
|2|15|15|



## References

https://social.msdn.microsoft.com/Forums/getfile/208801
