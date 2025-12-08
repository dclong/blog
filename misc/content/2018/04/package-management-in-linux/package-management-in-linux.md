UUID: c9c53a46-c8ca-4b4c-a5fd-b40f76478ead
Status: published
Date: 2018-04-11 10:11:29
Author: Ben Chuanlong Du
Slug: package-management-in-linux
Title: Package Management in Linux
Category: OS
Tags: Linux, package management, wajig, apt-get, dpkg
Modified: 2025-12-07 16:26:28

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There are many different ways to install packages in Linux.

1. Build from source.

2. Pre-built binaries.

3. Use distribution specific tools.
    For example,
    - Debian, Ubuntu Series: apt-get, wajig
    - Fedora: dnf
    Notice that Atomic Linux distributions have their own version of package managing tools.
    For example,
    - Fedora Atomic: rpm-ostree
    - AerynOS: moss

4. [Homebrew](https://www.legendu.net/misc/blog/homebrew-tips) and
    [Nix](https://nixos.org/nix/)
    are 2 popular package management tools for Linux
    when you do not have the root permission.
    Homebrew is preferred to Nix for multiple reasons.

    - Homebrew works for both macOS and Linux. 
        For people who have already been using Homebrew on macOS,
        there's no learning effort at all.

    - Homebrew has more packages.

5. Use cross‐platform and dependency‐free app formats,
    e.g.,
    [FlatPak](https://flatpak.org/)
    and 
    [AppImage](https://appimage.org/)
    .
    For the difference between FlatPak and AppImage,
    please refer to
    [What are the differences between snaps, appimage, flatpak and others?](https://askubuntu.com/questions/866511/what-are-the-differences-between-snaps-appimage-flatpak-and-others)
    .

## AppImage

3. Software Center (A fancy GUI for managing packages on Ubuntu/Debian)
4. Software Management (Linux Mint)

## Debian Series of Linux Distributions

wajig apt-get, dpkg,


use alien or rpm to install rpm packages, wajig install alien; sudo alien -i *.rpm
```
dpkg -S $(which free)
```
Apt-get有问题时可以试试dpkg,
apt-get worries about dependencies but dpkg not,
so then dependency is broken,
you can use dpkg to install/remove packages

$ aptitude why libpng12-0

apt-mark manual

## RedHat

https://www.digitalocean.com/community/tutorials/package-management-basics-apt-yum-dnf-pkg

https://pkgs.org/
