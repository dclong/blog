Status: published
Date: 2020-06-15 11:38:22
Author: Benjamin Du
Slug: logging-in-pyspark
Title: Logging in PySpark
Category: Computer Science
Tags: Computer Science, big data, PySpark, Spark, loguru, logging

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Excessive logging is better than no logging!
    This is generally true in distributed big data applications.
    
1. loguru works well by default while logging does not (seems that additional configuration is needed)

2. print works well too

3. Use loguru is if is available,
    otherwise, 
    use `print` or `pprint` for logging in simple PySpark scripts.