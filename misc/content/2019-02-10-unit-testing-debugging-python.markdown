Status: published
Date: 2020-05-30 20:38:30
Author: Benjamin Du
Slug: debugging-unit-testing-cicd-python
Title: Debugging, Unit Testing and CICD in Python
Category: Computer Science
Tags: programming, Python, unit testing, debugging, command-line tools, development, dev

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Debugging

1. [pdb](https://docs.python.org/3/library/pdb.html)

## Unit Testing

1. When separate teams/people are developing different components in a big project 
    and unit testing has to be written before other dependent components are ready,
    make sure that unit tests cover agreed interfaces.

2. Printing intermediate variables is the universal way (even inefficienty many times) for debugging.
    [PySnooper](https://github.com/cool-RR/PySnooper) is debugging tool 
    based on the idea of printing intermediate varibles 
    but is great improved over the plain `print` function 
    and is both easy and fun to use.

3. `unitest` is the official unit testing tool in Python
    and thus has better support and integration with other tools generally speaking. 
    However, 
    `pytest` is more concise than `unittest` and makes unit testing more efficiency.
    `pytest` is also widely adopted.
    Please refer to
    [Write Unit Tests Using unittest in Python](http://www.legendu.net/misc/blog/write-unit-tests-using-unittest-in-Python/)
    and
    [Write Unit Tests Using PyTest in Python](http://www.legendu.net/misc/blog/pytest-tips/)
    for more details on how to use unittest and pytest.

## Doctest 

## hypothesis

## coverage 

converage

https://coveralls.io/

https://github.com/codecov/codecov-python



## Mock and pytest Fixtures


## CICD

1. [nox](http://www.legendu.net/misc/blog/tips-on-nox/)

2. [pre-commit](https://github.com/pre-commit/pre-commit]
    A framework for managing and maintaining multi-language pre-commit hooks.
