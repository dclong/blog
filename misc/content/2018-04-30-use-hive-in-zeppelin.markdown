UUID: 11191fd4-7784-42df-b722-5317d43b1a0d
Status: published
Date: 2018-04-30 16:29:11
Author: Ben Chuanlong Du
Slug: use-hive-in-zeppelin
Title: Use Hive in Zeppelin
Category: Computer Science
Tags: programming

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Configuration

It seems that you have set a queue using the following code
even if you have already set a queue in properties.
```
%hive-interpreter

set mapred.job.queue.name = your_queue;
set mapred.min.split.size = 65536;
set mapred.max.split.size = 268435456;
```

## Tricks & Traps

1. When you write a query in Hive shell,
    you should end it with a semicolon (`;`).

        load data local inpath '/tmp/sql.txt' into table files;

    However,
    you should never end a SQL statement with a semicolon (`;`) in Zeppelin.

        load data local inpath '/tmp/sql.txt' into table files

    For this reason,
    you cannot run multiple SQL statements in a cell in Zeppelin.
    You should split different SQL statements into different cells.
