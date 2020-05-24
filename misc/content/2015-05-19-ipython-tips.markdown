Status: published
Date: 2020-05-23 22:00:32
Author: Ben Chuanlong Du
Slug: ipython-tips
Title: Tips on IPython
Category: Computer Science
Tags: programming, Python, tips, IPython

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Tricks & Traps 

### Help Doc

1. A prefixing/suffixing question mark (`?`) shows the help doc of an object in IPython.
    Two prefixing/suffixing questions marks (`??`) shows even more information. 
    This is called dynamic object retrospection.

2. You can use `?%alias_or_magic` to check the definition of an alias or line magic.
    Notice that `%` is required for aliases. 
    The suffixing `?` doesn't work in this case.

3. Wild cards can be used to match methods in dynamic object retrospection!

        :::ipython
        os.*dir*?
        ?os.*dir*

### Shell 

1. If you run a shell command, 
    it is suggested that you always prefix it with `!` 
    (even though it is not required sometimes),
    the reason is that pipe will fail to work without the prefixing `!`.

2. Both shell commands prefixed with `!` (e.g., `!ls`) and line magics (e.g., `%ls`) 
    can be mixed with Python code in IPython!!
    This makes things very convenient sometimes.

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

3. When you use the prefix `!` to run a shell command,
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

### Magics

1. `%lsmagic` lists all magic commands.

2. `%evn` shows and set environment variables.
    Of course, 
    you can also use `os.environ` to help management environment variables.
    However, 
    be aware that environment varaibles set by either `%env` or `os.environ` 
    are active in the current session only
    and are not visible to other shell/Python processes spawned using `subprocess`.

3. `%run` runs a Python script or a Jupyter/Lab notebook 
    and brings its content into the current namespace.
    This is different from importing a module!
    It is equivalent to "source in code" in other languages (such as R and Shell).

4. `%load` inserts the content of a text file into the current cell.
    The `%load` statement itself is commented out after loading the content of the text file.

5. `%%writefile` writes the content of the current cell to an external file.
    `%pycat` is the opposite. 
    It shows the content of an external file. 
    The difference between `%pycat` and `!cat` is that `%pycat` highlight the output so that is easy to read and understand.
    You can think of `%pycat some_file` as equivalent of `!cat some_file | highlight -O ansi`.

6. Magics for profiling code in IPython and Jupyter/Lab notebooks are also available.
    Please refer to
    [Python Profiler for JupyterLab Notebooks](http://www.legendu.net/misc/blog/python-profile-notebook/)
    for more discussions.

2. The magic command `%rehashx` automatically create aliases for the contents of your `$PATH`.
    After running `%rehashx`,
    most system commands can be used directly.

3. `%edit` is really useful ...

4. `%autoreload` always reload modules before running a function.
    This is extremely helpful if you update your own modules/scripts 
    while using them in IPython or Jupyter/Lab notebook.

4. `%notebook`

### Other

1. IPython accepts only script with the file extension `.ipy`.

2. If you parsing arguments in an IPython script, 
    you have to prepend `-- ` to you arguments passed to the IPython scripts,
    otherwise,
    the arguments are passed to the `ipython` command instead of your script.
    For more information,
    please check [this discussion on Stack Overflow](https://stackoverflow.com/questions/22631845/how-to-pass-command-line-arguments-to-ipython).

3. it seems that IPython tries to beautify outputs.

## Most Useful Magic Commandso

%rehashx

%autocall

## References

[Wait, IPython Can Do That?!](https://ep2019.europython.eu/media/conference/slides/cBeHNyZ-wait-ipython-can-do-that.pdf)

[​​​​28 Jupyter Notebook Tips, Tricks, and Shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

[IPython and Jupyter in Depth: High productivity, interactive Python - PyCon 2017](https://www.youtube.com/watch?v=VQBZ2MqWBZI)

[IPython Documentation](https://ipython.readthedocs.io/en/stable/index.html)

[IPython Magics](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

https://stackoverflow.com/questions/19579546/can-i-access-python-variables-within-a-bash-or-script-ipython-notebook-c

https://ipython.org/ipython-doc/3/interactive/shell.html

https://ipython.readthedocs.io/en/stable/interactive/magics.html

https://github.com/ipython/ipython/wiki/Cookbook:-Storing-aliases

[Can I access python variables within a `%%bash` or `%%script` ipython notebook cell?](https://stackoverflow.com/questions/19579546/can-i-access-python-variables-within-a-bash-or-script-ipython-notebook-c)