Status: published
Date: 2020-05-07 12:20:51
Author: Benjamin Du
Slug: insert-or-update-in-sqlite3
Title: Insert Or Update in SQLite3
Category: Computer Science
Tags: programming, SQLite3, upsert, insert or replace, insert or update

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

**Note: UPSERT does NOT work with virtual table in SQLite3 currently!**


The UPSERT clause (following PostgreSQL syntax)
is supported in SQLite 3.24.0+.

    :::sql
    INSERT INTO players (
        user_name, age
    ) VALUES (
        'steven', 32
    ) ON CONFLICT (user_name) DO UPDATE
    SET age=excluded.age
    ;

For older versions of SQLite3,
you can use `INSERT or REPLACE` clause together with the trick of embedded subselects 
to keep original value of fields of the existing rows.

## References

https://stackoverflow.com/questions/15277373/sqlite-upsert-update-or-insert/15277374

https://stackoverflow.com/questions/418898/sqlite-upsert-not-insert-or-replace

https://stackoverflow.com/questions/3634984/insert-if-not-exists-else-update
