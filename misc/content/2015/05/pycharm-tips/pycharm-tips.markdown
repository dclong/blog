Status: published
Date: 2015-05-22 15:30:47
Author: Ben Chuanlong Du
Slug: pycharm-tip
Title: Python Developing in PyCharm
Category: Software
Tags: software, PyCharm, Python, IDE
Modified: 2020-05-22 15:30:47

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Change Scheme

1. File -> Settings... -> Editor -> Colors & Fonts

2. Choose a scheme right to "Scheme name"

## Change Font of Terminal

1. Search for Console Font

2. Set the desired font size.

3. Restart terminal (the font size for terminal won't take effect until the terminal is restarted)

## PyCharm on WSL

PyCharm (starting from 2018.3) supports configuring a remote Python interpreter via Windows Subsystem Linux WSL).
See [Using WSL As a Remote Interpreter](https://www.jetbrains.com/help/pycharm/2018.3/using-wsl-as-a-remote-interpreter.html)
for detailed instructions.
However, 
be aware that this feature is **only available in the professional edition** but not in the community edition.

## pybuilder Integration

https://github.com/pybuilder/pybuilder/issues/24

## Limitations in PyCharm Community Edition

1. no good theme

2. auto completion does not complete file paths

## References

https://stackoverflow.com/questions/34412739/set-the-font-size-in-pycharms-python-console-or-terminal

https://www.jetbrains.com/help/pycharm/creating-and-registering-file-types.html
