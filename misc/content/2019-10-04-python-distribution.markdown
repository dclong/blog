Status: published
Date: 2020-06-22 09:36:27
Author: Benjamin Du
Slug: python-distribution
Title: Python Distribution
Category: Computer Science
Tags: programming, Python distribution
nohtyP 
**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. When people talks about Python,
  it usually means the CPython implementation
  which you can download from <www.python.org>.
  There are other interesting Python implementations
  such as [PyPy](https://pypy.org/) (Python implementation in Python),
  [Jython](http://www.jython.org/) (Python implementation in Java), etc. exists,
  however,
  they have relatively very small use groups.
  Generally speaking,
  you want to stay with CPython,
  i.e., the Python people are taling about unless you have very strong reasons to go with another choice.
  There are also different distributions among CPython implementations.
  Anaconda Python is a good one if you do not have sudo permissions in the system.

2. For the CPython implementation,
  there are different distributions as well.
  Besides the official Python distribution
  (which comes by default in many operating systems),
  Anaconda Python rules the unofficial distributions.
  It is a great choice which provies an all-in-one installer
  to use on machines that you don't have sudo permissions
  as it installs to your home directory by default.
  Anaconda Python supports 2 different flavors:
  Anaconda (binded with many popular Python packages) and miniconda (with minimum Python packages).
  It also invented another package management tool named `conda` to replace `pip`.
  `conda` is a general purpose package management tool instead of for Python only.
  It eases the pain of figuring out the right dependencies of Python packages
  but it is a little bit bloated (with larger installation sizes) compared to `pip`.
