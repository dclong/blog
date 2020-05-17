Status: published
Date: 2020-05-17 11:47:48
Author: Ben Chuanlong Du
Slug: work-with-teradata-sql-in-python
Title: Work With Teradata SQL in Python
Category: Computer Science
Tags: programming, Python, Teradata SQL, Teradata

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## ODBC

### teradata

1. `teradata` relies on either ODBC or RESTful.
    If you use teradata with ODBC,
    it is suggested that you use CentOS (docker can be leveraged) as Teradata SQL offers official RPM packages for CentOS
    but offers no official DEB package for Ubuntu.

2. It seems that Teradata ODBC 16.20 no longer requires unixODBC
    and actually it shouldn't be install in order for Teradata ODBC 16.20 to work.

### pyodbc

1. pyodbc works for Teradata too.

## JDBC

1. JayDeBeApi

## CLIv2

1. giraffez
