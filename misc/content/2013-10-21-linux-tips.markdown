Status: published
Author: Ben Chuanlong Du
Title: Tips on Linux
Date: 2020-02-29 17:13:18
Slug: linux-tips
Category: OS
Tags: tips, Linux

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Tricks and Traps

1. Use full paths of commands when you use a batch account
    or schedule a cron job.
    The reason is that batch account 
    and/or cron might have different environment from your personal account.
    So if a shell script works in your personal account,
    it might not work in a batch account or in cron. 

2. [explainshell.com](http://www.explainshell.com/) 
    is a great place for learning shell.

3. Broken symbolic link `.bashrc` (and probably other configuration files/scripts) 
    stops Xfce4 (and probably other DEs) from login to the GUI.
    Fix the broken symbolic links resolves the issue.
 
## Installation

1. After a new kernel is installed, 
    the old image is usually kept and you can still boot into the old kernel if you like.
    This make is convenient if the new kernel has some issues.

## Remote

1. The remote desktop software Remmina leaks the super key, 
    which is problematic ...
    I think the problem is Ubuntu, not the remote apps ...

2. When you connect to a server, 
    you'd better not use the super key. 
    Because it is active on both the server and the local machines. 

## File System

9. You cannot change permission of files on NTFS filesystem ..., 
    they are determined when mounted

10. Linux hard disk saves properties, user, group of files, 
    a different user must have enough permission to mount it

1. do not use gui to remove large file/directories, use command line instead

## Good Practice

1. The home directory is where you should work in, 
    you should put all your personal data in your home directory. 
    When you need to reinstall the system or backup your data, 
    you can make a copy of your home directory. 
    However, I go one step further to make things even more convenient. 
    I create a directory named archives in my home directory,
    put all my persoanl data including configuration files there
    (except cloud, such as Dropbox, TeamDrive, etc.) 

## Terminal

1. nautilus-open-terminal allow you to open a terminal 
    in any directory via short menu.

2. A good backgroup color setting for terminal Hue: 85, Saturation: 36,
    Value: 71, Red: 155, Green: 182 and Blue: 117. color name: \#9BB675.
    Cursor color: #B93A3A.
    The theme goes well with this color setting is "Xterm".

        ^P : move up through history list, one command at a time. (Up arrow key) 
        ^N : move down (or Down arrow key). 

3. Use `Shift+PageUp` and `Shift+PageDown` to scroll up and down in virtual console.

## Shell

1. White spaces matters a lot in bash. To assign a string to a variable,
    you can use `v=some_content` but not `v = some_content`. 
    The reason is that space is used to separate bash commands and arguments. 
    Bash will treat `v` as a command instead of a variable. 

2. To source in a bash file "a-bash-file" so that commands in the file
    will be executed, you can use `source a-bash-file`, or you can use a
    period "." in place of "source", i.e., you can also use `.
    a-bash-file`.

3. `return` returns a bash function and thus can only be used in a bash function. 
    The argument of `return` must be a numeric number. 
    `exit` exits the bash enviroment, 
    i.e., terminate the terminal you are using.


5. to add path to the "PATH" environment variable, use the following command

        PATH=$PATH:path_to_add

    If you want to add the path permanently, 
    you can put the command into the ".bashrc" file under your home directory. 
    If you have to add lots of paths into the PATH environment variable, 
    you can put them into a seperate file, 
    and link it in the ".bashrc" file.

## Path in Bash Script

1. Full path of current directory

        $PWD

2. base name of current directory

        ${PWD##*/}

    or

        basename $PWD

## cd 

1. use - to go back to last directory

2. use $CDPATH

3. use pushd and popd


## FTP

1. ftp transfer non-text use binary mode

## File Association

1. The user-specific file association information is save in the file
    ` /.local/share/applications/mimeapps.list`, 
    and the global file association information is saved in file `/etc/gnome/defaults.list`.

## Change Hostname

1. To change hostname permanently, 
    change the hostname to what you want
    in files [] `/etc/hostname` and [] `/etc/hosts`, and then use the
    following code to make the change in effect without restarting your
    computer.

        /etc/init.d/hostname.sh start

## sudo

1. To change the timeout of the sudo password, add the following line
    to the end of the /etc/sudoers file.

        Defaults:your_username timestamp_timeout=SECONDS
        Defaults syslog=auth,passwd_timeout=10
j
## users and groups

1. `id` displays information of a user.


## Skills

1. If you select some text, 
    right click on it but nothings happens (i.e., no short menu poped up), 
    it means that the selected text has already been copied to the mouse buffer. 
    This is one place that Linux is different from Windows. 
    Notice that no all selct and copy process is like this. 
    You still have to copy the selected text into the buffer manually sometimes.

2. Hard drive related operations: <http://www.skullbox.net/newsda.php>

3. check cpu information `cat /proc/cpuinfo` and memory `cat /proc/meminfo`

4.  Linux system support *true* random number generator, 
    which is implemented by collecting the noise generate by hardwares. 
    To use generate *true* random numbers, 
    you can use the command.

    head -1 /dev/random | od -i -N 10 | awk '{ print $2 }' 

    Note that `/dev/random` will block until additional environmental noise is gathered
    if the entropy pool in the machine is empty. 
    If you do not want to be block, 
    you can use `/dev/urandom` to generate random numbers, 
    which reuses the internal pool to produce more pseudo-random bits when the entropy pool is empty. 
    Though `/dev/urandom` might contain less entropy than `/dev/random` does,
    it is still valide for usual use.

## Copy using UI

1. Many Linux/Unix realted applications use `copy on selection`.
    This features makes things confusing sometimes. 
    For example, if you copy things from one place and want to paste it into a terminal which has `copy on selection` enable.
    Then you click on the terminal to paste. 
    The thing is that when you click on the terminal, 
    you often select a blank line which means that you have copied a blank line before pasting. 
    This often make your copy/paste fail to work.
    If copy/paste fail to work in some application, 
    it is possibly because of the `copy on selection` feature. 
    A workaround is to right click ...

## References

- [CommandLineFu](http://www.commandlinefu.com/commands/browse/sort-by-votes)
- [Best Documentation](http://www.cyberciti.biz/tips/linux-unix-bsd-documentations.html)
- [nixCraftA](http://www.cyberciti.biz/)
- [developerWorks](http://www.ibm.com/developerworks/cn/linux/)

- [How to mount a windows partition on Linux automatically on each start up](http://www.computerandyou.net/2011/05/how-to-mount-a-windows-partition-on-linux-automatically-on-each-start-up/)

- [Configure Automount/Autofs on Ubuntu 10.10 Maverick Linux](http://aaronwalrath.wordpress.com/2011/03/21/configure-automountautofs-on-ubuntu-10-10-maverick-linux/)

- [Linux on Laptops](http://www.linux-on-laptops.com/)
- [Linux: What are some time-saving tips that every Linux user should know?](http://www.quora.com/Linux/What-are-some-time-saving-tips-that-every-Linux-user-should-know#)
- [Linux: Find Wireless Driver Chipset Information](http://www.cyberciti.biz/faq/linux-find-wireless-driver-chipset/)




http://blog.scoutapp.com/articles/2015/02/24/understanding-linuxs-cpu-stats

https://h-node.org/home/index/en

http://www-03.ibm.com/systems/power/software/aix/linux/toolbox/alpha.html

[AIX - The getconf Command for System Information](http://www.redbooks.ibm.com/abstracts/tips0124.html?Open)
