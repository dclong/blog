Status: published
Date: 2025-12-07 18:19:15
Modified: 2025-12-07 20:40:15
Author: Benjamin Du
Slug: managing-fedora-atomic-core-system-using-rpm-ostree
Title: Managing Fedora Atomic Core System Using rpm-ostree
Category: Computer Science
Tags: Computer Science, programming, Linux, atomic, Fedora, rpm, ostree

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


Fedora Atomic Linux ditributions use 
`rpm-ostree` to install system tools.

## Upgrade

```
sudo ostree admin pin 0
rpm-ostree rebase
rpm-ostree rebase fedora:fedora/43/x86_64/kinoite
```


