UUID: 66efedd7-d918-4757-8b24-d9a6c28d1e46
Status: published
Date: 2015-08-28 13:02:17
Author: Ben Chuanlong Du
Slug: trap-duplicated-columns-sql-procedure-sas
Title: The Trap of Duplicated Columns in the SQL Procedure of SAS
Category: Computer Science
Tags: programming, SAS, SQL
Modified: 2015-08-28 13:02:17

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**


If 2 columns with the same names are selected from 2 tables when joining them,
the first selected column is kept and the other one is dropped.
If you don't like this behavior, you can rename and drop columns.

This potentially invite some very dangerous errors!!! you know that in sas sql cannot update using join,
so you might want to join to get the create .... when there are many columns, people just use *, the order matters!!!
you must be very carefule !!!!

```SAS
data s1;
	input x y;
	datalines;
1 2
3 7
4 5
;
run;


data s2;
	input x z;
	datalines;
1 0
3 9
9 7
;
run;

/*
1	2	0
3	7	9
*/
proc sql;
	create table s3 as
	select
		s1.*,
		s2.*
	from 
		s1
	inner join
		s2
	on
		s1.x = s2.x
	;
quit;

/*
1	0	2
3	9	7
.	.	5
*/
proc sql;
	create table s3 as
	select
		s1.*,
		s2.*
	from 
		s1
	left join
		s2
	on
		s1.x = s2.x
	;
quit;

/*
1	0	2
3	9	7
.	.	5
*/
proc sql;
	create table s3 as
	select
		s2.*,
		s1.*
	from 
		s1
	left join
		s2
	on
		s1.x = s2.x
	;
quit;

/*
1	2	0
3	7	9
.	.	7
*/
proc sql;
	create table s3 as
	select
		s1.*,
		s2.*
	from 
		s1
	right join
		s2
	on
		s1.x = s2.x
	;
quit;

/*
1	0	2
3	9	7
9	7	.
*/
proc sql;
	create table s3 as
	select
		s2.*,
		s1.*
	from 
		s1
	right join
		s2
	on
		s1.x = s2.x
	;
quit;
```
## same column appear twice

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
	select 
		y,
		y
	from	
		s
	;
run;
```
this actually works in sas ... there will be 2 columns with the same name
