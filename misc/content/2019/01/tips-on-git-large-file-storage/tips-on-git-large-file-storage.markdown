Status: published
Date: 2019-01-08 13:46:55
Author: Ben Chuanlong Du
Slug: tips-for-git-large-file-storage
Title: Git Large File Storage
Category: Software
Tags: Software, Git, version control, large file storage, LFS
Modified: 2021-01-08 13:46:55

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Installation

Please refer to 
[git-lfs Installation](https://github.com/git-lfs/git-lfs/wiki/Installation)
for instructions on how to install git-lfs.


## Tips and Traps

1. Track a large file.

        :::bash
        git lfs track "*.pickle"

1. It seems to be that git-lfs automatically tracks large files now if it is installed and enabled,
    which makes things more convenient.



## Large File
https://stackoverflow.com/questions/20002557/how-to-remove-a-too-large-file-in-a-commit-when-my-branch-is-ahead-of-master-by

https://rtyley.github.io/bfg-repo-cleaner/

https://github.com/rtyley/bfg-repo-cleaner

Removing a file added in the most recent unpushed commit
https://help.github.com/articles/removing-files-from-a-repository-s-history/

Removing Changes
https://stackoverflow.com/questions/1090309/git-undo-all-working-dir-changes-including-new-files

git checkout -f

## References

https://git-lfs.github.com/

https://help.github.com/articles/installing-git-large-file-storage/

https://help.github.com/articles/configuring-git-large-file-storage/

https://help.github.com/articles/removing-files-from-git-large-file-storage/

https://stackoverflow.com/questions/42597408/git-lfs-what-is-locking-support-and-should-i-enable-it

