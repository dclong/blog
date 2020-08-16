Status: published
Date: 2020-08-16 13:10:17
Author: Benjamin Du
Slug: avoid-database-lock-in-sqlite3
Title: Avoid Database Lock in SQLite3
Category: Computer Science
Tags: Computer Science, SQLite3, database, lock, connection

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Use the `Pooling=True;` option in the connection string.
    For example, `/path/to/database;Version=3;Pooling=True;Max Pool Size=100;`.

2. Use autocommit mode by using the option `isolation_level=None`.
    Notice that even if SQLite3 uses autocommit by default,
    the Python module SQLite3 does not have autocommit turned on by default.

## Third-party Libraries to Allievate the Issue 

https://github.com/smitchell556/cuttlepool

## References 

https://www.sqlite.org/lockingv3.html

https://www.arysontechnologies.com/blog/fix-sqlite-error-database-locked/

https://stackoverflow.com/questions/151026/how-do-i-unlock-a-sqlite-database

https://docs.python.org/3.8/library/sqlite3.html#sqlite3.connect

https://stackoverflow.com/questions/3172929/operationalerror-database-is-locked/3172950#:~:text=OperationalError%3A%20database%20is%20locked%20errors,the%20lock%20the%20be%20released.

https://stackoverflow.com/questions/53270520/how-to-know-which-process-is-responsible-for-a-operationalerror-database-is-lo/53470118#53470118

