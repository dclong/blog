Status: published
Date: 2019-03-07 03:11:14
Author: Ben Chuanlong Du
Slug: install-software-on-mac
Title: Install Software on Mac
Category: OS
Tags: macOS, installing software, Homebrew

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Homebrew

1. You might encounter link problems when you use the `brew` command to install packages on Mac.
    A quick and dirty way to solve the problem is to link the executable file into `$HOME/bin`.
    This will not solve all problems, of course.

2. You can install a specific version of a package using the `@` symbol.
    For example,
    the command below installs node 8.

        brew install node@8

    All available versions of a package (say, node) can be listed using the following command.

        brew search node@

    If there are multiple version of a package (say, node) installed, 
    you can set the default version of the package to use using the command below.

        brew switch node 10.15.0

2. Uninstall a package, say, `telnet`.

        brew uninstall telnet
        # or
        brew remove telnet

2. Do not install python using brew as you will end up with 2 copies of python

3. better to use MacVim instead of Vim. 

        brew install macvim

    The command for MacVim is `mvim`. 
    For convenience, 
    you can link it to `$HOME/bin/vim`.

4. No readlink on Mac.  Use `greadlink` instead.
    You have install the package `coreutils` in order to use `greadlink`.

        brew install coreutils

## References

https://apple.stackexchange.com/questions/329187/homebrew-rollback-from-python-3-7-to-python-3-6-5-x

https://stackoverflow.com/questions/3987683/homebrew-install-specific-version-of-formula

http://osxdaily.com/2018/06/13/how-install-update-python-3x-mac/
