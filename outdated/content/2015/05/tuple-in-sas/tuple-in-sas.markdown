UUID: 854033de-e834-44d4-a6ff-ea7baeccd3f8
Status: published
Date: 2015-05-26 02:34:45
Author: Ben Chuanlong Du
Slug: tuple-in-sas
Title: Tuple in SAS
Category: Computer Science
Tags: programming, SAS, tuple, comma, space
Modified: 2015-05-26 02:34:45

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
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

