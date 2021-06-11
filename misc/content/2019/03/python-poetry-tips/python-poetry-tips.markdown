Status: published
Date: 2021-06-02 11:17:44
Author: Benjamin Du
Slug: python-poetry-tips
Title: Manage Your Python Project Using Poetry
Category: Computer Science
Tags: programming, Python, poetry, build tool, dependency management
Modified: 2021-06-02 11:17:44

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Tips and Traps 

1. Python Poetry is current the best project management tool for Python!

2. Python Poetry supports Python package dependencies on GitHub.
    For example,
    if a Python package depends on https://github.com/dclong/dsutil,
    then you can add it using the following.

        :::bash
        poetry add git+https://github.com/dclong/dsutil.git

    Or

        :::bash
        poetry add git+ssh://git@github.com/dclong/dsutil.git

    For more details,
    please refer to
    [poetry add](https://python-poetry.org/docs/cli/#add.)
    and
    [git dependencies](https://python-poetry.org/docs/dependency-specification/#git-dependencies)
    .

3. `poetry install` removes non needed libraries. 
    A tricky situation is that if you have dependency A 
    which depends on dependency B,
    and you have specified both A and B in `pyproject.toml`.
    Removing dependency B from `pyrpoject.toml` and then running `poetry install` 
    won't remove the library B from the virtual environment as B is still needed by A.

4. Poetry has lots of issues in Windows currently.
    It is suggested that you avoid using poetry in Windows.

## Install Python Poetry

1. Follow the [official tutorial](https://python-poetry.org/docs/#installation).

2. Using xinstall.

        :::bash
        # install xinstall if it hasn't been installed
        sudo pip3 install -U git+https://github.com/dclong/xinstall@master
        # install poetry using xinstall
        xinstall pt -ic

## Updating Python Poetry

Updating poetry to the latest stable version is as simple as calling the self:update command.

    :::bash
    poetry self:update

If you want to install prerelease versions, you can use the --preview option.

    :::bash
    poetry self:update --preview

## Usage

### Create/Initialize a New Project

1. Create a new Python project using poetry.

        :::bash
        poetry new proj

2. Initialize an existing Python project using poetry.

        :::bash
        poetry init

### Install Dependencies

1. Installl all dependencies.

        :::bash
        poetry install 

2. Installl all but dev dependencies.

        :::bash
        poetry install  --no-dev

### Export Dependencies

1. Export the lock file to `requirements.txt` 
    so that the dependency can be installed using `pip`.

        :::bash
        poetry export -f requirements.txt > requirements.txt

### Run Commands in the Virtual Environment 

`peotry run cmd` is a quick to run `cmd` using the virtual environment managed by `poetry.
Another way is to manually set `PATH` before you invoke `cmd`. 
For example,

    :::bash
    PATH=.venv/bin:$PATH cmd

1. Run test suits using pytest.

        :::bash
        poetry run pytest

    Or if you want to make it specific to collect test suits from the `test` directory 
    under the root directory of the project.

        :::bash
        poetry run pytest test

2. Run pytype.

        :::bash
        poetry run pytype .

## User Tasks

https://github.com/sdispater/poetry/pull/591

https://github.com/sdispater/poetry/issues/241

## Configuration

https://python-poetry.org/docs/cli/#config

https://python-poetry.org/docs/configuration/

Pleaser refer to
[pyproject.toml](https://github.com/dclong/pyproject.toml)
for examples of configuration for Python Poetry.

## Restrict Operating Systems in Python Poetry

```
[tool.poetry]
# ...
classifiers = [
    "Operating System :: POSIX :: Linux",
]
```

https://python-poetry.org/docs/pyproject/#classifiers

https://pypi.org/classifiers/

https://github.com/python-poetry/poetry/issues/738

https://github.com/python-poetry/poetry/issues/3356


## References

https://github.com/sdispater/poetry/issues/522

https://github.com/sdispater/poetry/issues/655

https://github.com/sdispater/poetry/issues/621

[Poetry Documentation](https://poetry.eustace.io/docs/)

https://codingdose.info/2018/08/02/develop-and-publish-with-poetry/

https://hackersandslackers.com/poetic-python-project-packaging/
