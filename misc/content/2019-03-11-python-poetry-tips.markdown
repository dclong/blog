Status: published
Date: 2020-09-09 13:38:03
Author: Benjamin Du
Slug: python-poetry-tips
Title: Manage Your Python Project Using Poetry
Category: Computer Science
Tags: programming, Python, poetry, build tool, dependency management

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


[Poetry Documentation](https://poetry.eustace.io/docs/)

## Tips and Traps 

1. Python Poetry supports Python package dependencies on GitHub.
    For example,
    if a Python package depends on https://github.com/chdu/dsutil,
    then you can add it using the following.

        :::bash
        poetry add git+https://git@github.com/chdu/dsutil

    Or
        :::bash
        poetry add git+ssh://git@github.com/chdu/dsutil

## Usage

    :::bash
    poetry new proj

    :::bash
    poetry init

## Updating poetry

Updating poetry to the latest stable version is as simple as calling the self:update command.

    :::bash
    poetry self:update

If you want to install prerelease versions, you can use the --preview option.

    :::bash
    poetry self:update --preview

https://codingdose.info/2018/08/02/develop-and-publish-with-poetry/

https://hackersandslackers.com/poetic-python-project-packaging/

## export

This command exports the lock file to other formats.

    :::bash
    poetry export -f requirements.txt > requirements.txt

## User Tasks

https://github.com/sdispater/poetry/pull/591

https://github.com/sdispater/poetry/issues/241

## Run Test Suits Using Pytest

    :::bash
    poetry run pytest

Or if you want to make it specific to collect test suits from the `test` directory 
under the root directory of the project.

    :::bash
    poetry run pytest test

## Configuration

https://python-poetry.org/docs/cli/#config

https://python-poetry.org/docs/configuration/

## pyproject.toml Examples

https://github.com/dclong/pyproject.toml

## References

https://github.com/sdispater/poetry/issues/522

https://github.com/sdispater/poetry/issues/655

https://github.com/sdispater/poetry/issues/621


