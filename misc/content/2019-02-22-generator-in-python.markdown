Status: published
Date: 2019-02-22 08:55:04
Author: Benjamin Du
Slug: generator-in-python
Title: Generator in Python
Category: Programming
Tags: programming, Python, generator, iterator

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


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
