Status: published
Date: 2019-02-22 22:40:54
Author: Benjamin Du
Slug: python-profiler
Title: Python Profiler
Category: Computer Science
Tags: programming, Python, JupyterLab, notebook

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


## %time

## %timeit

## [%prun](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-prun)

## [pyheatmagic](https://github.com/csurfer/pyheatmagic)

### Installation
```Python
pip3 install py-heat-magic
```

### Usage
Load the magic.
```Python
%load_ext heat
```
%%heat 

%%heat -o file.png

## [Line Profiler](https://github.com/rkern/line_profiler)

Within your jupyter notebook, call: %load_ext line_profiler



## References

https://mortada.net/easily-profile-python-code-in-jupyter.html
