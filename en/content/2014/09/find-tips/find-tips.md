Status: published
Date: 2014-09-06 09:43:30
Author: Ben Chuanlong Du
Slug: find-tips
Title: Tips on the find command in Linux
Category: OS
Tags: Linux, find, tips, search, locate
Modified: 2025-06-19 11:03:55


## Better Alternatives to `find`

There are some better alternatives to find.
The Python module `pathlib` is the most suitable one for relatively complex jobs.
`fd`, `ripgrep`, `fselect` and `osquery` 
are other alternatives.

<table class="comparison-table">
    <thead>
        <tr>
            <th></th>
            <th>
                <a href="https://man7.org/linux/man-pages/man1/find.1.html">find</a>
            </th>
            <th>
                <a href="https://man7.org/linux/man-pages/man1/find.1.html">fd</a>
            </th>
            <th>
                <a href="https://github.com/jhspetersson/fselect">fselect</a>
            </th>
            <th>
                <a href="https://github.com/jhspetersson/fselect">osquery</a>
            </th>
            <th>
                <a href="https://github.com/BurntSushi/ripgrep ">ripgrep (rg)</a> 
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row"><strong>Primary Use Case</strong></th>
            <td><strong>File metadata search & execution</strong> (scripting)</td>
            <td><strong>Interactive file name search</strong> (developer productivity)</td>
            <td><strong>SQL-based file attribute search</strong> (data analysis)</td>
            <td><strong>System instrumentation & security</strong> (fleet management)</td>
            <td><strong>File content search</strong> (code searching)</td>
        </tr>
        <tr>
            <th scope="row"><strong>Usability/Syntax</strong></th>
            <td><strong>Low</strong>. Powerful but arcane, non-intuitive syntax.</td>
            <td><strong>Very High</strong>. Simple, ergonomic, sensible defaults.</td>
            <td><strong>High</strong>. SQL-like syntax is very readable for complex queries.</td>
            <td><strong>Low</strong>. Requires knowledge of SQL and specific OS schemas.</td>
            <td><strong>Very High</strong>. Simple, <code>grep</code>-like, sensible defaults.</td>
        </tr>
        <tr>
            <th scope="row"><strong>Performance</strong></th>
            <td><strong>Fair</strong>. Single-threaded by default. Slow in codebases.</td>
            <td><strong>Excellent</strong>. Parallel, ignores gitignored/hidden files by default.</td>
            <td><strong>Very Good</strong>. Optimized for its complex query execution.</td>
            <td><strong>Good</strong>. Optimized for low-overhead daemon, not raw traversal speed.</td>
            <td><strong>Exceptional</strong>. The gold standard for file content search speed.</td>
        </tr>
        <tr>
            <th scope="row"><strong>Implementation</strong></th>
            <td><strong>C</strong>. Universally available, part of <code>findutils</code>.</td>
            <td><strong>Rust</strong>. Single static binary, needs installation.</td>
            <td><strong>Rust</strong>. Single static binary, needs installation.</td>
            <td><strong>C++</strong>. Cross-platform framework, needs installation.</td>
            <td><strong>Rust</strong>. Single static binary, needs installation.</td>
        </tr>
        <tr>
            <th scope="row"><strong>Key Strength</strong></th>
            <td><strong>Ubiquity & <code>-exec</code></strong>. The POSIX standard, powerful actions.</td>
            <td><strong>Speed & Ergonomics</strong>. The perfect interactive <code>find</code> replacement.</td>
            <td><strong>Expressive Query Language</strong>. Unmatched for complex attribute filters.</td>
            <td><strong>Holistic System View</strong>. Queries files alongside processes, users, etc.</td>
            <td><strong>Raw Speed for Content Search</strong>. The fastest tool for finding text in files.</td>
        </tr>
        <tr>
            <th scope="row"><strong>Key Weakness</strong></th>
            <td><strong>Clunky syntax & poor defaults</strong>. Not user-friendly.</td>
            <td><strong>Less powerful expressions</strong> than <code>find</code> for edge cases.</td>
            <td><strong>Niche use case</strong>. Overkill for simple searches.</td>
            <td><strong>Massive overkill</strong> for just finding files. Steep learning curve.</td>
            <td><strong>Not a file finder</strong>. Only lists files as a secondary function (<code>-l</code>).</td>
        </tr>
        <tr>
            <th scope="row"><strong>Best For...</strong></th>
            <td>Shell scripts, system administration, guaranteed portability.</td>
            <td>Developers, daily interactive use, searching in git repos.</td>
            <td>Data analysts, sysadmins running complex filesystem audits.</td>
            <td>Security engineers, SREs, IT compliance teams.</td>
            <td>Developers, searching for code, log analysis.</td>
        </tr>
    </tbody>
</table>

## Example Usages
### Search Files By Name

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

### Search Files by Size

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

### Search Files by Time

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

### Search Files by Type

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

### Search Files by User Permission

1. Find files that belong to a user but writable by its group or other people.

        :::bash
        find /path/to/file -user user1 -perm /022

    - `-perm mode`: File's permission bits are exactly mode (octal or symbolic).
    - `-perm -mode`: All  of  the  permission bits mode are set for the file. 
    - `-perm /mode`: Any of the permission bits mode are set for the file. 

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

- [Find command Exclude or Ignore Files (e.g. Ignore All Hidden .dot Files )](https://www.cyberciti.biz/faq/find-command-exclude-ignore-files/)

- [How to Exclude Directories from the Find Command Search in Linux](https://linuxconfig.org/how-to-explicitly-exclude-directory-from-find-command-s-search)
