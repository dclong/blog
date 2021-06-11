Status: published
Date: 2021-01-10 10:27:02
Author: Benjamin Du
Slug: install-newer-version-of-sqlite3-on-debian
Title: Install Newer Version of SQLite3 on Debian Jessie
Category: OS
Tags: Linux, SQLite3, Debian, backports, SQLite
Modified: 2021-01-10 10:27:02

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. Open `/etc/apt/sources.list` and add the following line to the end.

        deb http://www.backports.org/debian jessie-backports main contrib non-free

    or

        deb http://ftp.us.debian.org/debian/ jessie-backports main contrib non-free
        deb-src http://ftp.us.debian.org/debian/ jessie-backports main contrib non-free

2. make sure the GPG signatures are correct by running the following command.

        sudo apt-get update
        sudo apt-get install debian-backports-keyring

3. Install SQLite3.

        sudo apt-get update
        sudo apt-get -t jessie-backports install sqlite3 libsqlite3-dev
