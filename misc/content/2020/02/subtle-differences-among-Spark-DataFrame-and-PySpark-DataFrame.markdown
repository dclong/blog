Status: published
Date: 2020-02-19 16:44:50
Author: Benjamin Du
Slug: subtle-differences-among-Spark-DataFrame-and-PySpark-DataFrame
Title: Subtle Differences Among Spark DataFrame and PySpark Dataframe
Category: Computer Science
Tags: programming, big data, Spark, PySpark, DataFrame, difference

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Besides using the `col` function to reference a column,
    Spark/Scala DataFrame supports using `$"col_name"` 
    (based on implicit conversion and must have `import spark.implicit._`)
    while PySpark DataFrame support using `df.col_name` 
    (similar to what you can do with a pandas DataFrame).

    |                     | Spark/Scala        | PySpark            |
    |---------------------|--------------------|--------------------|
    |                     | col\("col\_name"\) | col\("col\_name"\) |
    | Implicit Conversion | $"col\_name"       | X                  |
    | Dot reference       | X                  | df\.col\_name      |

    
3. `===` (null safe equality comparison) is supported in Spark/Scala but not available in PySpark.

## References

https://spark.apache.org/docs/latest/api/java/index.html?org/apache/spark/sql/Dataset.html

https://spark.apache.org/docs/latest/api/java/index.html?org/apache/spark/sql/functions.html

https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Row.html

https://spark.apache.org/docs/latest/api/python/pyspark.sql.html

https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame

https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.Column

https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#module-pyspark.sql.functions
