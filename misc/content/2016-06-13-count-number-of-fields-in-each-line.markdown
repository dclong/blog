UUID: fe55284a-a1e1-4de7-9950-5574ed757616
Status: published
Date: 2016-06-13 23:08:03
Author: Ben Chuanlong Du
Slug: count-number-of-fields-in-each-line
Title: Count Number of Fields in Each Line
Category: Computer Science
Tags: programming, data manipulation, R, awk, number, field, text file

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

Do not assume that structured text file are always in correct format.
So often want to count the number of fields in each line in a text file.
```sh
awk '{print NF}' filename
```
Unfortunately, awk does not take escaped characters into consideration.
So this only works for simple formatted (without escaped characters) text files.

There is a function named `count.field` in R.
