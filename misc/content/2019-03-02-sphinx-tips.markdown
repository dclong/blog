Status: published
Date: 2020-06-14 18:36:56
Author: Benjamin Du
Title: Genator Documentation Using Sphinx
Slug: sphinx-tips
Category: Computer Science
Tags: programming, Python, Sphinx, Python documentation generator

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


http://www.sphinx-doc.org/en/1.5/invocation.html#invocation-apidoc

https://www.sphinx-doc.org/en/master/usage/markdown.html

https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b

https://matplotlib.org/sampledoc/getting_started.html

## Generate Python Documentation 

https://developer.ridgerun.com/wiki/index.php/How_to_generate_sphinx_documentation_for_python_code_running_in_an_embedded_system

https://gisellezeno.com/tutorials/sphinx-for-python-documentation.html

https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/

## Public Host 

https://readthedocs.org/

## Sphinx Extensions

### Jupyter/Lab Notebooks

https://github.com/spatialaudio/nbsphinx/

https://github.com/jupyter/jupyter-sphinx

### Markdown 

https://www.sphinx-doc.org/en/master/usage/markdown.html

### AutoDoc 

sphinx.ext.autodoc 

https://github.com/agronholm/sphinx-autodoc-typehints

## Generate Documentation for a Python Project 

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

## References

https://stackoverflow.com/questions/2471804/using-sphinx-with-markdown-instead-of-rst