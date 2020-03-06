Status: published
Date: 2019-05-09 22:30:29
Author: Benjamin Du
Slug: check-whether-a-file-exists-in-spark
Title: Check Whether a File Exists in Spark
Category: Computer Science
Tags: programming, Spark, Hadoop, FileSystem, file system

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**



## org.apache.hadoop.fs.FileSystem
```
val conf = sc.hadoopConfiguration
val fs = org.apache.hadoop.fs.FileSystem.get(conf)
val exists = fs.exists(new org.apache.hadoop.fs.Path("/path/on/hdfs/to/SUCCESS.txt"))
```


```
import org.apache.hadoop.fs.FileSystem
import org.apache.hadoop.fs.Path

val hadoopfs: FileSystem = FileSystem.get(spark.sparkContext.hadoopConfiguration)

def testDirExist(path: String): Boolean = {
  val p = new Path(path)
  hadoopfs.exists(p) && hadoopfs.getFileStatus(p).isDirectory
}
val filteredPaths = paths.filter(p => testDirExists(p))
val dataframe = spark.read.parquet(filteredPaths: _*)
```

## org.apache.spark.streaming.util.HdfsUtils

`org.apache.spark.streaming.util.HdfsUtils` is implemented based on `org.apache.hadoop.fs.FileSystem`.

## References

https://spark.apache.org/docs/latest/api/java/index.html?org/apache/spark/streaming/util/HdfsUtils.html

https://stackoverflow.com/questions/30405728/apache-spark-check-if-file-exists


https://stackoverflow.com/questions/45193825/spark-read-file-only-if-the-path-exists?rq=1

https://stackoverflow.com/questions/27023766/spark-iterate-hdfs-directory
