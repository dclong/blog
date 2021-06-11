Status: published
Date: 2017-08-22 12:58:10
Author: Ben Chuanlong Du
Slug: scala-errors
Title: Common Errors Encountered in Scala and Solutions
Category: Computer Science
Tags: programming, Scala, error, issue, version
Modified: 2020-05-22 12:58:10

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Java Version Issue

    Unsupported major minor version 

    https://stackoverflow.com/questions/22489398/unsupported-major-minor-version-52-0



## java.lang.NoSuchMethodError: scala.Product.$init$

> Fixing the Scala error: java.lang.NoSuchMethodError: scala.Product.$init$

It probably means 
This error is likely due to that you have a mismatch in the Scala versions 
you are using in your project. 
For example, 
I was using Scala 2.11 but mistakely specified Scala 2.12 for `scala_xml` for testing.
It is suggested that you never hardcode Scala versions but instead define Scala versions (full version and compact version) 
in variables and use the version variables when specifying dependencies.

https://alvinalexander.com/misc/fixing-scala-error-java-lang.nosuchmethoderror-scala.product-init

## Exception in thread "main" java.lang.NoClassDefFoundError: ...

This issue happens when you try to run the main function of a Scala object in IntelliJ IDEA.
There are 2 possible causes. 
First,
it might due to conflicting versions of Scala.
If so, 
unify the version of Scala will resolve the issue.
It is suggested that you never hardcode Scala versions but instead define Scala versions (full version and compact version)
in variables and use the version variables when specifying dependencies.
Second, 
it might due to the fact that Scala is specified as `compileOnly` dependency (Gradle).
If so, 
specifying Scala as `compile` dependency resolves the issue.

