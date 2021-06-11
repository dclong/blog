Status: published
Date: 2020-02-19 10:18:07
Author: Benjamin Du
Slug: install-python-in-mac
Title: Install Python in Mac
Category: Software
Tags: software, install, Python, macOS
Modified: 2020-02-19 10:18:07




There are a few ways to install Python in Mac. 

1. Install system-wide via the official Python installation package.

2. Install a Anaconda Python distribution locally.

3. Install locally using Homebrew (recommended).

A few comments about different ways of installation.

1. Avoid installing multiple versions of Python in your system. 
    It usually brings more troubles than conveniences.
    Docker is usually a much better option 
    when you need different versions of Python.
    
1. Anaconda and Homebrew installs Python locally rather than system-wide.
  You have to install Python using an official installation package manually 
  (downloading the installation package and double click to install)
  if you need a system-wide installation.

2. The recommended way to instlal Python on Mac is to use Homebrew.
  However, 
  there are limited choices of Python versions in Homebrew.
  Go with Anaconda Python if you cannot find the version you need in Homebrew.

## References

https://stackoverflow.com/questions/51125013/how-can-i-install-a-previous-version-of-python-3-in-macos-using-homebrew

https://osxuninstaller.com/uninstall-guides/properly-uninstall-python-mac/
