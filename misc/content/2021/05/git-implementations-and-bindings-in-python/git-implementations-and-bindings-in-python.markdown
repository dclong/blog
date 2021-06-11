Status: published
Date: 2021-06-02 12:31:26
Author: Benjamin Du
Slug: git-implementations-and-bindings-in-python
Title: Git Implementations and Bindings in Python
Category: Computer Science
Tags: Computer Science, programming, Git, Python, Dulwich, pygit2, GitPython 
Modified: 2021-06-02 12:31:26
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There are multiple Git implementations/bindings in Python:
[Dulwich](https://github.com/dulwich/dulwich),
[pygit2](https://github.com/libgit2/pygit2)
and
[GitPython](https://github.com/gitpython-developers/GitPython)
.
Both 
[Dulwich](https://github.com/dulwich/dulwich)
and
[pygit2](https://github.com/libgit2/pygit2)
are good choices.
[Dulwich](https://github.com/dulwich/dulwich)
is preferred as it has a more freindly licence agreement.

## [Dulwich](https://github.com/dulwich/dulwich)
[Dulwich](https://github.com/dulwich/dulwich)
is a Python implementation of the Git file formats and protocols, which does not depend on Git itself.
All functionality is available in pure Python. Optional C extensions can be built for improved performance.

## [pygit2](https://github.com/libgit2/pygit2)
[pygit2](https://github.com/libgit2/pygit2)
is Python bindings for libgit2.

## [GitPython](https://github.com/gitpython-developers/GitPython)
[GitPython](https://github.com/gitpython-developers/GitPython)
is a python library used to interact with Git repositories.
