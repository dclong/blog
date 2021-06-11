Status: published
Date: 2019-02-07 22:02:18
Author: Benjamin Du
Slug: debugging-unit-testing-cicd-python
Title: Debugging, Unit Testing and CICD in Python
Category: Computer Science
Tags: programming, Python, unit testing, debugging, command-line tools, development, dev
Modified: 2020-10-07 22:02:18

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Debugging

1. [pdb](https://docs.python.org/3/library/pdb.html)

[Goodbye Print, Hello Debugger! - Nina Zakharenko - Talk](https://www.youtube.com/watch?v=5AYIe-3cD-s)


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

## [coverage](http://www.legendu.net/misc/blog/measure-python-code-coverage)

Please refer to 
[coverage](http://www.legendu.net/misc/blog/measure-python-code-coverage)
for details.

## Mock and pytest Fixtures


## CICD

1. It is suggested that you leverage professional CICD tools such as GitHub Actions 
    instead of 
    [nox](http://www.legendu.net/misc/blog/tips-on-nox/)
    or
    [pre-commit](https://github.com/pre-commit/pre-commit] (Git hooks)
    for CICD. 
    However, 
    Git hooks can be useful for simple and fast local code formatting.

2. GitHub Actions seems to the best CICD (and more) tool for projects on GitHub.

## Travis CI

To setup Travis-CI on a github project, all you have to do is:

add a .travis.yml file at the root of your project
create an account at travis-ci.com and activate your project
The features you get are:

Travis will run your tests for every push made on your repo
Travis will run your tests on every pull request contributors will make


## Jenkins 
Jenkins is another popular one.
https://stackoverflow.com/questions/32422264/jenkins-vs-travis-ci-which-one-would-you-use-for-a-open-source-project

## [GoCD](https://www.gocd.org/)

## Reference

http://www.legendu.net/misc/blog/summary-of-python-linting-tools/

http://www.legendu.net/misc/blog/type-annotation-in-python/