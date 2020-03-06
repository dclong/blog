UUID: 04d5b491-e930-470f-b355-8d60f283534b
Status: published
Date: 2017-08-26 21:48:07
Author: Ben Chuanlong Du
Slug: pyodbc-tips
Title: pyodbc Tips
Category: Computer Science
Tags: programming, pyodbc, Python, tips, ODBC, database, SQL, Vertica, Teradata

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

pyodbc only supports qmark

https://github.com/mkleehammer/pyodbc/wiki




## Unicode Converter Buffer Overflow 

This issues arises in Python3 but not Python2,
so the simplest way is to use Python2 if you do not have use Python3. 
And make sure do not use unicode queries.

1. If you are using `pyodbc` in Python3 to query Vertica, 
then set the `VERTICAINI` environment variable
and set `DriverManagerEncoding=UTF-16` in `vertica.ini`. 
For more information, 
please refer to the issue 
[Not working with Python 3.4.3 on OS X (Vertica driver) #44](https://github.com/mkleehammer/pyodbc/issues/44)
on GitHub.
