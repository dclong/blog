Status: published
Date: 2020-11-22 19:44:09
Author: Ben Chuanlong Du
Slug: python-module-tips
Title: Python Module Tips
Category: Computer Science
Tags: programming, Python, module, tips, module access

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Import a Module

1. sys.path.append

        :::bash
        import module_name
        import module_name as alias
        from module import pkg_mod_or_fun

https://stackoverflow.com/questions/3144089/expand-python-search-path-to-other-source


1. By default, 
    the current path of the Python interpreter is in the module search path (i.e., `sys.path`).
    If the current directory has a Python script 
    with the same name as a built-in model, 
    it might causes issues. 
    A simple way to fix the issue is to remove the empty path 
    (represent the current working directory)
    from `sys.path`.

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

        from a.b import C, D

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