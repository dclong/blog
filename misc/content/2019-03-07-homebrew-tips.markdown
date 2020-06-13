Status: published
Date: 2020-06-13 10:18:43
Author: Benjamin Du
Title: Install Packages Using Homebrew on macOS
Slug: homebrew-tips
Category: Software
Tags: software, Homebrew, macOS, Linuxbrew

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


```
brew install 
brew uninstall
brew link 
brew search 
brew list | xargs brew uninstall
brew search python@3.6
```

1. Linuxbrew/brew has been merged into Homebrew/brew.
    For more please refer to [this issue](https://github.com/Linuxbrew/brew/issues/1).
    **Linuxbrew is a good tool to install Linux packages 
    in environments which you do not have sudo permission**.

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
