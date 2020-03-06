Status: published
Date: 2020-02-18 10:42:24
Author: Benjamin Du
Slug: tips-on-conda-pack
Title: Tips on conda-pack
Category: Computer Science
Tags: programming, conda-pack, conda, dependency, virtual environment

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

1. All packages in a virtual environment must be managed by conda (rather than pip)
    so that it can be packe using conda-pack.

2. When using a conda-pack virtual environment with PySpark,
    the Python package `pyyspark` comes with Spark is automatically injected into PYTHONPATH
    so that users do not have to install `pyspark` into the virtual environemnt by themselves.
    As a matter of fact,
    the `pyspark` comes with Spark is always used
    even if you have a local copy installed 
    when you submit a PySpark application with a conda-pack virtual environment.
    For more discussions,
    please refer to [this isue](https://github.com/conda/conda-pack/issues/102).

## References

https://conda.github.io/conda-pack/

https://conda.github.io/conda-pack/cli.html

https://github.com/conda/conda-pack/

