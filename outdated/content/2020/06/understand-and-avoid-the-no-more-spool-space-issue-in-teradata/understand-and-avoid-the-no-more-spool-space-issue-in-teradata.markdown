Status: published
Date: 2020-06-22 08:53:57
Author: Benjamin Du
Slug: understand-and-avoid-the-no-more-spool-space-issue-in-teradata
Title: Understand and Avoid the No More Spool Space Issue in Teradata
Category: Computer Science
Tags: Computer Science, Teradata, spool space, no more spool space, database, SQL

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Knowledge About Spool Space in Teradata

1. Volatile Tables and subqueries are both built in Spool

## Causes of No More Spool Issue 

1. The main cause of "no more spool space" errors 
    is usually data skew. 


## Some Potential Solutions

1. Choose a **good primary index** when creating a data tabel.

2. Reduce the number of rows and columns you’re working with

3. Break down a big query into smaller ones.

2. Use Subqueries to Reduce Joined Rows and Columns

3. reduce spool with COMPRESS



## References

https://robertlambert.net/2018/02/escaping-teradata-purgatory-select-failed-2646-no-more-spool-space/