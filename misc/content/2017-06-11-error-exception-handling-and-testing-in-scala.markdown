Status: published
Date: 2019-07-25 01:15:11
Author: Ben Chuanlong Du
Slug: error-exception-handling-and-testing-in-scala
Title: Error/Exception Handling and Testing in Scala
Category: Computer Science
Tags: programming

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## assert vs require vs assume

`assert` means that your program has reached an inconsistent state.
This might be a problem with the current method/function 
(think of it a bit as e.g., HTTP 500 InternalServerError).

`require` means that the caller of the method is at fault 
and should fix its call (think of it a bit as e.g., HTTP 400 BadRequest).
Use `require` whenever you want a constraint on parameters.
Use `assert` whenever you want to make sure some conditions (like invariants) are always true during execution. 
It is a way of testing.

```scala
def assert(assertion: Boolean) { 
    if (!assertion) 
        throw new java.lang.AssertionError("assertion failed") 
} 

def assume(assumption: Boolean) { 
    if (!assumption) 
        throw new java.lang.AssertionError("assumption failed") 
} 

def require(requirement: Boolean) { 
    if (!requirement) 
        throw new IllegalArgumentException("requirement failed") 
} 
```

`assert` (java.lang.AssertionError) – a predicate which needs to be proven by a static code analyser to attempt to prove. 
It is something that you expect the static checker to be able to prove at compile time.

`assume` (java.lang.AssertionError) – an axiom for a static checker. 
It is something that the static checker can rely upon.

`require` (IllegalArgumentException) – Blames the caller of the method for violating the condition. 
Used as a pre-condition. ensuring is a post-condition.


## scalaTest

1. It seems to be that scalaTest doesn't work well with junit5 at this time. 
  The suggestion is to stick to junit4 when using scalaTest.

2. Java discourages the use of Singletons and unit testing on Singletons is not supported any more in JUnit5. 
  However, 
  due to the nature of functional programming, 
  you will find Singletons to be nature in Scala.


