UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Date: 2014-10-19 19:40:40
Author: Ben Chuanlong Du
Slug: generating-random-numbers-in-java
Title: Generating Random Numbers in Java
Category: Computer Science
Tags: programming, random number generating, Java

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. The java.util.Random class provides a low-quallity generator 
suitable for "informal" uses of random numbers.

2. It is suggested that you use the classs 
  [org.apache.commons.math3.random.RandomDataGenerator](http://commons.apache.org/proper/commons-math/javadocs/api-3.6/org/apache/commons/math3/random/RandomDataGenerator.html)
  for generating random numbers if quality is of a concern. 
  Please refer to 
  [Summary on Random Number Generators](http://www.legendu.net/en/blog/summary-random-number-generators/)
  for more details.