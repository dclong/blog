Status: published
Date: 2020-05-23 00:04:26
Author: Ben Chuanlong Du
Title: Make Your Life Easier with Portable Applications
Slug: portable-apps
Category: Software
Tags: application, Chinese, software, portable, apps, CygwinPortable, Portable Python

Using portable applications is a good way to make your digital life easier. 
They do not eat up your disk quickly nor do they mess up the registry of your Windows OS.
You can always copy these applications from one computer to another and use it out of box.
Or you can install portable applications on a flash drive 
and use it on any computer with a Windows OS.
[PortableApps](http://www.portableapps.com/) offers all kinds of portable apps.
What is better is that it also offers a plotform 
which integrate many functionalities together 
such as installing portable apps (directly from the repository), 
updating portable apps, 
searching for installed apps, etc.
There is also a [Chinese website](http://www.portableappc.com/) 
whcih offers portable apps with Chinese characteristics 
that are compatible with the PortableApps platform. 

There are some software that I use often 
but is not support offically by PortableApps yet.
For example, Cygwin and Python.
There is a good portable version of Cygwin named 
[CygwinPortable](https://github.com/CybeSystems/CygwinPortable)
on GitHub.
It uses ConEmu for the console which supports multi-tabs 
and can also be used as Windows command prompt. 
CygwinPortable also allows you to create users and define the default user, 
which is very convenient.
Another advantage of CygwinPortable 
(over [MobaXterm](http://mobaxterm.mobatek.net/) and other portable version of Cygwin)
is that it has built-in Python suppport,
which makes Vim and other software installed on it Python-supported.
Though CygwinPortable has built-in Python support, 
the Python coming with it has limitations due to library dependencies.
For example, 
some Python packages such as FuzzyWuzzy and NLTK fails to work in CygwinPortable.
[Anaconda Python](http://portablepython.com/) is great portable distribution of Python.
It comes with many popular Python packages 
such as NumPy, SciPy, Matplotlib, PIL, PyQt, etc.
and also code editors such as PyCharm, PyScripter and IDLE.


## Tips on [PortableApps](https://portableapps.com/) 

1. The PortableApps launcher might causes desktop icon not to show up. 
    Closing the PortableApps launcher solves the problem.

2. You can actually run PortableApps programs directly (without using the PortableApps launcher). 
    If you'd like to do so, 
    you can make shortcuts of PortableApps programs on the desktop and/or in the start menu 
    to make things easier.