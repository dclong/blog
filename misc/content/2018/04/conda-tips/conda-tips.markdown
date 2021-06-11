Status: published
Date: 2018-04-22 09:36:27
Author: Ben Chuanlong Du
Slug: conda-tips
Title: Tips on Conda
Category: Computer Science
Tags: programming, Python, conda, tips, Anaconda Python
Modified: 2020-06-22 09:36:27

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. conda and executables installed by conda might not be able to run by sudo directly. 
    If this happends, 
    use the full path of the executable
    or add the option `-E "PATH=$PATH"` to sudo.
    
        :::bash
        sudo -E env "PATH=$PATH" <command> [arguments]

2. By defaut, conda installs things into /opt/conda.

## Download Archives

https://repo.anaconda.com/miniconda/

https://repo.anaconda.com/archive/

## Conda Environment

https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

### Create a Conda Virtual Environment

Create a conda virtual environment with Python 3.7, numpy, pandas and scikit-learn installed.

    :::bash
    conda create -n myenv python=3.7 numpy pandas scikit-learn

If you have issues creating a conda virtual environment 
(e.g., due to package not found in the current conda channel),
you can create a bare conda virtual environment,
install `pip` into the environment 
and then use `pip` to install the needed packages.
For example,
the below code creates a conda virtual environment 
with the Python package `optimuspyspark` installed.

    :::bash
    conda create -n optimus
    conda activate optimus
    conda install pip
    pip install optimuspyspark

Be careful though, 
as pip in a virtual environment sometimes installs packages into global location rather than your virtual environment. 
This won't affect usage of your virtual environment locally, 
generally speaking.
However,
if you want to package your virtual environemnt using conda-pack 
and use it somewhere else,
the Python packages installed outside the virtual environemnt won't be packed.
Make sure to use `conda list -n env_name` 
to check that the Python packages are installed into the virtual environment 
before you pack it using `conda-pack`.
If the issue appears, 
you can always manually specify the installation location for `pip`.

### Activate a Conda Virtual Environment

    :::bash
    conda activate myenv

### Pack a Conda Virtual Environment

A conda virtual environment can be packed 
([conda-pack](https://conda.github.io/conda-pack/index.html) required) 
into a `tar.gz` file 
and be used on other machines with the same type of OS.
Notice that all packages in a conda virtual environment 
must be managed by conda (rather than pip)
so that it can be packed by conda-pack.

    :::bash
    conda pack -n myenv -o myenv.tar.gz

### Deactivate a Conda Environment

    :::bash
    conda deactivate myenv

### Remove a Conda Environment

    :::bash
    conda env remove -n myenv

## Administering a multi-user conda installation

https://conda.io/docs/user-guide/configuration/admin-multi-user-install.html

## My Conda Packages

https://anaconda.org/legendu/sqlalchemy-teradata

## References

https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html

https://stackoverflow.com/questions/41060382/using-pip-to-install-packages-to-anaconda-environment

https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

[Conda Cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

[Conda Cheatsheet](https://kapeli.com/cheat_sheets/Conda.docset/Contents/Resources/Documents/index)