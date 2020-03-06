Status: published
Date: 2019-12-03 10:14:14
Author: Benjamin Du
Slug: a-jni-error-has-occured
Title: A JNI Error Has Occured
Category: Computer Science
Tags: programming, Java, JNI error, dependency management

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Error Messages

Error: A JNI error has occurred, please check your installation and try again 

Caused by: java.lang.ClassNotFoundException: org.apache.spark.sql.SparkSession


## Cause

Some dependencies (Spark in this case) is not specified as a runtime dependency.
It is often a good idea to exlucde Spark from the runtime dependencies
and only specify it as test dependencies.
However, 
you will not be able to run your code directly in local.
Test can still be run of course.
