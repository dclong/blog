Status: published
Author: Ben Chuanlong Du
Date: 2019-10-23 06:40:27
Slug: python-tips
Title: Tips on Python
Category: Computer Science
Tags: tips, Python, programming

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

<img src="http://dclong.github.io/media/python/python.png" height="200" width="240" align="right"/>

## Python Doc

https://docs.quantifiedcode.com/python-anti-patterns/index.html


## Functions

https://jeffknupp.com/blog/2018/10/11/write-better-python-functions/

https://softwareengineering.stackexchange.com/questions/225682/is-it-a-bad-idea-to-return-different-data-types-from-a-single-function-in-a-dyna

https://stackoverflow.com/questions/1839289/why-should-functions-always-return-the-same-type

https://treyhunner.com/2018/04/keyword-arguments-in-python/


[Comprehensive Python Cheatsheet](https://gto76.github.io/python-cheatsheet/)

- [The Python Wiki](https://wiki.python.org/moin/)
- [Useful Modules](https://wiki.python.org/moin/UsefulModules)
- [The Hitchhiker’s Guide to Python!](http://docs.python-guide.org/en/latest/)
- [PyVideo](http://pyvideo.org/)

## Environment Variable

1. `os.getenv` gets the value of an environment variable
  while `os.setenv` creates a new environment variable or
  sets the value of an environment variable.

2. You should use `os.pathexpanduser("~")` instead of `os.getenv('HOME')`
  to get the home directory of the current user in Python.
  `os.getenv('HOME')` only works on Linux/Unix.

## Programming Skills

1. Python varadic args can mimic function overloading

3. Python eval

4. `*args` and `**kwargs`. Arguments after `*` must be called by name.

6. `sys.stdout.write`, `sys.stdout.flush`, `print`

9. Global variables in a Python module are readable but not writable to functions in the same module by default.
  If you want to write to a global variable in a function (in the same module),
  you have to declare the global variable in the method using the keyword `global`.
  For example, if `x` is a global variable
  and you want to write to it in a method,
  you have to declare `global x` at the beginning of the method.


## Numerical

1. Division is float division in Python 3 which is different from Python 2.
    If you want integer division,
    use the `//` operator.

## Misc

1. Keys for set and dict objects must be immutable in Python
    (and the same concept holds in other programming languages too).
    Since a list in Python is mutable,
    it cannot be used as a key in set and dict objects.
    You have to convert it to an immutable equivalence (e.g., tuple).

2. Use sys.exit(msg) to print error message and quit when error happens

3. Get the class name of an object.

		type(obj).__name__

## File System

2. `os.mkdir` acts like `mkdir` in Linux and `os.makedirs` acts like `mkdir -p` in Linux.
    Both of them throw an exception if the file already exists.

3. Use `execfile(open(filename).read())` to source a file,
    variables defined in 'filename' are visible,
    however, imported packages are invisible to the script running execfile

## Encoding

`ord` `unichar`
return `ascii` number of characters
`chr` return a string from a ascii number

## Syntax

1. Python expression is calculated from left to right.

7. You can use a `dict` structure to mimic switch in other programming languages.
    However, it is kind of evil and has very limited usage.,
    You should avoid use this.
    Just use multiple `if ... else ...` branches instead.

5. `:` has higher priority than arithmetic operators in Python,
    which is opposite to that in R.

3.  `return v1, v2` returns a tuple `(v1, v2)`.
    And if a function `f` returns a tuple `(v1, v2, v3)`,
    you can use
    `v1, v2, v3 = f()`

11. Stay away from functions/methods/members starting with `_`.
    For example,
    you should use the built-in function `len` to get the length of a list
    instead of using its method `__len__`.

7. Python does not support `++`, `--` but support `+=`, `-+`, etc.


### Encryption

- [pycrypto](https://pypi.python.org/pypi/pycrypto)

https://github.com/dlitz/pycrypto

http://stackoverflow.com/questions/3504955/using-rsa-in-python


## References

- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/documentation/)
- [Python日报](http://py.memect.com/)
- [Python Homepage](http://www.python.org/)
- [Python Documentation](http://docs.python.org/py3k/)
- [Useful Modules](https://wiki.python.org/moin/UsefulModules)
- [LearningJython](http://wiki.python.org/jython/LearningJython)
- [Jython Tutorial](http://www.jython.org/currentdocs.html)
- [PEP 8 -- Style Guide for Python](http://legacy.python.org/dev/peps/pep-0008/)
- [Documentating Python](https://devguide.python.org/documenting/)


http://builtoncement.org/

https://pythonhosted.org/pyCLI/

