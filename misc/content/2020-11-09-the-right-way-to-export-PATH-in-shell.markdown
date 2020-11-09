Status: published
Date: 2020-11-09 11:10:06
Author: Benjamin Du
Slug: the-right-way-to-export-PATH-in-shell
Title: The Right Way to Export Path in Shell
Category: Computer Science
Tags: Computer Science, Shell, Bash, PATH, bashrc, bash_profile

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

Some people suggest exporting `PATH` only in `.bash_profile` 
instead of in `.bashrc` (for Bash).
The helps but does not resolve the issue of possible duplicated paths in `$PATH`.
The right way is to check for existence of the path in the `$PATH` environment variable first,
and add it only when it does NOT already exist in `$PATH`.
Below is an example snippet of adding the directory `$HOME/env_python/bin` into `$PATH`.

    :::bash
    BIN_DIR=$HOME/env_python/bin
    if [[ ! "$PATH" =~ (^$BIN_DIR:)|(:$BIN_DIR:)|(:$BIN_DIR$) ]]; then
        export PATH=$BIN_DIR:$PATH
    fi

The snippet has the advatage that it works well in both `.bashrc` and `.bash_profile`.
So, 
you can safely add such snippets into `.bashrc`
and keep your `.bash_profile` as simple as the following. 

    :::bash
    if [[ -f ~/.bashrc ]]; then
        . ~/.bashrc
    fi
