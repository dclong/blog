Status: published
Date: 2019-10-20 21:35:44
Author: Benjamin Du
Slug: disable-the-checkers-layer-in-spacevim
Title: Disable the Checkers Layer in SpaceVim
Category: Software
Tags: Software, SpaceVim, Vim, checkers, layer, LSP, language server protocol

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


You can use the following command in SpaceVim to disable the `checkers` layer temporarily.

    :::vim
    let g:spacevim_lint_on_save = 0

If you want to disable the `checkers` layer permanently,
add the following lines into your `init.toml` file.

    [[layers]]
    name = "checkers"
    enable = fals

Note that language server protocol (LSP) plugins are better alternatives to the `checkers` layer.

## References

https://spacevim.org/layers/checkers/

https://github.com/SpaceVim/SpaceVim/issues/399

https://github.com/SpaceVim/SpaceVim/issues/3163
