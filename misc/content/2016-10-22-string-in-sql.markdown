UUID: 457f14c2-bc29-49c4-939d-4c35e67447ef
Status: published
Date: 2016-11-20 18:55:31
Author: Ben Chuanlong Du
Slug: string-in-sql
Title: String in SQL
Category: Computer Science
Tags: programming, SQL, string

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## Teradata
regexp_instr
REGEXP_LIKE
REGEXP_REPLACE
REGEXP_SUBSTR

1. trim
trim specified pad characters or bytes from a character or byte string

2. like %, _
like, case-insensitive
You can also 
`like any (pattern_1, pattern_2, ...)`
`like all (pattern_1, pattern_2, ...)`

3. Collation can be simply thought of as sort order.


CHAR2HEXINT
convert a character string to hexadecimal representation


• INDEX
• POSITION
get the starting position of a substring within another string

LOWER
convert a character string to lowercase

SOUNDEX
get the Soundex code for a character string


• SUBSTRING
• SUBSTR
extract a substring from another string

TRANSLATE
translate a character string to another server character set

TRANSLATE_CHK
determine if TRANSLATE can successfully translate a character string to a specified server character set


UPPER
convert a character string to uppercase

VARGRAPHIC
convert a character string to VARGRAPHIC representation
