Status: published
Date: 2019-12-28 11:49:09
Author: Benjamin Du
Slug: iterators-and-generators-in-python
Title: Iterators and Generators in Python
Category: Computer Science
Tags: programming, Python, generator, iterator

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!

## Iterator vs Generator

Generator is a special case of Iterator.
Generator is easy and convenient to use but at additional cost (memory and speed).
If you need performance, use plain iterator (with the help of the `itertools` module).
If you need convenience and concise code, use generator.

Please refer to [Python Generator vs Iterator](https://data-flair.training/blogs/python-generator-vs-iterator/)
for more detailed discussions.

## When Not to Use Generator 

1. You need to access the data multiple times (i.e. cache the results instead of recomputing them).

        for i in outer:           # used once, okay to be a generator or return a list
            for j in inner:       # used multiple times, reusing a list is better
                ...

2. You need random access (or any access other than forward sequential order).

        for i in reversed(data): ...     # generators aren't reversible

        s[i], s[j] = s[j], s[i]          # generators aren't indexable

3. You need to join strings (which requires two passes over the data).

        s = ''.join(data)                # lists are faster than generators in this use case

4. You are using PyPy which sometimes can't optimize generator code as much as it can 
    with normal function calls and list manipulations.

## References

https://stackoverflow.com/questions/245792/when-is-not-a-good-time-to-use-python-generators

https://data-flair.training/blogs/python-generator-vs-iterator/
