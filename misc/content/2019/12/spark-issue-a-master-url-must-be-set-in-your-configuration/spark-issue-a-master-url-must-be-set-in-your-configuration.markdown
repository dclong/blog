Status: published
Date: 2019-12-21 12:14:37
Author: Benjamin Du
Slug: spark-issue-a-master-url-must-be-set-in-your-configuration
Title: Spark Issue: a Master URL Must Be Set in Your Configuration
Category: Computer Science
Tags: programming, Spark, issue, error, master, yarn, master URL, Spark issue
Modified: 2021-03-21 12:14:37

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Error Message

> Error initializzing SparkContext: A master URL must be set in your configuration.

## Possible Causes

The master of Spark cluster is not specified.

## Solutions

Add `.master("yarn")` into the following code

    :::bash
    val spark = SparkSession.builder()
        .appName("SomeAppName")
        .getOrCreate();

making it become

    :::bash
    val spark = SparkSession.builder()
        .master("yarn")
        .appName("SomeAppName")
        .getOrCreate();



## References

https://stackoverflow.com/questions/42032169/error-initializing-sparkcontext-a-master-url-must-be-set-in-your-configuration?noredirect=1&lq=1

https://slack-redir.net/link?url=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F38008330%2Fspark-error-a-master-url-must-be-set-in-your-configuration-when-submitting-a
