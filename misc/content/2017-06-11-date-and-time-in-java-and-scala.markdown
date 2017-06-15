UUID: ea054750-361b-449f-85ea-8482e2a1b312
Status: published
Date: 2017-06-11 11:54:41
Author: Ben Chuanlong Du
Slug: date-and-time-in-java-and-scala
Title: Date and Time in Java and Scala
Category: Programming
Tags: programming, Scala, Java, date, time, java.time, Joda time

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

Use Joda time if you are using JDK <= 7
and java.time if you are using JDK8 and above.

If you do prefer Scala libraries (when working in Scala),
https://github.com/nscala-time/nscala-time wrapper of Joda time
libraryDependencies += "com.github.nscala-time" %% "nscala-time" % "2.16.0"


https://github.com/reactivecodes/scala-time
wrapper of java.time
// Requires JDK 1.8 and above
"codes.reactive" %% "scala-time" % "0.4.1"
