Status: published
Date: 2022-10-16 19:54:05
Modified: 2025-05-31 20:28:01
Author: Benjamin Du
Slug: tips-on-neovim
Title: Tips on NeoVim
Category: Computer Science
Tags: Computer Science, programming, neovim, IDE, PPA

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation on Ubuntu

You can install the latest stable version of neovim using the command below.

    sudo add-apt-repository ppa:neovim-ppa/stable
    wajig update
    wajig install neovim

## Tips and Traps

1. AppImage is a good way to install the latest version of NeoVim.

2. [AstroNvim](https://github.com/AstroNvim/AstroNvim) is a great configuration for NeoVim.

3. NeoVim with a complicated configuration (e.g., AstroNvim, SpaceVim, etc) 
    might be too slow when editing a large (>50M) text file.
    One trick helps is to disable plugins when editing large files.
    For example,
    you can use the following command to edit a large file without loading plugins.

        :::bash
        nvim --noplugin /path/to/large/text/file

## Repeat

- [Adding dot-repeat to your Neovim plugin](https://gist.github.com/kylechui/a5c1258cd2d86755f97b10fc921315c3)

- [Better repeat #1025](https://github.com/neovim/neovim/issues/1025)
