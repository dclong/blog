Status: published
Date: 2020-08-08 10:46:18
Author: Ben Chuanlong Du
Slug: useful-tools-for-python-developing
Title: Useful Tools for Python Developing
Category: Computer Science
Tags: programming, Python development, command-line, pylint, yapf, pdb, linter, formatting, debugging
Modified: 2020-08-08 10:46:18


## Lint Python Scripts

- [isort](http://www.legendu.net/misc/blog/sort-python-imports-using-isort/)

- [pylint](http://www.legendu.net/misc/blog/pylint-tips/)

- [darglint](https://github.com/terrencepreilly/darglint) checks that the docstring description matches the definition.

- [coala](https://github.com/coala/coala/) provides a unified command-line interface 
    for linting and fixing all your code, regardless of the programming languages you use.

- [Type Annotation](http://www.legendu.net/misc/blog/type-annotation-in-python/)

## Formatting

1. [yapf](https://github.com/google/yapf)

        :::bash
        yapf -d yourscript.py

2. [black](https://github.com/ambv/black)

Please refer to 
[Auto formatters for Python](https://medium.com/3yourmind/auto-formatters-for-python-8925065f9505)
for detailed comparison between yapf and black.

## [Debugging, Unit Testing and CICD](http://www.legendu.net/misc/blog/unit-testing-debugging-python/)

## References


https://cjolowicz.github.io/posts/hypermodern-python-01-setup/

https://cjolowicz.github.io/posts/hypermodern-python-02-testing/

https://cjolowicz.github.io/posts/hypermodern-python-03-linting/#managing-dependencies-in-nox-sessions-with-poetry

https://cjolowicz.github.io/posts/hypermodern-python-02-testing/#code-coverage-with-coveragepy

https://github.com/life4/awesome-python-code-formatters