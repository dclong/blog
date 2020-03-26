Status: published
Date: 2020-03-24 19:09:23
Author: Ben Chuanlong Du
Slug: scala-tips
Title: Tips on Scala
Category: Computer Science
Tags: programming, Scala, functional programming, big data, Spark

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

- [Scala Root Package](http://www.scala-lang.org/api/current/#package)
- [Scala Documentation](http://docs.scala-lang.org/index.html)
- [Scala Tutorial](http://docs.scala-lang.org/tutorials/)
- [Scala Coding Style](http://docs.scala-lang.org/style/)
- [Scala Glossary](http://docs.scala-lang.org/glossary/)
- [Scala Cheatsheet](http://docs.scala-lang.org/cheatsheets/)
- [Scala Style Guide](https://github.com/databricks/scala-style-guide)

## Trick & Traps 

- [Scala and 22](https://underscore.io/blog/posts/2016/10/11/twenty-two.html)

## General Tips

1. IntelliJ IDEA is the recommended IDE.
    Eclipse (with the Scala IDE plugin) is alternative.

## Style

1. avoid using break, continue, return even though you can use them in Scala

2. avoid using while loop but don't go too crazy

## scala.util.Random

It is a wrapper of `java.util.Random` which is NOT a high quality random number generator.

## Argument Parsing


Scala Args Parsing 

https://github.com/scopt/scopt


## Links

http://blog.plasmaconduit.com/reduve-vs-fold-in-scala/

http://stackoverflow.com/questions/9727637/new-keyword-in-scala

### Collections

http://docs.scala-lang.org/overviews/collections/overview.html

http://docs.scala-lang.org/overviews/collections/performance-characteristics.html

http://alvinalexander.com/scala/understanding-scala-collections-hierarchy-cookbook

http://stackoverflow.com/questions/19478244/how-does-a-case-anonymous-function-really-work-in-scala
