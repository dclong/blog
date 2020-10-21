Status: published
Date: 2020-10-21 14:31:57
Author: Benjamin Du
Slug: avoid-database-lock-in-sqlite3
Title: Avoid Database Lock in SQLite3
Category: Computer Science
Tags: Computer Science, SQLite3, database, lock, connection

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. The simple answer is do NOT use SQLite3 on NFS. 
    Use MySQL, etc. instead.

2. Use autocommit mode by using the option `isolation_level=None`.
    Notice that even if SQLite3 uses autocommit by default,
    the Python module SQLite3 does not have autocommit turned on by default.

3. According to https://www.sqlite.org/lockingv3.html,
    POSIX advisory locking is known to be buggy or even unimplemented on many NFS implementations 
    (including recent versions of Mac OS X) 
    and that there are reports of locking problems for network filesystems under Windows. 
    Your best defense is to not use SQLite for files on a network filesystem.

## Fix "OperationError: Database is locked" 

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

[How do I unlock a SQLite database?](https://stackoverflow.com/questions/151026/how-do-i-unlock-a-sqlite-database)

[“The database file is locked” error even when the file is newly created](https://forum.duplicati.com/t/the-database-file-is-locked-error-even-when-the-file-is-newly-created/6893)

https://docs.python.org/3.8/library/sqlite3.html#sqlite3.connect

https://stackoverflow.com/questions/3172929/operationalerror-database-is-locked/3172950#:~:text=OperationalError%3A%20database%20is%20locked%20errors,the%20lock%20the%20be%20released.

https://stackoverflow.com/questions/53270520/how-to-know-which-process-is-responsible-for-a-operationalerror-database-is-lo/53470118#53470118

