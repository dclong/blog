UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Author: Ben Chuanlong Du
Slug: interact-between-different-vim-sessions
Date: 2014-12-26 10:35:12
Title: Interact with System Clipboard in Vim
Category: Software
Tags: Vim, software, Linux, clipboard, copy, paste

The following are ways for a Vim session 
to interact (copy/cut, paste) with other Vim sessions or other applications.

## Use X Windows Clipboard Directly

If you prefer to use X windows clipboard as the default buffer for Vim,
put `set clipboard=unnamedplus` in your `.vimrc` file.
This obviously makes your Vim talk to the system clipboard (all the time).
However, 
this makes different Vim sessions interact with each other 
which might or might not what you want.
Generally speaking,
this is not recommended if you want to interact with system clipboard within Vim.

## Use Vim Buffers (recommended)

You need to install a GUI version of Vim (e.g., `vim-gnome`) 
before you use this way to interact with the system clipboard.
You can simply use the `+` (sometimes `*`) register. 
For example, 
you can use `"+yy` to copy the current line in Vim to the system clipboard
and `"+p` to paste from from the system clipboard to Vim.


## The SHIFT Key

2. Hold `SHIFT` while you select text in Vim using mouse. 
You can then right click on the selection and choose `Copy` to copy it to the system clipboard, 
or you can use `CTRL + SHFIT + C` to copy the selection to the system clipboard.

4. You can right click and choose `paste` in Vim to pate from the system clipboard into Vim, 
or you can use `CTRL + SHIFT + V` to paste from the system clipboard into Vim.

5. Another way to copy from Vim to a text editor is to first select text in Vim with `SHFIT` pressed, 
and then middle-click in the text editor.
Notice that `CTRL + V` won't work, 
because you did not use `CTRL + SHFIT + C` (or `right click -> paste`) to copy the selection to the system clipboard.

## Use a Temporary Buffer/File

It's very convenient to copy/cut and paste text between different buffers/files of a same Vim session. 
So you can use temporary buffer/file to interact with other Vim sessions or other applications.

## See Also

<http://vim.wikia.com/wiki/Accessing_the_system_clipboard>
