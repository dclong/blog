Status: published
Date: 2018-07-08 10:46:18
Author: Ben Chuanlong Du
Slug: useful-tools-for-python-developing
Title: Useful Tools for Python Developing
Category: Computer Science
Tags: programming, Python, development, command-line, pylint, yapf, pdb, linter, formatting, debugging, dev, lint, format, dead code, type, annotation
Modified: 2025-06-03 01:05:56


[vulture](https://github.com/jendrikseipp/vulture)
finds unused code in Python programs. 
It is useful for cleaning up and finding errors in large code bases. 

- [pandas-stubs](https://pypi.org/project/pandas-stubs/)

## Testing

- [pytest](https://github.com/pytest-dev/pytest)

## Typing Checker

https://github.com/astral-sh/ty
An extremely fast Python type checker and language server, written in Rust.

https://github.com/facebook/pyrefly
A fast type checker and IDE for Python

- [pytype](https://github.com/google/pytype)

## Lint Python Scripts

### [ruff](https://github.com/charliermarsh/ruff/)
[ruff](https://github.com/charliermarsh/ruff/)
is an extremely fast Python linter, written in Rust.


### [pylint](http://www.legendu.net/misc/blog/pylint-tips/)
[pylint](http://www.legendu.net/misc/blog/pylint-tips/)

### [flake8](http://www.legendu.net/misc/blog/use-flake8-to-lint-python-scripts/)
[flake8](http://www.legendu.net/misc/blog/use-flake8-to-lint-python-scripts/)

1. `Flake8` focus on logical errors rather than stylistic errors.
    It strives to reduce false positives.

2. `pylint` performs deeper analysis and thus is slower.


## Formatting

The Python package 
[black](https://github.com/ambv/black)
is the best formatting tool for Python currently.

1. [yapf](https://github.com/google/yapf)

        :::bash
        yapf -d yourscript.py

2. [black](https://github.com/ambv/black)

Please refer to 
[Auto formatters for Python](https://medium.com/3yourmind/auto-formatters-for-python-8925065f9505)
for detailed comparison between yapf and black.

## [Debugging, Unit Testing and CICD](http://www.legendu.net/misc/blog/unit-testing-debugging-python/)


## Reference

- [Type Annotation in Python](http://www.legendu.net/misc/blog/type-annotation-in-python/)

- [isort](http://www.legendu.net/misc/blog/sort-python-imports-using-isort/)

- [pylint](http://www.legendu.net/misc/blog/pylint-tips/)

- [darglint](https://github.com/terrencepreilly/darglint) checks that the docstring description matches the definition.

- [coala](https://github.com/coala/coala/) provides a unified command-line interface 
    for linting and fixing all your code, regardless of the programming languages you use.

- [Type Annotation](http://www.legendu.net/misc/blog/type-annotation-in-python/)


https://cjolowicz.github.io/posts/hypermodern-python-01-setup/

https://cjolowicz.github.io/posts/hypermodern-python-02-testing/

https://cjolowicz.github.io/posts/hypermodern-python-03-linting/#managing-dependencies-in-nox-sessions-with-poetry

https://cjolowicz.github.io/posts/hypermodern-python-02-testing/#code-coverage-with-coveragepy

