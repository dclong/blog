Status: published
Date: 2020-09-27 22:55:07
Author: Benjamin Du
Title: Install Packages Using Homebrew on macOS
Slug: homebrew-tips
Category: Software
Tags: software, Homebrew, macOS, Linuxbrew
Modified: 2020-09-27 22:55:07

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Tips and Traps

1. All Homebrew formulas are listed at https://formulae.brew.sh/formula/.
    You can search on the site for available formulas.

1. Linuxbrew/brew has been merged into Homebrew/brew.
    For more please refer to [this issue](https://github.com/Linuxbrew/brew/issues/1).
    **Linuxbrew is a good tool to install Linux packages 
    in environments which you do not have sudo permission**.

1. You might encounter link problems when you use the `brew` command to install packages on Mac.
    A possible way to fix the issue is to manually configure the `PATH` environemnt variable.
    Or a quick and dirty way to resolve the problem is to link the executable file into `$HOME/bin`.

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

## Example Commands

```
brew install 
brew uninstall
brew link
brew unlink 
brew search 
brew list
brew list | xargs brew uninstall
brew search python@3.6
brew ls --versions node
```

## Install gcc/g++

```Bash
brew install gcc
```

## [Install Linuxbrew](https://github.com/Homebrew/install)

https://github.com/Homebrew/install

```Bash
sh -c "$(curl --proxy http://your.proxy.servder:port -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
```
The installation script installs Homebrew to /home/linuxbrew/.linuxbrew using sudo if possible 
and in your home directory at ~/.linuxbrew otherwise. 
Homebrew does not use sudo after installation. 
Using /home/linuxbrew/.linuxbrew allows the use of more binary packages (bottles) 
than installing in your personal home directory.

Follow the instructions below if you have to install Linuxbrew using a proxy.

1. Configure the environment variables `http_proxy` and `https_proxy`.
    ```Bash
    export http_proxy=http://your.proxy.server:port
    export https_proxy=http://your.proxy.server:port
    ```
2. Configure proxy for Git (as Linuxbrew rely on Git to work) following instructions in
    [Use Git Behind a Proxy](http://www.legendu.net/en/blog/use-git-behind-a-proxy/).


You can export environment variables for Linuxbrew using the following command
assuming Linuxbrew is installed to `/home/linuxbrew/.linuxbrew`.
```Bash
/home/linuxbrew/.linuxbrew/bin/brew shellenv >> .bash_profile
```
Or use the following command if Linuxbrew is installed to `~/.linuxbrew`.
```Bash
~/.linuxbrew/bin/brew shellenv >> .bash_profile
```

## References

[Homebrew](https://brew.sh/)

[Linuxbrew](https://docs.brew.sh/Homebrew-on-Linux)

[Homebrew Discussion Forum](https://discourse.brew.sh/latest)

[Homebrew Cheatsheet](https://devhints.io/homebrew)

[What does “brew link” do?](https://stackoverflow.com/questions/33268389/what-does-brew-link-do)

[Why linking keg-only formulae requires –force option in homebrew?](https://discourse.brew.sh/t/why-linking-keg-only-formulae-requires-force-option-in-homebrew/2435)

https://apple.stackexchange.com/questions/329187/homebrew-rollback-from-python-3-7-to-python-3-6-5-x

https://stackoverflow.com/questions/3987683/homebrew-install-specific-version-of-formula

http://osxdaily.com/2018/06/13/how-install-update-python-3x-mac/

