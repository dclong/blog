UUID: 1d0a3d78-fff8-4882-a19e-1ca87841dbcd
Status: published
Date: 2016-10-16 11:22:18
Author: Ben Chuanlong Du
Slug: teradata-table-type
Title: Teradata Table Type
Category: Computer Science
Tags: programming, SQL, table, type

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

1. MULTISET Table

create table test
( id int,
  name char(20)
)

当你用show table test检查表定义的时候发现，它已经变成如下定义：
CREATE MULTISET TABLE test ,NO FALLBACK ,
     NO BEFORE JOURNAL,
     NO AFTER JOURNAL,
     CHECKSUM = DEFAULT
     (
      id INTEGER,
      name CHAR(20) CHARACTER SET LATIN CASESPECIFIC)
PRIMARY INDEX ( id );

可以看到，系统默认会将表设置为MULTISET Table，没有备份（FALLBACK ）和恢复日志（BEFORE JOURNAL/AFTER JOURNAL），而且会默认将第一列设置为PRIMARY INDEX。

执行如下SQL：
insert into test values(1,'test');
insert into test values(1,'test');

可以看到，多次插入重复数据都成功，检查表数据验证结果。

2. SET Table

当创建表定义为create set table test，则系统表定义为CREATE SET TABLE test ,NO FALLBACK……

在这种情况下执行SQL：
insert into test values(1,'test');
insert into test values(1,'test');

可以看到，插入重复数据将会出错，检查表数据验证结果

区别：
SET Table 不可以包含重复数据
MULTISET Table 可以包含重复数据

3. VOLATILE Table

定义如下：
create volatile table test as
( select * from table
) with data
on commit preserve rows

这个表只存在于cache中，data dictionary中也找不到这个表，当User结束一个session时，这个表将自动删除，所有用户无法访问，下次用户需要重新建表。

4. GLOBAL TEMPORARY Table

定义如下：
create global temporary table test as
( select * from table
) with no data    -- global temporary table cannot define with data
on commit preserve rows

这个表存在于data dictionary中，当User结束一个session时，这个表中的数据将自动删除，表还保留，其它用户可以继续访问这个表，但是数据只存在于某一session中。

在上边的定义中，我们使用的是on commit preserve rows，执行以下SQL，我们可以看到表中存有数据。
insert into test
select *
from table

然后执行
select *
from test

如果把定义改为on commit delete rows，我们看到表中依然没有数据，这是因为每个SQL 语句都是一个隐性事务。
