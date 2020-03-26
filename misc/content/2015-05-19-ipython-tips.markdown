Status: published
Date: 2020-03-24 18:54:14
Author: Ben Chuanlong Du
Slug: ipython-tips
Title: Tips on IPython
Category: Computer Science
Tags: programming, Python, tips, IPython

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**


## Tricks & Traps 

1. Both shell commands prefixed with `!` (e.g., `!ls`) and line magics (e.g., `%ls`) 
    can be mixed with Python code in IPython!!
    This makes things very convenient sometimes.

2. You can use `?%alias_or_magic` to check the definition of an alias or line magic.
    Notice that `%` is required for aliases. 
    The suffixing `?` doesn't work in this case.

1. The magic command `%rehashx` automatically create aliases for the contents of your `$PATH`.
    After running `%rehashx`,
    most system commands can be used directly.

1. IPython accepts only script with the file extension `.ipy`.

2. If you parsing arguments in an IPython script, 
    you have to prepend `-- ` to you arguments passed to the IPython scripts,
    otherwise,
    the arguments are passed to the `ipython` command instead of your script.
    For more information,
    please check [this discussion on Stack Overflow](https://stackoverflow.com/questions/22631845/how-to-pass-command-line-arguments-to-ipython).

2. Python variables can used in a shell command like an environment variable. 
    For example, 
	if there is a Python named `pkg` which refers to a local package file,
	then you can use `!cp $pkg ~` to copy it to the home directory. 
	Another even more general approach is to use the curly braces
	which accepts an arbitrary Python expresion.
	Still, 
	let's assume that `pkg` is a Python variable which refers to a local package file 
	but in relative path w.r.t. `/tmp`.
	You can copy it to the home directory using the following command.

        :::bash
		!cp {os.path.join('/tmp', pkg)} ~

    And also, 
    Python variables can be accessed in the first line 
    of a `%%bash` or `%%script` cell, 
    and so can be passed as command line parameters to the script. 
    For example, with bash you can do this:

        :::bash
        %%bash -s "$myPythonVar" "$myOtherVar"
        echo "This bash script knows about $1 and $2"

3. When you the prefix `!` to run a shell command,
    background jobs by suffixing `&` is not supported!
    However, 
    there are a few simple ways to run background shell jobs 
    (or to be more accurately, run jobs in parallel).
    The first way to run background shell jobs is via the module `subprocess`. 
    For example, 
    the below code use start a separate process to zip each subdirectory 
    in the current directory.

        :::python
        from pathlib import Path
        import subprocess as sp

        for path in Path(".").iterdir():
            if path.is_dir():
                sp.run(f"zip -r {path} {path.with_suffix('.zip')} &", shell=True)

    The second way is to use the Python moduel `multiprocessing`. 
    
        :::python
        from multiprocessing import Pool
        
        def job(arg):
            ...

        Pool(4).map(job, [v1, v2, v3])

    The last (not recommend) way is to use the cell magic `%%script` with the option `--bg`.

1. it seems that IPython tries to beautify outputs.

## Most Useful Magic Commandso

%rehashx

%autocall

## References

[IPython Documentation](https://ipython.readthedocs.io/en/stable/index.html)

[IPython Magics](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

https://stackoverflow.com/questions/19579546/can-i-access-python-variables-within-a-bash-or-script-ipython-notebook-c

https://ipython.org/ipython-doc/3/interactive/shell.html

https://ipython.readthedocs.io/en/stable/interactive/magics.html

https://github.com/ipython/ipython/wiki/Cookbook:-Storing-aliases

[Can I access python variables within a `%%bash` or `%%script` ipython notebook cell?](https://stackoverflow.com/questions/19579546/can-i-access-python-variables-within-a-bash-or-script-ipython-notebook-c)