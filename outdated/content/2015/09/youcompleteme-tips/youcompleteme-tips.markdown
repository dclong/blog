Status: published
Date: 2015-09-22 14:00:13
Author: Ben Chuanlong Du
Title: Auto Completion Using YouCompleteMe in Vim
Slug: YouCompleteMe-tips
Category: Software
Tags: software, YouCompleteMe, YCM, Vim, plugin, addon, editor, tips  
Modified: 2020-05-22 14:00:13

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
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
