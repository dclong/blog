Status: published
Date: 2021-05-02 12:31:26
Author: Benjamin Du
Slug: git-implementations-and-bindings-in-python
Title: Git Implementations and Bindings in Python
Category: Computer Science
Tags: Computer Science, programming, Git, Python, Dulwich, pygit2, GitPython 
Modified: 2026-01-10 17:03:46

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There are multiple Git implementations/bindings in Python:
[pygit2](https://github.com/libgit2/pygit2),
[Dulwich](https://github.com/dulwich/dulwich)
and
[GitPython](https://github.com/gitpython-developers/GitPython)
.

Below is a simple comparison of the 3 packages.

|                | pygit2              | dulwich       | GitPython                   |
|----------------|---------------------|---------------|-----------------------------|
| Status         | Active              | Active        | Maintenance mode            |
| Implementation | bindings to libgit2 | pure Python   | bindings to the git command |
| License        | GPLv2               | Apache, GPLv2 | BSD 3                       |
| Feature        | complete            | incomplete    | complete                    |

Overall,
dulwich is recommended.

## References 

- [Hands on Dulwich](http://www.legendu.net/misc/blog/hands-on-Dulwich)

