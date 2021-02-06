UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Install Softwares in Linux
Date: 2012-04-30 00:00:00
Tags: Linux, softwares, permission
Category: OS
Slug: install-software-linux
Author: Ben Chuanlong Du

Sometime when you install softwares in Linux, 
you get an error message saying that you do not have permission while you used sudo or the root account. 
This probably means that you do not have full access to some installation files.
An easy way to solve this problem is to change file permissions of these installation files.
For example, 
suppose "inst" is the directory containing installation files, 
you can 
change file access use the following command and try installation again.

    chmod -R 755 inst

