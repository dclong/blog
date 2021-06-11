Status: published
Date: 2021-04-19 09:53:27
Author: Benjamin Du
Slug: tips-on-pypy
Title: Tips on PyPy
Category: Computer Science
Tags: Computer Science, programming, PyPy, Python, pip, ensurepip
Modified: 2021-04-19 09:53:27

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Installation

1. Download PyPy from https://www.pypy.org/download.html.

2. Unzip it.

3. Install pip.

    :::bash
    /path/to/pypy -m ensurepip
    /path/to/pypy -m pip install ...

### Packages Failed to Install 
## pytype

wajig install gcc cmake g++

ast27/Parser/tokenizer.c:17:10: fatal error: codecs.h: No such file or directory