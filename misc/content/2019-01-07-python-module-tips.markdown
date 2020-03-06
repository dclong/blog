Status: published
Date: 2019-03-09 13:31:07
Author: Ben Chuanlong Du
Slug: python-module-tips
Title: Python Module Tips
Category: Computer Science
Tags: programming, Python, module, tips, module access

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Import a Module

1. sys.path.append

```bash
import module_name
import module_name as alias
from module import pkg_mod_or_fun
```

https://stackoverflow.com/questions/3144089/expand-python-search-path-to-other-source


1. A module is cached in memory when it is loaded into Python.
    Changes to the module after loading of the module will not take effect
	unless the module is reloaded.
	A module can be reloaded using `imp.reload(module)` In Python3.

## Module Access

https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python

http://xion.io/post/code/python-all-wild-imports.html



## Import Warning

https://stackoverflow.com/questions/43393764/python-3-6-project-structure-leads-to-runtimewarning


## Misc

[depfinder](https://github.com/ericdill/depfinder) finds all the unique imports in your library.

