Status: published
Date: 2020-01-03 17:21:11
Author: Benjamin Du
Slug: debug-code-in-jupyterlab-notebooks
Title: Debug Code in JupyterLab Notebooks
Category: Computer Science
Tags: programming, Python, debug, notebook, Jupyter, JupyterLab, debugger, debugging, %debug, ipdb, pdb

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## Use the %debug Magic

The easiest way to debug a Jupyter notebook is to use the %debug magic command. 
Whenever you encounter an error or exception, 
just open a new notebook cell, type %debug and run the cell. 
This will open a command line where you can test your code 
and inspect all variables right up to the line that threw the error.


Type "n" and hit Enter to run the next line of code 
(The → arrow shows you the current position). 
Use "c" to continue until the next breakpoint. 
"q" quits the debugger and code execution.

## IPython Debugger

	:::bash
	from IPython.core.debugger import set_trace
	set_trace()

## [debugger](https://github.com/jupyterlab/debugger)

[debugger](https://github.com/jupyterlab/debugger)
is a good JupyterLab extension enabling debugging support.

## PixieDebugger of the pixiedust Package

pixiedust is only for Jupyter notebooks.
and JupyterLab is not support at this time.

https://github.com/pixiedust/pixiedust/issues/613

## References

https://medium.com/@chrieke/jupyter-tips-and-tricks-994fdddb2057

https://medium.com/codait/the-visual-python-debugger-for-jupyter-notebooks-youve-always-wanted-761713babc62
