Status: published
Date: 2019-05-12 13:27:21
Author: Benjamin Du
Slug: tips-on-gitpython
Title: Tips on GitPython
Category: Computer Science
Tags: programming, Python, Git, GitPython, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


## Changes Files

    from git import Repo
    repo = Repo('.')
    files_changed = [item.a_path for item in repo.index.diff(None)]


## Staged Files

    from git import Repo
    repo = Repo('.')
    files_changed = [item.a_path for item in repo.index.diff('HEAD')]


## References

https://github.com/gitpython-developers/GitPython

https://stackoverflow.com/questions/33733453/get-changed-files-using-gitpython

https://stackoverflow.com/questions/31959425/how-to-get-staged-files-using-gitpython
