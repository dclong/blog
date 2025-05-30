Status: published
Date: 2021-12-04 20:03:49
Modified: 2025-05-30 07:56:53
Author: Benjamin Du
Slug: firenvim-brings-neovim-into-your-browser
Title: FireNVim Brings NeoVim into Your Browser
Category: Computer Science
Tags: Computer Science, Vim, NeoVim, FireNVim, browser

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation 

1. Install [icon](https://github.com/legendu-net/icon).

        :::bash
        curl -sSL https://raw.githubusercontent.com/legendu-net/icon/main/install_icon.sh | sudo bash -

2. Install and configure 
    [NeoVim](https://github.com/neovim/neovim)
    using icon.

        :::bash
        icon nvim -ic

2. Install the FireNVim plugin for your browser.
    - [FireNVim - Chrome](https://chrome.google.com/webstore/detail/firenvim/egpjdkipkomnmjhjmdamaniclmdlobbo?hl=en)
    - [FireNVim - Firefox](https://addons.mozilla.org/en-US/firefox/addon/firenvim/)

3. Run the command `nvim` 
    and then inside NeoVim run the command `:call firenvim#install(0)`.
    
4. If you are using Linux, 
    configure your brower to trigger FireNVim on the shortcut `ctrl + e`.
    - For chrome, you can configure this via 
    [chrome://extensions/shortcuts](chrome://extensions/shortcuts)
    .
    ![firenvim-chrome-shortcuts](https://user-images.githubusercontent.com/824507/196080758-ce9a706e-c746-4642-92ca-0e5eebe8e9b3.png)

The above installation configures FireNVim to never automatially prompt up.
You have to manually bring it up 
using the shortcut `ctrl + e` (Linux and Windows) 
or `Command + e`  (macOS)
.
In case it doesn't work,
please refer to
[Trouble Shooting Firenvim](https://github.com/glacambre/firenvim/blob/master/TROUBLESHOOTING.md#troubleshooting-firenvim)
for instructions on how to trouble shoot it.
<span style="color:red">
Note: If you update the FireNVim plugin for your browser to a newer version,
you will also have to repeat step 2 above.
</span>

## Font Size 

Use the following command to adjust font and its size.

    :::vim
    :set guifont=Monaco:h16

Use the following commands to adjust the frame size for editing.

    :::vim
    :set lines=80 
    :set columns=100 

## Troubleshooting

### Disable Hardware Acceleration

`:set lines=30` is very slow due to hardware acceleration in browsers.
Disabling hardware acceleration helps.
Please refer to
[How to Turn Hardware Acceleration On and Off in Chrome](https://www.howtogeek.com/412738/how-to-turn-hardware-acceleration-on-and-off-in-chrome/)
and
[Hardware acceleration and WindowBlinds causes Firefox to crash](https://support.mozilla.org/en-US/kb/hardware-acceleration-and-windowblinds-crash)
on how to disable hardware acceleration in Chrome and Firefox.

## References 

[Firenvim: Neovim inside Your Browser](https://jdhao.github.io/2020/01/01/firenvim_nvim_inside_browser/)

[FireNvim @ GitHub](https://github.com/glacambre/firenvim)
