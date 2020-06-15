Status: published
Date: 2020-06-14 18:38:36
Author: Benjamin Du
Slug: write-documentation-for-python-packages-using-sphinx
Title: Write Documentation for Python Packages Using Sphinx
Category: Computer Science
Tags: Computer Science, Python, Sphinx, documentation

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/

https://docs-python2readthedocs.readthedocs.io/en/master/code-doc.html

1. It is strongly suggested that you create a separate directory `docs` (or use another name you like)
    and use it as the root directory for documentation.

2. You have to enable the sphinx extension `sphinx.ext.autodoc`.
    Please refer to https://github.com/dclong/xinstall/blob/dev/docs/conf.py#L36 for an example.

3. Generate docs from docstrings.
    Takeing [xinstall](https://github.com/dclong/xinstall) as an example,
    run the following command in the root directory of xinstall.

        :::bash
        sphinx-apidoc -f -o docs/ xinstall

4. 
