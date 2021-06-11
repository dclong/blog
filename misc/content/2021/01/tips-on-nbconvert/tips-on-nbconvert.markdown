Status: published
Date: 2021-01-08 13:59:41
Author: Benjamin Du
Slug: tips-on-nbconvert
Title: Tips on nbconvert
Category: Computer Science
Tags: Computer Science, Jupyter, JupyterLab, notebook, nbconvert, template
Modified: 2021-01-08 13:59:41

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. Converting too many notebooks at the same (multiprocessing) causes `zmq.error.ZMQError: Address already in use`.
    The simple way to fix this issue is to limit the number of processes converting notebooks.
    It is suggested that you keep in within 3.

2. Convert a notebook to HTML.

        :::bash
        jupyter nbconvert --to HTML notebook.ipynb
        # or
        jupyter nbconvert notebook.ipynb

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


## Template 

jupyter nbconvert --template=nbextensions mynotebook.ipynb

http://nbconvert.readthedocs.io/en/latest/customizing.html#Custom-Templates

jupyter nbconvert --to python 'example.ipynb' --stdout --template=simplepython.tpl

## References

https://nbconvert.readthedocs.io/en/latest/usage.html

https://nbconvert.readthedocs.io/en/latest/usage.html#default-output-format-html

http://jupyter-contrib-nbextensions.readthedocs.io/en/latest/exporting.html#nbextensions-tpl