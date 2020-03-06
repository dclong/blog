UUID: 4f4de2f8-b6e1-4792-b842-f81b2d103490
Status: published
Date: 2015-05-17 18:38:29
Author: Ben Chuanlong Du
Slug: combine-data-vertically-in-sas
Title: Combine Data Vertically in SAS
Category: Computer Science
Tags: programming, SAS, combine, concatenate, vertically, rbind

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**



1. union all (keep all rows) vs union (distinct/unique) 
prefer to use union all
union and union all relies on column positions
another way is to use proc append which appends data by matching column names


append as advantages over sql union
append tries to match column names while sql union relies on the column orders. 

be careful when you use append, be sure to remove previous data sets ...
as you might run the same piece of code multiple times
