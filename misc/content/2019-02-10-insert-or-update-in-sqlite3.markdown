Status: published
Date: 2019-02-10 09:51:58
Author: Benjamin Du
Slug: insert-or-update-in-sqlite3
Title: Insert Or Update in Sqlite3
Category: Computer Science
Tags: programming, SQLite3, upsert, insert or replace, insert or update

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

**Note: UPSERT does not with virtual table in SQLite3 currently!**


The UPSERT clause (following PostgreSQL syntax)
is supported in SQLite 3.24.0+.
```
INSERT INTO players (
    user_name, age
) VALUES (
    'steven', 32
) ON CONFLICT (user_name) DO UPDATE
SET age=excluded.age
;
```
For older versions of SQLite3,
you can use `INSERT or REPLACE` clause together with the trick of embedded subselects 
to keep original value of fields of the existing rows.

## References

https://stackoverflow.com/questions/15277373/sqlite-upsert-update-or-insert/15277374

https://stackoverflow.com/questions/418898/sqlite-upsert-not-insert-or-replace

https://stackoverflow.com/questions/3634984/insert-if-not-exists-else-update
