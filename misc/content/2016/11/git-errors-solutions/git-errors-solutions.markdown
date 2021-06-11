Status: published
Date: 2020-07-14 14:02:46
Author: Ben Chuanlong Du
Slug: git-errors-solutions
Title: Git Errors and Solutions
Category: Software
Tags: programming, Git, version control, error, solutions, issues
Modified: 2020-07-14 14:02:46

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## `git clone` throws the error message "fatal: unable to fork"

The reason is due to missing SSH.

The solution is simply to install `openssh-client`.

    sudo apt-get install openssh

## `git pull` throw the error message "fatal: early EOF fatal: index-pack failed"

There are a few possible reasons that caused this error.

1. Compression runs out of memory.

2. Poor network connection.

Below are some possible solutions to this issue.

1. turn off compression.

        git config --global core.compression 0

2. Try with a better network connection.

3. Do a shallow clone.

        git clone --depth 1 repos_url

    The command trieves the latest commit.

4. Repack remote.

5. Use Git submodules.

## Force push lead to "bad object" message from git rev-list

Run the command `git fetch` first and then try force push again.

https://github.com/git-lfs/git-lfs/issues/3977

https://ar.al/2019/10/19/scary-git-lfs-bad-object-error-not-so-scary-after-all/

## References

- [fatal: early EOF fatal: index-pack failed](http://stackoverflow.com/questions/21277806/fatal-early-eof-fatal-index-pack-failed)
- [Retrieve specific commit from a remote Git repository](http://stackoverflow.com/questions/14872486/retrieve-specific-commit-from-a-remote-git-repository/30701724#30701724)
- [Convert shallow clone to full clone](http://stackoverflow.com/questions/6802145/convert-shallow-clone-to-full-clone/6802238#6802238)
- [Git Fails On Large Files](http://blog.dinaburg.org/2013/07/git-fails-on-large-files.html)
