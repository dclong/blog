UUID: 425b3e0b-617c-42ce-aaae-ed2a04354e98
Status: published
Date: 2016-12-10 02:09:11
Author: Ben Chuanlong Du
Slug: start-rstudio-server-after-upgrading
Title: Start RStudio Server After Upgrading
Category: Software
Tags: software, IDE, RStudio
Modified: 2016-12-10 02:09:11

It is quite often that the RStudio server cannot be start after upgrading. 
This is due to running R session in the background. 
A simple solution is to just restart the host machine. 
However, it is very risky to start servers (especially remote shared ones).
An alternative way is to find the R session in the background,
kill it and then start the RStudio server.
The following instruction assumes that 
the port 8787 (default) is used by RStudio server.

1. Find processes that listen to the port 8787.

        sudo fuser 8787/tcp

2. Kill all processes that listen to the port 8787. 

        sudo fuser -k 8787/tcp

    Or you can also use the command `kill` to terminate processes. 

3. Start RStudio server.

        sudo rstudio-server start

