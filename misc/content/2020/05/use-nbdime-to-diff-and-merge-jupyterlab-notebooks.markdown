Status: published
Date: 2021-04-26 23:50:45
Author: Benjamin Du
Slug: use-nbdime-to-diff-and-merge-jupyterlab-notebooks
Title: Use nbdime to Diff and Merge JupyterLab Notebooks
Category: Computer Science
Tags: Computer Science, JupyterLab, notebook, diff, merge, version control, nbdime, Git

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

`nbdime` is a tool for diffing and merging of Jupyter notebooks.
Notice that nbdime integrates with git well.

## Tips and Traps

If you install nbdime to your local directory,
make sure that the directory containing executables (usually `~/.local/bin`) 
is in `$PATH` so that it can be used without issues.

## Installation and Configuration

You can use the following command to configure nbdime for Git.

    :::bash
    nbdime config-git (--enable | --disable) [--global | --system]

Register nbdime with Git for the current project/repository.

    :::bash
    nbdime config-git --enable

Deregister nbdime with Git for the current project/repository.

    :::bash
    nbdime config-git --disable

Register nbdime with Git for global users.

    :::bash
    nbdime config-git --enable --global

Deregister nbdime with Git for global users.

    :::bash
    nbdime config-git --disable --global

If you are using [xinstall](https://github.com/dclong/xinstall),
a simple way to install and configure nbdime is to run the following commandd.

    :::bash
    xinstall nbdime -ic

## Version Control Integration

nbdime config-git --enable --global

nbdime config-git --disable --global

## References

[nbdime](https://github.com/jupyter/nbdime)

http://nbdime.readthedocs.io/en/stable/

http://nbdime.readthedocs.io/en/stable/vcs.html