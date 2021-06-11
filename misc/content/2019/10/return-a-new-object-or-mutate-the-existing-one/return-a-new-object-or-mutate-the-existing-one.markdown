Status: published
Date: 2019-10-31 17:09:56
Author: Benjamin Du
Slug: return-a-new-object-or-mutate-the-existing-one
Title: Return a New Object Or Mutate the Existing Object
Category: Computer Science
Tags: programming, Python, design pattern, copy, mutate
Modified: 2019-10-31 17:09:56

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Generally speaking,
prefer to return a new object rather than mutating the existing object.
This is true in most programming languages besides C who seeks for best peformance.


The pandas package in Python keeps a good balance between good design and performance.
By default, 
pandas always return a copy.
When a DataFrame is large (and performance matteers),
in-place changes on the DataFrame (rather than copy) can be made by specifying the option `inplace=True`.


## References

[Idiomatic Python - return new object or mutate the existing one?](https://www.reddit.com/r/learnpython/comments/2931ph/idiomatic_python_return_new_object_or_mutate_the/)
