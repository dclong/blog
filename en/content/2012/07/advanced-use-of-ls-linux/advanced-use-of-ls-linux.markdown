Status: published
Date: 2012-07-29 09:29:01
Slug: list-files-without-tilde-linux
Author: Ben Chuanlong Du
Title: Advanced Use of "ls" in Linux
Category: OS
Tags: Linux, ls, shell
Modified: 2019-03-29 09:29:01


## List Files Sorted by Time

You can list files sorted by time (newest first) using the `-t` option.
Notice that the `-t` option is also support by `hdfs dfs -ls`.

    ls -lht

## Ignore Files

1. You have to either enclose the pattern in quotes or escape the wildcard in patterns.

2. Equivalent commands to ignore JSON files.

        ls --ignore=*.json
        ls -I*.json
        ls -I \*.json
        ls -I '*.json' # quote needed due to the space!
        find . ! -iname '*.json'

3. Ignore multiple patterns.

        ls -I '*.txt' -I '*.pdf'
        find . ! -iname '*.json' ! -iname '*.pdf'
        find . -type f -name "*.txt" ! -path "./Movies/*" ! -path "./Downloads/*" ! -path "./Music/*"

4. Ignore backup files (whose names end with `~`).

        ls -B

    Or you can use

        ls --ignore=*~

## List Contents of a Directory with the Directory Name Prefixed

When you list the contents of a directory (e.g., `raw`) using the following command.
```bash
ls raw
```
the directory name `raw` is not prefixed to the returned/printed contents.
You can of course concatenate the directory name `raw` to each of its subdirectory/subfile manually,
however,
a more convenient way is to use the the following command.
```bash
ls raw/*
```

## List Only Subdirectories
You can use the following command to list directories only in the current directory.
```bash
ls -d ./*
```

## List Hidden Files and Directories
```language
ls -d .*
```

