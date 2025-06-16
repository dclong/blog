Status: published
Date: 2014-09-06 09:43:30
Author: Ben Chuanlong Du
Slug: find-tips
Title: Tips on the find command in Linux
Category: OS
Tags: Linux, find, tips, search, locate
Modified: 2025-06-16 16:41:10


## Better Alternatives to `find`

There are some better alternatives to find.

1. `pathlib` module in Python

2. [fd]( https://www.legendu.net/misc/blog/tips-on-fd )

2. [ripgrep](https://github.com/BurntSushi/ripgrep)

3. [fselect](https://github.com/jhspetersson/fselect)

4. [osquery](http://www.legendu.net/misc/blog/osquery-tips) 

- The Python module `pathlib` is the most suitable one for relatively complex jobs.
- `ripgrep` is a more user-friendly alternative to find.
- Both fselect and osquery support SQL-like syntax and are more intuitive than the `find` command.

## Search Files By Name

1. Find all files with the extension ".out" in the current directory and its subdirectory, 
    and then make them executable.

        :::bash
        find . -type f -iname *.out -exec chmod +x '{}' \;
        # or you can use 
        find . -type f -iname *.out -print0 | xargs -0 chmod +x


2. Find files whose names contain "conflicted" and remove them.

        :::bash
        find . -iname '*conflicted*' -print0 | xargs -0 rm

3. Find Python scripts in the current directory recursively
    but ignore those under directories with the name `.ipynb_checkpoints`.

    :::bash
    find . -type f -iname '*.py' -not -path '*/.ipynb_checkpoints/*'

## Search Files by Size

1. Find files with 0 size and delete them.

        :::bash
        find /path/to/files -size 0 -ok -exec rm {} \;
        # or you can use
        find /path/to/files -size 0 -ok | xargs rm 


2. Find empty directories. 

        :::bash
        find / -type d -empty


3. Find files greater than 1G.

        :::bash
        find . -xdev -type f -size +1G


4. First find files and then pass them to other commands is a very useful trick.
    For example, 
    you can use the following command to find all R scripts containing the word `paste`.

        :::bash
        find . -type f -iname '*.r' | grep --color=auto paste

## Search Files by Time

1. Find files created with in 60 minutes.

        :::bash
        find . -cmin 60

2. Find files more than 30 days ago
        
        :::bash
        find . -ctime +30

3. Find file less than 30 days ago.

        :::bash
        find . -ctime -30

4. Find files that are exactly 30 days ago.

        :::bash
        find . -ctime 30

2. Find all files modified on the June 7, 2007 in the current directory.

        :::bash
        find . -type f -newermt 2007-06-07 ! -newermt 2007-06-08


3. Find all files accessed on the Sep 29, 2008 in the current directory.

        :::bash
        find . -type f -newerat 2008-09-29 ! -newerat 2008-09-30

4. Find files which had their permission changed on the same day.

        :::bash
        find . -type f -newerct 2008-09-29 ! -newerct 2008-09-30

## Search Files by Type

1. Find broken symbolic links.

        :::bash
        find . -xtype l
        # or
        find -L . -type l

2. Find executable files in current directory 
        
        :::bash
        find .  -maxdepth 1 -type f -executable

3. Check file type of all files under the current directory.

        :::bash
        find . -type f | xargs file

## Search Files by User Permission

1. Find files that belong to a user but writable by its group or other people.

        :::bash
        find /path/to/file -user user1 -perm /022

    -perm mode: File's permission bits are exactly mode (octal or symbolic).
    -perm -mode: All  of  the  permission bits mode are set for the file. 
    -perm /mode: Any of the permission bits mode are set for the file. 
    a little bit trick about how to understand the last 2 permission criterias.
    as suggested, think in terms of permission BITs (0/1)

2. The following command finds all files that readable or writable by the group or (readable or writable) by others.

    :::bash
    find /path/to/file -user user1 -perm /066

3. The following command find all files that readable and writable by the group and (readable and writable) by others.

    :::bash
    find /path/to/file -user user1 -perm -066

4. The following command find all files that readable or writable by the group and (readable or writable) by others.

    :::bash
    find /path/to/file -user user1 -perm /060 -perm /006

## References

https://www.cyberciti.biz/faq/find-command-exclude-ignore-files/

https://linuxconfig.org/how-to-explicitly-exclude-directory-from-find-command-s-search
