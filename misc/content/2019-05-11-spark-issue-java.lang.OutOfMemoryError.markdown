Status: published
Date: 2019-05-11 02:50:52
Author: Benjamin Du
Slug: spark-issue-java.lang.OutOfMemoryError
Title: Spark Issue Java.Lang.Outofmemoryerror
Category: Computer Science
Tags: programming, Spark, issue, big data

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

Cause:  Executor out of memory

Solution: Increase executor memory from 4G to 6G: --executor-memory "6G" 

Reference:

 http://stackoverflow.com/questions/27462061/why-does-spark-fail-with-java-lang-outofmemoryerror-gc-overhead-limit-exceeded
