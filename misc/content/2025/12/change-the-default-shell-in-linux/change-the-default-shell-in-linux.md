Status: published
Date: 2025-12-07 17:48:30
Modified: 2025-12-07 18:30:28
Author: Benjamin Du
Slug: change-the-default-shell-in-linux
Title: Change the Default Shell in Linux
Category: Computer Science
Tags: Computer Science, programming, Linux, shell, chsh, Atomic, change

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Atomic Linux Distributions

[How to change the default shell in fedora silverblue?](https://discussion.fedoraproject.org/t/how-to-change-the-default-shell-in-fedora-silverblue/21203/10)

```
sudo usermod --shell $(which fish) $(id -un)
```

## Mutable Linux Distributions

```
sudo chsh -s $(which fish) $(id -un)
```
