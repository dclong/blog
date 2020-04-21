Status: published
Date: 2019-11-20 17:11:16
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

## References

https://nbconvert.readthedocs.io/en/latest/usage.html
