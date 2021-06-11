Status: published
Date: 2020-03-05 16:19:58
Author: Ben Chuanlong Du
Slug: q-query-text-file-sql
Title: Use q to Query Text File Using SQL Syntax
Category: Programming
Tags: programming, SQL, structured text, CSV, TSV
Modified: 2020-03-05 16:19:58


It is suggested that you use Python 
instead of [q](http://harelba.github.io/q/) 
to manipulate text files!

## Installation on Ubuntu

```bash
wajig install python3-q-text-as-data
```

## General Tips

1. The semantics of `q` is identical to `sqlite`. 
    `q` preserve the original order of rows if no sorting (order by) is applied.
    You force querying by the order of insertion 
    by adding an `order by rowid` if needed (similar to sqlite).

2. Output in quote mode does not work well. 
    Double quotes are not escaped.

3. Joins do not work on files with different separators. 
    You have to convert them to have the same field separator first
    and then perform joins. 

7. If no header, then use c$i$ to stand for the $i^{th}$ column.

## Examples 

1. Randomly select 500 records.

        q "select * from text_file order by random() limit 5"

2. Sample with acceptance ratio 0.01.

        q "select * from text_file where random() % 100 = 0"

3. Use `-` to stand the piped in output. 

        head -n 1000 text_file | q "select * from - where age < 30"

5. Use q to find Docker images without repository names.

        docker images | tail -n +2 | q 'select c3 from - where c1 = "<none>"' 

6. Remove all images belong to the eclipse organization with the help of sed and q.

        docker images | sed 's/ \+/\t/g' | q -tH "select [image id] from - where repository like 'eclipse/%'" | xargs docker rmi

## Alternative Tools

1. [textql](https://github.com/dinedal/textql) (developed in Go) 
    is a very similar tool to [q](http://harelba.github.io/q/).
    It has even simplier syntax than q.
    However, 
    it has several disadvantages compared to q.
    First, it is not as actively maintained as q.
    Second, no easy way to install except in Mac (using Homebrew). 
    You have to install from source by yourself in Linux and Windows.

2. You can import text files into database tables and work on them. 
    SQLite3 is a great choice (of embeded database). 
    As a matter of fact, 
    both q and textql are based on SQLite3.
    You can refer to https://www.sqlite.org/cvstrac/wiki?p=ImportingFiles 
    on how to importing files into SQLite3.
    If you prefer a client-server database, 
    you can either MySQL, etc. 

        CREATE TABLE foo (
            id Int, 
            msg VarChar(255), 
            value Decimal(8, 4)
        )
        ;

        LOAD DATA INFILE '/tmp/data.txt' 
        INTO TABLE foo
        ;
    
## References

http://harelba.github.io/q/