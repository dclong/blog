UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2015-08-28 12:58:18
Title: SAS SQL Tips
Slug: sas-sql-tips
Category: Computer Science
Tags: programming, SAS, tips, SQL

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
1. A const column does not work if no row is selected. 
This becomes trickier if you use `count(*)` in your query.
For example, 
if the returned value of `n` in the following query is 0, 
then `yyyymm` is missing instead of the value `201311`.
```SAS
proc sql;
    select 
        '201311' as yyyymm, 
        count(*) as n 
    from 
        lib.tran_201311 
    where tran_date >= '1Jan2014'd;
quit;
```

2. SAS can map a database on a data platform (e.g., Teradata) as a library. 
This is only suggested when you want to download data from or upload data to the database.
Don't manipulate data directly in library mapping to a database. 
Also you cannot save a sorted data set in the library,
as SQL stories data differently than SAS. 
If you use the print procedure to print a previously sorted data in the database, 
you will probably still get an unsorted data set.

3. You can use multiple SQL statements in one sql procedure (before the quite statement).

4. While records in a relational database management system (RDMS) does not perserve
the order that they were created 
(i.e., 
the order of records returned by a query (without sorting) 
is not necessarily the same as the order of them being created),
a dataset in SAS preserves the order of records created.
Even if you use a SQL procedure to insert records into a dataset in SAS,
the order of records is preserved.

6. Most SAS functions can be used in the SQL procedure,
e.g., `intnx`, etc. 

7. The `pctl` function in SAS cannot be used in the SQL procedure.

3. select into, sql. great!
and can be one variable `separated by " "`.


3. The noprint option of the SQL procedure supress displaying of results returned by select clauses.
However, if you create a table SAS Enterprise Guide will still show the dataset created.

4. When you select values into macro variables using a sql procedure in a macro function, 
the macro varibles created are local to the macro function.

5. In many procedures of SAS,
you can use the option `obs` (together with `firstObs`) to select/limit records to work on or return.
For `proc sql`, 
you can use the option `outObs` to limit the number of records to display/return. 
```SAS
proc sql outobs=12;
    select 
        city, 
        (avgHigh - 32) * 5/9 as highC format=5.1, 
        (avgLow - 32) * 5/9 as lowC format=5.1,
        (CALCULATED HighC - CALCULATED lowC) as range format=4.1
    from 
        worldTemps
    ;
quit;
```

6. You can use an column alias in `where`, `having`, `on` clauses directly. 
However, if you want to use an column alias to create another column in a `select` statement,
you have to use the `CALCULATED` keywords to let `proc sql` know that it is an alias.
```SAS
proc sql;
    select 
        city, 
        (avgHigh - 32) * 5/9 as highC format=5.1, 
        (avgLow - 32) * 5/9 as lowC format=5.1,
        (CALCULATED highC - CALCULATED lowC) as range format=4.1
    from 
        worldTemps
    ;
quit;
```


1. union all (keep all rows) vs union (distinct/unique) 
prefer to use union all
union and union all relies on column positions
another way is to use proc append which appends data by matching column names


append as advantages over sql union
append tries to match column names while sql union relies on the column orders. 

be careful when you use append, be sure to remove previous data sets ...
as you might run the same piece of code multiple times

2. If you sort observations using the `order by` clause
when creating a table (using the `create table` stateemnt), 
then observations in the created table is sorted.
It is equivalent to sort a table using the `proc sort` procedure.

3. Even if observations in a table is sorted, 
you have to rely on the `order by` clause to get sorted observations.
That is the `select` statement without `order by` guarantees no specific order of observations.
This is true for all versions of SQLs.

4. When creating a new table/view using the SQL procedure,
you can specify columns to keep/drop similarly as you can do in other procedures.
```SAS
data s;
	input x $10. y;
	datalines;
1234567890 2 
3          4
5          6
;
run;

proc sql;
	create table s2 (keep=y) as
	select
		*
	from 
		s
	;
quit;

proc sql;
	create table s3 (drop=x) as
	select
		*
	from 
		s
	;
quit;
```
