Status: published
Date: 2019-07-26 18:55:03
Author: Ben Chuanlong Du
Slug: command-line-tools-for-python-developing
Title: Command-line Tools for Python Developing
Category: Computer Science
Tags: programming, Python development, command-line, pylint, yapf, pdb, linter, formatting, debugging


## Check Python Scripts

### [pylint](https://github.com/PyCQA/pylint)

    pylint your_script.py

### mypy

    mypy your_script.py

    mypy --ignore-missing-imports roas.py

## Type Annotation

### [MonkeyType](https://github.com/Instagram/MonkeyType)

1. Run the following command to annotate your Python script.

        monkeytype run yourscript.py


2. MonkeyType supports pytest.

        monkeytype run `which pytest`

## Formatting

1. [yapf](https://github.com/google/yapf)

        yapf -d yourscript.py

2. [black](https://github.com/ambv/black)

Please refer to 
[Auto formatters for Python](https://medium.com/3yourmind/auto-formatters-for-python-8925065f9505)
for detailed comparison between yapf and black.

## Debugging

1. [pdb](https://docs.python.org/3/library/pdb.html)


## Installation of the Tools

```
pip3 install yapf, pylint, monkeytype, mypy
```
```
conda install -c conda-forge MonkeyType
conda install mypy
```
