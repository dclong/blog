UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2015-01-09 15:47:17
Author: Ben Chuanlong Du
Slug: simple-data-manipulating-example
Title: Simple Data Manipulating Example
Category: Computer Science
Tags: programming, SAS, IML, R, CRAN, example

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Suppose there is a data `s` in SAS containing a variable `x`.

x
3
3
4
5
2
3
9
7
1
100
3
5
0

Now we want to create another variable `y` such that

y = 3 if x =3
y = B_2 y + 2, o.w.


This is very hard to using the data step in SAS 
while very easy to do in R or the SAS IML procedure.
