Status: published
Date: 2020-03-24 18:33:39
Author: Benjamin Du
Slug: tips-on-the-almond-scala-kernel
Title: Tips on the Almond Scala Kernel
Category: Computer Science
Tags: Computer Science, Scala, Almond, JupyterLab

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**



1. `kernel.silent(true)` 
    supress outputs of cells.


2. Currently each line in a cell have an output,
    which is messy.
    There are 2 ways to avoid this.

        :::scala
        val resObj = {
            ...
            ...
        }

        {{
            ...
            ...
        }}

## References

[Use Spark with the Almond Scala Kernel in JupyterLab](http://www.legendu.net/misc/blog/spark-almond-jupyterlab/)

[Specify Dependencies in the Almond Scala Kernel in JupyterLab](http://www.legendu.net/misc/blog/scala-almond-dependencies/)