UUID: 0689247d-f19c-44a9-94c9-79e55a49227d
Status: published
Date: 2018-10-29 08:28:14
Author: Ben Chuanlong Du
Slug: use-autojump-to-help-quick-navigation-in-terminal-in-linux
Title: Use Autojump to Help Quick Navigation in Terminal in Linux
Category: OS
Tags: Linux, autojump, cd, terminal, shell, navigation

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

[autojump](https://github.com/wting/autojump) 


## Installation

Use the following command to install autojump on Ubuntu.
```bash
wajig install autojump
```
Place the following code in your `.bashrc` file and you are good to go.
```bash
if [[ -f /usr/share/autojump/autojump.bash ]]; then
    . /usr/share/autojump/autojump.bash
fi
```