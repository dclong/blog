Status: published
Date: 2025-12-16 15:40:51
Modified: 2025-12-16 16:13:21
Author: Benjamin Du
Slug: install-dropbox-using-flatpak
Title: Install Dropbox Using Flatpak
Category: Computer Science
Tags: Computer Science, programming, Linux, flatpak, Dropbox, FlatHub, Atomic, distribution

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation

flatpak install flathub com.dropbox.Client

## Configuration on Fedora Atomic Linux Distributions and Variants

Fedora Atomic Linux distributions changed the root (/) filesystem type to 
[composefs](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221qbOoyFENm5dUVRx9Advue8wZ3FJQgN24%22%5D,%22action%22:%22open%22,%22userId%22:%22100282891140280543929%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
for reasons.
Composefs is not a widely recognized filesystem type across the Linux landscape. 
For example,
the Dropbox flatpak does not recognize composefs and does not know what to do with it.
One workaround to make Dropbox installed via flatpak to work on Fedora Atomic Linux distributions 
is to configure the flatpak (using flatseal) to point to `/var/home/userid` instead of `/home/userid`.

- Grant the flatpak permission to `/var/home/userid`.
- Set the HOME environment variable for the flatpak to be `/var/home/userid` instead of `/home/userid`.

<img width="1919" height="1724" alt="Image" src="https://github.com/user-attachments/assets/cbb2202c-05e9-48d5-9fe5-4ee8ba2676e2" />

The workaround is effective because on Linux Atomic Linux distributions (and variants)
`/var/home` is of the type btrfs instead, 
which is widely recognized.

## References

- [Dropbox support](https://universal-blue.discourse.group/t/dropbox-support/10297)
