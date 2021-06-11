Status: published
Date: 2021-04-10 23:47:18
Author: Benjamin Du
Slug: connect-to-teradata-from-the-beakerx-sql-kernel-in-jupyterlab
Title: Connect to Teradata from the BeakerX SQL Kernel in JupyterLab
Category: Computer Science
Tags: programming, Jupyter, JupyterLab, SQL, BeakerX
Modified: 2021-02-10 23:47:18
You can run the following magics in a cell to connect to Teradata from a BeakerX SQL kernel.

    :::bash
    %classpath add jar /workdir/jars/teradata/tdgssconfig.jar
    %classpath add jar /workdir/jars/teradata/terajdbc4.jar
    %defaultDatasource jdbc:teradata://your.teradata.com/USER=your_username,PASSWORD=your_password

After connecting to a Teradata server,
you can write SQL code in a cell just like in any other SQL IDE.
