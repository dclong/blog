Status: published
Date: 2021-03-26 10:25:39
Author: Benjamin Du
Slug: tips-on-pex
Title: Tips on pex
Category: Computer Science
Tags: programming, Python, pex, dependency, virtual environment

## Steps to Build a pex Environment File

1. Start a Python Docker image with the right version of Python interpreter installed.
    For example,

        :::bash
        docker run -it -v $(pwd):/workdir python:3.5-buster /bin/bash

2. Install pex.

        :::bash
        pip3 install pex

3. Build a pex environment file.

        :::bash
        pex --python=python3 -v pyspark findspark -o env.pex
        pex --python=python3 --python-shebang=/usr/share/anaconda3/bin/python --inherit-path=fallback -v pyspark -o env.pex

## General Tips

1. pex to Python is like JAR to Java.

2. Python packages that have native code (C/C++, Fortran, etc.) dependencies work well in pex.
    However,
    you have to make sure that pex runs on the same type of OS. 
    For example, 
    if you build a pex environment containing numpy on macOS,
    it won't run on a Linux OS.
    You will get the following error message 
    if you try to run the pex environment (generated on macOS) in a Linux OS.

    > root@013f556f0076:/workdir# ./my_virtualenv.pex 
    > Failed to execute PEX file. Needed manylinux2014_x86_64-cp-37-cp37m compatible dependencies for:
    > 1: numpy==1.18.1
    >    But this pex only contains:
    >      numpy-1.18.1-cp37-cp37m-macosx_10_9_x86_64.whl

2. Python with the same version as the one that generated the pex file
    need to be installed in on the machine to run the pex file.
    And the Python executable must be searchable by `/usr/bin/env` if you use the default settings.
    It is kind of like that Java need to be installed on the machine to run a JAR application.

3. If there are multiple versions of Python installed in your system,
    you use the option `--python` to specify the Python interpreter 
    (e.g., `--python=python3.7`)
    to use when building a pex environment file.
    The specified Python interpreter is written into the shebang 
    (e.g., `#!/usr/bin/env python3.7`) 
    for running the built pex environment file.
    There are 2 ways to customize thee shebang used for running the built pex environment file.
    The first way is via the option `--python-shebang` at BUILDING time
    which allows you to specify an explicit shebang line
    (e.g. `--python-shebang=/usr/share/anaconda3/bin/python`).
    The second way is via the `PEX_PYTHON` environment variable at RUN time
    which allows you to specify an explicit Python 
    (e.g. `PEX_PYTHON=python3`) 
    even if the pex file says something else.
    It is suggested that you use the environment variable `PEX_PYTHON`
    to control the Python interpreter to run the PEX environment file
    as it is more flexible.

5. By default, 
    a pex environment file does not inherit the contents of `sys.path`.
    There are 2 ways to make a pex environment file inherit the contents of `sys.path`. 
    One way is to issue one of the options at bulid time.

        :::bash
        --inherit-path
        --inherit-path=prefer
        --inherit-path=fallback

    Another way is to export the environment variable `PEX_INHERIT_PATH` at run time.
    For more discussions,
    please refer to 
    [this issue](https://github.com/pantsbuild/pex/issues/904#event-3057832565)
    .

4. It is suggested that you turn on verbosity mode 
    using the option `-v` 
    (can be specified multiple times, e.g., `-vvv` to increase verbosity).

## pex vs conda-pack

1. A pex file contain only Python packages but not a Python interpreger in it 
    while a conda-pack environment has a Python interpreter as well,
    so with the same Python packages a conda-pack environment is much larger than a pex file.

2. A conda-pack environment is a `tar.gz` file and need to be decompressed before being used
    while a pex file can be used directly.

3. If a Python interpreter exists,
    pex is a better option than conda-pack. 
    However, 
    conda-pack is the ONLY CHOICE if you need a specific version of Python interpreter 
    which does not exist and you do not have permission to install one
    (e.g., when you need to use a specific version of Python interpreter with an enterprise PySpark cluster). 
    If the pex file or conda-pack environment needs to be distributed to machines on demand,
    there are some overhead before running your application. 
    With the same Python packages, 
    a conda-pack environment has large overhead/latency than the pex file
    as the conda-pack environment is usually much larger and need to be decompressed before being used.

## References

https://github.com/pantsbuild/pex

https://punchplatform.com/2019/10/08/packaging-python/

https://github.com/pantsbuild/pex/issues/746