Status: published
Date: 2021-04-29 09:37:32
Author: Benjamin Du
Slug: write-documentation-for-python-packages-using-sphinx
Title: Write Documentation for Python Packages Using Sphinx
Category: Computer Science
Tags: Computer Science, Python, Sphinx, documentation, mkdocs

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. Create a directory named `docs` (other names are OK too) in the root directory of your Python project.
    It is strongly NOT recommended to use the Python project root directory 
    as the root directory for the docs
    as it will make your Python project root directory messy. 

        :::bash 
        mkdir docs

2. Go to the directory `docs` and run the command `sphinx-quickstart`.

        :::bash 
        cd docs 
        sphinx-quickstart 

3. Update the generated configuration script `conf.py`. 
    Below are a few important ones.

    - Configure the `sys.path`
        to [tell autodoc where to find your code](https://docs-python2readthedocs.readthedocs.io/en/master/code-doc.html#tell-autodoc-how-to-find-your-code).
        Taking [xinstall](https://github.com/dclong/xinstall) as an example,
 
            import os 
            import sys
            sys.path.insert(0, "../xinstall")            

    - Enable sphinx extensions.

            extensions = [
                "sphinx.ext.todo",
                "sphinx.ext.viewcode",
                "sphinx.ext.autodoc",
                "sphinx_autodoc_typehints",
                "sphinx.ext.doctest",
            ]

3. Run the following command in the root directory of your Python project 
    (taking [xinstall](https://github.com/dclong/xinstall) as an example) 
    to generate docs from docstrings 
    (you only have to do this once).

        :::bash
        sphinx-apidoc -f -o docs/ xinstall

4. Run the following command in the `docs` directory to generate HTML documentation. 

        :::bash 
        make clean && make html 

## Public Host 

https://readthedocs.org/

## Generate Python Documentation 

https://developer.ridgerun.com/wiki/index.php/How_to_generate_sphinx_documentation_for_python_code_running_in_an_embedded_system

https://gisellezeno.com/tutorials/sphinx-for-python-documentation.html

https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/


## AutoDoc 

sphinx.ext.autodoc 

https://github.com/agronholm/sphinx-autodoc-typehints

http://www.legendu.net/misc/blog/write-documentation-for-python-packages-using-sphinx/

https://stackoverflow.com/questions/2471804/using-sphinx-with-markdown-instead-of-rst

## Sphinx Extensions

### Jupyter/Lab Notebooks

https://github.com/spatialaudio/nbsphinx/

https://github.com/jupyter/jupyter-sphinx


## References 

https://docs-python2readthedocs.readthedocs.io/en/master/code-doc.html

https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/

https://netgen.io/blog/the-most-overlooked-part-in-software-development-writing-project-documentation


http://www.sphinx-doc.org/en/1.5/invocation.html#invocation-apidoc

https://www.sphinx-doc.org/en/master/usage/markdown.html

https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b

https://matplotlib.org/sampledoc/getting_started.html

