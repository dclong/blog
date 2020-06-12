Status: published
Date: 2020-06-12 08:42:27
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

### mypy

    :::bash
    mypy your_script.py
    :::bash
    mypy --ignore-missing-imports roas.py

### [darglint](https://github.com/terrencepreilly/darglint)

A python documentation linter which checks that the docstring description matches the definition.

## Type Annotation

### [MonkeyType](https://github.com/Instagram/MonkeyType)

1. Run the following command to annotate your Python script.

        :::bash
        monkeytype run yourscript.py


2. MonkeyType supports pytest.

        :::bash
        monkeytype run `which pytest`

## Formatting

1. [yapf](https://github.com/google/yapf)

        :::bash
        yapf -d yourscript.py

2. [black](https://github.com/ambv/black)

Please refer to 
[Auto formatters for Python](https://medium.com/3yourmind/auto-formatters-for-python-8925065f9505)
for detailed comparison between yapf and black.

## Debugging

1. [pdb](https://docs.python.org/3/library/pdb.html)


## Installation of the Tools

    :::bash
    pip3 install yapf, pylint, monkeytype, mypy

    :::bash
    conda install -c conda-forge MonkeyType
    conda install mypy
