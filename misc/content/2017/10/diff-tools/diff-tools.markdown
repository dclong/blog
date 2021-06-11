Status: published
Date: 2020-05-27 15:04:30
Author: Ben Chuanlong Du
Slug: diff-tools
Title: Tools for Differencing Text Files
Category: Software
Tags: diff, tools, Linux, cli, command line, colordiff, vimdiff
Modified: 2020-05-27 15:04:30


## General Tips

1. If 2 files are formatted differently,
  you can first format them and then check the differences between them.
  An extreme way is to get rid of all white spaces in the 2 files and then compare them.

        sed -i 's/ //g' file_1 file_2

## Command-line Tools

### git-diff

`git diff` is a generally useful command. 
It can not only show you the changes of files in side a Git repository
but can also be used to compare files/directories outside of a Git repository.

1. Show differences between 2 files.
    The option `--no-index` can be omitted if at least one of the two files is outside a Git repository.
    Output of `git diff` is colorized.

        git diff --no-index file_1 file_2

2. Show differences between 2 directories,
    which is similar to that of showing differences between 2 files.

        git diff --no-index dir_1 dir_2

### colordiff/diff

It is suggested that you use `colordiff` instead of `diff`
as `colordiff` colorizes the output of `diff`.
However, 
both `colordiff` and `diff` can be replaced by `git diff` as shown above.


### vimdiff

All of `git diff`, `colordiff` and `diff` show line-leve changes. 
`vimdiff` is great command-line tool that is able to show differences inside lines.

## Online Tools

### [text-compare](https://text-compare.com/)
[text-compare](https://text-compare.com/)
is a good one.


### [diffnow](https://www.diffnow.com/)


## References

https://stackoverflow.com/questions/16683121/git-diff-between-two-different-files

https://wiki.dandascalescu.com/reviews/software/diffuse_-_the_one_best_visual_diff_tool_for_linux


https://coderwall.com/p/ydluzg/better-git-diff

https://stackoverflow.com/questions/5326008/highlight-changed-lines-and-changed-bytes-in-each-changed-line


https://stackoverflow.com/questions/18069611/fastest-way-of-finding-differences-between-two-files-in-unix

https://stackoverflow.com/questions/4544709/compare-two-files-line-by-line-and-generate-the-difference-in-another-file


https://unix.stackexchange.com/questions/11128/diff-within-a-line

https://www.networkworld.com/article/3190407/linux/nine-ways-to-compare-files-on-unix.html

