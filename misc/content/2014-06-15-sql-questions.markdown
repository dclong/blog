UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2020-01-27 20:34:47
Title: SQL Questions
Slug: sql-questions
Category: Computer Science
Tags: programming, SQL, questions

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
1. 比如在 LEFT JOIN 中过滤条件写在 ON 和 WHERE 的区别。

2. 函数和存储过程的区别？

3. Table-value function 和 scalar-valued function 的区别.

4. char、varchar、nvarchar之间的区别(包括用途和空间占用

5. 有哪些操作会使用到TempDB;如果TempDB异常变大，可能的原因是什么，该如何处理;

6. Index有哪些类型，它们的区别和实现原理是什么，索引有啥优点和缺点;如何为SQL
    语句创建合适的索引，索引创建时有哪些需要注意的项

7. 临时表、表变量、CTE(公用表表达式)有啥区别和联系，保存位置有啥不一样，使用
    时如何决定选哪种;

8. 视图和索引视图有什么区别

9. 如何实现分区，分区的步骤，分区有什么好处，怎么实现 Sliding Window.

10. 如何比较两个同结构的表数据的差异

11. SQL调优步骤，如何来判断SQL语句存在问题，怎么定位问题，如何解决这些问题;
    平时也可以看看 http://www.flybi.net/ 里面有很多这种问题

13. 一个table，就两个field， ManagerID 和 direct Reporter ID
    要求是得出每个manager下面的有多少direct和indirect reporters


## General SQL Questions

## Teradata Related

1. select, union: strange that sometimes white spaces at the end causes problems ...
not sure this is an issue of Teradata SQL or Teradata Studio

2. is there convenient way to calculate percentiles in Teradata SQL?
Some SQL has `percentile_disc` and `percentile_cont`.

6. sql exist vs in?

14. Is/are the primary key(s) automatically indexed?

1. create PI on multiple columns, what are the advantages and disadvantages?
why not create PI on all columns?

2. Does SQL truncate integer/float computation results?
What is they type of new created columns?

3. how to create a small temp table?

## Questions

1. when join, which talbe to use first? 
Does this affect performance a lot? might be
I heard that you should use the smaller table as the first one.

3. doesn't join create large table sometimes? 
Which is prefered? smaller talbes using multiple queries 
or a really large talbe with just one query?

4. what happens if an left/right join retrieve fields 
from a table with constraint NOT NULL
but match is not found?

5. how to use keywords as column names?

6. how to use space in column names?
In teratadata sql, you can just quote it (double quotes?)

7. prefer to compare numbers or strings?
I think comparing number will be much faster.


8. Is it possible to define variables in teradata sql? 
so that we don't have type the same value again and again?
it seems that there is no simple way to do this

9. what issue does the following style of code have?
recursive? actually will this work? probably not ...
have a try on this ...
```code
create table t as
select * from t;
```
Generally speaking, this does not work. 
You want to avoid it.

1. what is the difference between cast and convert in transaction-SQL (MS SQL)?

sql: some expression is used multiple times, is it better to define it as a column alias and then use it? Better alternative? nad temp volatile volumn?

2. why cannot I create a view in Hopper?

3. which rows are updated in the following code?
```SQL
update #ST_Master
set  #ST_Master.'+ @Var_ST_1st + '= #t1.Var_ST_1st
from  #ST_Master left join #t1
on  #ST_Master.LoanID = #t1.LoanID
```
Must number of rows be the same?

4. is there any way to check functions and function args in SQL?

4. group by and partition over together? partition over runs after group by?

5. is there a better way of formatting besides casting?

6. self join in each group, is there any efficient way to do it? avoid the full n^2 join?
