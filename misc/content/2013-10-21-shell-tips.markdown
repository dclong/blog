Status: published
Author: Ben Chuanlong Du
Title: Tips on Shell Commands
Date: 2020-05-27 15:14:02
Slug: shell-tips
Category: OS
Tags: tips, Linux, shell, terminal

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

[explainshell.com](http://www.explainshell.com/)


0. command-not-found - Suggest installation of packages in interactive bash sessions

1. [Hyper](https://hyper.is/), terminator, terra, terminology, TermKit, XiKi (inactive)

3. screen, tmux

4. nohup, disown

5. nautilus-open-terminal

6. script (logging terminal activities)


## export

A new child process forked from a parent process does not inherit parent's variables by default.
The export command marks an environment variable to be exported with any newly forked child processes 
and thus it allows a child process to inherit all marked variables. 

## References

http://www.legendu.net/misc/blog/terminator-tips/

http://www.legendu.net/misc/blog/terminology-tips/

## Tips & Traps

1. Do NOT use `;` to delimit paths passed to a shell command because `;` terminates shell commands.
  Use `,` to delimit paths if needed.


## Configuration

1. Debian does not read in the `.profile` file on start-up of X windows.
    To solve this problem,
    you can source in `.profile` in in the `.xsessionrc` file.
    Ubuntu and Mint does read in the `.profile` file on start-up of  X windows.

2. You'd better use robust configuration files.
    If an error is encountered in the `.xsessionrc` file,
    the desktop environment might fail to start.

3. Bash supports both Vi mode and Emacs mode.
    The default is Emacs mode.
    You can turn on the Vim mode by `set -o vi` in `.bashrc`.

## Programming

1. Dash is faster than bash and thus is often used as login shell
    while bash has more features and is often used as interactive shell
    `.profile` is intend to be read by shell script
    you should not use any bash specific feature in it.

2. You do not have to escape quotes in sub shells (command in `$()`).

### Media

1. Empty CD tray, cannot eject by pressing the bussion,
    an interesting trick to eject CD: try to amount the CD eject the tray

## Cool Command

1. `~` is recognized as the home directory of the current user in shell only.
    You'd better not use it in other places.
    Whenever the home directory of the current user is needed,
    you can always use `$HOME` instead.

2. Check whether a system is 32 bit or 64 bit

        getconf LONG_BIT

3. all parameters: `$@` (what about `$*`?)

4. advance use of `[[ ]]` wild cards ...

5. alias, function versus scripts, function is more robust, convenient,
    but you have to source them in every time, which decreases performance
    you should think about things similar to python and ruby, use them in both ways!
    alias similar to function,
    prefer script than alias and function, generally speaking
    counter example cs
    Vim !: has no access to shell alias or functions
    another reason to use script
    function versus script:
    function need to refreshed (fun is cached)
    while scripts need not after modified
    so I think scripts is more suitable to use
    I vote for separate fun and script

6. shell scripts are more flexible than shell functions,
    because you can use shabang, which gives flexibility to use any script language
    shell function is must sometimes, e.g., cs example, shell scripts are run in sub shell
    () ... $() ...
    use $0 and $BASH_SOURCE to write ... your example


8. avoid using "global" bash variables in sub shell,
    many things are sub shell, very dangerous, and be careful!!!,
    duplicity, aerofs, dropbox examples ...

24. bash array index is 0-based

28. Be careful about `.` when using regular expressions (e.g., sed),
    this is really a general problem


`-b file` = True if the file exists and is block special file.

`-c file` = True if the file exists and is character special file.

`-d file` = True if the file exists and is a directory.

`-e file` = True if the file exists.

`-f file` = True if the file exists and is a regular file

`-g file` = True if the file exists and the set-group-id bit is set.

`-k file` = True if the files' "sticky" bit is set.

`-L file` = True if the file exists and is a symbolic link.

`-p file` = True if the file exists and is a named pipe.

`-r file` = True if the file exists and is readable.

`-s file` = True if the file exists and its size is greater than zero.

`-s file` = True if the file exists and is a socket.

`-t fd` = True if the file descriptor is opened on a terminal.

`-u file` = True if the file exists and its set-user-id bit is set.

`-w file` = True if the file exists and is writable.

`-x file` = True if the file exists and is executable.

`-O file` = True if the file exists and is owned by the effective user id.

`-G file` = True if the file exists and is owned by the effective group id.

`file1 –nt file2` = True if file1 is newer, by modification date, than file2.

`file1 ot file2` = True if file1 is older than file2.

`file1 ef file2` = True if file1 and file2 have the same device and inode numbers.

`-z string` = True if the length of the string is 0.

`-n string` = True if the length of the string is non-zero.

`string1 = string2` = True if the strings are equal.

`string1 != string2` = True if the strings are not equal.

`!expr =` True if the expr evaluates to false.

`expr1 –a expr2` = True if both expr1 and expr2 are true.

`expr1 –o expr2` = True is either expr1 or expr2 is true.

if a function has the same name as a script,
the function comes first,
but if you prefix it with sudo, then the script is run as a function
is invisible in sub shells

2. the trick of "--" end of command after which only positional arguments are accepted

3. variable substituation makes things very interesting in shell,
    for example awk and so on ..., always be careful if you use "$" and so on....

4. process of substitution <() >(), pipe ...

15. variables defined in bash function won't polute the global environment
    and local make the variables visible only to the scope of the function

17. prefer dot rather than source for sourcing script,
    because source is only for bash

18. executable files:
    if in $HOME/bin, prefer symbolic links,
    if for general uer, prefer to make a global copy,
    don't use symbolic link in /usr/bin pointing to your own files,
    you might change your file permissions and mess up the program

23. If an environment path contains spaces,
    you have to quote it with double/single quotations marks
    in order to make shell commands work correctly.

### Bash Programming

1. case ... esac is different from switch(){} in C/C++.
    You do not have to return/exit manually after each branch.


not condition
```bash
if [ ! -d "$1" ]; then
fi
```

### top

3.  top command
    Unit of the Time+ column: minutes:seconds.hundredths

### ls

7. `ls -d */` displays all directories in the current folder

1. `ls /home/*` in bash, don't use it, instead use `(/home/*)` directly

        ls -d "/home/dclong/btsync/backup/tbp_"*

    instead of

        ls -d "/home/dclong/btsync/backup/tbp_*"

    it seems to me that if you wildcard,
    then full names are returned, otherwise, short names are returned.

20. By default,
    the year for files older than 6 month are not displayed.
    You can force `ls` to show full time information by `ls -lh --full-time`.

### rsync

10. `rsync`, `/` at the end is important,
    this decides whether the folder is copy or its content is copied, unison is similar ...
    This is the same for some other commands like Amazon S3, etc.
    Also if you want to exclude an folder from `rsync`,
    you have to include the trailing slash.

### alias

25. it seems alias has lots of limitations ... only use single quotation mark,
    causes lots of problem
    YOU ACTUALLY CAN USE DOUBLE QUTOES

1. If you define an alias of a path (especially a Windows path in Cygwin, MobaXterm, etc.),
    you have to quote the path in commands, generally speaking.
    For example, if the alias of path you define is `p` (which contains spaces),
    you can use `cd "$p"` to change working directory to it.
    Note that you cannot omit the quotes.

## Filesystem

### cp

26. always use `cp` with `-i` option!

2. `cp -a` might not be a good idea sometimes,
    e.g., when in Cygwin/MobaXterm, because you might lose file permissions due to unmatch of users

1. Both cp and mv overwrite the destination file
    if is is already exists.
    cp does not overwrite existing destination directory
    but instead acts as merging contents of directories.
    mv refuses to rename a directory to a destination directory
    if the destination directory is not empty.

It is suggested that you use rsync as much as possible
as an alternative to cp.

```bash
# copy sub files/folders excluding hidden files/folders
cp a/* b
# copy sub files/folders including hidden files/folders
cp a/. b
```

### mv

5. always use interactive version of `mv` and `cp` ...
    and always use `trash` instead of `rm`

### rm

1. Remove a file whose name starts with `--` and has special characters.

        rm ./'--exclude.!sync'

2. Get file name without extension.

        basename -s .txt f.txt

3. Create a temp file.

        mktemp -tu file.XXXXX

    `mktemp` is preferred over `tempfile`.

### gpasswd

6. `gpasswd` is great for adding and removing user to/from groups

    gpasswd -d user group

### type

27. `type fun_name` shows source code of bash functions or use `declare -f`
    `type command` path of command

### mount

10. check if a path is a mount point

        if [ $(stat -fc%t:%T "mnt/wd") != $(stat -fc%t:%T "mnt/wd/..") ]; then
            echo "mounted"; else echo "not mounted";
        fi

13. mount as normal user instead of root

        mount -o uid=dclong ...

### sudo

8. I think it's better to use sudo inside bash script
    instead of prefix sudo to script names to invoke them.
    The reason is that you use sudo only when needed.

1. sudo alias

        alias sudo='sudo '

the space is necessary

### real absolute path

19. realpath: absolute path

22. absolute path
```bash
readlink path
```

### random

1. Generate a random number.

    random 0 - 32767 uniform

### Power Management

14. Show battery/power information

        acpi -bi

### Shell Programing Trick

2. Generate 00, 01, ..., to 25.

        for i in {00..25}; do echo $i; done
    or
        seq -f %02g 0 25

## Administration

3. shutdown, poweroff, halt
    It seems these commands have different meanings on different Linux distributions.
    The actually case is really complicated.
    It depends on different Linux distributions and also the services running on laptops.
    If a service fails to stop,
    the shutdown process might freeze at the logo page.

        halt -p

    It is suggested that you always use the `poweroff` command to shutdown (and poweroff) your computer.
    You should close all programs before you logout or shutdown your computer.

7. to change time zone using command sudo dpkg-reconfigure tzdata

25. `ssh -X` X11 forwarding, make it possible for you to use GUI applications on server

## Task

8. `at` command run in backgroud,
    so do not use it to do things that have to communicate with stdin stdout ...

## Shell Scripting

22. It is recommended that you use single quotes when defining aliases
    unless you have good reasons to use double quotes.
    The reason is that shell variables in aliases defined in single quotes
    are not expanded until runtime.
    This makes your alias more robust (shell variables do not have to defined before aliases)
    and flexible (you can change definition of shell variables later as needed).

6. In terminal,
    wild cards are expanded before passed to functions.
    This means that if you pass wild cards from a function to nested functions,
    it usually will not work.
    Instead,
    you should pass the whole argument list,
    which is represented by `$@`.


## Archive

1. DO NOT USE the 7-zip format for backup purpose on Linux/Unix
    because 7-zip does not store the owner/group of the file.

2. difference between 7za and 7z?

## UI

5. use syndaemon -dti 0.5 to disable touchpad while typing.
    You have to have `Option SHMConfig "on"` or `Option SHMConfig "true"` in the synaptics configuration file.

8. Sometimes when you login into a server,
    it freezes after printing the welcome message.
    You can press `CTRL + C` to kill running process and it might help you bring the terminal back.

9. Linux release specific information

        lsb_release -a

    the lsb-release package

## Process

1. Use `Ctrl + Z` to pause a process and use `bg` to send it to background to run.
    Use `fg` to bring a background process to foreground.

7. `ldd --version` check glibc version

3. You can use `ps aux | grep -i user_id` to list your jobs
    and `kill -9 process_id` to kill a process.
    On platform Load Sharing Facility (LSF),
    you probably don't have access to `kill` unless are a privileged user.
    Instead of using `ps` and `kill`,
    you can use `bjobs` to show your jobs and `bkill process_id` to kill your process.


1. when defining alias,
    do not use tailing `/` in paths unless you have a good reason for that ...

2. file to check link cannot use trailing `/`

4. what have caused the blog difference issue?, line terminators


5. comm: make sure you don't screw up by invisible white spaces!!!,
    intersection/inner join, left join, right join (add keywords to your blog)

10. type of disk

        df -T


11. In a `case ... esac` clause, you have to espace spaces in matching patterns,
    e.g., You should use `*Linux\ Mint*` instead of `*Linux Mint*` in the following code.

        case "$dist" in
            *Debian* | *LMDE* | *Ubuntu* | *Linux\ Mint* )
                # install minimum texlive and some extra fonts
                wajig install texlive texlive-latex-extra texlive-fonts-extra dvipng texstudio
                return 0;;
            * )
                echo "This script does not support ${dist:13}."
                return 1;;
        esac

