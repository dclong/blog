Status: published
Date: 2020-03-07 12:13:01
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

```Bash
jupyter labextension install some_extension
```

```Bash
jupyter labextension uninstall some_extension
```

    :::bash
    jupyter serverextension enable --py jupyterlab_code_formatter
    jupyter serverextension disable --py jupyterlab_code_formatter


https://jupyterlab.readthedocs.io/en/stable/user/extensions.html

https://github.com/topics/jupyterlab-extension

https://medium.com/@subpath/jupyter-lab-extensions-for-data-scientist-e0d97d529fc1

https://github.com/mauhai/awesome-jupyterlab

## Useful Tools

### [jupyter/nbdime](https://github.com/jupyter/nbdime)

Tools for diffing and merging of Jupyter notebooks.
Notice that nbdime integrates with git well.

You can use the following command to configure nbdime for Git.

    nbdime config-git (--enable | --disable) [--global | --system]

Register nbdime with Git for the current project/repository.

    nbdime config-git --enable

Deregister nbdime with Git for the current project/repository.

    nbdime config-git --disable


Register nbdime with Git for global users.

    nbdime config-git --enable --global

Deregister nbdime with Git for global users.

    nbdime config-git --disable --global

### JupyterHub

### sudospawner


## Useful Extensions for JupyterLab


### [jupyterlab-toc](https://github.com/jupyterlab/jupyterlab-toc)

### [jupyterlab-drawio](https://github.com/QuantStack/jupyterlab-drawio)

www.draw.io is also interesting,

### [wallneradam/jupyterlab-output-auto-scroll](https://github.com/wallneradam/jupyterlab-output-auto-scroll)

Automatically scrolls scrollable output cells to bottom when content has changed

### [jupyterlab-latex](https://github.com/jupyterlab/jupyterlab-latex)

### [Voila](https://github.com/QuantStack/voila)

### [jupyterlab-spreadsheet](https://github.com/quigleyj97/jupyterlab-spreadsheet)

### [ipywidgets](https://github.com/ipython/ipywidgets/tree/master/jupyterlab_widgets)
    Interactive HTML widgets (slider, button, textbox, etc.) for Python Notebook.

        pip install jupyterlab_widgets
        jupyter labextension install --sys-prefix --py jupyterlab_widgets
        jupyter labextension enable --sys-prefix --py jupyterlab_widgets

    Examples of custom widget libraries built upon ipywidgets are

    - bqplot a 2d data visualization library enabling custom user interactions.

    - pythreejs a Jupyter - Three.js wrapper, bringing Three.js to the notebook.

    - ipyleaflet a leaflet widget for Jupyter.


## Some Other Extensions for JupyterLab

### [jupyterlab_geojson](https://github.com/jupyterlab/jupyterlab_geojson)
```bash
pip3 install jupyterlab_geojson
jupyter labextension install --py --sys-prefix jupyterlab_geojson
jupyter labextension enable --py --sys-prefix jupyterlab_geojson
```

### [jupyterlab-quickopen](https://github.com/parente/jupyterlab-quickopen)

Very slow when there are lots of files.

### [jupyterlab-monaco](https://github.com/jupyterlab/jupyterlab-monaco)

### [jupyterlab_spellchecker](https://github.com/ijmbarr/jupyterlab_spellchecker)

### [jupyterlab-flake8](https://github.com/mlshapiro/jupyterlab-flake8)

A non polished product. Too much messages.

### [jupyterlab_code_formatter](https://github.com/ryantam626/jupyterlab_code_formatter)

### [qgrid](https://github.com/quantopian/qgrid)

### [jupyterlab-google-drive](https://github.com/jupyterlab/jupyterlab-google-drive)
Not sure whether this is useful.

### [widget-cookiecutter](https://github.com/jupyter/widget-cookiecutter)

    pip3 install cookiecutter

### jupyter_declarativewidgets

### jupyter-wysiwyg

not available for jupyterlab yet ...
