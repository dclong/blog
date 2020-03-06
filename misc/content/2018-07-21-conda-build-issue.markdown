Status: published
Date: 2020-02-18 11:55:27
Author: Ben Chuanlong Du
Slug: conda-build-issue
Title: Conda Build Issue
Category: Computer Science
Tags: programming, Anaconda, Python, conda build, sqlalchemy-teradata, conda

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

I encountered an issue building the package
[sqlalchemy-teradata](https://pypi.org/project/sqlalchemy-teradata/).
There are a few related issues:
[issues/2790](https://github.com/conda/conda-build/issues/2790),
[issues/2826](https://github.com/conda/conda-build/issues/2826).
It seems that the recipe uses an outdated URL.
Change the URL to 
[this one](https://files.pythonhosted.org/packages/13/ba/bd5ebedd251630a822cfa2ad819caa99f6b494726aa05c8ef69bbb39330e/sqlalchemy_teradata-0.1.0.dev0.tar.gz)
resolves the issue.



## Build A Conda Package

[Building conda packages from scratch](https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html)
has detailed instructions on how to build a conda package from scratch.
In most situations,
you can simplify the building process with the help of `conda skeleton`.
Please refer to 
[Building conda packages with conda skeleton](https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs-skeleton.html)
on how to use build a conda package using conda skeleton.

## Example

https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/building-conda-packages.html#building-a-sep-package-with-conda-and-python-2-or-3

https://github.com/conda/conda-recipes

## References

https://www.anaconda.com/patching-source-code-to-conda-build-recipes/

https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs-skeleton.html

https://docs.conda.io/projects/conda-build/en/latest/concepts/recipe.html

https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/index.html

https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/building-conda-packages.html

https://github.com/conda/conda-build/issues/3779