12. loop throught English letters

        for letter in {a..z} ; do
        echo $letter
        done

        for letter in {c..f} ; do
        echo $letter
        done


2. Direct output and error message

        command1 > out.txt 2> err.txt

        command2 -f -z -y > out.txt 2> err.txt


## Environment Variables

using envrionment variables in script that doesn't exists is really dangerous!!!
came across this multiple times.
how should solve the problem?
Check whether a variable exists before you use it?

CPU Stats

## UUID in Bash
```bash
uuidgen
```
need the libuuid library which is part of `util-linux`

1. `id -un` is a better alternative than `whoami`.

## Timezone
Linux
```
cat /etc/timezone
```
Mac
<https://slaptijack.com/system-administration/set-mac-os-x-time-zone-from-the-command-line/>

## References

- [你可能不知道的Shell](http://coolshell.cn/articles/8619.html)
- [28个Unix/Linux的命令行神器](http://coolshell.cn/articles/7829.html)
- [35 Terminal ( text ) based application for Linux](http://www.linuxnov.com/35-terminal-text-based-application-for-linux/)
- [Rolo](http://rolo.sourceforge.net/)
- [http://abook.sourceforge.net/](http://abook.sourceforge.net/)
- [Five Really Handy Google Command Line Tricks](http://lifehacker.com/5568817/five-really-handy-google-command-line-tricks)
