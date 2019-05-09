Status: published
Date: 2019-05-09 19:48:11
Author: Benjamin Du
Slug: spark-unable-to-find-encoder-type-issue
Title: Unable to Find Encoder Type Issue in Spark
Category: Programming
Tags: programming, Spark, issue, encoder

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Issue Unable to find encoder for type stored in a Dataset

## Solution 

Import Spark implicits in the right scope resolves the issue.

    import spark.implicits._


## References 

https://stackoverflow.com/questions/38664972/why-is-unable-to-find-encoder-for-type-stored-in-a-dataset-when-creating-a-dat
