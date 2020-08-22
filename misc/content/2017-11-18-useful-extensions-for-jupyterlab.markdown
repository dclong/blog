Status: published
Date: 2020-08-22 12:15:10
Author: Ben Chuanlong Du
Slug: useful-tools-extensions-for-jupyterlab
Title: Useful Tools and Extensions for JupyterLab
Category: Software
Tags: software, JupyterLab, extension, plugin, JupyterHub, nbdime

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Install/Uninstall Jupyter/Lab Extensions

Install a Jupyter/Lab extension.

    :::bash
    jupyter labextension install some_extension

Unnstall a Jupyter/Lab extension.

    :::bash
    jupyter labextension uninstall some_extension

Enable an installed Jupyter/Lab extension.

    :::bash
    jupyter serverextension enable --py jupyterlab_code_formatter

Disable an istallledd Jupyter/Lab extension.

    :::bash
    jupyter serverextension disable --py jupyterlab_code_formatter

## Extensions/Tools to Avoid 

### Variable Inspaction in Notebook 

1. makes notebook run slow
2. why do you want such a tool if you can check any vairable in notebook already?

### jupyterlab-lsp 

1. slow and might crash on pandas DataFrame

### [jupyterLab/debugger](https://github.com/jupyterlab/debugger)

I'm not really convinced that it is useful at this time ...

## Useful Tools

### [nbdime](http://www.legendu.net/misc/blog/use-nbdime-to-diff-and-merge-jupyterlab-notebooks/)

[nbdime](http://www.legendu.net/misc/blog/use-nbdime-to-diff-and-merge-jupyterlab-notebooks/)
is a tool for diffing and merging Jupyter/Lab notebooks.
It works well with Git.

### [JupyterHub](http://www.legendu.net/misc/blog/jupyterhub-tips/)

[JupyterHub](http://www.legendu.net/misc/blog/jupyterhub-tips/)
is a multi-user server for Jupyter notebooks.

## Useful Extensions for JupyterLab

### [jupyterlab-toc](https://github.com/jupyterlab/jupyterlab-toc)

### [Jupyter/Lab Extensions for Spreadsheet](http://www.legendu.net/misc/blog/jupyterlab-extensions-for-spreadsheet/)

### [wallneradam/jupyterlab-output-auto-scroll](https://github.com/wallneradam/jupyterlab-output-auto-scroll)

Automatically scrolls scrollable output cells to bottom when content has changed

### [jupyterlab-latex](https://github.com/jupyterlab/jupyterlab-latex)

### [Voila](https://github.com/QuantStack/voila)

### [ipywidgets](https://github.com/ipython/ipywidgets/tree/master/jupyterlab_widgets)

Interactive HTML widgets (slider, button, textbox, etc.) for Python Notebook.

    :::bash
    pip install jupyterlab_widgets
    jupyter labextension install --sys-prefix --py jupyterlab_widgets
    jupyter labextension enable --sys-prefix --py jupyterlab_widgets

Examples of custom widget libraries built upon ipywidgets are

- bqplot a 2d data visualization library enabling custom user interactions.

- pythreejs a Jupyter - Three.js wrapper, bringing Three.js to the notebook.

- ipyleaflet a leaflet widget for Jupyter.

## Some Other Extensions for JupyterLab

### [jupyterlab_geojson](https://github.com/jupyterlab/jupyterlab_geojson)

    :::bash
    pip3 install jupyterlab_geojson
    jupyter labextension install --py --sys-prefix jupyterlab_geojson
    jupyter labextension enable --py --sys-prefix jupyterlab_geojson

### [jupyterlab-drawio](https://github.com/QuantStack/jupyterlab-drawio)

[jupyterlab-drawio](https://github.com/QuantStack/jupyterlab-drawio)
is a standalone embedding of the FOSS drawio/mxgraph package into JupyterLab.
If you using a office tool (MS/Google PPT/Slides/Doc),
it is suggested that you use the built-in flowchart support instead.
Please refer to
[Text-based Diagram Tools](http://www.legendu.net/misc/blog/text-based-flowchart-tools/)
and
[GUI Mind Mapping Tools](http://www.legendu.net/misc/blog/gui-mind-mapping-tools/)
for more discussions on flowchart and UML tools.

### [jupyterlab-quickopen](https://github.com/parente/jupyterlab-quickopen)

[jupyterlab-quickopen](https://github.com/parente/jupyterlab-quickopen)
aims to quickly open a file in JupyterLab by typing part of its name.
However,
it does not work well if the working directory of Jupyter/Lab contains a large number of files.
[jupyterlab-quickopen](https://github.com/parente/jupyterlab-quickopen)
eithers hangs or crashes when building indexes for a large number of files.
Unfortunately, 
users use [jupyterlab-quickopen](https://github.com/parente/jupyterlab-quickopen)
mostly when the working directory of Jupyter/Lab get complicated 
and contains lots of files.
So, 
overall I think [jupyterlab-quickopen](https://github.com/parente/jupyterlab-quickopen) 
failed its mission.


As an alternative,
it is must faster and more reliable to use the `find` command to help locate files in a terminal.
You can also use the `Open Path` command to help you open a file 
without changing directory in the navigation panel in JupyterLab.

### [jupyterlab-email](https://github.com/timkpaine/jupyterlab_email)

### [jupyterlab-monaco](https://github.com/jupyterlab/jupyterlab-monaco)

### [jupyterlab_spellchecker](https://github.com/ijmbarr/jupyterlab_spellchecker)

### [jupyterlab-flake8](https://github.com/mlshapiro/jupyterlab-flake8)

A non polished product. Too much messages.

### [jupyterlab_code_formatter](https://github.com/ryantam626/jupyterlab_code_formatter)

### [jupyterlab-google-drive](https://github.com/jupyterlab/jupyterlab-google-drive)
Not sure whether this is useful.

### [widget-cookiecutter](https://github.com/jupyter/widget-cookiecutter)

    :::bash
    pip3 install cookiecutter

### jupyter_declarativewidgets

### jupyter-wysiwyg

not available for jupyterlab yet ...

## References

https://jupyterlab.readthedocs.io/en/stable/user/extensions.html

https://github.com/topics/jupyterlab-extension

https://medium.com/@subpath/jupyter-lab-extensions-for-data-scientist-e0d97d529fc1

https://github.com/mauhai/awesome-jupyterlab
