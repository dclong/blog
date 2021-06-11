Status: published
Date: 2017-11-11 10:39:11
Author: Ben Chuanlong Du
Slug: jupyter-notebook-kernels
Title: Jupyter Notebook Kernels
Category: Software
Tags: software, Jupyter Notebook, JupyterLab, kernel
Modified: 2020-09-11 10:39:11

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

[Jupyter Kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)

By default, 
Python kernels are installed to `/usr/local/share/jupyter/kernels`
and BeakerX kernels are installed to `/usr/share/jupyter/kernels`.


## Python

### [ipykernel](https://github.com/ipython/ipykernel)

IPython Kernel for Jupyter/Lab,
which is the default Python kernel for Jupyter/Lab currently.

### [xeus-python](https://github.com/jupyter-xeus/xeus-python)

`xeus-python` is a Jupyter kernel for Python 
based on the native implementation of the Jupyter protocol [xeus](https://github.com/jupyter-xeus/xeus).

[A new Python kernel for Jupyter](https://blog.jupyter.org/a-new-python-kernel-for-jupyter-fcdf211e30a8)


## SQL Kernels

https://github.com/catherinedevlin/ipython-sql

tmthyjames/SQLCell

## Spark Kernel

1. toree (a good one）

2. sparkmagic (seems like a good choice)

3. spylon-kernel

## Remote Kernels

IPython is able to run remtoe kernels.

https://github.com/ipython/ipython/wiki/Cookbook:-Connecting-to-a-remote-kernel-via-ssh

https://stackoverflow.com/questions/29037211/how-do-i-add-a-kernel-on-a-remote-machine-in-ipython-jupyter-notebook

https://github.com/jupyter/notebook/issues/1487
