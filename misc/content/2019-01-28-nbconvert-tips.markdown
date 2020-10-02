Status: published
Date: 2020-10-01 19:24:15
Author: Ben Chuanlong Du
Slug: nbconvert-tips
Title: Converting JupyterLab Notebooks
Category: Software
Tags: JupyterLab, notebook, nbconvert, tips, zmq.error.ZMQError

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## [jupyter-book](http://www.legendu.net/misc/blog/tips-on-jupyter-book/)

## [fastpages](https://github.com/fastai/fastpages)

## nbconvert

1. Converting too many notebooks at the same (multiprocessing) causes `zmq.error.ZMQError: Address already in use`.
    The simple way to fix this issue is to limit the number of processes converting notebooks.
    It is suggested that you keep in within 3.

2. You can execute a notebook without converting it to a different format using the following command.

        :::bash
        jupyter nbconvert --to notebook --execute mynotebook.ipynb

    This will generate another notebook with the output inlined.
    You can use the option `--inplace` to overwrite the file inplace.

        :::bash
        jupyter nbconvert --to notebook --inplace --execute mynotebook.ipynb

3. There is no way to control the work directory of `jupyter nbconvert` at this time.
    A recommended alternative is to manually change the directory in the notebook. 
    It is possible to specify the output directory where things will be deployed.
    For more discussions,
    pleas refer to [this issue](https://github.com/jupyter/nbconvert/issues/1343).

## [jupyter/nbclient](https://github.com/jupyter/nbclient)

## [PaperMill](https://github.com/nteract/papermill)

PaperMill is a tool for parameterizing, executing, and analyzing Jupyter Notebooks.

## References

https://nbconvert.readthedocs.io/en/latest/usage.html
