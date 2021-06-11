Status: published
Date: 2020-10-30 09:16:10
Author: Benjamin Du
Slug: static-type-checking-of-Python-Scripts-using-pytype
Title: Static Type Checking of Python Scripts Using pytype
Category: Computer Science
Tags: Computer Science, Python, type annotation, static, type checking, pytype
Modified: 2020-10-30 09:16:10
## Configuration 

There are 3 ways to control the behavior of `pytype.

1. Pass command-line options to `pytype`. 

2. Specify a configuration file using `pytype --config /path/to/config/file ...`.
    You can generate an example configuration file 
    using the command `pytype --generate-config pytype.cfg`.

3. If no configuration file is found,
    pytype uses the first `setup.cfg` it founds 
    and use the `[pytype]` section. 

Please refer to 
[xinstalll::pytype/setup.cfg](https://github.com/dclong/xinstall/blob/dev/xinstall/data/pytype/setup.cfg)
for an example of configuration file of `pytype`.

## Exclude Files and/or Directories

1. Use the `--exclude` option. 

        :::bash
        PATH=.venv/bin:$PATH pytype xinstall --exclude xinstall/data

2. Specify files and/or directories to exclude in the configuration file `setup.cfg`. 

        [pytype]
        exclude = 
            **/*_test.py 
            **/test_*.py 

## Silent Errors

Please refer to 
[Silencing errors](https://google.github.io/pytype/user_guide.html#silencing-errors)
for detailed explanations.

## References 

https://google.github.io/pytype/faq.html

https://google.github.io/pytype/user_guide.html

https://google.github.io/pytype/