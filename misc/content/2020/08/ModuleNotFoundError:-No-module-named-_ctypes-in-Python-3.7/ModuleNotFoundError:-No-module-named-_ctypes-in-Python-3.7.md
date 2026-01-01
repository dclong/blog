Status: published
Date: 2020-08-14 10:47:00
Author: Benjamin Du
Slug: ModuleNotFoundError:-No-module-named-_ctypes-in-Python
Title: ModuleNotFoundError: No Module Named _Ctypes in Python
Category: Computer Science
Tags: Computer Science, Python, ctypes, _ctypes, ModuleNotFoundError, error, exception
Modified: 2026-01-01 08:31:48

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Issue

The error message "ModuleNotFoundError: No Module Named _Ctypes"
is thrown when using Python.

## Cause

A crucial built-in module, _ctypes, 
is either missing from your Python installation or cannot be located.

For more discussions,
please refer to
[Chat with Gemini - Resolving _ctypes Module Not Found](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221XBVxZepSxAYqCPelMgHG000RIFLu5a8w%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
.

## Solution

1. Remove Python.
2. Install `libffi-dev`

        :::bash
        sudo apt-get update
        sudo apt-get install libffi-dev

3. Reinstall Python. 

## References 

- [Exception and Error Handling in Python](https://misc.legendu.net/blog/exception-and-error-handling-in-python/)

- [Python3: ImportError: No module named '_ctypes' when using Value from module multiprocessing](https://stackoverflow.com/questions/27022373/python3-importerror-no-module-named-ctypes-when-using-value-from-module-mul)
