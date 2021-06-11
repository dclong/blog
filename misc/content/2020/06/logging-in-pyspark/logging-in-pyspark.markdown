Status: published
Date: 2020-06-15 11:38:22
Author: Benjamin Du
Slug: logging-in-pyspark
Title: Logging in PySpark
Category: Computer Science
Tags: Computer Science, big data, PySpark, Spark, loguru, logging
Modified: 2020-06-15 11:38:22

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Excessive logging is better than no logging!
    This is generally true in distributed big data applications.
    
2. Use `loguru` if it is available.
    If you have to use the `logging` module,
    be aware of traps in using it.
    For more details, 
    please refer to [Hands on the logging Module in Python](http://www.legendu.net/misc/blog/python-logging-module/).