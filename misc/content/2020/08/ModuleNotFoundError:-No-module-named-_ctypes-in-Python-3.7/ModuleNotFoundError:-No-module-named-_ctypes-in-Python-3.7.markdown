Status: published
Date: 2020-08-14 10:47:00
Author: Benjamin Du
Slug: ModuleNotFoundError:-No-module-named-_ctypes-in-Python-3.7
Title: ModuleNotFoundError: No Module Named _Ctypes in Python 3.7
Category: Computer Science
Tags: Computer Science, Python, 3.7, ctypes, _ctypes, ModuleNotFoundError
Modified: 2020-08-14 10:47:00

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Issue

The error message "Modulenotfounderror: No Module Named _Ctypes"
is thrown when intalling packages in Python 3.7.

## Cause

`libffi-dev` is needed to cleanly build Python 3.7.

## Solution

1. Remove Python 3.7.
2. Install `libffi-dev`

        :::bash
        sudo apt-get update
        sudo apt-get install libffi-dev

3. Reinstall Python 3.7. 

## References 

https://stackoverflow.com/questions/27022373/python3-importerror-no-module-named-ctypes-when-using-value-from-module-mul