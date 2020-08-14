Status: published
Date: 2020-08-14 10:58:59
Author: Benjamin Du
Slug: tips-on-pyenv
Title: Tips on pyenv
Category: Computer Science
Tags: programming, Python, pyenv, versions

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

`pyenv` lets you easily switch between multiple versions of Python. 
It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.

## Install pyenv

    :::bash
    curl https://pyenv.run | bash

## Usage 

1. Install a specific version of Python.

        :::bash
        pyenv install 3.7.8 

2. Use a specific version of Python.

        :::bash
        pyenv local 3.7.8

3. Uninstall a specific version of Python 

        :::bash 
        pyenv uninstall 3.7.8 

## Tips & Traps

Precedence of versions of Python are defined in `$HOME/.pyenv/version`.
Place the version of Python that you want to use in the first line of the file.

## References 

https://github.com/pyenv/pyenv

https://github.com/pyenv/pyenv-installer