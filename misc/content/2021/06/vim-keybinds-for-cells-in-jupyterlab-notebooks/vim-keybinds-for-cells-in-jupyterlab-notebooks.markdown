Status: published
Date: 2021-06-08 08:42:41
Author: Benjamin Du
Slug: vim-keybinds-for-cells-in-jupyterlab-notebooks
Title: Vim Keybinds for Cells of JupyterLab Notebooks
Category: Computer Science
Tags: Computer Science, software, tools, Jupyter, JupyterLab, notebook, cell, Vim, keybindings
Modified: 2021-06-08 08:42:41
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[jupyterlab-vim](https://github.com/jwkvam/jupyterlab-vim)
is a JupyterLab extension which brings Vim keybindings to cells of JupyterLab notebooks.
It can be installed using the following command in JupyterLab 3+.

    :::bash
    pip3 install jupyterlab_vim

And it can be uninstalled using the following command.

    :::bash
    pip3 uninstall jupyterlab_vim

By default, 
a JupyterLab extension is enabled after installtion.
You can disable an extension, 
e.g., jupyterlab_vim, using the following command. 

    :::bash
    sudo jupyter labextension disable @axlair/jupyterlab_vim

And enable it again using the command below.

    :::bash
    sudo jupyter labextension enable @axlair/jupyterlab_vim
