UUID: 854033de-e834-44d4-a6ff-ea7baeccd3f8
Status: published
Date: 2015-05-26 02:34:45
Author: Ben Chuanlong Du
Slug: tuple-in-sas
Title: Tuple in SAS
Category: Computer Science
Tags: programming, SAS, tuple, comma, space

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


A tuple can be used both in a sql procedure or a data step.
Values are usually separated by commas, 
e.g., `(v1, v2, v3)`.
However, commas are not necessary.

```SAS
where x in (v1, v2, v3) 
```
can also be
```SAS
where x in (v1 v2 v3) 
```

