UUID: 73d864a1-baff-459d-a310-67b077688ac5
Status: published
Date: 2020-03-07 12:06:47
Author: Ben Chuanlong Du
Slug: install-nodejs-on-ubuntu
Title: Install NodeJS on Ubuntu
Category: Software
Tags: software, NodeJS, installation, Ubuntu, node

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

    :::bash
    wajig install nodejs npm
    sudo ln -s /usr/bin/nodejs /usr/bin/node

Notice that it is necessary to create a symbolic link for node, 
as many Node.js tools use this name to execute.
