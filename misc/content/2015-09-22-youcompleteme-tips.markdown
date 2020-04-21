UUID: 1a1f4a84-139b-49c8-a7c7-79c2e44123cd
Status: published
Date: 2017-03-18 19:23:42
Author: Ben Chuanlong Du
Slug: YouCompleteMe-tips
Title: YouCompleteMe Tips
Category: Software
Tags: software, YouCompleteMe, YCM, Vim, plugin, addon, editor, tips  

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. You might need the package `python-dev` (in Debian Series) 
    or `python-devel` (in Arch Linux) in order to compile the Vim addon YouCompleteMe. 

2. you should use install.py instead of install.sh. 
    The later one is deprecated.

3. Run the following command to compile YouCompleteMe with clang support.
    ```bash
    ./install.py --clang-completer
    ```
    This has been integrated into the script `linfig.vim`

4. YouCompeleteMe configuration file, this is done via the command linfig.vim currently

5. YCM can be installed on Cygwin as well
    if you do not have clang installed on cygwin then compile with the following command
    ```language
    ./install.py 
    ```

3. functions opened in all buffers are accessible by YCM, 
    so they can be autocompleted

4. requires cmake to compile, added to linstall.vim
