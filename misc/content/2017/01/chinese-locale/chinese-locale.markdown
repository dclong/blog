Status: published
Date: 2017-01-15 12:06:13
Author: Ben Chuanlong Du
Slug: chinese-locale
Title: Chinese Locale in Linux
Category: OS
Tags: Linux, Chinese, Locale, locale-gen, locales, Ubuntu, Debian
Modified: 2021-02-15 12:06:13

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

First you have to make sure `locales` is installed.
If not,
you can install it using the following command (on Ubuntu/Debian).

    :::bash
    sudo apt-get install locales

## Ubuntu

    :::bash
    # GB2312 encoding support
    sudo locale-gen zh_CN
    # UTF-8 encoding support
    sudo locale-gen zh_CN.UTF-8

`$LANG` environment control the different language to use ...

## Debian

Notice that `locale-gen` is one of those things that Ubuntu differs from Debian.
While `locale-gen` in Ubuntu takes arguments from command-line,
`locale-gen` in Debain read locales from the file `/etc/locale.gen`.
You can follow the steps below to generate locales in Debian.

1. Uncomment locales to generate in the file `/etc/locale.gen`.

2. Run the command `sudo locale-gen`.

## References

- [Can't generate en_US.UTF-8 Locale](https://unix.stackexchange.com/questions/246846/cant-generate-en-us-utf-8-locale)

- [CONFIGURE SYSTEM LOCALE ON DEBIAN 9](https://blog.here-host.com/configure-system-locale-debian-9/)
