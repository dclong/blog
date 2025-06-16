Status: published
Date: 2025-06-15 20:40:23
Modified: 2025-06-15 20:40:23
Author: Benjamin Du
Slug: tips-on-fd
Title: Tips on Fd
Category: Computer Science
Tags: Computer Science, fd, fdfind, Linux, shell, find

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://github.com/sharkdp/fd

wajig install fd-find

The install binary is `fdfind`.

## Example Usages

1. Find all directories under `$dir`. 

    fdfind --type d . $dir 

2. Find all files under `$dir`. 

    fdfind --type f --print0 . $dir 

