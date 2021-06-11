Status: published
Date: 2015-05-24 13:00:31
Author: Ben Chuanlong Du
Slug: ipython-is-the-best-shell
Title: IPython Is the Best Shell
Category: Computer Science
Tags: programming, Python, tips, IPython, Shell
Modified: 2020-10-24 13:00:31

## Tips & Traps 

### Profile of IPython

1. IPython leverages SQLite3 for configuration.
    SQLite3 is notorious for the database locking issues on network fileystesm (NFS, SAMBA, etc).
    This means that you might encounter issues running IPython
    if the configuration file of IPython is stored on a network filesystem.
    You should avoid storing IPython configuration files on network filesystems!!

2. You can the below command to generate (default) IPython configuration files.

        :::bash
        # generate an IPython configuration dir
        ipython profile create [profilename]
        # generate an IPython configuration dir in the specified location
        ipython profile create [profilename] --profile-dir ~/.ipython

### Start IPython

1. It is suggested that you run IPython using the comamnd `/path/to/python -m IPython`
    unless you are sure that `ipython` pointing to the right Python version.
    Even if `ipython` points to the right Python version,
    you might encounter ModuleNotFouneError (saying "cannot import IPython")
    due to library path (`~/.local/lib/python3.7/site-packages`) confliction. 
    If this every happens
    and assuming that IPython is installed with the right permission 
    (you cannot import it if you do not have read permission), 
    run IPython `/path/to/python -m IPython` might resolve the issue.

2. According to [Configuration file location](https://ipython.readthedocs.io/en/stable/development/config.html#configuration-file-location),
    the configuration directory of a IPython session is determined in the following order.

    - Use the directory specified by the option `--ipython-dir` if any.

            :::bash
            ipython --ipython-dir /path/to/ipython/profile/directory

    - Use the directory return by `IPython.paths.get_ipython_dir()`,
        which is determined in the order below. 
        - Use the directory specified by the environment variable `IPYTHONDIR`.
        - Default to `~/.ipython`.

    If you want to define the environment variable `IPYTHONDIR` manually,
    it is better to export it as `$HOME/.ipython/` rather than leave it blank
    (which causes IPython to use the current directory as the configuration directory in rare buggy situations).

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

4. You can use both Shell environment variables and Python variables in a shell command.
    However, 
    you must use double dollar signs for shell variables.

        :::ipython
        x = 1
        echo $$HOME {x}

### Magics

1. `%lsmagic` lists all magic commands.

2. The magic command `%rehashx` automatically create aliases for the contents of your `$PATH`.
    After running `%rehashx`,
    most system commands can be used directly.

2. `%edit` is very useful for editing the definition of Python objects (functions, classes, etc.).

10. `%notebook` exports the current IPython history to a notebook file. 
    For example, 
    to export the history to `foo.ipynb` do `%notebook foo.ipynb`.

2. `%env` shows and set environment variables.
    Of course, 
    you can also use `os.environ` to help management environment variables.
    However, 
    be aware that environment varaibles set by either `%env` or `os.environ` 
    are active in the current session only
    and are not visible to other shell/Python processes spawned using `subprocess`.
    For more details, 
    please refer to [Environment variables](https://ipython.readthedocs.io/en/stable/interactive/shell.html#environment-variables).

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

9. `%autoreload` always reload modules before running a function.
    This is extremely helpful if you update your own modules/scripts 
    while using them in IPython or Jupyter/Lab notebook.

2. You can enable auto call (calling without using parentheses) of Python functions/method 
    using the alias `%autocall`.
    However, 
    this is not a good idea generally speaking.

### Misc

1. IPython accepts only script with the file extension `.ipy`.

2. If you parsing arguments in an IPython script, 
    you have to prepend `-- ` to you arguments passed to the IPython scripts,
    otherwise,
    the arguments are passed to the `ipython` command instead of your script.
    For more information,
    please check [this discussion on Stack Overflow](https://stackoverflow.com/questions/22631845/how-to-pass-command-line-arguments-to-ipython).

3. IPython automatically beautify outputs.

## References

http://www.legendu.net/misc/blog/set-environment-varibles-in-ipython/

http://www.legendu.net/misc/blog/disable-jedi-in-ipython/

http://www.legendu.net/en/blog/shell-alternatives/

[Wait, IPython Can Do That?!](https://ep2019.europython.eu/media/conference/slides/cBeHNyZ-wait-ipython-can-do-that.pdf)

[​​​​28 Jupyter Notebook Tips, Tricks, and Shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

[IPython and Jupyter in Depth: High productivity, interactive Python - PyCon 2017](https://www.youtube.com/watch?v=VQBZ2MqWBZI)

[IPython Documentation](https://ipython.readthedocs.io/en/stable/index.html)

[IPython Magics](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

[Introduction to IPython configuration](https://ipython.readthedocs.io/en/stable/config/intro.html)

https://stackoverflow.com/questions/19579546/can-i-access-python-variables-within-a-bash-or-script-ipython-notebook-c

https://ipython.org/ipython-doc/3/interactive/shell.html

https://ipython.readthedocs.io/en/stable/interactive/magics.html

https://github.com/ipython/ipython/wiki/Cookbook:-Storing-aliases

[Can I access python variables within a `%%bash` or `%%script` ipython notebook cell?](https://stackoverflow.com/questions/19579546/can-i-access-python-variables-within-a-bash-or-script-ipython-notebook-c)

[system commands: python variables don't get evaluated when environment variables are also used](https://github.com/ipython/ipython/issues/6527)
