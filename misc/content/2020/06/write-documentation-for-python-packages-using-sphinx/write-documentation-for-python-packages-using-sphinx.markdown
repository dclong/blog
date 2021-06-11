Status: published
Date: 2021-06-01 21:51:41
Author: Benjamin Du
Slug: write-documentation-for-python-packages-using-sphinx
Title: Write Documentation for Python Packages Using Sphinx
Category: Computer Science
Tags: Computer Science, Python, Sphinx, documentation, mkdocs
Modified: 2021-06-01 21:51:41

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Installation

You can install Sphinx and necessary extensions using the following command.

    :::bash
    pip3 install sphinx sphinx-autodoc-typehints

Or simply

    :::bash
    xinstall sphinx -ic

Since the above commands installs Sphinx to the user's local directory,
Sphinx executables are placed into the directory `~/.local/bin`. 
So you might have to configure your `PATH` environment variable 
so that you can use Sphinx commands directly.

## Generate Docs Using Sphinx

1. Create a directory named `docs` in the root directory of your Python project.
    Do NOT use the root directory of your project 
    as the root directory for documentations
    as it will make your the root directory of your project messy. 

        :::bash 
        mkdir docs

2. Go to the directory `docs` and run the command `sphinx-quickstart`.

        :::bash 
        cd docs 
        sphinx-quickstart 

    A few questions will be asked to you.
    Note: It is suggested that you choose to **separate build and source directories**
    when the question is asked.
    This option makes the `docs` directory tidier especially for large projects.

3. Update the generated configuration script `conf.py`. 
    Below are a few important ones.

    - Configure `sys.path`
        to [tell autodoc where to find your code](https://docs-python2readthedocs.readthedocs.io/en/master/code-doc.html#tell-autodoc-how-to-find-your-code).
        In short, 
        you should insert the path to your source code directory as the first element to `sys.path`.
        Relative paths (w.r.t the directory of the file `conf.py`) are allowed.
        Assume your project has the following structure,

            :::text
            proj_name/
                proj_name/
                    __init__.py
                docs/
                ...

        you can use the following generic code to help you to insert the correct path of the source code directory.
 
            :::python
            import sys
            from pathlib import Path


            def get_source_dir() -> str:
                path = Path(__file__).resolve()
                while path.name != "docs":
                    path = path.parent
                return str(path.parent)


            sys.path.insert(0, get_source_dir())

    - Enable sphinx extensions.

            :::python
            extensions = [
                "sphinx.ext.todo",
                "sphinx.ext.viewcode",
                "sphinx.ext.autodoc",
                "sphinx_autodoc_typehints",
                "sphinx.ext.doctest",
            ]

3. Run the following command in the `docs` directory to generate documentation from docstrings.
    Notice that the command `sphinx-apidoc` does not extract docstrings from your source code
    but instead generate a RST file to tell Sphinx to use docstrings when building the docs.
    So you only have to run the command `aphinx-apidoc` once.

        :::bash
        # if build and source are NOT separated
        sphinx-apidoc -f -o ./ ../proj_name
        # if build and source are separated
        sphinx-apidoc -f -o source/ ../proj_name

    A file named `modules.rst` (together with some other RST files) will be generated.
    Include it into the file `index.rst`.


4. Add more RST files into `index.rst` if necessary.

5. Run the following command in the `docs` directory to generate HTML documentation. 

        :::bash 
        make clean && make html 

## Use Markdown Together with RST in Sphinx

Please refer to the official documentation
[markdown](https://www.sphinx-doc.org/en/master/usage/markdown.html)
for instructions.

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

[sphinx-autodoc-typehints](https://github.com/agronholm/sphinx-autodoc-typehints)

[nbsphinx](https://github.com/spatialaudio/nbsphinx/)

[jupyter-sphinx](https://github.com/jupyter/jupyter-sphinx)

## References 

https://docs-python2readthedocs.readthedocs.io/en/master/code-doc.html

https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/

https://netgen.io/blog/the-most-overlooked-part-in-software-development-writing-project-documentation


http://www.sphinx-doc.org/en/1.5/invocation.html#invocation-apidoc

https://www.sphinx-doc.org/en/master/usage/markdown.html

https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b

https://matplotlib.org/sampledoc/getting_started.html

