Status: published
Date: 2015-02-05 22:58:56
Author: Ben Chuanlong Du
Slug: map-function-in-python
Title: Function Programming in Python
Category: Computer Science
Tags: programming, Python, map, functional programming, reduce, apply

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


1. The built-in function `map` applies a function to each element of an iterable.
    `map` is not useful mostly of time as Python has list comprehension, etc.
    `map` support iterating multiple iterables at the same time.

        map(f, sequence1, sequence2)

    which is equivalent to

        [f(x1, x2) for x1, x2 in zip(sequence1, sequence2)]


2. There are some useful functions in the modules `functools` and `operator`.
    Below is the functional programming way of summing all elements in an array.

        functools.reduce(operator.add, L)


## References

http://briansimulator.org/

https://pypi.python.org/pypi/brian/
