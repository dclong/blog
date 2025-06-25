Status: published
Date: 2025-06-15 20:40:23
Modified: 2025-06-25 00:36:41
Author: Benjamin Du
Slug: tips-on-fd
Title: Tips on fd
Category: Computer Science
Tags: Computer Science, fd, fdfind, Linux, shell, find

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## Tips & Traps

1. `fd` is much faster compared to `find`.

## Installation

    wajig install fd-find

The install binary is `fdfind`.

## Example Usages

1. Find all directories under `$dir`. 

        fdfind --type d . $dir 

2. Find all files under `$dir`. 

        fdfind --type f --print0 . $dir 

## References

- [fd @ GitHub](https://github.com/sharkdp/fd)

