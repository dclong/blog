Status: published
Author: Ben Chuanlong Du
Date: 2021-03-11 11:35:36
Title: Tips on Git
Slug: git-tips
Category: Software
Tags: tips, Git, software, version control, distributed

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

https://www.gitignore.io/

## General Git Tips

1. `-C` vs `--git-dir` vs `--work-tree`

        :::Bash
        git -C /path/to/repository status
        # which is equivalent to
        git --git-dir=jupyterhub-ds/.git --work-tree=jupyterhub-ds status

0. Do not work on the master branch directly. 
    Use it purely as the production branch and merge mature features from other branches. 
    You can apply one or more commits in a branch into other branches.
    @TODO: give an example

1. Keep a production repository for using the your product and dev repository for developing.

1. Do not use symbolic links (to files outside the repository) in a Git repository.

2. Keep each commit small and specific. 
    Do not mix different work together in a single commit. 
    This make it convenient to apply part of your work to other branches. 

4. Git support several protocols: Git, SSH and HTTP. 
    The Git protocol is preferred.
    If you are behind a firewall and/or proxy server and cannot use the Git protocol,
    you can try the HTTP protocol.
    The HTTP protocol requires a password every time you access a private repository 
    or you push to a repository (not matter private or not).


1. Do not amend public commits.

3. it seems to me that you should use many smaller files
    rather than a single big file to avoid conflicts while working collaboratively.
0. not a good practice to track non text files
    especially when the files are large.
    It suggested that you separate (large) non-text files into another place (e.g., a file host).

1. `#` or `;` start a comment line

5. Working in remote directory mounted by fuse might cause problems.
    Avoid using Git in a remote file system.

6. Generally speaking,
    it is not a good idea to puts things into the global Git ignoring file.

7. not a good idea to track .gitignore ... this depends

10. When you want to change a part of the code,
    and this change might also be applied to other branches,
    then you'd better fork from the base of all branches.
    This allows you to patch the changes to all branches easily.

14. It seems that the git repo for criss's project is very large even though it is the first commit.
    Why is this? 1.9G? while things recorded is much smaller than this.

18. In Git 1.x+,
    you can use `git add -u` to stage all tracked files including deleting previously tracked files.
    In Git 2.0,
    you can use `git add -u :/` to stage your whole working tree,
    and you can use `git add -u .` to stage just the current path.

19. Git with http proctol ask for passwords when one push to or pull from a repository.
    There are ways to cache Git password in Windows,
    however,
    I'd rather save the pain and use AutoHotkey to help me type in password.

5. To rebase, follow the steps below.

        git pull --rebase origin master
        git add <some-file>
        git rebase --continue
        git rebase --abort

6. Use the following comamnd to clone into a specific directory.
    Please refer to 
    [How do you clone a Git repository into a specific foler?](https://stackoverflow.com/questions/651038/how-do-you-clone-a-git-repository-into-a-specific-folder)
    for more discussions.

        :::Bash
        git clone git@github.com:user/repos.git dir_name

## Shadow Clone

1. use

        git clone --depth 1 repos_url

    You can get the full clone later by running either of the following two commands.

        git fetch --unshallow

    or

        git fetch --depth 1000000

## Clone a Specific Tag

    :::bash
    git clone --depth 1 --branch 2.4.5 https://github.com/apache/spark.git                                                 

https://stackoverflow.com/questions/20280726/how-to-git-clone-a-specific-tag

## Proxy/Tunnel Related

You can use Git with ProxyChains.

    :::bash
    proxychains git ...

What is corkscrew?
    :::bash
    #!/bin/bash

    corkscrew http://10.135.227.47 80 $*

## Git Syntax

### Repository

1. Add a Remote repository `origin` 

        git remote add origin git@github.com:dclong/jmail.git

    `origin` is a popular default name for remote repositories,
    however, you can use any valid name you like.
    If you want to add a local bare repository, 

        git remote add origin path_to_repository_dir

7. Overwrite the remote repository `origin` using the master branch.
    Notice that no patching is going on. 
    The entire remote repository is overwritten by the master branch.

        git push origin master --force

10. Tells git default branches to use when pushing

        git push -u origin master

### Misc

2. Track all Files

        git add *

    or 

        git add .

3. Add all modifed tracked files for commit

        git add *

    or

        git add .

4. Remove a file but keep it in the local repository

        git rm --cached file_name

6. Init current directory as a bare repository (for local sharing purpose).

        git init --bare

    Note that the directory must end with `.git` 
    in order to be a sharing repository.

5. Other commands

    git cherry-pick
    git push


### Branching

1. Show all branches.

        git branch -v

2. Checkout the branch "dev".

        git checkout dev

2. Checkout the last branch that you were on.

        git checkout -

3. Check out the remote branch named "dev".

        git fetch
        git checkout dev

4. Create a branch named "dev" and switch to it.

        git checkout -b dev

5. Merge the branch named "hotfix" to the current branch

        git merge hotfix

6. Rename "old_branch" to "new_branch".

        git branch -m old_branch new_branch

7. Delete a fully merged branch.

        git branch -d branch_name

8. Force to delete a branch no matter it has been merged or not.

        git branch -D branch_name


### Patch

1. Show patches of a file

        git log -p file_name

6. Show diff of a staged file

        git diff -cache file_name

1. to find commits not on remote

        git log origin/master..

    or 

        git cherry -v origin/master


2. `git log origin/master..HEAD` lists unpushed commits.
    Uncommitted changes are not listed.
    Notice the syntax `git log <since>..<until>` is similar to Bash `..` in list.

4. Switching branches carries uncommitted changes with you. 
    Either commit first, run git checkout . to undo them, 
    or run git stash before switching. 
    (You can get your changes back with git stash apply)

### Tags

1. List your tags

        git tag

2. Create a tag

        git tag -a v0.1 -m "description about the tag"

3. Show a tag

        git show v0.1

4. Push tags to remote repository

        git push origin v0.1

5. Create a branch at a specific tag

        git checkout -b branch_name v0.1


### Configuration

16. Git in Windows automatically convert Linux/OSX line termiantors to Windows line terminators. 
    To turn off auto line terminator conversion globally, use the following command.

        git config core.autocrlf false

    You can also use the `dos2unix` command 
    to change a Windows text file (with Windows line terminators) 
    to a Unix/Linux file (with Unix/Linux line terminators).
    The `unix2dos` does the opposite conversion.

17. Git track permissions of files by default. 
    This can be an issue if you work on multiple operating systems.
    You can use the following command to ask Git 
    to ignore executable differences between the index and the working copy.

        git config --global core.fileMode false

    For one-off ignoring, you use

        git -c core.fileMode false

20. Git does not colorize output automatically on some (old) Linux servers. 
    You can use `git config --global color.ui auto` to force Git to colorize output. 

11. List all tracked files in a git repository

        git ls-tree --full-tree -r HEAD

1. Stash your work

        git stash

## References

- [Git reset, revert and rebase commands](https://opensource.com/article/18/6/git-reset-revert-rebase-commands)
- [Git Documentation](http://git-scm.com/documentation)
- [Using Git to manage a web site](http://toroid.org/ams/git-website-howto)
- [A web-focused Git workflow](http://joemaller.com/990/a-web-focused-git-workflow/)
- [Why is my Git repository so big?](http://stackoverflow.com/questions/1029969/why-is-my-git-repository-so-big)
