"""°°°
- Title: Python Tips and Traps
- Slug: python-tips-and-traps
- Date: 2020-11-15 10:10:12
- Category: Computer Science
- Tags: programming, Python, tips, traps
- Author: Ben Du
- Modified: 2021-02-15 10:10:12
°°°"""

# |%%--%%| <VYVhghrXrh|0f54Wgdsq1>
"""°°°
## [Tips on Python Module](http://www.legendu.net/2019/blog/python-module-tips)

## [Exception and Error Handling in Python](http://www.legendu.net/2020/blog/exception-and-error-handling-in-python)
°°°"""
# |%%--%%| <0f54Wgdsq1|p1a3H1HGzz>
"""°°°
## Misc

https://docs.python-guide.org/writing/gotchas/

https://stackoverflow.com/questions/101268/hidden-features-of-python


2. The `int` type in Python 3 is unbounded,
    which means that there is no limit on the range of integer numbers that an `int` can represent. 
    However, 
    there are still various integer related limits in Python 3 due to the interpreter's word size (`sys.maxsize`)
    (which is the same as the machine's word size in most cases).
    This number is the size of the largest possible list or in-memory sequence.
°°°"""
# |%%--%%| <p1a3H1HGzz|c4i76IMHlf>

x = 1111111111111111111111111111111111111111111111111111111111111111111111111111
type(x)

# |%%--%%| <c4i76IMHlf|0mSIE23243>
"""°°°
3. Use type annotation to make your code more readable and easier to understand.
°°°"""
# |%%--%%| <0mSIE23243|dOHFUBJhPS>
"""°°°
## Functions and Classes

1. Restrict the types of objects that your function/method can be applied to 
  and throw a (ValueError) exception when a wrong type is provided.
  This helps minimize surprisings.
  If you must make a function accepts 2 (or more) customized types of objects, 
  it is best to make them have similar duck types. 
  For example, 
  one object has members `mem1` and `mem2` (which are used in the function),
  instead of representing the 2nd type of object as a tuple (of 2 elements)
  it is better to define a class to match interfaces of the first type of object 
  so that implementation of the function is simple and concise. 
  Noticce that dataclass is a good way to implement simple classes.

3. AVOID returning objects of different types from a Python function/method.
  
7. Almost all modern programming languages follow the convention
  of not returnting anything (or in another words, retun void, None, etc.)
  from a mutator method so that you cannot chain on a mutator method.
  Functional programming languages enough chaining on methods
  as they often have immutable objects and the methods return new objects
  rather than changing the original objects.

2. Python functions (except lambda functions) do not automatically return value
  unlike functional programming languages.
  Forgotting a `return` statement is a common mistake in Python.


6. You cannot use `return` to return result from a generator function.
  Instead a `return` behaves like raising a StopIteration.
  Please see this [issue](https://stackoverflow.com/questions/26595895/return-and-yield-in-the-same-function)
  for more discussions.


https://jeffknupp.com/blog/2018/10/11/write-better-python-functions/

https://softwareengineering.stackexchange.com/questions/225682/is-it-a-bad-idea-to-return-different-data-types-from-a-single-function-in-a-dyna

https://stackoverflow.com/questions/1839289/why-should-functions-always-return-the-same-type

https://treyhunner.com/2018/04/keyword-arguments-in-python/
°°°"""
# |%%--%%| <dOHFUBJhPS|SKBJIj9u6n>
"""°°°
## Operator Precedence

1. According to [Python Operator Precedence](https://docs.python.org/2/reference/expressions.html#operator-precedence),
  the ternary expression `if - else` has a very low precedence. 
  However, it has higher precedence than the tuple operator `,`.
  It is suggested that you always use parentheses to make the precedence clear 
  when you use the ternary expression in a complicated expression.
  Below is an example illustrating the precedence of the ternary expression.
°°°"""
# |%%--%%| <SKBJIj9u6n|PZmTOWFT2o>

update = {
    "status": "succeed",
    "partitions": 52,
    "size": 28836,
    "end_time": 1563259850.937318,
}
[
    key + " = " + f"{val}" if isinstance(val, (int, float)) else f"'{val}'"
    for key, val in update.items()
]

# |%%--%%| <PZmTOWFT2o|lv90pC8nKs>

update = {
    "status": "succeed",
    "partitions": 52,
    "size": 28836,
    "end_time": 1563259850.937318,
}
[
    key + " = " + (f"{val}" if isinstance(val, (int, float)) else f"'{val}'")
    for key, val in update.items()
]

# |%%--%%| <lv90pC8nKs|POBsAYKnwd>
"""°°°

°°°"""
# |%%--%%| <POBsAYKnwd|NFD7HWLBek>
"""°°°
## Advanced Python 

[Talk: Anthony Shaw - Why is Python slow?](https://www.youtube.com/watch?v=I4nkgJdVZFA)

[When Python Practices Go Wrong - Brandon Rhodes - code::dive 2019](https://www.youtube.com/watch?v=S0No2zSJmks)
°°°"""
# |%%--%%| <NFD7HWLBek|9K9Ty5emJX>
"""°°°
<img src="http://dclong.github.io/media/python/python.png" height="200" width="240" align="right"/>

## Python Doc

https://docs.quantifiedcode.com/python-anti-patterns/index.html




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
°°°"""
# |%%--%%| <9K9Ty5emJX|cTqfcYDXG8>
"""°°°
## Referneces

- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#381-docstrings)

- [Awesome Python](https://github.com/uhub/awesome-python)

- [Common Mistakes](http://www.toptal.com/python/top-10-mistakes-that-python-programmers-make)

- [Least Astonishment and The Mutble Default Argument](https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument)

- [Maximum and Minimum Values for Ints](https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints)

- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/documentation/)

- https://github.com/pypa

- [Python日报](http://py.memect.com/)

- [Python Homepage](http://www.python.org/)

- [Python Documentation](http://docs.python.org/py3k/)

- [Useful Modules](https://wiki.python.org/moin/UsefulModules)

- [LearningJython](http://wiki.python.org/jython/LearningJython)

- [Jython Tutorial](http://www.jython.org/currentdocs.html)

- [PEP 8 -- Style Guide for Python](http://legacy.python.org/dev/peps/pep-0008/)

- [Documentating Python](https://devguide.python.org/documenting/)

- http://builtoncement.org/

- https://pythonhosted.org/pyCLI/
°°°"""
# |%%--%%| <cTqfcYDXG8|B9p8FRkqsR>
