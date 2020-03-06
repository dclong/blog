UUID: 86ce8329-7bce-4ab4-86af-534fe51e6bd9
Status: published
Date: 2016-10-23 12:33:22
Author: Ben Chuanlong Du
Slug: auto-increment-in-sql
Title: Auto Increment in SQL
Category: Computer Science
Tags: programming, SQL, auto increment

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


http://plsql4all.blogspot.com/2014/08/auto-increment-column-in-teradata.html
http://stackoverflow.com/questions/21982004/how-to-generate-automatic-number-in-teradata-sql
https://forums.teradata.com/forum/enterprise/auto-increment-column

1. Be careful with batch insert if there is an auto increment column. 
A batch insert triggers auto increment only once rather than 
multiple (the number of insrted records) times
unless you specifically trigger auto increment multiple times.
This means that records inserted with a batch insert 
have the same value for the auto increment column.

### Teradata SQL
```SQL
seq_num decimal(10,0) not null generated always as identity
(start with 1 
increment by 1 
minvalue 1 
maxvalue 2147483647 
no cycle)
```
### Oracle SQL
sequence.nextval

```SQL
create table t as (
select ...
) 
```
can we add an auto increament column here? if not, first create the table and then select into ...

<https://mikesmithers.wordpress.com/2015/09/20/becoming-unhinged-with-insert-all-and-sequence-nextval/>
