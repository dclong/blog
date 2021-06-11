Status: published
Date: 2020-01-29 20:14:09
Author: Benjamin Du
Slug: trust-a-jupyterlab-notebook
Title: Trust a JupyterLab Notebook
Category: Software
Tags: Software, tools, JupyterLab, trust notebook
Modified: 2020-01-29 20:14:09

By default, 
IPython (kernel of Jupyter/Lab notebook) disables executation of untrusted code without explicit user input.
If you have notebook whose output containings JavaScript (e.g., JS-based visualiation)
and code wasn't run by you (e.g., the notebook is shared by someone else),
the JS-based output won't be shown by default.
For more explanation,
please refer to 
[Notebook Security](https://jupyter-notebook.readthedocs.io/en/stable/security.html#notebook-security).


There are currently 2 ways to trust a notebook.
First, you can trust (multiple) notebooks via command-line.

    :::bash
    jupyter trust path_to_notebook.ipynb
    jupyter trust notebook1.ipynb notebook2.ipynb
    jupyter trust *.ipynb

Second, 
you can trust a notebook using the `Trust Notebook` comamnd from the command tab in the left panel.

1. Click the on the `Commands` tab in the left panel.

2. Search for `Trust Notebook`.

3. Click the `Trust Notebook` button to trust a notebook.
    You will get a prompt to confirm your action.

![Trust a Notebook](https://user-images.githubusercontent.com/824507/71461881-4ff7aa80-2766-11ea-8c35-0de71284907b.png)

## References

[Notebook Security](https://jupyter-notebook.readthedocs.io/en/stable/security.html#notebook-security)

[Trusting Notebooks](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#trusting-notebooks)

