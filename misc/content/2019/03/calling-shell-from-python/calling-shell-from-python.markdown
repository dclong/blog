Status: published
Date: 2019-03-24 06:48:05
Author: Benjamin Du
Slug: calling-shell-from-python
Title: Calling Shell from Python
Category: Computer Science
Tags: programming, Python, shell, os.system, subprocess
Modified: 2019-08-24 06:48:05

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**



1. It is suggested that you always use full path of command as the environment is not always identical across machines.

2. Generally speaking,
    functions in the module `subprocess` are preferred to the function `os.system`
    as functions in the module `subproces` are more flexible. 
    However, 
    be careful when you use `subprocess.call` to replace `os.system`.
    You might want to pass the option `check=True` 
    to turn on exception throwing on erros (turned off by default)
    if the status of running a command matters. 

3. `echo` and pipe is common trick to feed input into another comamnd. 
    For exampel, 
    suppose `kinit` is an authentication command that takes a password interactively,
    you can use the following command to authenticate directly without typing password interactively.

        echo 'your_password' | kinit

    This trick works with the `os.system` function in Python.
    Basically `os.system` takes whatever you run in shell and run it.
    Methods in `subprocess` does not take pipe commands by default. 
    If the pipe is used to feed input into another command,
    you can simply use the `input` argument of methods in `subprocess`.
    For example,

        subprocess.check_output(['kinit'], input=b'your_password')

    If you do want to use pipe directly in methods of `subprocess`, 
    you can set the option `shell=True`.


## [shlex](https://docs.python.org/3/library/shlex.html)

Parsing Shell commands.


## References

https://stackoverflow.com/questions/41171791/how-to-suppress-the-output-of-subprocess-run

https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline

https://docs.python.org/3/library/subprocess.html#replacing-os-system
