Status: published
Date: 2019-06-21 21:20:15
Author: Ben Chuanlong Du
Slug: sql-equivalent
Title: SQL Equivalent
Category: Computer Science
Tags: programming, SQL, database, equivalent, querying

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

[SQL translation](https://www.jooq.org/translate/)
is a great tool that transalte any SQL statement(s) to a different dialetc using the JOOQ Parser.

## Show Tables

### Oracle SQL
1. List all tables owned by the current user.
```SQL
select * from user_tables;
```
2. List all tables in a database.
```SQL
select * from dba_tables;
```
1. List all tables accessible to the current user.
```SQL
select * from all_tables;
```

### MySQL
```SQL
show tables;
```
 To list all databases, in the MySQL prompt type:

 show databases

 Then choose the right database:

 use <database-name>

 List all tables in the database:

 show tables

 Describe a table:

 desc <table-name>

### SQL Server


SQL Server 2005, 2008, 2012 or 2014:

SELECT * FROM information_schema.tables WHERE TABLE_TYPE='BASE TABLE'

To show only tables from a particular database

SELECT TABLE_NAME FROM <DATABASE_NAME>.INFORMATION_SCHEMA.Tables WHERE TABLE_TYPE = 'BASE TABLE'

Or,

SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='dbName' --(for MySql, use: TABLE_SCHEMA='dbName' )

PS: For SQL Server 2000:

SELECT * FROM sysobjects WHERE xtype='U' 



## Display Table Schema
### Teradata SQL
```SQL
help table table_name;
```
or
```SQL
help column table_name.*;
```

### Orace SQL
```SQL
desc table_name;
```

### MySQL
```SQL
describe table_name;
```

## Drop a Table Conditionally

### Microsoft SQL Server

```SQL
if object_id(table_name) is not null then drop table table_name
```

### SAS Proc SQL
```SQL
proc sql;
    drop table table_name;
quit;
```
If the table does not exists, 
`proc sql` throws an error but the remaining code can continue to run.
So this acts like a conditional drop. 

## Top N/Percent Queries

### Microsoft SQL Server
```SQL
-- select top 5 queries
select top 5 * from table;
-- select top 50% queries
select top 50 percent * from table;
```

### SAS Proc SQL

### Teradata SQL
```SQL
select top 5 * from table;
```

### Oracle SQL
```SQL
select * from table limit 5;
```

### MySQL
```SQL
select * from table limit 5;
```

### SQLite
```SQL
select * from table limit 5;
```

## Randomly Sample 100 Queries

### Teradata SQL
```SQL
select * from table sample 100;
```
Teradata also has the function `random`, 
probably can do the same as SQLite ...

### SQLite
```SQL
select * from table order by random() limit 100;
```

## Random Sample with Acceptance Ratio 0.1
### Teradata SQL
```SQL
select * from table sample 0.1;
```
### SQLite
```SQL
select * from table where random() % 10 = 0;
```
Note that `random()` generates a pseudo-random integer 
between -9223372036854775808 and +9223372036854775807. 

## Multiple Insert
1. You can always put multiple single insert statement together.
### Oracle SQL
```SQL
insert into pager (PAG_ID,PAG_PARENT,PAG_NAME,PAG_ACTIVE)
select 8000,0,'Multi 8000',1 from dual
union all 
select 8001,0,'Multi 8001',1 from dual
```
```SQL
INSERT ALL
INTO t (col1, col2, col3) VALUES ('val1_1', 'val1_2', 'val1_3')
INTO t (col1, col2, col3) VALUES ('val2_1', 'val2_2', 'val2_3')
INTO t (col1, col2, col3) VALUES ('val3_1', 'val3_2', 'val3_3')
.
.
.
SELECT 1 FROM DUAL;
```
### Teradata SQL
```SQL
insert into table1 (
    First,
    Last
) values 
    ('Fred','Smith'),
    ('John','Smith'),
    ('Michael','Smith'),
    ('Robert','Smith')
;
```
