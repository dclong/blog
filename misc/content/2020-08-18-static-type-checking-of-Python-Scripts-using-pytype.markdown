Status: published
Date: 2020-08-18 21:29:34
Author: Benjamin Du
Slug: static-type-checking-of-Python-Scripts-using-pytype
Title: Static Type Checking of Python Scripts Using Pytype
Category: Computer Science
Tags: Computer Science, Python, type annotation, static, type checking, pytype

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Configuration 

1. Pass command-line options to `pytype`. 

2. Specify a configuration file using `pytype --config /path/to/config/file ...`.
    You can generate an example configuration file 
    using the command `pytype --generate-config pytype.cfg`.

3. If no configuration file is found,
    pytype uses the first `setup.cfg` it founds 
    and use the `[pytype]` section. 

## Exclude Files and/or Directories

1. Use the `--exclude` option. 

        :::bash
        PATH=.venv/bin:$PATH pytype xinstall --exclude xinstall/data

2. Specify files and/or directories to exclude in the configuration file. 

        [pytype]
        exclude = 
            **/*_test.py 
            **/test_*.py 

## References 

https://google.github.io/pytype/faq.html

https://google.github.io/pytype/user_guide.html

https://google.github.io/pytype/