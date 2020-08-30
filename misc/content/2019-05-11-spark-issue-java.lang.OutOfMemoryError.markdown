Status: published
Date: 2020-08-29 22:05:22
Author: Benjamin Du
Slug: spark-issue-java.lang.OutOfMemoryError
Title: Spark Issue: Java.Lang.OutOfMemoryerror
Category: Computer Science
Tags: programming, Spark, issue, big data, OutOfMemoryError, OOM, error

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Cause:  Executor out of memory

Solution: Increase executor memory from 4G to 6G: --executor-memory "6G" 

Reference:

 http://stackoverflow.com/questions/27462061/why-does-spark-fail-with-java-lang-outofmemoryerror-gc-overhead-limit-exceeded
