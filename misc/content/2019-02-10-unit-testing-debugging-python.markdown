Status: published
Date: 2020-05-03 21:42:55
Author: Benjamin Du
Slug: unit-testing-debugging-python
Title: Unit Testing and Debugging Tools for Python
Category: Computer Science
Tags: programming, Python, unit testing, debugging, command-line tools, development, dev

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

- [TDDA](https://github.com/tdda/tdda)


## [PySnooper](https://github.com/cool-RR/PySnooper)

A poor man's tool for debugging which is much better than print.

## unittest vs pytest

1. `unitest` is the official unit testing tool in Python
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

## Coverage

## Mock and pytest Fixtures

## Flake8 vs MyPy vs pylint 

1. Flake8 focus on logical errors rather than stylistic errors.
    It strives to reduce false positives.

2. `mypy` does the best on type hint.

3. `pylint` performs deeper analysis and thus is slower.

To sum up,
I'd try the tools in the following order
`Flake8 > mypy > pylint`.
