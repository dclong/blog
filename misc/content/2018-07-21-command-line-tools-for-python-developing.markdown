Status: published
Date: 2020-07-23 14:27:55
Author: Ben Chuanlong Du
Slug: command-line-tools-for-python-developing
Title: Command-line Tools for Python Developing
Category: Computer Science
Tags: programming, Python development, command-line, pylint, yapf, pdb, linter, formatting, debugging


## Lint Python Scripts

### [isort](https://github.com/timothycrosley/isort)
[isort](https://github.com/timothycrosley/isort)
is a Python utility/library to sort imports.

### [pylint](https://github.com/PyCQA/pylint)

    :::bash
    pylint your_script.py

### [mypy](https://github.com/python/mypy)

    :::bash
    mypy your_script.py
    :::bash
    mypy --ignore-missing-imports roas.py

### [darglint](https://github.com/terrencepreilly/darglint)

A python documentation linter which checks that the docstring description matches the definition.

## [Type Annotation](http://www.legendu.net/misc/blog/type-annotation-in-python/)

## Formatting

1. [yapf](https://github.com/google/yapf)

        :::bash
        yapf -d yourscript.py

2. [black](https://github.com/ambv/black)

Please refer to 
[Auto formatters for Python](https://medium.com/3yourmind/auto-formatters-for-python-8925065f9505)
for detailed comparison between yapf and black.

## [coala](https://github.com/coala/coala/)
coala provides a unified command-line interface for linting and fixing all your code, regardless of the programming languages you use.

## coverage 

converage

https://coveralls.io/

https://github.com/codecov/codecov-python

## Debugging

1. [pdb](https://docs.python.org/3/library/pdb.html)

## CICD

1. [nox](http://www.legendu.net/misc/blog/tips-on-nox/)

2. [pre-commit](https://github.com/pre-commit/pre-commit]
    A framework for managing and maintaining multi-language pre-commit hooks.

## Installation of the Tools

    :::bash
    pip3 install yapf, pylint, monkeytype, mypy

    :::bash
    conda install -c conda-forge MonkeyType
    conda install mypy

## References

https://cjolowicz.github.io/posts/hypermodern-python-01-setup/

https://cjolowicz.github.io/posts/hypermodern-python-02-testing/

https://cjolowicz.github.io/posts/hypermodern-python-03-linting/#managing-dependencies-in-nox-sessions-with-poetry

https://cjolowicz.github.io/posts/hypermodern-python-02-testing/#code-coverage-with-coveragepy

https://github.com/life4/awesome-python-code-formatters