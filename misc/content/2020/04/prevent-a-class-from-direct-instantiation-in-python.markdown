Status: published
Date: 2021-02-20 08:43:33
Author: Benjamin Du
Slug: prevent-a-class-from-direct-instantiation-in-python
Title: Prevent a Class from Direct Instantiation in Python
Category: Computer Science
Tags: Computer Science, Python, class, instantiation, __new__, ABC, abstract base class

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Inherit the class `abc.ABC`

from abc import ABC

class MyABC(ABC):
    pass

## Define a Customized `__new__` Method


## Reference

https://docs.python.org/3/library/abc.html

[Preventing a class from direct instantiation in Python](https://stackoverflow.com/questions/7989042/preventing-a-class-from-direct-instantiation-in-python)
