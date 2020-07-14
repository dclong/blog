Status: published
Date: 2020-07-14 14:05:22
Author: Ben Chuanlong Du
Slug: tips-for-git-large-file-storage
Title: Git Large File Storage
Category: Software
Tags: Software, Git, version control, large file storage, LFS

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


## References

https://git-lfs.github.com/

https://help.github.com/articles/installing-git-large-file-storage/

https://help.github.com/articles/configuring-git-large-file-storage/

https://help.github.com/articles/removing-files-from-git-large-file-storage/

https://stackoverflow.com/questions/42597408/git-lfs-what-is-locking-support-and-should-i-enable-it

