Status: published
Date: 2020-08-18 18:27:32
Author: Benjamin Du
Slug: tips-on-pyenv
Title: Tips on pyenv
Category: Computer Science
Tags: programming, Python, pyenv, versions
Modified: 2020-08-18 18:27:32

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

1. Precedence of versions of Python are defined in `$HOME/.pyenv/version`.
    Place the version of Python that you want to use in the first line of the file.

2. The root directory of pyenv is controled by the environment variable `$PYENV_ROOT`. 
    You can report the root directory of pyenv by running the command `pyenv root`.

## References 

https://github.com/pyenv/pyenv

https://github.com/pyenv/pyenv-installer

https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/

https://medium.com/faun/pyenv-multi-version-python-development-on-mac-578736fb91aa#:~:text=pyenv%20makes%20it%20easy%20to,a%20tool%20like%20tox%20handy.

https://realpython.com/intro-to-pyenv/

https://github.com/pyenv/pyenv#locating-the-python-installation