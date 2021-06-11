Status: published
Date: 2017-03-23 07:43:12
Author: Ben Chuanlong Du
Slug: reduce-size-of-git-repository
Title: Reduce Size of Git Repository
Category: Software
Tags: software, Git, repository, size
Modified: 2019-05-23 07:43:12

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Use Git Large File Storage to Manage Large Files

Git Large File Storage (Git-LFS) is the recommended way to work with large files.
Please read the following if have already committed large files into your repository.

## Run `git gc --aggressive` Manually 
    
    :::bash
    git gc --aggressive

https://stackoverflow.com/questions/3313908/git-is-really-slow-for-100-000-objects-any-fixes

## [BFG Repo Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)

```
java -jar bfg.jar --strip-blobs-bigger-than 100M some-big-repo.git
```

## Other Ways

```bash
git push --force


$ git gc --prune=now --aggressive

git filter-branch --prune-empty -d /dev/shm/scratch \
  --index-filter "git rm --cached -f --ignore-unmatch oops.iso" \
  --tag-name-filter cat -- --all
$ git reflog expire --expire=now --all
git filter-branch --tree-filter 'rm -f DVD-rip' HEAD

git filter-branch --force --index-filter 'git rm --cached -r --ignore-unmatch oops.iso' --prune-empty --tag-name-filter cat -- --all
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now
git gc --aggressive --prune=now
```

```bash
git checkout --orphan temp $1 # create a new branch without parent history
git commit -m "Truncated history" # create a first commit on this branch
git rebase --onto temp $1 master # now rebase the part of master branch that we want to keep onto this branch
git branch -D temp # delete the temp branch
```

The following 2 commands are optional - they keep your git repo in good shape.

```bash
git prune --progress # delete all the objects w/o references
git gc --aggressive # aggressively collect garbage; may take a lot of time on large repos
```

Or another way is just to remove the .git directory, 
reinitial a git repository and push to remote with the `--force` option.

http://stackoverflow.com/questions/2100907/how-to-remove-delete-a-large-file-from-commit-history-in-git-repository

http://blog.gbacon.com/2009/08/git-shrinking-subversion-import.html

http://stackoverflow.com/questions/2116778/reduce-git-repository-size

shallow clone using the depth option
```bash
git clone git://source.winehq.org/git/wine.git ~/wine-git --depth 1
```
