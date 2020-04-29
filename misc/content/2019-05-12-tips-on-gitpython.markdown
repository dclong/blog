Status: published
Date: 2019-05-12 13:27:21
Author: Benjamin Du
Slug: tips-on-gitpython
Title: Tips on GitPython
Category: Computer Science
Tags: programming, Python, Git, GitPython, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

import git
repo = git.Repo.clone_from(self._small_repo_url(), os.path.join(rw_dir, 'repo'), branch='master')

heads = repo.heads
master = heads.master       # lists can be accessed by name for convenience
master.commit               # the commit pointed to by head called master
master.rename('new_name')   # rename heads
master.rename('master')

import git
git.Git("/your/directory/to/clone").clone("git://gitorious.org/git-python/mainline.git")

https://gitpython.readthedocs.io/en/stable/tutorial.html#tutorial-label

repo = Repo(self.rorepo.working_tree_dir)
cloned_repo = repo.clone(os.path.join(rw_dir, 'to/this/path'))


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
