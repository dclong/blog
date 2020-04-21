Status: published
Date: 2020-04-06 14:44:14
Author: Ben Chuanlong Du
Slug: odbc-vs-jdbc-in-python
Title: ODBC vs JDBC in Python
Category: Computer Science
Tags: programming, Python, ODBC, JDBC, database, SQL

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Overall speaking,
Python has better ODBC support than JDBC support.
Most database related packages in Python support or rely on ODBC.
Currently, ODBC packages also have richer feathers than JDBC packages.
However,
it is not an easy job to install and configure ODBC drivers for a non-open source databases.

## ODBC vs JDBC

### JDBC Packages in Python

1. `JayDeBeApi` (NOT `JayDeBeApi3`, just ignore it) is currently the first choice 
    even thought it is not fully DB-API compliant
    and not actively maintained any more.

2. `py4jdbc` (based on Py4j) is another JDBC package 
    which claims to be faster than `JayDeBeApi` (based on JPype)
    but it is relative young compared to JayDeBeApi
    and is not actively maintained any more.

4. PyAthenaJDBC is a JDBC package specifically for Amazon Athena.

### ODBC Packages in Python

1. `pyodbc` and `SQLAlchemy` are general purpose packages relying on ODBC.

2. There are lots of database specific packages relying on ODBC.
    For example,
    `teradata` is a Python package for Teradata SQL which relies on ODBC or RESTful.

## Database Modules

1. json: JSON parsing.

2. sqlite3

3. [jreese/aiosqlite](https://github.com/jreese/aiosqlite)

3. [JayDeBeApi](https://github.com/baztian/jaydebeapi): connect to databases using Java JDBC in Python.

4. PyMySQL, MySQLdb

5. PyMongo

6. teradata

7. pyodbc, pypyodbc: Python ODBC bridget.

8. SQLAlchemy

9. sqlalchemy-teradata


## Misc

http://docs.python-guide.org/en/latest/scenarios/db/


the teradata package is weird, the file option can be used to run multiple statements in file ...
but if I manually pass a string, it doesn't work ... check the implementation ...
https://support.microsoft.com/en-us/help/3103282/teradata-odbc-configuration-on-linux
https://developer.teradata.com/tools/articles/teradata-sqlalchemy-introduction
https://github.com/Teradata/sqlalchemy-teradata
http://developer.teradata.com/tools/reference/teradata-python-module#Installing
http://stackoverflow.com/questions/34948453/read-teradata-query-into-pandas


## ORM

1. [SQLAlchemy](https://www.sqlalchemy.org/)
    is the most popular ORM package for Python.
    [peewee](https://github.com/coleifer/peewee)
    and
    [orator](https://github.com/sdispater/orator)
    are lightweight ORM solutions compared to `SQLAlchemy`.


http://stackoverflow.com/questions/10797794/multiple-queries-executed-in-java-in-single-statement

https://wiki.vip.corp.ebay.com/pages/viewpage.action?pageId=327124647



http://stackoverflow.com/questions/4493614/sqlalchemy-equivalent-of-pyodbc-connect-string-using-freetds

https://developer.teradata.com/tools/articles/teradata-sqlalchemy-introduction

http://stackoverflow.com/questions/12047193/how-to-convert-sql-query-result-to-pandas-data-structure

http://stackoverflow.com/questions/29525808/sqlalchemy-orm-conversion-to-pandas-dataframe/29528804#29528804


## JDBC

https://analyticsanvil.wordpress.com/2016/06/08/python-jdbc-dyanmic-hive-scripting/

https://github.com/minatverma/pythonWorks/blob/master/DQM.py

https://www.fullstackpython.com/databases.html

http://docs.python-guide.org/en/latest/scenarios/db/

## References

[DB-API V2.0](https://www.python.org/dev/peps/pep-0249/)

https://docs.python-guide.org/scenarios/db/

https://www.python.org/dev/peps/pep-0249/
