Status: published
Date: 2020-01-06 00:02:49
Author: Benjamin Du
Slug: managing-virtual-environments-in-poetry
Title: Managing Virtual Environments in Poetry
Category: Computer Science
Tags: programming, Python, Poetry, virtual environment, shell

## Where to Create Virtual Environments

By default,
Poetry create virtual environment in `$HOME/.poetry` for cahcing/sharing purpose.
However,
it is inconvenient if you use Docker-based web IDE for a Python project 
as you will lose the created virtual environment once the Docker container is restarted.
In that situation, 
you have to create a new virtual environment, 
set up the Python interpreter again,
which is tedious.
Fortunately, 
Poetry allows to create virtual environment in th root directory of a Python project,
and it is recommended to do so for the situation described above.
Run the following command to configure Poetry to create virtual environment in the root directory of the current project.

    :::bash
    poetry config --local virtualenvs.in-project true

Notice that the above configure works for the current project only.
Use the following command
if you want to make Poetry always create virtual environment in the root directory of a project.

    :::bash
    poetry config virtualenvs.in-project true


## Create a Virtual Environment

Poetry supports the `env` subcomamnd starting from version 1.0.0.
You can use `poetry env use python_version` to specify the Python version to use for the project.

    :::bash
    poetry env use python3

## Activate Vitual Environment

The virtual environment shell can be activated using the following command.

    :::bash
    poetry shell

If you have the virtual environment created in the directory `.venv` 
under the root directory of the project,
you can also use the following command to activate the virtual environment.

    :::bash
    . .venv/bin/activate

## Show Information of the Vitual Environment

You can list information of virtual environments using the following command.

    :::bash
    poetry env info

## References

https://python-poetry.org/docs/managing-environments/

https://github.com/python-poetry/poetry/issues/108
