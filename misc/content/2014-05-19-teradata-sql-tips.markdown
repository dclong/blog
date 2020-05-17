Status: published
Date: 2020-05-17 11:47:48
Author: Ben Chuanlong Du
Title: Tips on Teradata SQL
Slug: teradata-sql-tips
Category: Computer Science
Tags: programming, tips, Teradata SQL, database

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

- [Teradata Open Source Project on GitHub](https://github.com/Teradata)
- [Teradata SQL笔记](http://cuishen.iteye.com/blog/638968)
- [无知的比较：R和Teradata SQL(附赠TD经验几枚)](http://www.loyhome.com/%E6%97%A0%E7%9F%A5%E7%9A%84%E6%AF%94%E8%BE%83%EF%BC%9Ar%E5%92%8Cteradata-sql%E9%99%84%E8%B5%A0td%E7%BB%8F%E9%AA%8C%E5%87%A0%E6%9E%9A/)
- [The SQL Server DBA’s Guide to Teradata](http://sqlfool.com/mssql-dba-guide-to-teradata/)

## Performance Tips

http://www.legendu.net/misc/blog/sql-tips/#performance

## Trick and Trap

1. Must use on commit preserve rows to persist data if you create a volatile table.

2. Data cast using parentheses is discouraged in Teradata SQL. 
    Use the `CAST` function instead. 
    Another way is to use suffix to indicate the type of literal values, 
    e.g., `'1'XI8`.


2. Below code get informtion about the table `cat123`.

        :::sql
        SELECT * FROM dbc.TablesV WHERE DataBaseName = '' AND TableName = 'cat123'

1. Instead of using macros of other extensions of SQL
    (which many versions of SQL does not support),
    an better alternative is to call SQL in other languages (Python, R, etc.).
    This also makes it easier to do visualization or generalize reports.

2. In Teradata, the maximum row size is approx 64K bytes.
    So that you cannot define columns of size greater than 64K.
    For example,
    you cannot define a column of size 65K.

3. You cannot create a new table using `insert into`.
    `insert into` can only insert into an existing table.

## Volatile

There is no way to check if a specific Volatile Table exists besides HELP VOLATILE TABLE which returns all VT.
identity, auto increment]: 
1. better not to set value by yourself (even if you can) as confliction might happen later; 
2. insert one by one works well however insert into using select seems not to work as expected ...
    over (order by field) necessary for row_number() etc.? 
    u can use order by 0 if no ordering wanted ..., and is probably faster ...

## Syntax

1. Always end a complete Teradata SQL statement with a semicolon.
    Sometimes in Some SQL (e.g., SAS),
    the codes runs OK without an ending semicolon but sometimes might not.
    It is always good practice to end a complete SQL statement with a semicolon.

2. Commands in Teradata (and other versions of SQL) SQL are case-insensitive.

2. You can use `sel` as short for `select` in Teradata SQL,
    however,
    it is suggested that you always use `select` instead of `sel`.
    This is because `sel` is not support in some other versions of SQL.
    You can use SQL template to generate code for you if you are tired of typing.

3. Use `--` for one line comment and `/*...*/` for multiple line comment.
    The `/*...*/` way is recommended as it is a widely used way for commenting.

4. The `as` keyword is optional when creating column aliases,
    however,
    it is tricky in `create table` statement.
    When you create table schema,
    you cannot not use the keyword `as`
    but when you create a table using a query you must use the keyword `as`.

        create table A /*no as here*/(
            a integer,
            b char(20),
            c decimal(12,3),
            d date
        )
        ;

        create table A as /*must use as here*/(
            select * from B
        )
        with data
        primary index (id)
        ;

5. `union (all)` does not match column names.
    Columns of the two tables to be united together must have the same order.
    If the types of a column does not match,
    then the type of the first column is used
    and the corresponding columns of other tables will be casted into this type.

2. Both count and sum can be used to count the number of rows satisfying some condition.
    Generally speaking, count is preferred because it is able to remove duplicated records.
    For example, suppose we have a table A with columns `case_id` (non-unique)
    and `sar` (Y or N). We can count the number of rows with `sar = Y` using

        sum(
            case(
                when sar = 'Y' then
                    1
                else
                    0
            end)
        ) as n

    How,
    if `case_id` has duplicated values and we want to count the number of distinct cases with `sar = 1`,
    then `sum` does not work well. In stead, we can use

        count(
            case(
                when sar = 'Y' then
                    case_id
                else
                    null
                end)
        ) as n

    It is recommended that you always use `count` to count rows satisfying a condition.

4. In a case statement,
    at most one `when/else` branch is executed.
    As soon as a `when/else` statement is executed,
    it jumps out (like `break;` in C) of the case statement instead of continuing to the next branch.

14. Do not use natural joins (relying on same column names for joining) as it is dangerous to do so.

17. When joining multiple tables,
    SQL will determine the best way to perform the joins.
    So do not help the SQL compiler when you do multiple joins.

1. The precedence of logical operators are `not`, `and` and `or`.
    However,
    it is suggested that you always use parentheses to make your code easier to understand.

2. Displays the code used to generate the view or table.

        show table table_name;

5. Display table schema (i.e., show column names and attributes).

        help table table_name;

    or you can use

        help column table_name.*;


## Null Values

3. Most functions in SQL (unless specially for `null` values) ignore
    `null` values like they never appear in the table.

### Create an Empty Table

You can manually specify the structure of the table.

    :::sql
    CREATE TABLE t1 /*no as here*/ (
        a Integer,
        b Char(20),
        c Decimal(12,3),
        d Date
    )
    ;

If there is an existing table `t1` 
and you want to create another table `t2` with the same schema,
you can use

    :::sql
    CREATE TABLE t2 AS t1
    WITH NO DATA;

or

    :::sql
    CREATE TABLE t2 as /*as cannot be omitted here*/ (
        SELECT * FROM t1
    )
    WITH NO DATA
    PRIMARY INDEX (id)
    ;

Notice that the syntax of Teradata SQL is different from other SQL languages
when creating a table using a select clause.
You have to specify either `WITH DATA` or `WITH NO DATA`.
`WITH DATA` means that you want to append the selected records into the created table
while `WITH NO DATA` creates an empty table.

## Database Information

1. Get version of Teradata SQL.

    :::sql
    SELECT * FROM dbc.dbcinfo;

## Error Code

http://info.teradata.com/htmlpubs/DB_TTU_16_00/index.html#page/Query_Management_Tools/B035-2414-086K/BTEQReturnCodes_USE_2414.html#wwID0EKJNM
[TeraJDBC 15.10.00.14] [Error 9804] [SQLState HY000] Response Row size or Constant Row size overflow: might be because too large column definition
using distinct (the result has only about 1,000 rows) causes the following error, how can I avoid the issue? 
[Teradata Database] [TeraJDBC 15.10.00.22] [Error 2646] [SQLState HY000] No more spool space in dclong.
No More Spool Space http://kedar.nitty-witty.com/blog/no-more-spool-space-teradata-query-solution
Instead of distinct (which might cause "no more spool space" issue), you can try group by.

## Error Message

1. unknown error, probably network issue

2. Error code 3754: precision error, character, numeric, .. -> float ...

## Date

Be careful when you work with date in SQL.
A non-exist date can result in tricky errors.
For example (note that `2016-09-31` does not exist)

    :::sql
    WHERE dt BETWEEN '2016-09-01' AND '2016-09-31'  

in Teradata throws the error message "a character string failed to convert to a numeric value".

## References

http://www.dwhpro.com/teradata-golden-tuning-tipps-2017/

http://community.teradata.com/t5/Database/Teradata-IDENTITY-columns/td-p/8025

http://www.info.teradata.com/HTMLPubs/DB_TTU_14_00/index.html#page/SQL_Reference/B035_1184_111A/Create_Table-Details.012.046.html

http://teradatafaqs.blogspot.com/2013/05/teradata-generated-identity-column.html

https://developer.teradata.com/uda/articles/working-with-identity-columns-and-unity-director-and-loader

http://www.info.teradata.com/htmlpubs/DB_TTU_14_00/index.html#page/SQL_Reference/B035_1184_111A/Create_Table-Details.012.045.html

https://community.teradata.com/t5/Analytics/identity-columns/td-p/143

http://forgetcode.com/Teradata/1741-INSERT-SELECT

http://forgetcode.com/Teradata/1779-ROW-NUMBER

http://www.dwhpro.com/ a very good teradata blog

http://kedar.nitty-witty.com/blog/no-more-spool-space-teradata-query-solution
