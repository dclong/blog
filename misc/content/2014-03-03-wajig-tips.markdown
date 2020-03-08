Status: published
Author: Ben Chuanlong Du
Date: 2020-03-07 22:54:45
Slug: wajig-tips
Title: Tips on Wajig
Category: OS
Tags: Wajig, Linux, package management, tips

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

[Wajig on Debian Wiki](https://wiki.debian.org/Wajig)


1. You can type enter the CLI of `wajig` by typing `wajig` in terminal,
    so that you can use commands of `wajig` directly
    instead of typing `wajig` every time.

        :::bash
        $ wajig
        wajig>

## wajig install

From the documentation,
`wajig install` is equivalent to `apt-get install --no-install-recommends`.
`wajig install-r` is equivalent to `apt-get install`.

## wajig search

1. `wajig search` use regular expression by default.
    For example, 
    `wajig search g++` does not search for literal `g++` but any package that contains `g`. 
    To search for `g++` related packages, 
    you can use `wajig search g\\+\\+` instead.

2. Let wajig also search description

        :::bash
        wajig search -v youtube

## wajig download

1. Download a package for install later.
    This is very helpful if the package is big.

        :::bash
        wajig download pkg_name

1. Remove all GNOME desktop related packages

        :::bash
        wajig list | awk '{print $2}' | grep -i ^gnome | xargs wajig purge

2. install a package of specific version using wajig

        :::bash
        wajig search libssl/testing

3. check which repository a package comes from

        :::bash
        wajig policy geary

6. To install backport packages, use

        :::bash
        wajig install libreoffice/wheezy-backports
        apt-get -t wheezy-backports libreoffice

    It does not work if you use

        :::bash
        wajig install libreoffice/stable-backports

## Download Packages (for Installation Later)

If your network speed is a concern,
you can download a package for installation later using the command below. 

    :::bash
    wajig download pkg_name  

## Issues

1. it seems to me that `wajig purge package_name` fails to remove packages sometimes
    even though it seems to succeed.
