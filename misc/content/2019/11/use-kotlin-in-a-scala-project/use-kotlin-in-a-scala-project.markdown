Status: published
Date: 2019-11-27 09:25:16
Author: Benjamin Du
Slug: use-kotlin-in-a-scala-project
Title: Use Kotlin in a Scala Project
Category: Computer Science
Tags: programming, JVM, Kotlin, Scala

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Methods of a Kotlin object can be called in a Scala project by `KotlinObject.INSTANCE.methodToCall()`

2. You might need to provide the Kotlin standard library `kotlin-stdlib.jar`
    in order to run the compiled JAR. 
    One way to avoid this is to compile a fat/uber JAR 
    that contains all dependencies (including `kotlin-stdlib.jar`).

##. Use Kotlin in Spark/Scala

http://tomstechnicalblog.blogspot.com/2016/11/using-kotlin-language-with-spark.html?m=1

https://thegmariottiblog.blogspot.com/2017/05/lets-make-apache-spark-more-kotlinesque.html
