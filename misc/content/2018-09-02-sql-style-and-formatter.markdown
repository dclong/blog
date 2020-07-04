Status: published
Date: 2020-07-04 10:59:35
Author: Ben Chuanlong Du
Slug: sql-style-and-formatter
Title: SQL Style and Formatter
Category: Computer Science
Tags: programming, SQL, SQL formatter, SQL style

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


[SQL translation](https://www.jooq.org/translate/)

## SQL Formatter

You can use online SQL formatters to help you format SQL queries.

1. [SQL-Formatter](https://www.freeformatter.com/sql-formatter.html) seems to be a good one.

2. [SQL formatter from ExtendsClass](https://extendsclass.com/sql-formatter.html)

2. [EverSQL Query Formatter](https://www.eversql.com/sql-query-formatter/)

1. [Instant SQL Formatter](http://www.dpriver.com/pp/sqlformat.htm)

2. [SQLFormat](https://sqlformat.org/)

3. [SQL Formatter](http://www.sql-format.com/)

https://codebeautify.org/sqlformatter

[Poor SQL](https://poorsql.com/)

You can also use the Python library 
[andialbrecht/sqlparse](https://github.com/andialbrecht/sqlparse)
to help you format SQL queries.
It is actually the backend of [SQLFormat](https://sqlformat.org/).
```
import sqlparse as sp

sql = '''
    select c1, c2 /* this is a comment */
    from t where c1 > 1"
    '''
sql_fmt = sp.format(sql,
    keyword_case= upper',
    identifier_case='lower',
    strip_comments=False,
    reindent=True,
    indent_width=2
)
print(sql_fmt)
```

## JavaScipt/TypeScript Libraries

https://github.com/zeroturnaround/sql-formatter

## Java Libraries

[vertical-blank/sql-formatter](https://github.com/vertical-blank/sql-formatter)
is Java port of the great JS-based SQL formatter 
[zeroturnaround/sql-formatter](https://github.com/zeroturnaround/sql-formatter)
(which is itself a JS port of the PHP-based SQL formatter.)

## PHP Libraries

[jdorn/sql-formatter](https://github.com/jdorn/sql-formatter)

## SQL Style and Formatting

https://www.sqlstyle.guide/

1. `||` works differently on different date types. 
    This is because different data types have different (default) padding/formatting styles.
    You can manually cast date types to produce the format you want. 

2. some people like to put `,` 
    before column names in select, 
    I don't think this is a good practices, 
    as what if we want to remove the first column? 
    it similarly inconvenient to removing the last column when put comma after column names

## References

https://stackoverflow.com/questions/3310188/what-free-sql-formatting-tools-exist

http://stackoverflow.com/questions/1394998/parsing-sql-with-python
