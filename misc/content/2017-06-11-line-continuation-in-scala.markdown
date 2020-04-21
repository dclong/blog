UUID: c2f77786-8408-4db9-854d-99abcec1dc38
Status: published
Date: 2017-10-22 13:35:34
Author: Ben Chuanlong Du
Slug: line-continuation-in-scala
Title: Line Continuation in Scala
Category: Computer Science
Tags: programming, Scala, line continuation

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Scala does not have a line continuation character.
It infers a semicolon always when:

1. an expression can end

2. The following (not whitespace) line begins not with a token that can start a statement

3. There are no unclosed ( or [ found before

Thus, 
to "delay" semicolon inference one can place a method call 
or the dot at the end of the line 
or place the dot at the beginning of the following line:

```scala
ConditionParser.
    parseSingleCondition("field=*value1*").
    description must equalTo("field should contain value1")

a +
b +
c
```

```scala
List(1,2,3)
    .map(_+1)
```

Wrap it in parentheses.
Note that wrap in curly braces doesn't work.
