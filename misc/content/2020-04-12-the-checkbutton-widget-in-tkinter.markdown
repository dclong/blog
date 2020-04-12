Status: published
Date: 2020-04-12 09:46:15
Author: Benjamin Du
Slug: the-checkbutton-widget-in-tkinter
Title: the Checkbutton Widget in Tkinter
Category: Computer Science
Tags: Computer Science, Python, programming, Tkinter, GUI, Checkbutton

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**


1. `ttk.Checkbutton` is preferred to `tk.Checkbutton`.

2. It seems to me that the `Checkbutton.bind` doesn't work.
    However, 
    specifying a callback function using the `command` option 
    when creating a Checkbutton still work.
