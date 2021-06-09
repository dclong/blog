Status: published
Date: 2019-12-13 10:55:31
Author: Benjamin Du
Slug: dataframe-for-jvm
Title: Dataframe for JVM
Category: Computer Science
Tags: programming, DataFrame, Spark, Tablesaw, krangl, JVM

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Spark DataFrame

Spark DataFrame is a great implementation of distributed DataFrame,
if you don't mind having dependency on Spark.
It can be used in a non-distributed way of course.
Spark DataFrame is mostly friendly for Scala (Spark/Scala) and Python (PySpark),
and can be used in Jupyter/Lab notebooks.

## pandas 

Via Python/Java interfaces (jpype, py4j or pyjnius).

## Tablesaw

Tablesaw is currently the most mature non-distributed DataFrame implementation for JVM languages.
However, 
its usability is still far behind Spark DataFrame and Python pandas DataFrame.


## [krangl](https://github.com/holgerbrandl/krangl)
krangl is a DataFrame implementation in Kotlin.