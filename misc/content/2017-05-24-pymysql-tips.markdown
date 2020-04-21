UUID: e5321142-cc73-4331-8a08-2e9a2f2db4ca
Status: published
Date: 2017-10-22 13:21:25
Author: Ben Chuanlong Du
Slug: pymysql-tips
Title: PyMySQL Tips
Category: Computer Science
Tags: programming, PyMySQL, tips, Python

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**



```sh
sudo pip3 install PyMySQL
```

## Tricks

1. Connection in PyMySQL is not autocommit by default. 
You must commit to save your changes.

        # suppose conn is the connection object
        conn.commit()

2. parameterized sql: %s instead of ?

3. cursor returns tuple of tuples instead of list of tuples ...


## PyMYSQL vs MySQLdb

`PyMySQL` and `MySQLdb` provide the same functionality - 
they are both database connectors. 
The difference is in the implementation where `MySQLdb` is a C extension and `PyMySQL` is pure Python.

There are a few reasons to try `PyMySQL`:

1. it might be easier to get running on some systems

2. it works with PyPy

3. it can be "greened" and works with gevent


## Issues

    pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '127.0.0.1' 
    ([Errno 2] No such file or directory)")

在所有信息正确的情况下可能是my.conf下开启了skip-networking或绑定了IP

    skip-networking
    bind-address = 127.0.0.1

若要开启skip-networking的情况下使用，则用unix_socket来连接

    pymysql.connect(host='127.0.0.1',
    unix_socket='/xxx/mysqld.sock',
    user='root',
    passwd='root',
    db='test',
    charset='utf8')

## Configuration

1. bind-address

2. admin user (non root)

```SQL
create user 'monty'@'localhost' identified by 'some_pass';
grant all privileges on *.* to 'monty'@'localhost' with grant option;
```

```SQL
create user 'monty'@'%' identified by 'some_pass';
grant all privileges on *.* to 'monty'@'%' with grant option;
```

## Backup

XtraBackup is an open-source MySQL hot backup software program. 
Features include hot, non-locking backups for InnoDB storage, incremental backups, streaming, parallel-compressed backups, 
throttling based on the number of I/O operations per second, etc.[74]

