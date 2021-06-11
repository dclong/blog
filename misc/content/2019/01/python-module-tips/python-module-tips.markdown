Status: published
Date: 2019-01-13 09:48:04
Author: Ben Chuanlong Du
Slug: python-module-tips
Title: Tips on Python Module 
Category: Computer Science
Tags: programming, Python, module, tips, module access
Modified: 2021-04-13 09:48:04

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Import a Module

1. There are 3 different ways import Python modules.

        :::python
        import module_name
        import module_name as alias
        from module import pkg_mod_or_fun

2. The module `importlib.resources` (since Python 3.7+) leverages Python's import system to provide access to resources within packages. 
  If you can import a package, 
  you can access resources within that package. 
  Resources can be opened or read, in either binary or text mode.
  Resources are roughly akin to files inside directories, 
  though it’s important to keep in mind that this is just a metaphor. 
  Resources and packages do not have to exist as physical files and directories on the file system. 
  `importlib.resources` is analogue to `getClass.getResource` in Java.

1. One of the trickiest problem in Python is conflicting package/module names. 
    It happens when there are more than one Python scripts with the same name on Python module search paths.
    This is often not a problem when developing Python packages due to absolute and relative import.
    However, 
    this issue can come up in a few situations and can be quite tricky for uers to figure out.

    - If an user run a Python script whose parent directory contains a Python script with a name conflicting with other (official) Python modules,
        this issue will come up.
    - An even trickier situation is when a Python script is piped to a Python interpreter directly. 
        According to [docs about sys.path](https://docs.python.org/3/library/sys.html#sys.path),
        `sys.path[0]` is initailized to be the empty string on the startup of Python in this situation 
        which directs Python to search modules in the current directly first.
        Since an user can run the command in any directory, 
        it is more likely for him/her to encounter the issue of conflicting module names. 
    
    For example, 
    if you have a Python script named `abc.py` in the current directory 
    and your script depends on the Python module `collections.abc`,
    you code will likely fail to run. 
    Another (really tricky) eample is that if you have a Python script named `pyspark.py`
    and submit it to  a Spark cluster to run (using `spark-submit`).
    The PySpark application will likely throw an error saying that the `pyspark` module is not found.
    Those are just 2 commonly seen examples. 
    You can easily run into this issue when you run ad hoc Python scripts 
    (unlikely to encounter this issue when you develop a Python package).
    A possible way to avoid this issue is to always prefix your ad hoc Python script with a leading underscore (`_`).
    Another solution is to remove the emtpry string 
    (represent the current working directory from `sys.path`)
    if your Python script does not import other modules in the current directory.

        :::python
        import sys
        sys.path.remove("")

1. Python searches for modules at paths in `sys.path`.
    To add a path into the module search path,
    you can simply append it into `sys.path`.

        :::python
        sys.path.append("/new/path/to/search/for/modules")

    By default, 
    the current path of the Python interpreter is on the module search path (i.e., `sys.path`).
    If the current directory has a Python script 
    with the same name as a built-in model, 
    it might causes issues. 
    A simple way to fix the issue is to remove the empty path 
    (represent the current working directory)
    from `sys.path`.

        :::python
        import sys
        sys.path.remove("")

2. A module is cached in memory when it is loaded into Python.
    Changes to the module after loading of the module will not take effect
	unless the module is reloaded.
	A module can be reloaded using `importlib.reload(module)` In Python3.

3. Both the import styles of `import a.b.C as C`
    and `from a.b import C` work.
    `import a.b.C as C` is better if you work with Java classes via JPype
    as you get a very similar experience as you do import in Java.
    However, 
    `from a.b import C` is better if you work with python modules
    as it is easier to add more imports from `a.b` if necessary.
    The following is an example of import both classes `C` and `D` from `a.b`.

        :::python
        from a.b import C, D

## Issues and Solutions

### Cannot Import an Installed Module

I have met the issue that some packages cannot be imported even if they have been installed.
The issue was due to file permissions (the installed Python packages are not readable).
A simple fix (even not optimal) is to make these Python packages readable, 
e.g., make the permissions `777` (sudo required).

## Module Access

https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python

http://xion.io/post/code/python-all-wild-imports.html



## Import Warning

https://stackoverflow.com/questions/43393764/python-3-6-project-structure-leads-to-runtimewarning


## Misc

[depfinder](https://github.com/ericdill/depfinder) finds all the unique imports in your library.

[awesome-python](https://github.com/uhub/awesome-python)

## References 

https://github.com/pypa