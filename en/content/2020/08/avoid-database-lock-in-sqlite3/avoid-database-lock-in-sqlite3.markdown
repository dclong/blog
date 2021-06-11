Status: published
Date: 2020-08-24 09:49:04
Author: Benjamin Du
Slug: avoid-database-lock-in-sqlite3
Title: Avoid Database Lock in SQLite3
Category: Computer Science
Tags: Computer Science, SQLite3, database, lock, connection
Modified: 2020-10-24 09:49:04
1. According to https://www.sqlite.org/lockingv3.html,
    POSIX advisory locking is known to be buggy or even unimplemented on many NFS implementations 
    (including recent versions of Mac OS X) 
    and that there are reports of locking problems for network filesystems under Windows. 
    So, the **rule of thumb** is to avoid using SQLite3 on network filesystems (Samba, NFS, etc). 
    You are guaranteed to encounter issues in the long run 
    (even though there lots articles talking about ways to alleviate the problem).
    Use JSON (on NFS) if you don't really need database
    or use MySQL, etc. if a database is needed.

2. Use the `autocommit` mode by using the option `isolation_level=None` 
    when you use the `sqlite3` module in Python.
    Notice that even if SQLite3 uses `autocommit` by default,
    the Python module `sqlite3` does not have `autocommit` turned on by default.

## Ways to Fix The Error "OperationError: Database is locked" 

The best practice is to create a backup of the datase
which has no locks on it. 
After that, replace the database with its backup copy.
```
Sqlite> .backup main backup.Sqlite
Sqlite> .exit
$mv .x.Sqlite old.Sqlite
$mv backup.Sqlite .x.Sqlite
```

You can also directly make a copy of the original SQLite3 file to backup it.

## References 

https://www.sqlite.org/lockingv3.html

https://www.arysontechnologies.com/blog/fix-sqlite-error-database-locked/

[Can SQLite and TDB databases be used with NFS?](https://access.redhat.com/solutions/120733)

[How do I unlock a SQLite database?](https://stackoverflow.com/questions/151026/how-do-i-unlock-a-sqlite-database)

[“The database file is locked” error even when the file is newly created](https://forum.duplicati.com/t/the-database-file-is-locked-error-even-when-the-file-is-newly-created/6893)

https://docs.python.org/3.8/library/sqlite3.html#sqlite3.connect

[OperationalError: database is locked](https://stackoverflow.com/questions/3172929/operationalerror-database-is-locked/3172950#:~:text=OperationalError%3A%20database%20is%20locked%20errors,the%20lock%20the%20be%20released.)

[How to know which process is responsible for a “OperationalError: database is locked”?](https://stackoverflow.com/questions/53270520/how-to-know-which-process-is-responsible-for-a-operationalerror-database-is-lo/53470118#53470118)

