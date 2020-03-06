Status: published
Date: 2019-10-19 21:06:24
Author: Benjamin Du
Slug: disable-jedi-in-ipython
Title: Disable Jedi in IPython
Category: Computer Science
Tags: programming, Python, jedi, ipython, autocomplete

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


In the meantime, looks like there is a way one can disable jedi in ipython with Completer.use_jedi: https://ipython.readthedocs.io/en/stable/config/options/terminal.html

Specifically you can use ipython locate profile to find your current profile directory, and edit the ipython_config.py to add c.IPCompleter.use_jedi = False


In jupyter just run a cell with the following contents %config IPCompleter.use_jedi = False

## Refences

https://tutorials.technology/solved_errors/Slow-tab-completion-on-large-data-object-in-notebook.html