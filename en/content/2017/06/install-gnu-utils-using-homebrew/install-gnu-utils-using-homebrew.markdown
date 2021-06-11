Status: published
Date: 2017-06-22 13:26:28
Author: Ben Chuanlong Du
Slug: install-gnu-utils-using-homebrew
Title: Install GNU Utils Using Homebrew
Category: OS
Tags: macOS, Homebrew, GNU
Modified: 2017-10-22 13:26:28


# Configuration

Run the following command in terminal before you install any GNU utils using Homebrew.
It will ensures that the installed GNU utils get used by default.

```bash
export PATH="/usr/local/opt/findutils/libexec/gnubin:$PATH"
export MANPATH="/usr/local/opt/findutils/libexec/gnuman:$MANPATH"
```

Notice that upgrading your Mac OS will reset the 2 environment variables.
So you will have to run the above commands again after you upgrading your Mac OS.

# GNU Core Utils

```bash
brew install coreutils
```

# Key Commands

```bash
brew install binutils
brew install diffutils
brew install ed --default-names
brew install findutils --with-default-names
brew install gawk
brew install gnu-indent --with-default-names
brew install gnu-sed --with-default-names
brew install gnu-tar --with-default-names
brew install gnu-which --with-default-names
brew install gnutls
brew install grep --with-default-names
brew install gzip
brew install screen
brew install watch
brew install wdiff --with-gettext
brew install wget
```

# OS X ships a GNU version, but too old

```bash
brew install bash
brew install emacs
brew install gdb # gdb requires further actions to make it work. See `brew info gdb`.
brew install gpatch
brew install m4
brew install make
brew install nano
```

# Other commands (non-GNU)

```bash
brew install file-formula
brew install git
brew install less
brew install openssh
brew install perl518 # must run "brew tap homebrew/versions" first!
brew install python
brew install rsync
brew install svn
brew install unzip
brew install vim --override-system-vi
brew install macvim --override-system-vim --custom-system-icons
brew install zsh
```

# References

[Install and Use GNU Command Line Tools in Mac OSX](https://www.topbug.net/blog/2013/04/14/install-and-use-gnu-command-line-tools-in-mac-os-x/)
