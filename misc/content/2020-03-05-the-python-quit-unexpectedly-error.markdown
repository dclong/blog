Status: published
Date: 2020-03-05 11:11:51
Author: Benjamin Du
Slug: the-python-quit-unexpectedly-error
Title: The Python Quit Unexpectedly Error
Category: Computer Science
Tags: programming, Python, error, quit

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**



If you are using Homebrew, you can reinstall a corrupted Python environment like this:

brew uninstall --ignore-dependencies --force python python@2
unset PYTHONPATH
brew install python python@2
I had another "quit unexpectedly" issue and this resolved it for me.


https://bugs.python.org/issue36154