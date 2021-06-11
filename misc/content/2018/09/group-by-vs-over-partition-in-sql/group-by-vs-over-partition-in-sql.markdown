Status: published
Date: 2018-09-12 18:40:34
Author: Ben Chuanlong Du
Slug: group-by-vs-over-partition-in-sql
Title: Group by vs Over Partition in SQL
Category: Computer Science
Tags: programming, SQL, group by, over partition
Modified: 2019-09-12 18:40:34

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

[SQL Server: Difference between PARTITION BY and GROUP BY](http://stackoverflow.com/questions/2404565/sql-server-difference-between-partition-by-and-group-by)

1. `group by` alwasy aggreates values. 
    That is `group by` alwasy reduces a group of values to 1 value.
    Hoever, `analytics_function() over(partition by column)` does not aggreage.
    It returns a value for each record in the group.
    Even if an aggregation function is applied and returns only 1 value,
    this value is returned for each value in the group.
    real example, meta_cat, sub_cat, want to find all sub_cat that have multiple meta_cat, over partition is an easier way


They are used in different places. group by modifies the entire query, like:

```SQL
select 
    customerId, 
    count(*) as orderCount
from 
    Orders
group by 
    customerId

```
But partition by just works on a window function, like row_number:

```SQL
select 
    row_number() over (partition by customerId order by orderId) as OrderNumberForThisCustomer
from 
    Orders
```

A group by normally reduces the number of rows returned 
by rolling them up and calculating averages or sums for each row. 
partition by does not affect the number of rows returned, 
but it changes how a window function's result is calculated.
