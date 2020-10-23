Status: published
Date: 2020-08-22 12:13:37
Author: Ben Chuanlong Du
Slug: jupyterlab-tips
Title: Tips on JupyterLab
Category: Software
Tags: software, JupyterLab, Jupyter, tips

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## General Tips

1. You might lose data if you edit a notebook in multiple places 
    (e.g., in different browsers or on different machines)!
    If you do have to work on the same notebook across multiple machine at the same time,
    a simple trick is to always close the tab of a notebook after you have updated it.
    This ensures that you sync the changes of the notebook to JupyterLab server.

2. If you have a notebook open on a machine 
    but have it edited before on another machine, 
    the changes might not be synchronized automatically.
    If you jump to edit the notebook on the current machine without refreshing it, 
    you might loss data.
    Even if JupyterLab do warn you about the notebook is changed on the disk,
    it is a hassle to go back to figure out new changes you've made.
    To avoid data loss,
    you'd better close notebook tabs and reopen them
    if you switch to another machine to use JupyterLab. 

3. If you work across multiple machines, 
    the resolution of a terminal might not be messed up when you use Vim in it.
    A simple way to resolve the issue is create a new terminal.

4. If a notebook is running and outputing results, 
    disconnecting and reconnecting to it will lose future outputs
    even if the notebook continues to run.
    And what is even trickier is that the kernel icon won't display itself as busy,
    which can confuse users that the notebook was iterrupted or has finished running.
    This issue is being tracked at 
    [issue 6003](https://github.com/jupyterlab/jupyterlab/issues/6003)
    and
    [issue 5382](https://github.com/jupyterlab/jupyterlab/issues/5382).
    Be cautions about it before it is fixed.

2. Shutdown a kernel will kill the kernel associated with a notebook
    but it won't affect content in the notebook if no code is running. 
    After shutdowning the kernel, 
    a notebook behaves like a pure text editor.

1. `find.scala | xargs vim` makes terminal fail to display correctly.
    `reset` resolves the issue.

2. hard to do interactive UI in JupyterLab right now ...
    many interactive UI pacakges in R relies on RStudio to work.

3. Convert Jupyter Notebook to another format.

        jupyter nbconvert --to FORMAT notebook.ipynb

4. Notice that you'd better turn off proxies while using JupyterLab. 

5. If a JupyerLab notebook doesn't render well due to trust issues, 
    you can rerun everything in the notebook and save it. 
    This will usually resolve the trust issue.

## Format a Jupyter/Lab Notebook 

https://github.com/krassowski/jupyterlab-lsp/blob/master/scripts/nblint.py

https://github.com/dclong/dsutil/blob/dev/dsutil/filesystem.py#L266

## Find & Replace 

https://stackoverflow.com/questions/59498649/how-to-find-replace-in-jupyter-lab

## More Tips on IPython and Jupyter/Lab

- [Tips on IPython](http://www.legendu.net/misc/blog/ipython-tips/)

- [28 Jupyter Notebook tips, tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

- [Wait, IPython Can Do That?!](https://ep2019.europython.eu/media/conference/slides/cBeHNyZ-wait-ipython-can-do-that.pdf)

## [JupyterLab Extenions](http://www.legendu.net/misc/blog/useful-tools-extensions-for-jupyterlab/)
Please refer to
[JupyterLab Extenions](http://www.legendu.net/misc/blog/useful-tools-extensions-for-jupyterlab/)
for more details.

## References

- [JupyterLab Change Log](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html)

- [IPython and Jupyter in Depth: High productivity, interactive Python - PyCon 2017](https://www.youtube.com/watch?v=VQBZ2MqWBZI)

https://blog.dominodatalab.com/lesser-known-ways-of-using-notebooks/

http://arogozhnikov.github.io/2016/09/10/jupyter-features.html

[Running a notebook server](http://jupyter-notebook.readthedocs.io/en/latest/public_server.html)

[Jupyter Notebook Enhancements, Tips And Tricks](https://forums.fast.ai/t/jupyter-notebook-enhancements-tips-and-tricks/17064)


- https://toree.incubator.apache.org/documentation/user/quick-start
- https://datascience.berkeley.edu/10-data-science-newsletters-subscribe/ 
- https://github.com/jupyter-incubator/declarativewidgets
- https://github.com/jupyter-incubator/dashboards
- http://people.duke.edu/~ccc14/sta-663-2016/Customizing_Jupyter.html
- http://ramhiser.com/2015/02/01/configuring-ipython-notebook-support-for-pyspark/
- https://groups.google.com/forum/#!topic/jupyter/iaaKOeRwyjs
- https://toree.incubator.apache.org/documentation/user/installation.html
- https://github.com/michhar/useR2016-tutorial-jupyter/blob/master/INSTALLATIONS.md
- http://stackoverflow.com/questions/31855794/whats-the-best-way-to-share-jupyter-notebooks-with-non-programmers
- https://www.polymer-project.org/1.0/
- https://github.com/jupyter-incubator/declarativewidgets
- http://nbgrader.readthedocs.io/en/stable/
- http://webcomponents.org/
- https://geomesa.atlassian.net/wiki/display/GEOMESA/How+to+install+the+Scala+Spark+(Apache+Toree)+Jupyter+kernel+with+GeoMesa+support
