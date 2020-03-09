Status: published
Date: 2020-03-09 16:37:34
Author: Benjamin Du
Slug: issues-in-pip-and-solutions
Title: Issues in pip and Solutions
Category: Computer Science
Tags: Computer Science, Python, pip, issue, solution

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

## Abort trap: 6 when using `pip3 search`

The issue is due to to `pyopenssl` using old dependencies. 
It can be fixed by removing the Python package `cryptography` package
and then upgrading `cryptography` to version 2.8.

1. Find the location of the Python package cryptography.

        :::bash
        pip3 show cryptograph

2. Remove the whole package directory.

        :::bash
        sudo rm -rf /path/to/cryptograph

3. Reinstall the latest version of `cryptograph`.

        :::bash
        pip3 install cryptograph



https://github.com/pypa/pip/issues/7254
