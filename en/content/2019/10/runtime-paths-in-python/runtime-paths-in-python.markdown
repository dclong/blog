Status: published
Date: 2019-10-18 10:20:43
Author: Benjamin Du
Slug: runtime-paths-in-python
Title: Runtime Paths in Python
Category: Computer Science
Tags: programming, Python, runtime paths


`__file__` is the path of the Python script.
Note that if you make a sybolic link to a Python script and run the symbolic link, 
then `__file__` is the path of the symbolic link.
Of course, you can use `os.path.realpath` to get real path of files.


`pathlib.Path.cwd()`, `os.getcwd()` and `'.'` returns/represents the path where the Python script was invoked,
which is often different from `__file__`.
