Status: published
Date: 2019-10-22 01:00:07
Author: Benjamin Du
Slug: connect-to-teradata-from-the-bekaerx-sql-kernel-in-jupyterlab
Title: Connect to Teradata from the Bekaerx SQL Kernel in JupyterLab
Category: Computer Science
Tags: programming, Jupyter, JupyterLab, SQL, BeakerX

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

You can run the following magics in a cell to connect to Teradata from a BeakerX SQL kernel.

    :::bash
    %classpath add jar /workdir/jars/teradata/tdgssconfig.jar
    %classpath add jar /workdir/jars/teradata/terajdbc4.jar
    %defaultDatasource jdbc:teradata://your.teradata.com/USER=your_username,PASSWORD=your_password

After connecting to a Teradata server,
you can write SQL code in a cell just like in any other SQL IDE.
