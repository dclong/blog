Status: published
Date: 2019-03-03 20:02:57
Author: Benjamin Du
Slug: spacevim-tips
Title: SpaceVim - A Modern Vim Distribution
Category: Software
Tags: software, SpaceVim, Vim, tips
Modified: 2021-06-18 10:28:17

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**
## Installation
```
curl -sLf https://spacevim.org/install.sh | bash
```

## Uninstallation
```
curl -sLf https://spacevim.org/install.sh | bash -s -- --uninstall
```

https://github.com/SpaceVim/SpaceVim/issues/84

https://github.com/SpaceVim/SpaceVim/issues/78

## Tricks & Traps

1. By default SpaceVim enables GUI colors.
    This makes SpaceVim extremely slow in terminals that does not support 24 bits true colors.
    To resolve the performance issue, 
    simplify disable GUI colors by setting `enable_guicolors = false`
    under `[options]` in your SpaceVim configure file `$HOME/.SpaceVim.d/init.toml`.

2. SpaceVim has mapped `q` as smart buffer close.
    The normal functionality (recording macros) of `q` can be get by `<leader>`qr.
    By default, 
    `<leader>` is `\` so you can use `\qr` to record macros in SpaceVim.

3. Custom configuration files are in the directory `$HOME/.SpaceVim.d`.


## Some Useful Key Bindings

<table style="width:100%">
  <tr>
    <th> Key Binding </th>
    <th> Description </th> 
  </tr>
  <tr>
    <td> SPC b f </td>
    <td> format the buffer </td>
  </tr>
  <tr>
    <td> SPC t 8 </td>
    <td> highlight characters that execeeds 80th column </td>
  </tr>
  <tr>
    <td> SPC t f </td>
    <td> highlight characters that execeeds the fill column </td>
  </tr>
  <tr>
    <td> SPC [1-9] </td>
    <td> jump to the windows with the specific number </td>
  </tr>
</table>

### [Window](https://spacevim.org/documentation/#window-manipulation)

<table style="width:100%">
  <tr>
    <th> Key Binding </th>
    <th> Description </th> 
  </tr>
  <tr>
    <td> SPC 1 </td>
    <td> got to window number 1 </td>
  </tr>
  <tr>
    <td> SPC 2 </td>
    <td> go to window number 2 </td>
  </tr>
</table>


### [Comment](https://spacevim.org/documentation/#commenting)

<table style="width:100%">
  <tr>
    <th> Key Binding </th>
    <th> Description </th> 
  </tr>
  <tr>
    <td> SPC c h </td>
    <td> hide/show comments </td>
  </tr>
  <tr>
    <td> SPC c l </td>
    <td> toggle comment line </td>
  </tr>
</table>

### [Buffers and Files](https://spacevim.org/documentation/#buffers-and-files)

<table style="width:100%">
  <tr>
    <th> Key Binding </th>
    <th> Description </th> 
  </tr>
  <tr>
    <td> :bn </td>
    <td> go to the next buffer </td>
  </tr>
  <tr>
    <td> SPC b n </td>
    <td> go to the next buffer </td>
  </tr>
  <tr>
    <td> :bp </td>
    <td> go to the previous buffer </td>
  </tr>
  <tr>
    <td> :e # </td>
    <td> go to the previous buffer </td>
  </tr>
  <tr>
    <td> SPC b p </td>
    <td> go to the previous buffer </td>
  </tr>
  <tr>
    <td> SPC t f </td>
    <td> highlight characters that execeeds the fill column </td>
  </tr>
  <tr>
    <td> SPC [1-9] </td>
    <td> jump to the windows with the specific number </td>
  </tr>
</table>

## Lanugage Server Protocol

https://spacevim.org/layers/language-server-protocol/

## Language Layers

[Available Layers >> lang#python](https://spacevim.org/layers/lang/python/)

I'm not sure whether this layer is really helpful 
given that you always uses the LSP layer.

## Additional Useful Plugins

```
[[custom_plugins]]
name = "vim-scripts/dbext.vim"
merged = false

[[custom_plugins]]
repo = "machakann/vim-swap"
merged = false
```

## References

- [SpaceVim Documentation](https://spacevim.org/documentation/)
