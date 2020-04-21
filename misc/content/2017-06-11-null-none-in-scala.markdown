UUID: eb376cce-1701-4c29-933b-ef40621a7750
Status: published
Date: 2017-10-22 13:37:40
Author: Ben Chuanlong Du
Slug: null,-none-and-alike-in-Scala
Title: Null, None and Alike in Scala
Category: Computer Science
Tags: programming, null, none, Scala

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

`Nil` represents an emptry List of anything of zero length. 
It is not that it refers to nothing but it refers to List which has no contents.
In other words, `Nil` is equivalent to `List()` or `List.empty`.

`Null` is a Trait and `null` is an instance of `Null`,
which is similar to null in Java.

`Nothing` is a Trait. 
It is a subtype of everything 
but not superclass of anything. 
There are no instances of Nothing.

`None` is used to represent a sensible return value,
which is a way to avoid null pointer exception.
`Option` has exactly 2 subclasses: `Some` and `None`. 
`None` signifies no result from the method.

`Unit` represents type of method that does not return a value of anys sort.

`Any` is the supertype of `AnyRef` and `AnyVal`. 
`AnyRef` is the supertype of all the reference classes (like String, List, Iterable) in scala. 
`AnyVal` is the supertype of all the value classes (like Int, Float, Double, Byte, Short..). 
`Null` is a subtype of all the reference classes. 
`null` is the only instance of `Null`. 
`Nothing` is subtype of every other type i.e of reference and value classes. 

Think- AnyRef == Object in Java.

## Ref

http://oldfashionedsoftware.com/2008/08/20/a-post-about-nothing/
